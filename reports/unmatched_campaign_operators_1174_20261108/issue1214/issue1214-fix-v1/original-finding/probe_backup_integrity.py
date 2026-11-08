"""Narrow private recovery-backup probe; no real campaign or integration writes."""

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

from mediaingredientmech import campaign_publication as c


HERE = Path(__file__).absolute().parent
PACKAGE = HERE / "exact-head-package"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


spec = importlib.util.spec_from_file_location(
    "private_publication_fixture", PACKAGE / "tests/test_campaign_publication.py"
)
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)

results = []
for attack in (None, "canonical-before.tsv", "policy-before.json"):
    name = "positive" if attack is None else "inplace-" + attack
    workspace = HERE / "fixtures" / name
    workspace.mkdir(parents=True)
    with pytest.MonkeyPatch.context() as patch:
        case = fixture.case.__wrapped__(workspace, patch)
        original = c.finish_receipt
        mutation = {}

        def wrapped(handle, path, payload, recheck):
            if attack is not None and not mutation:
                backup = case["out"] / attack
                info = backup.stat()
                before = backup.read_bytes()
                backup.write_bytes(b"CORRUPTED PRIVATE RECOVERY BACKUP\n")
                after_info = backup.stat()
                mutation.update(
                    path=str(backup.relative_to(HERE)),
                    original_sha256=sha(before),
                    corrupt_sha256=sha(backup.read_bytes()),
                    same_inode=(info.st_dev, info.st_ino)
                    == (after_info.st_dev, after_info.st_ino),
                    phase="immediately before the real native finish_receipt call",
                )
            return original(handle, path, payload, recheck)

        patch.setattr(c, "finish_receipt", wrapped)
        outcome = {"case": name, "attack": attack}
        try:
            publication = c.publish(case["root"], case["path"], case["out"], apply=True)
            verification = c.validate(case["root"], case["path"])
            log = json.loads((case["out"] / "publication.json").read_bytes())
            native_receipt = json.loads(
                (case["root"] / publication["receipt_path"]).read_bytes()
            )
            outcome.update(
                returned_status=publication["status"],
                separate_validator_status=verification["status"],
                publication_log_status=log["status"],
                native_receipt_approval=native_receipt["approval"],
                native_receipt_sha256=sha(
                    (case["root"] / publication["receipt_path"]).read_bytes()
                ),
            )
        except Exception as error:
            outcome["error"] = type(error).__name__ + ": " + str(error)
        outcome["mutation"] = mutation
        outcome["backup_checks"] = []
        for filename, role in (
            ("canonical-before.tsv", "canonical"),
            ("policy-before.json", "policy"),
        ):
            expected = case["plan"]["before"][role]
            original_before = case["root"] / expected["path"]
            backup = case["out"] / filename
            outcome["backup_checks"].append(
                {
                    "backup": filename,
                    "expected_sha256": expected["sha256"],
                    "actual_backup_sha256": sha(backup.read_bytes()),
                    "backup_matches_beforeimage": sha(backup.read_bytes()) == expected["sha256"],
                    "immutable_plan_beforeimage_still_valid": sha(original_before.read_bytes())
                    == expected["sha256"],
                }
            )
        results.append(outcome)

report = {
    "head": "4c8a987da40d48cceeb4390550f1ff7545927a0b",
    "publisher_sha256": sha(Path(c.__file__).read_bytes()),
    "fixture_sha256": sha((PACKAGE / "tests/test_campaign_publication.py").read_bytes()),
    "scope": "Exact copied publisher and native code; existing synthetic fixture explicitly mocks owner proof and native generation. Actual projection, policy, receipt maker/replay, output reservation and publication/validation execute inside worker-private fixtures only.",
    "results": results,
    "limits": "Immutable plan beforeimages remain intact and provide independent recovery evidence. No maintained source, real canonical publication, scientific approval, suite run or integration-worktree writes.",
}
(HERE / "backup-integrity-probe-result.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
