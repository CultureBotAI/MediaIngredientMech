"""Private publisher/native-owner-chain continuity control."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import pytest

D = Path(__file__).resolve().parent
S = D / "publisher-snapshot-v2"
sys.path.insert(0, str(S / "src"))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


c = load("mediaingredientmech.campaign_publication", S / "src/mediaingredientmech/campaign_publication.py")
t = load("independent_chain_fixture", S / "tests/test_campaign_publication.py")
outcomes = []
for gap in (False, True):
    directory = D / "chain-preflight-fixtures-v3" / ("gap" if gap else "positive")
    directory.mkdir(parents=True)
    with pytest.MonkeyPatch.context() as monkey:
        case = t.case.__wrapped__(directory, monkey)
        root, plan = case["root"], case["plan"]
        owner = case["records"][0]
        last = c.sha(b"different current native owner endpoint") if gap else owner["before_yaml_sha256"]
        historical = {
            "schema_version": 1, "batch": "historical-owner", "sequence": 1,
            "approval": "NONE: fixture", "before_sha256": c.sha(case["before"]),
            "after_sha256": c.sha(case["before"]), "before_row_count": 2,
            "after_row_count": 2, "position_map": [1, 2], "changes": [],
            "changed_rows": 0, "added_rows": 0, "removed_rows": 0,
            "records": [{"source_record": owner["source_record"], "shape": "previous_edit",
                         "before_yaml_sha256": c.sha(b"prior historical owner"),
                         "after_yaml_sha256": last}],
        }
        name = t.native.RECEIPTS_DIR + "/history.json"
        p = t.put(root, name, historical)
        plan["receipt_prefix"][name] = c.sha(p.read_bytes())
        case["owner_proof"]["checkpoint"]["input_sha256"][name] = plan["receipt_prefix"][name]
        t.source_snapshots(root, case["owner_proof"])
        t.save(case)
        # Prove the starting native receipt chain is internally valid.
        proof = t.native.verify_mapping_chain(root)
        before_policy = (root / c.POLICY).read_bytes()
        row = {"case": "owner_chain_gap" if gap else "positive", "prefix_verified": True,
               "latest_native_owner_sha256": proof["owner_chains"][owner["source_record"]][-1]["after_sha256"],
               "proposed_before_owner_sha256": owner["before_yaml_sha256"]}
        try:
            row["dry_run"] = c.publish(root, case["path"], case["out"])["status"]
        except Exception as error:
            row["dry_run_error"] = type(error).__name__ + ": " + str(error)
        try:
            row["apply"] = c.publish(root, case["path"], case["out"], apply=True)["status"]
        except Exception as error:
            row["apply_error"] = type(error).__name__ + ": " + str(error)
        row["canonical_changed"] = (root / c.SOURCE).read_bytes() != case["before"]
        row["policy_changed"] = (root / c.POLICY).read_bytes() != before_policy
        row["publication_log"] = (case["out"] / "publication.json").read_text() if (case["out"] / "publication.json").exists() else None
        outcomes.append(row)
report = {"source_sha256": hashlib.sha256((S / "src/mediaingredientmech/campaign_publication.py").read_bytes()).hexdigest(), "scope": "Private synthetic author fixture; owner proof and generation isolated, actual native history/replay/receipt maker and canonical/policy writes. No corpus publication.", "results": outcomes}
with (D / "chain-preflight-probe-v3.json").open("x") as f:
    json.dump(report, f, indent=2)
    f.write("\n")
print(json.dumps(report, indent=2))
