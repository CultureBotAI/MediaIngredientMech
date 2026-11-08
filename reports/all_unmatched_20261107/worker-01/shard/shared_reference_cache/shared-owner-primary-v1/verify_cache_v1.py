"""Offline byte/reference verification only; this does not review source-case science."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads((HERE / "MANIFEST.json").read_text())
    for relative, expected in manifest["file_sha256"].items():
        path = HERE / relative
        assert path.is_file() and not path.is_symlink() and sha(path) == expected, relative
    inputs = json.loads((HERE / "verified-owner-inputs.json").read_text())
    records = json.loads((HERE / "primary-records.json").read_text())
    index = json.loads((HERE / "owner-reference-index.json").read_text())
    by_id = {row["evidence_id"]: row for row in records}
    assert len(by_id) == len(records) == 25
    for row in records:
        path = HERE / row["capture_path"]
        assert sha(path) == row["payload_sha256"]
        payload = json.loads(path.read_text())
        if row["evidence_id"].startswith("OLS:"):
            terms = payload["_embedded"]["terms"]
            assert len(terms) == 1 and terms[0]["obo_id"] == row["requested_id"]
        else:
            group = payload.get("PropertyTable", {}).get("Properties")
            if group is None:
                group = payload["InformationList"]["Information"]
            assert len(group) == 1 and group[0]["CID"] == row["observed"]["CID"]
            if row["requested_id"].startswith("PUBCHEM:"):
                assert group[0]["CID"] == int(row["requested_id"].split(":")[1])
            elif "Synonym" in group[0]:
                assert row["requested_id"].removeprefix("cas:") in group[0]["Synonym"]
        assert row["scientific_case_or_mapping_approval"] is False
    assert len(index) == len(inputs["owners"]) == 18
    for owner in index:
        assert sha(HERE / owner["raw_snapshot"]) == owner["sha256"]
        assert owner["primary_evidence_ids"] and set(owner["primary_evidence_ids"]) <= set(by_id)
        assert owner["scientific_approval"] is False and owner["source_cases_reviewed_by_this_cache"] == 0
    print(json.dumps({"file_hashes_verified": len(manifest["file_sha256"]), "exact_reference_records": len(records), "owner_snapshots": len(index), "scientific_review_or_approval": False}))


if __name__ == "__main__":
    main()
