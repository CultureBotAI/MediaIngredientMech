"""External controls for the frozen Step7d source plan; no maintained writes.

Native transaction applications below use private temporary fixture trees only.
Actual source-operator calls use dry-run. This is not scientific approval.
"""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import os
import tempfile

D = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("step7d_owner_controls", D / "apply_reviewed_owners.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
from mediaingredientmech.validation.write_validated import ValidationFailedError
W = m.ROOT
PLAN_SHA = "a82bc6d32e750f16fc7ecfa4c0a5e172a5930c849d7dc3ec5a6ca106ed60fca4"
passed = []


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def reject(name, operation):
    try:
        operation()
    except (ValueError, FileExistsError, KeyError, TypeError, IndexError, ValidationFailedError):
        passed.append(name)
        return
    raise AssertionError("Accepted invalid case: " + name)


def main():
    plan_raw = (D / "owner-plan.json").read_bytes()
    assert sha(plan_raw) == PLAN_SHA
    plan = json.loads(plan_raw)
    paths = m.policy.ingredient_paths(W)
    before_inputs = {p: p.read_bytes() for p in paths}
    before_inputs.update({W / name: (W / name).read_bytes() for name in plan["auxiliary"]})
    assert len(plan["owners"]) == 38
    assert {g: sum(x["group"] == g for x in plan["owners"].values())
            for g in ("1117-carbonate", "1117-maltose", "901")} == {
                "1117-carbonate": 1, "1117-maltose": 1, "901": 36}
    assert not (set(plan["auxiliary"]) & (set(plan["evidence_sha256"]) | set(plan["protected_sha256"])))
    proposed = {}
    for name, item in plan["owners"].items():
        old = before_inputs[W / name]
        new = m.propose(old, item, plan["timestamp"])
        assert new == (D / "owner-previews" / Path(name).name).read_bytes()
        oldrecord, newrecord = map(m.yaml.safe_load, (old, new))
        assert newrecord["curation_history"][:-1] == oldrecord.get("curation_history", [])
        assert len(newrecord["curation_history"]) == len(oldrecord.get("curation_history", [])) + 1
        for field in m.PROTECTED_FIELDS:
            assert oldrecord.get(field) == newrecord.get(field)
        proposed[name] = newrecord
    passed.append("all38 outputs reproduce native validated previews; history appended once; roles/status/occurrences preserved")
    current_ids = {str(p.relative_to(W)): m.yaml.safe_load(raw).get("identifier")
                   for p, raw in before_inputs.items() if p in paths}
    after_ids = {name: proposed[name]["identifier"] if name in proposed else identity
                 for name, identity in current_ids.items()}
    for name, item in plan["owners"].items():
        identity = after_ids[name]
        if identity != item["before_identifier"]:
            assert all(other == name or not isinstance(value, str) or value.casefold() != identity.casefold()
                       for ids in (current_ids, after_ids) for other, value in ids.items())
    passed.append("all promoted identities unique against complete base/current inventories including casefold")
    name, item = next(iter(plan["owners"].items()))
    raw = before_inputs[W / name]
    reject("stale owner preimage", lambda: m.propose(raw + b"\n", item, plan["timestamp"]))
    changed = copy.deepcopy(item)
    changed["before_identifier"] = "wrong:identity"
    reject("wrong owner identity", lambda: m.propose(raw, changed, plan["timestamp"]))
    changed = copy.deepcopy(item)
    changed["operations"][0]["before"] = "not the actual preimage"
    reject("wrong field preimage", lambda: m.propose(raw, changed, plan["timestamp"]))
    changed = copy.deepcopy(item)
    changed["operations"][0]["before_exists"] = not changed["operations"][0]["before_exists"]
    reject("wrong field presence", lambda: m.propose(raw, changed, plan["timestamp"]))
    changed = copy.deepcopy(item)
    changed["operations"][0]["path"] = ["nutritional_roles"]
    reject("role edit forbidden", lambda: m.propose(raw, changed, plan["timestamp"]))
    changed = copy.deepcopy(item)
    changed["operations"][0]["path"] = ["curation_history"]
    reject("history edit forbidden", lambda: m.propose(raw, changed, plan["timestamp"]))
    changed = copy.deepcopy(item)
    changed["operations"] = []
    reject("no-op history event forbidden", lambda: m.propose(raw, changed, plan["timestamp"]))
    changed = copy.deepcopy(item)
    changed["after_sha256"] = "0" * 64
    reject("wrong reviewed output hash", lambda: m.propose(raw, changed, plan["timestamp"]))
    broken = m.yaml.safe_load(raw)
    broken["unreviewed_unknown_schema_field"] = True
    reject("native writer rejects unknown schema field", lambda: m.render(broken))

    for name, stages in plan["auxiliary"].items():
        raw = before_inputs[W / name]
        for stage in stages:
            before = raw
            raw = m.propose_auxiliary(name, before, stage)
            assert raw == (D / "auxiliary-previews" / stage["group"] / Path(name).name).read_bytes()
            for migration in stage["migrations"]:
                item = plan["owners"][migration["owner_path"]]
                assert item["group"] == stage["group"]
                assert item["before_identifier"] == migration["before_identifier"]
                assert proposed[migration["owner_path"]]["identifier"] == migration["after_identifier"]
            reject("stale auxiliary preimage " + name + "/" + stage["group"],
                   lambda: m.propose_auxiliary(name, before + b"\n", stage))
            bad = copy.deepcopy(stage)
            bad["group"] = "1117-carbonate"
            reject("wrong auxiliary group " + name + "/" + stage["group"],
                   lambda: m.propose_auxiliary(name, before, bad))
            bad = copy.deepcopy(stage)
            bad["migrations"][0]["owner_path"] = "data/ingredients/mapped/Other.yaml"
            reject("wrong auxiliary owner " + name + "/" + stage["group"],
                   lambda: m.propose_auxiliary(name, before, bad))
            bad = copy.deepcopy(stage)
            bad["after_sha256"] = "0" * 64
            reject("wrong auxiliary output " + name + "/" + stage["group"],
                   lambda: m.propose_auxiliary(name, before, bad))
            if name.endswith("culturemech_recipe_membership.tsv"):
                target = stage["migrations"][0]["after_identifier"]
                collision = before + (target + "\tfixture-recipe\t1\n").encode()
                bad = copy.deepcopy(stage)
                bad["before_sha256"] = sha(collision)
                reject("destination membership collision " + stage["group"],
                       lambda: m.propose_auxiliary(name, collision, bad))
            else:
                bad = copy.deepcopy(stage)
                bad["migrations"][0]["before_row"]["ingredient_name"] = "Wrong owner label"
                reject("ledger exact owner/source pairing " + stage["group"],
                       lambda: m.propose_auxiliary(name, before, bad))
        passed.append("exact two-stage auxiliary replay and selected owner coupling: " + name)

    with tempfile.TemporaryDirectory(prefix="mim-step7d-operator-controls-") as directory:
        temp = Path(directory).resolve()
        original = temp / "single.txt"
        original.write_bytes(b"single")
        symlink = temp / "alias.txt"
        symlink.symlink_to(original)
        reject("symlink input alias", lambda: m.regular(symlink))
        hardlink = temp / "hardlink.txt"
        os.link(original, hardlink)
        reject("hardlink input alias", lambda: m.regular(original))
        for case in ("receipt-existing", "backup-existing", "journal-existing", "receipt-symlink", "success"):
            root = temp / case
            root.mkdir()
            owner = root / "owner.txt"
            reference = root / "reference.txt"
            owner.write_bytes(b"before owner\n")
            reference.write_bytes(b"before reference\n")
            external = temp / (case + "-evidence")
            external.mkdir()
            log = external / "receipt.json"
            backup = external / "before-owner.txt"
            if case == "receipt-existing":
                log.write_bytes(b"preserve prior receipt")
            elif case == "backup-existing":
                backup.write_bytes(b"preserve prior backup")
            elif case == "journal-existing":
                m.publication._journal_path(log).mkdir()
            elif case == "receipt-symlink":
                target = external / "prior.json"
                target.write_bytes(b"preserve alias target")
                log.symlink_to(target)
            operation = lambda: m.publication.publish(
                root, {Path("owner.txt"): b"after owner\n", Path("reference.txt"): b"after reference\n"},
                {owner: b"before owner\n", reference: b"before reference\n"}, log,
                {backup: b"before owner\n"}, {"fixture_only": True}, apply=True)
            if case != "success":
                reject("native publication reserves " + case + " before mutation", operation)
                assert owner.read_bytes() == b"before owner\n" and reference.read_bytes() == b"before reference\n"
                if case == "receipt-existing":
                    assert log.read_bytes() == b"preserve prior receipt"
                elif case == "backup-existing":
                    assert backup.read_bytes() == b"preserve prior backup"
                elif case == "receipt-symlink":
                    assert target.read_bytes() == b"preserve alias target"
            else:
                result = operation()
                assert result["applied"] is True
                saved = json.loads(log.read_bytes())
                assert saved["state"] == "complete" and saved["applied"] is True
                assert owner.read_bytes() == b"after owner\n" and reference.read_bytes() == b"after reference\n"
                assert backup.read_bytes() == b"before owner\n"
                m.publication.completed_journal(root, log, saved, previous={
                    Path("owner.txt"): b"before owner\n", Path("reference.txt"): b"before reference\n"})
                passed.append("native guarded paired publication and completed recovery journal in private fixture")
        result = m.execute(D / "owner-plan.json", PLAN_SHA, "1117-carbonate", temp / "actual-dry.json", apply=False)
        assert result["applied"] is False and not (temp / "actual-dry.json").exists()
        passed.append("actual frozen carbonate source plan native dry-run without receipt or source write")
        reject("901 cannot run before maltose auxiliary phase",
               lambda: m.execute(D / "owner-plan.json", PLAN_SHA, "901", temp / "wrong-order.json", apply=False))
    assert all(path.read_bytes() == raw for path, raw in before_inputs.items())
    passed.append("all maintained owners and both auxiliary files byte-identical after controls")
    print(json.dumps({"passed": len(passed), "controls": passed, "plan_sha256": PLAN_SHA,
                      "operator_sha256": sha((D / "apply_reviewed_owners.py").read_bytes()),
                      "maintained_writes": False, "github_mutations": False,
                      "private_temporary_fixture_transactions_only": True}, indent=2))


if __name__ == "__main__":
    main()
