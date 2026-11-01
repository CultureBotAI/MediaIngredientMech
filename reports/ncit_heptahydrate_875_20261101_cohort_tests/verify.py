#!/usr/bin/env python3
"""Read-only verification of this evidence package and its historical references.

This is not a live-corpus CI gate: later legitimate curation can change a
referenced repository file without invalidating the archived evidence.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def confined(root, relative):
    path = root / relative
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Unsafe evidence/reference path: {relative}")
    if not path.is_file():
        raise ValueError(f"Missing evidence/reference file: {relative}")
    return path


def main():
    package = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=package.parents[1])
    args = parser.parse_args()
    index = json.loads((package / "inventory.json").read_text())
    expected = set(index["files"]) | {"inventory.json"}
    actual = {str(path.relative_to(package)) for path in package.rglob("*") if path.is_file()}
    if actual != expected:
        raise ValueError(f"Package file-set mismatch: {sorted(actual ^ expected)}")
    for relative, info in index["files"].items():
        data = confined(package, relative).read_bytes()
        if digest(data) != info["sha256"] or len(data) != info["bytes"]:
            raise ValueError(f"Evidence bytes changed: {relative}")
    checks = json.loads((package / "check-log-bindings.json").read_text())
    for check in checks:
        receipt = json.loads(confined(package, check["receipt"]).read_text())
        log = confined(package, check["log"]).read_bytes()
        if check["gzip"]:
            log = gzip.decompress(log)
        if receipt["exit_code"] != 0 or digest(log) != receipt["log_sha256"]:
            raise ValueError(f"Successful check receipt/log mismatch: {check['receipt']}")
    references = json.loads((package / "protected-references.json").read_text())
    for relative, expected_sha in references["repository_files"].items():
        if digest(confined(args.repository, relative).read_bytes()) != expected_sha:
            raise ValueError(f"Historical repository reference changed: {relative}")
    application = references["historical_application"]
    archive = confined(args.repository, application["archive"]).read_bytes()
    receipt_bytes = confined(args.repository, application["receipt"]).read_bytes()
    receipt = json.loads(receipt_bytes)
    if (digest(archive) != application["archive_sha256"]
            or digest(receipt_bytes) != application["receipt_sha256"]
            or digest(gzip.decompress(archive)) != application["decompressed_sha256"]
            or application["decompressed_sha256"] != receipt["before_sha256"]):
        raise ValueError("Historical application archive/receipt binding failed")
    print(json.dumps({"status": "PASS", "package_files": len(index["files"]),
                      "repository_references": len(references["repository_files"]),
                      "successful_check_logs": len(checks),
                      "inventory_sha256": digest((package / "inventory.json").read_bytes()),
                      "writes": False}, indent=2))


if __name__ == "__main__":
    main()
