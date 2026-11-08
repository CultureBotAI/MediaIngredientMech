"""Failure controls for the fragment assembler; these are not science tests."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "assemble", Path(__file__).with_name("assemble_outcomes.py")
)
ASSEMBLE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ASSEMBLE)


class AssemblyControls(unittest.TestCase):
    def setUp(self):
        private = Path(".temp/all-unmatched-worker-02/helper-tests")
        private.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=private)
        self.root = Path(self.temp.name)
        (self.root / "context").mkdir()
        frozen = (ASSEMBLE.ROOT / "context/frozen-shard-02.json").read_bytes()
        (self.root / "context/frozen-shard-02.json").write_bytes(frozen)
        self.cases = json.loads(frozen)["cases"]
        for author, cases in zip(
            ("a", "b", "c"), (self.cases[:63], self.cases[63:130], self.cases[130:])
        ):
            (self.root / author).mkdir()
            for key, rows in (
                ("decisions", [{"case_id": case["case_id"]} for case in cases]),
                ("evidence", [{"evidence_id": f"{author}-synthetic-evidence"}]),
                ("proposals", []),
            ):
                (self.root / author / f"{key}.json").write_text(json.dumps({key: rows}))

    def tearDown(self):
        self.temp.cleanup()

    def test_preserves_complete_case_order_without_review_claims(self):
        result = ASSEMBLE.collect(self.root)
        self.assertEqual(
            result["decisions"]["decisions"],
            [{"case_id": case["case_id"]} for case in self.cases],
        )
        self.assertEqual(len(result["evidence"]["evidence"]), 3)
        self.assertEqual(result["proposals"]["proposals"], [])

    def test_duplicate_case_rejected(self):
        path = self.root / "b/decisions.json"
        rows = json.loads(path.read_text())
        rows["decisions"][0] = {"case_id": self.cases[0]["case_id"]}
        path.write_text(json.dumps(rows))
        with self.assertRaisesRegex(ValueError, "duplicate case_id"):
            ASSEMBLE.collect(self.root)

    def test_missing_case_rejected(self):
        path = self.root / "b/decisions.json"
        rows = json.loads(path.read_text())
        rows["decisions"].pop()
        path.write_text(json.dumps(rows))
        with self.assertRaisesRegex(ValueError, "case accounting differs"):
            ASSEMBLE.collect(self.root)

    def test_duplicate_evidence_rejected(self):
        (self.root / "b/evidence.json").write_text(
            json.dumps({"evidence": [{"evidence_id": "a-synthetic-evidence"}]})
        )
        with self.assertRaisesRegex(ValueError, "duplicate evidence_id"):
            ASSEMBLE.collect(self.root)

    def test_modified_frozen_bytes_rejected(self):
        path = self.root / "context/frozen-shard-02.json"
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(ValueError, "frozen shard bytes changed"):
            ASSEMBLE.collect(self.root)


if __name__ == "__main__":
    unittest.main()
