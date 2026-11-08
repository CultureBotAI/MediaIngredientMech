"""Negative controls for proposal composition and label/provenance validation."""
from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

import yaml


def module(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + ".py"))
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


COMPOSE = module("compose_shared_proposals")
LABELS = module("validate_proposal_labels")
DEPENDENCIES = module("find_cross_shard_dependencies")


class CompositionControls(unittest.TestCase):
    def setUp(self):
        self.before = {"identifier": "CHEBI:1", "synonyms": [{"synonym_text": "kept"}], "curation_history": [], "ontology_mapping": {"ontology_id": "CHEBI:1", "evidence": []}}

    def test_union_preserves_originals_and_both_sources(self):
        left, right = deepcopy(self.before), deepcopy(self.before)
        left["synonyms"].append({"synonym_text": "left"})
        right["curation_history"].append({"action": "PROPOSED"})
        merged = COMPOSE.compose(self.before, [left, right])
        self.assertEqual(merged["synonyms"], left["synonyms"])
        self.assertEqual(merged["curation_history"], right["curation_history"])
        self.assertEqual(self.before["synonyms"], [{"synonym_text": "kept"}])

    def test_removal_is_not_silently_composed(self):
        after = deepcopy(self.before)
        after["synonyms"] = []
        with self.assertRaisesRegex(ValueError, "removal"):
            COMPOSE.compose(self.before, [after])

    def test_identity_change_is_not_silently_composed(self):
        after = deepcopy(self.before)
        after["identifier"] = "CHEBI:2"
        with self.assertRaisesRegex(ValueError, "Non-additive"):
            COMPOSE.compose(self.before, [after])


class LabelControls(unittest.TestCase):
    def setUp(self):
        private = Path(".temp/all-unmatched-worker-02/helper-tests")
        private.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=private)
        self.root = Path(self.temp.name)
        self.old_root, self.old_dbs = LABELS.ROOT, LABELS.DATABASES
        LABELS.ROOT = self.root
        db = self.root / "synthetic.db"
        connection = sqlite3.connect(db)
        connection.execute("CREATE TABLE statements(subject TEXT,predicate TEXT,value TEXT,object TEXT)")
        connection.execute("INSERT INTO statements VALUES ('TEST:1','rdfs:label','correct',NULL)")
        connection.commit()
        connection.close()
        LABELS.DATABASES = {"TEST": db}
        self.after = self.root / "after.yaml"
        self.proposals = self.root / "proposals.json"

    def tearDown(self):
        LABELS.ROOT, LABELS.DATABASES = self.old_root, self.old_dbs
        self.temp.cleanup()

    def write_proposal(self, label):
        self.after.write_text(yaml.safe_dump({"ontology_mapping": {"ontology_id": "TEST:1", "ontology_label": label}}))
        self.proposals.write_text(json.dumps({"proposals": [{"proposal_id": "synthetic", "after_capture": {"root": "artifact", "path": "after.yaml", "sha256": hashlib.sha256(self.after.read_bytes()).hexdigest()}}]}))

    def test_wrong_canonical_label_fails(self):
        self.write_proposal("wrong")
        self.assertEqual(LABELS.run([self.proposals])["results"][0]["status"], "MISMATCH_OR_DEPRECATED")

    def test_mutated_payload_is_rejected_before_label_check(self):
        self.write_proposal("correct")
        self.after.write_text(self.after.read_text() + "# changed\n")
        with self.assertRaisesRegex(ValueError, "after payload changed"):
            LABELS.run([self.proposals])

    def test_known_label_has_no_scientific_approval(self):
        self.write_proposal("correct")
        result = LABELS.run([self.proposals])
        self.assertEqual(result["results"][0]["status"], "OK_CANONICAL")
        self.assertFalse(result["scientific_approval_established"])


class DependencyControls(unittest.TestCase):
    def test_explicit_nested_owner_fields_only(self):
        nested = {"candidate": [{"owner_record": "data/ingredients/mapped/X.yaml"}], "reasoning": "data/ingredients/mapped/Y.yaml"}
        self.assertEqual(list(DEPENDENCIES.owner_mentions(nested)), ["data/ingredients/mapped/X.yaml"])


if __name__ == "__main__":
    unittest.main()
