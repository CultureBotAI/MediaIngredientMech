"""Source evidence and original IRIs must survive the legacy MICRO restoration."""

import csv
import json
import shutil
from pathlib import Path
from urllib.parse import unquote

import pytest
import yaml

from mediaingredientmech.micro_source import SOURCE, load_source, source_term
from mediaingredientmech.render_ingredient_pages import curie_to_url
from mediaingredientmech.curie import CurieNormalizer


def test_reviewed_source_terms_and_original_iris():
    terms = load_source()
    assert {curie: term.label for curie, term in terms.items()} == {
        "MICRO:0002393": "Proteose Peptone No. 2",
        "MICRO:0002392": "rabbit serum",
        "MICRO:0002250": "V-8 juice",
    }
    for term in terms.values():
        assert term.iri.endswith("MicrO.owl/" + term.curie.replace(":", "_"))
        assert unquote(unquote(curie_to_url(term.curie))).endswith(term.iri)
    assert source_term("MICRO:0002390") is None
    assert source_term("MICRO:0000180") is None  # context node, not a new source approval


def test_modified_source_payload_is_rejected(tmp_path):
    target = tmp_path / "micro"
    shutil.copytree(SOURCE, target)
    path = target / "micro_nodes.tsv"
    path.write_text(path.read_text().replace("rabbit serum", "horse serum"))
    with pytest.raises(ValueError, match="source checksum mismatch"):
        load_source(target)


@pytest.mark.parametrize("field,value,problem", [
    ("label", "proteose peptone", "label or status mismatch"),
    ("parents", ["MICRO:9999999"], "parent mismatch"),
    ("iri", "http://purl.obolibrary.org/obo/MICRO_0002393", "IRI mismatch"),
])
def test_manifest_cannot_misrepresent_the_archived_class(tmp_path, field, value, problem):
    target = tmp_path / "micro"
    shutil.copytree(SOURCE, target)
    path = target / "manifest.json"
    manifest = json.loads(path.read_text())
    manifest["reviewed_terms"]["MICRO:0002393"][field] = value
    path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match=problem):
        load_source(target)


def test_restored_identity_rows_and_recipe_memberships_agree():
    root = Path(__file__).resolve().parents[1]
    with (root / "mappings/ingredient_mappings.sssom.tsv").open() as handle:
        rows = list(csv.DictReader((line for line in handle if not line.startswith("#")), delimiter="\t"))
    with (root / "mappings/culturemech_recipe_membership.tsv").open() as handle:
        memberships = list(csv.DictReader((line for line in handle if not line.startswith("#")), delimiter="\t"))
    normalizer = CurieNormalizer()
    for slug, curie, count in (
        ("Proteose_Peptone_No_2", "MICRO:0002393", 7),
        ("Rabbit_Serum", "MICRO:0002392", 21),
        ("V-8_Juice", "MICRO:0002250", 3),
    ):
        record = yaml.safe_load((root / f"data/ingredients/mapped/{slug}.yaml").read_text())
        assert record["identifier"] == record["ontology_mapping"]["ontology_id"] == curie
        assert record["ontology_mapping"]["ontology_label"] == source_term(curie).label
        mapped = [row for row in rows if row["subject_id"] == f"MIM:{slug}"]
        assert len(mapped) == 1
        assert mapped[0]["object_id"] == curie
        assert mapped[0]["predicate_id"] == "skos:exactMatch"
        assert normalizer.equivalent_term(f"MIM:{slug}").curie == curie
        assert len([row for row in memberships if row["mim_identifier"] == curie]) == count
        assert not (record.get("chemical_properties") or {}).get("cas_rn")
        assert not (record.get("supplied_form") or {}).get("cas_rn")
        assert not any(token.startswith("CAS:") for token in mapped[0]["other"].split("|"))
