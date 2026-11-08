"""Offline hash/lookup verification only; no scientific identity or form selection."""

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
    binding = json.loads((HERE / "source-binding.json").read_text())
    frozen = json.loads((HERE / "source/frozen-case.json").read_text())
    worker = json.loads((HERE / "source/worker-case-159.json").read_text())
    assert frozen == worker["case"] and worker["index"] == 159
    assert frozen["case_id"] == binding["case_id"]
    assert hashlib.sha256(json.dumps(frozen, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()).hexdigest() == binding["case_input_sha256"]
    for occurrence in binding["occurrences"]:
        assert sha(HERE / occurrence["cache_path"]) == occurrence["source_sha256"]
    results = json.loads((HERE / "http-results.json").read_text())
    assert len(results) == 5
    for row in results:
        assert row["attempt"] == 1 and row["scientific_identity_verified"] is False
        path = HERE / row["capture_path"]
        assert sha(path) == row["payload_sha256"]
        if row.get("status") != 200:
            continue
        payload = json.loads(path.read_text())
        if "requested_cid" in row:
            entries = payload["PropertyTable"]["Properties"]
            assert len(entries) == 1 and entries[0]["CID"] == row["requested_cid"]
            assert all(key in entries[0] for key in ["MolecularFormula", "InChI", "InChIKey", "IUPACName"])
        else:
            assert isinstance(payload["IdentifierList"]["CID"], list)
    print(json.dumps({"file_hashes_verified": len(manifest["file_sha256"]), "requests": 5, "source_case": binding["case_id"], "occurrences": len(binding["occurrences"]), "scientific_identity_or_mapping_approval": False}))


if __name__ == "__main__":
    main()
