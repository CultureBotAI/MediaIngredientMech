"""An audit receipt cannot renew a scientific review after owner bytes change."""

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ASSEMBLER_PATH = ROOT / "reports/sssom_completion_20260921/assemble_review.py"
SPEC = importlib.util.spec_from_file_location("strict_approval_chain_assembler", ASSEMBLER_PATH)
assembler = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(assembler)


@pytest.mark.parametrize("stem", ["Aromatic_Compound", "Arsenate"])
def test_mapping_change_receipt_cannot_renew_corrected_identity_approval(monkeypatch, stem):
    """Keep the row and parsed record unchanged, but change its exact YAML bytes.

    A later mapping-change receipt can account for the new owner hash in the
    audit chain. It must not extend the earlier, explicit identity approval.
    Mock reads only: the real records and historical receipts remain intact.
    """
    owner = ROOT / f"data/ingredients/mapped/{stem}.yaml"
    before = owner.read_bytes()
    after = before + b"\n"
    before_sha = hashlib.sha256(before).hexdigest()
    after_sha = hashlib.sha256(after).hexdigest()
    receipt_dir = ASSEMBLER_PATH.parent / "mapping_changes"
    receipt_path = max(
        receipt_dir.glob("*.json"), key=lambda path: json.loads(path.read_text())["sequence"]
    )
    receipt_before = receipt_path.read_bytes()
    receipt = json.loads(receipt_before)
    receipt["records"].append(
        {
            "source_record": str(owner.relative_to(ROOT)),
            "before_yaml_sha256": before_sha,
            "after_yaml_sha256": after_sha,
        }
    )
    receipt_after = (json.dumps(receipt, indent=2) + "\n").encode()
    replacements = {owner: after, receipt_path: receipt_after}
    original_read_bytes = Path.read_bytes
    original_read_text = Path.read_text

    def read_bytes(path):
        return replacements[path] if path in replacements else original_read_bytes(path)

    def read_text(path, *args, **kwargs):
        if path in replacements:
            return replacements[path].decode()
        return original_read_text(path, *args, **kwargs)

    with monkeypatch.context() as reads:
        reads.setattr(Path, "read_bytes", read_bytes)
        reads.setattr(Path, "read_text", read_text)
        with pytest.raises(
            ValueError, match="Explicit corrected identity review has stale owner bytes"
        ):
            assembler.assemble()

    assert owner.read_bytes() == before
    assert receipt_path.read_bytes() == receipt_before
