"""Independent real-evidence probes; no maintained writes; execute only after author freeze."""
from pathlib import Path
from copy import deepcopy
import argparse
import datetime
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
W = RUN / "step8-aliases"
BASE = "0ee56c11a2894ed50a476b331d56297be0a3ee12"
EVIDENCE = "reports/sssom_completion_20260921/mapping-evidence.json"
PRIOR = "reports/step7d_mapping_901_20261103/refresh-v2/companion-review.json"
CONTEXT = "src/mediaingredientmech/owned_name_suppression_refresh.py"
HELPER = "src/mediaingredientmech/ingredient_bundle_refresh.py"
TEST = "tests/test_owned_name_suppression_refresh.py"
POSITIONS = (926, 927, 2610, 2611, 3013, 3014)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2) + "\n").encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--context-sha256", required=True)
    parser.add_argument("--helper-sha256", required=True)
    parser.add_argument("--tests-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    expected_code = {CONTEXT: args.context_sha256, HELPER: args.helper_sha256, TEST: args.tests_sha256}
    for name, expected in expected_code.items():
        assert sha((W / name).read_bytes()) == expected, name
    plan = json.loads((HERE / "continuation-rereview-plan-v1.json").read_text())
    for name, expected in plan["pinned_stable_inputs"].items():
        assert sha((W / name).read_bytes()) == expected, name
    sys.path[:0] = [str(W), str(W / "src")]
    from mediaingredientmech import ingredient_bundle_refresh as refresh
    from mediaingredientmech import owned_name_suppression_refresh as policy
    from mediaingredientmech.validation.mapping_change_receipts import verify_mapping_chain

    cache = {}
    def historical(name):
        if name not in cache:
            cache[name] = subprocess.check_output(["git", "-C", str(W), "show", BASE + ":" + name])
        return cache[name]

    def historical_unchanged(name):
        raw = historical(name)
        assert (W / name).read_bytes() == raw, ("historical authority changed", name)
        return raw

    prior = json.loads((W / PRIOR).read_bytes())
    assert (W / PRIOR).read_bytes() == historical(PRIOR)
    before = {name: historical(name) for name in refresh.source_names(prior)}
    current = {name: (W / name).read_bytes() for name in before}
    context = refresh.OwnedNameSuppressionContext(W, BASE, sha(current[policy.MANIFEST]))
    actual_proof = policy.verify_owned_name_suppression(prior, before, current, context)
    assert actual_proof["scientific_approval_added"] is False
    proof = verify_mapping_chain(W)
    assert len(proof["receipts"]) == 26
    old_entries = json.loads(historical(EVIDENCE))["entries"]
    new_entries = json.loads((W / EVIDENCE).read_bytes())["entries"]
    results = [{"case": "public-context-real-baseline-and-current", "outcome": "passed", "input_count": len(actual_proof["input_sha256"])}]

    def check(position, name, *, mutate_old=None, mutate_new=None, owner=None, altered_proof=None, reader=None):
        old, new = deepcopy(old_entries[str(position)]), deepcopy(new_entries[str(position)])
        if mutate_old:
            mutate_old(old)
        if mutate_new:
            mutate_new(new)
        owner_hash = owner or sha((W / old_entries[str(position)]["owner_record"]).read_bytes())
        try:
            policy._continued_form_evidence(old, new, position, owner_hash, altered_proof or proof, reader or historical_unchanged)
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            if name == "valid-native-continuation":
                raise
            results.append({"position": position, "case": name, "outcome": "rejected", "error": str(exc)})
        else:
            assert name == "valid-native-continuation", ("unexpected acceptance", position, name)
            results.append({"position": position, "case": name, "outcome": "passed"})

    def suffix(entry):
        return entry["basis"]["form_followup"]["continuation"][-1]

    for position in POSITIONS:
        check(position, "valid-native-continuation")
        for key, bad in (("sequence", 25), ("path", "reports/forged-receipt.json"), ("sha256", "0" * 64), ("before_position", position + 1), ("after_position", position + 1)):
            check(position, "forged-suffix-" + key, mutate_new=lambda e, k=key, b=bad: suffix(e).__setitem__(k, b))
        check(position, "missing-suffix", mutate_new=lambda e: e["basis"]["form_followup"]["continuation"].pop())
        check(position, "extra-suffix", mutate_new=lambda e: e["basis"]["form_followup"]["continuation"].append(deepcopy(suffix(e))))
        check(position, "changed-earlier-prefix", mutate_new=lambda e: e["basis"]["form_followup"]["continuation"][0].__setitem__("sha256", "0" * 64))
        check(position, "changed-historical-prefix", mutate_old=lambda e: e["basis"]["form_followup"]["continuation"][0].__setitem__("sha256", "0" * 64))
        check(position, "changed-checkpoint", mutate_new=lambda e: e["basis"]["form_followup"]["checkpoint"].__setitem__("after_sha256", "0" * 64))
        check(position, "changed-native-authority-binding", mutate_new=lambda e: e["basis"]["form_followup"]["native_review"].__setitem__("sha256", "0" * 64))
        check(position, "changed-row-hash", mutate_new=lambda e: e.__setitem__("row_sha256", "0" * 64))
        check(position, "changed-owner-hash", owner="0" * 64)
        check(position, "changed-disposition", mutate_new=lambda e: e.__setitem__("disposition", "WITHHOLD" if e["disposition"] == "SUPPORTED" else "SUPPORTED"))
        check(position, "changed-review-reason", mutate_new=lambda e: e.__setitem__("review_reason", "invented replacement scientific basis"))
        check(position, "extra-basis-evidence", mutate_new=lambda e: e["basis"].__setitem__("invented", "extra support"))
        touched = dict(proof)
        touched["receipts"] = [*proof["receipts"][:-1], {**proof["receipts"][-1], "changes": [*proof["receipts"][-1]["changes"], {"before_position": position}]}]
        check(position, "native-row-touched-after-checkpoint", altered_proof=touched)
        altered = dict(proof)
        altered["state"] = list(proof["state"])
        altered["state"][position - 1] = {**proof["state"][position - 1], "object_id": "CHEBI:999999"}
        check(position, "native-current-row-changed", altered_proof=altered)
        authority_path = old_entries[str(position)]["basis"]["form_followup"]["file"]
        def forged_authority(name, target=authority_path):
            raw = historical_unchanged(name)
            if name == target:
                doc = json.loads(raw)
                doc["checkpoint"]["sha256"] = "0" * 64
                return encoded(doc)
            return raw
        check(position, "changed-earlier-authority-checkpoint", reader=forged_authority)

    position = 927
    receipt_path = proof["receipt_paths"][-1]
    def receipt_map(entry):
        return entry["basis"]["superseded_scoped_review"]["receipt_inputs"]
    check(position, "missing-receipt-input-extension", mutate_new=lambda e: receipt_map(e).pop(receipt_path))
    check(position, "forged-receipt-input-extension", mutate_new=lambda e: receipt_map(e).__setitem__(receipt_path, "0" * 64))
    previous_path = proof["receipt_paths"][0]
    check(position, "changed-earlier-receipt-input", mutate_new=lambda e: receipt_map(e).__setitem__(previous_path, "0" * 64))
    check(position, "extra-receipt-input", mutate_new=lambda e: receipt_map(e).__setitem__("reports/forged-receipt.json", "0" * 64))
    no_form = next(int(k) for k, entry in old_entries.items() if "form_followup" not in entry.get("basis", {}) and entry == new_entries[k])
    check(no_form, "valid-native-continuation")
    check(no_form, "new-authority-on-unrelated-entry", mutate_new=lambda e: e["basis"].__setitem__("form_followup", deepcopy(old_entries["926"]["basis"]["form_followup"])))
    for name, expected in expected_code.items():
        assert sha((W / name).read_bytes()) == expected, name
    for name, expected in plan["pinned_stable_inputs"].items():
        assert sha((W / name).read_bytes()) == expected, name
    report = {"reviewer": "/root/step7d_independent_review", "at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1133", "code_sha256": expected_code, "pinned_stable_inputs": plan["pinned_stable_inputs"], "results": results, "passed": sum(x["outcome"] == "passed" for x in results), "expected_rejections": sum(x["outcome"] == "rejected" for x in results), "limitations": ["Positive public context uses actual baseline/current snapshots and full native replay. Negative differential probes call the bounded helper with copies of real entries/proof; they are not full CLI tests.", "No maintained file was modified. Complete native CLI refresh and final head checks remain separately required."]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("xb") as stream:
        stream.write(encoded(report))
    print(json.dumps({"output": str(args.output), "sha256": sha(args.output.read_bytes()), "passed": report["passed"], "expected_rejections": report["expected_rejections"]}, indent=2))


if __name__ == "__main__":
    main()
