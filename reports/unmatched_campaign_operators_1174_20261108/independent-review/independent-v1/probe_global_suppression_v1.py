"""Use native alias policy and Rule K around a private bounded publisher fixture."""
from pathlib import Path
import importlib.util
import json
import sys
import pytest

D = Path(__file__).resolve().parent
S = D / "snapshot-v1"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


c = load("mediaingredientmech.campaign_publication", S / "src/mediaingredientmech/campaign_publication.py")
t = load("independent_suppression_fixture", S / "tests/test_campaign_publication.py")
policy = load("independent_native_owned_policy", D / "native-checks/owned_name_policy.py")
rules = load("independent_native_sssom_rules", D / "native-checks/validate_sssom_invariants.py")
directory = D / "global-suppression-fixture-v1"
directory.mkdir()
with pytest.MonkeyPatch.context() as monkey:
    case = t.case.__wrapped__(directory, monkey)
    root, plan = case["root"], case["plan"]
    before = t.sssom([t.row("A"), t.row("Unrelated", "CHEBI:9", other="B")])
    t.put(root, c.SOURCE, before)
    t.put(root, plan["before"]["canonical"]["path"], before)
    plan["before"]["canonical"]["sha256"] = c.sha(before)
    old_policy = json.loads((root / c.POLICY).read_bytes())
    old_policy["artifacts"][c.SOURCE] = c.sha(before)
    t.put(root, c.POLICY, old_policy)
    t.put(root, plan["before"]["policy"]["path"], old_policy)
    plan["before"]["policy"]["sha256"] = c.sha((root / c.POLICY).read_bytes())
    t.history(root, before)
    plan["native_context"] = {p: c.sha((root / p).read_bytes()) for p in t.native.HISTORICAL_CONTEXT}
    case["owner_proof"]["checkpoint"]["input_sha256"] = {**plan["native_context"], c.SOURCE: c.sha(before)}
    case["owner_proof"]["protected_snapshot"]["input_sha256"][c.POLICY] = plan["before"]["policy"]["sha256"]
    kept, events = policy.filter_owned_aliases(
        "MIM:Unrelated",
        [policy.AliasCandidate("B", "prior_sssom", ("fixture-prior-row",), ("fixture-primary",))],
        policy.build_owner_index({"MIM:B": {"identifier": "CHEBI:2", "preferred_term": "B"}, "MIM:Unrelated": {"identifier": "CHEBI:9", "preferred_term": "Unrelated"}}),
    )
    assert not kept and len(events) == 1
    sidecar = policy.render_suppressed_aliases(events)
    t.put(root, plan["generation"]["sidecar"]["path"], sidecar)
    plan["generation"]["sidecar"]["sha256"] = c.sha(sidecar)
    t.save(case)

    def generation(capture, actual_plan, old, inventory):
        assert old == before
        a, b, m = (capture.ref(actual_plan["generation"][key]) for key in ("candidate", "sidecar", "manifest"))
        return a, b, json.loads(m)

    monkey.setattr(c, "_generation", generation)
    prepared = c.prepare(root, case["path"])
    result = c.publish(root, case["path"], case["out"])
    rules.INGREDIENTS_DIR = root / "data/ingredients/mapped"
    rules.OTHER_BASELINE = root / c.BASELINE
    candidate = (root / plan["generation"]["candidate"]["path"]).read_bytes()
    rejected_candidate = list(rules.evaluate_rule_k(c.table(candidate)[2]))
    rejected_projection = list(rules.evaluate_rule_k(c.table(prepared["canonical"])[2]))
    report = {"publisher_dry_run": result["status"], "selected_owners": [r["source_record"] for r in case["records"]], "native_suppression": sidecar.decode(), "native_candidate_rule_k_rejects": rejected_candidate, "projected_canonical_rule_k_rejects": rejected_projection, "canonical_not_written": (root / c.SOURCE).read_bytes() == before, "scope": "Native owned-name policy and actual MIM Rule K evaluator; publisher owner proof/native generation are explicit synthetic fixture boundaries. No data publication or maintained writes."}
with (D / "global-suppression-probe-v1.json").open("x") as f:
    json.dump(report, f, indent=2)
    f.write("\n")
print(json.dumps(report, indent=2))
