"""Assemble separately authored worker-02 fragments without scientific inference.

Run from the worktree root after the three primary authors finish. The external
whole-shard auditor remains the authoritative structural check. This helper
rejects duplicate/missing cases and duplicate fragment IDs rather than guessing
which author's payload to keep. It does not mark independent review complete,
combine competing owner proposals, edit maintained data, or clear any hold.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_SHARD_SHA256 = "993e393b8a50e6061e4a9863bd60b3ab2a48ee584907a97e3066c1cbc03d6db0"


def read_rows(path: Path, key: str) -> list[dict]:
    value = json.loads(path.read_text())
    rows = value if isinstance(value, list) else value[key]
    if not isinstance(rows, list):
        raise ValueError(f"{path}: {key} must be a list")
    return rows


def require_unique(rows: list[dict], key: str) -> None:
    seen = set()
    for row in rows:
        value = row[key]
        if value in seen:
            raise ValueError(f"duplicate {key}: {value}")
        seen.add(value)


def collect(root: Path = ROOT) -> dict[str, dict]:
    shard_bytes = (root / "context/frozen-shard-02.json").read_bytes()
    if hashlib.sha256(shard_bytes).hexdigest() != EXPECTED_SHARD_SHA256:
        raise ValueError("frozen shard bytes changed")
    shard = json.loads(shard_bytes)
    cases = shard["cases"]
    result = {}
    for key, id_key in (
        ("decisions", "case_id"),
        ("evidence", "evidence_id"),
        ("proposals", "proposal_id"),
    ):
        rows = []
        for author in ("a", "b", "c"):
            rows.extend(read_rows(root / author / f"{key}.json", key))
        require_unique(rows, id_key)
        result[key] = {"schema_version": 1, key: rows}
    expected = [case["case_id"] for case in cases]
    observed = {row["case_id"] for row in result["decisions"]["decisions"]}
    if observed != set(expected):
        raise ValueError(
            f"case accounting differs: missing={set(expected) - observed}; "
            f"extra={observed - set(expected)}"
        )
    by_case = {row["case_id"]: row for row in result["decisions"]["decisions"]}
    result["decisions"].update(
        worker_slot=2,
        shard_sha256=EXPECTED_SHARD_SHA256,
        phase="shard",
        decisions=[by_case[case_id] for case_id in expected],
    )
    return result


if __name__ == "__main__":
    assembled = collect()
    for key, value in assembled.items():
        output = ROOT / f"{key}.json"
        if output.exists():
            raise FileExistsError(f"Refusing to overwrite reviewed assembly: {output}")
    for key, value in assembled.items():
        (ROOT / f"{key}.json").write_text(
            json.dumps(value, ensure_ascii=False, indent=2) + "\n"
        )
    print({key: len(value[key]) for key, value in assembled.items()})
