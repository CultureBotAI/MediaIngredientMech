"""Retained private controls for the deferred23 publisher; never apply to W."""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

D = next(p for p in Path(__file__).resolve().parents if (p / "promote_deferred_aliases_v2.py").is_file())
RUN = D.parent
W = RUN / "step8-aliases"
C = Path(__file__).resolve().parent
OPERATOR = D / "promote_deferred_aliases_v2.py"
PIN = "112e2303176db3530f88469f220367f14041d7ae9a84d879efe8623255e6fa34"
spec = importlib.util.spec_from_file_location("deferred23_controlled_operator", OPERATOR)
op = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = op
exec(compile(OPERATOR.read_bytes(), str(OPERATOR), "exec"), op.__dict__)


def write_new(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(raw)


def main():
    assert not (C / "results.json").exists(), "Retain old controls; use a new run directory"
    p = op.prepare(W, W / "output/next23-native-candidate-v1", RUN / "step7c-claw", PIN)
    native, publication, context, chain = p["modules"]
    before = p["before"]
    plan = p["plan"]
    source = {str(path.relative_to(W)): raw for path, raw in p["inputs"].items() if path.is_relative_to(W)}
    rows = []
    real_inputs = {str(path): op.digest(raw) for path, raw in p["inputs"].items()}
    real_outputs = {name: op.digest(op.regular(W / name)) for name in before}
    write_new(C / "real-preflight-inputs.json", op.encoded(real_inputs))
    write_new(C / "real-preflight-output-preimages.json", op.encoded(real_outputs))
    def record(name, call, expected_error=None):
        try:
            result = call()
        except Exception as error:
            if expected_error is None:
                raise
            assert expected_error in str(error), (name, expected_error, repr(error))
            rows.append({"name": name, "outcome": "rejected", "exception": type(error).__name__, "message": str(error)})
        else:
            assert expected_error is None, name + " unexpectedly succeeded"
            rows.append({"name": name, "outcome": "passed", "detail": result})
    def project(pairs):
        return op.build_projection(before[op.SSSOM], before[op.SIDECAR], before[op.BASELINE], pairs, plan["policy_evidence"], p["producer"])
    def changed_pair(field, value):
        pairs = copy.deepcopy(plan["pairs"])
        pairs[0][field] = value
        return lambda: project(pairs)
    record("valid-three-artifact-projection", lambda: {str(k): op.digest(v) for k,v in project(plan["pairs"]).items()})
    record("wrong-plan-pin", lambda: op.prepare(W, p["bundle"], p["producer"], "0"*64), "caller plan hash differs")
    bad = copy.deepcopy(plan["pairs"]);bad[0]["baseline_row"]["token"] = "wrong-token"
    record("wrong-token", lambda: project(bad), "complete baseline")
    record("wrong-position", changed_pair("source_position", plan["pairs"][0]["source_position"]+1), "stale subject/token/row payload")
    record("boolean-position", changed_pair("source_position", True), "invalid source position")
    record("extra-other-edit", changed_pair("after_other", "invented-extra-token"), "another raw token")
    record("extra-origin", changed_pair("input_surfaces", ["prior_sssom", "yaml"]), "extra origin")
    bad = copy.deepcopy(plan);bad["pairs"][0]["credited_owners"][0]["subject_id"] = "MIM:Wrong_Owner"
    record("wrong-preferred-owner", lambda: context._pairs(bad,before,{str(k):v for k,v in p["outputs"].items()},source), "native credited owner set differs")
    import yaml
    multi_plan, multi_source = copy.deepcopy(plan), dict(source)
    selected_paths = {x["source_owner"]["path"] for x in plan["pairs"]}
    selected_paths.update(o["path"] for x in plan["pairs"] for o in x["credited_owners"])
    extra_name = next(name for name in sorted(source) if name.startswith("data/ingredients/mapped/") and name not in selected_paths)
    extra = yaml.safe_load(source[extra_name]); extra["preferred_term"] = plan["pairs"][0]["baseline_row"]["token"]
    multi_source[extra_name] = yaml.safe_dump(extra,allow_unicode=True,sort_keys=False).encode()
    from mediaingredientmech.curie import mim_curie_for_stem
    additional = {"subject_id":mim_curie_for_stem(Path(extra_name).stem),"path":extra_name,"sha256":op.digest(multi_source[extra_name])}
    multi_plan["pairs"][0]["credited_owners"].append(additional)
    multi_plan["pairs"][0]["credited_owners"].sort(key=lambda item:item["subject_id"])
    record("complete-multi-owner-credit-fixture", lambda: len(context._pairs(multi_plan,before,{str(k):v for k,v in p["outputs"].items()},multi_source)[2]))
    incomplete = copy.deepcopy(multi_plan); incomplete["pairs"][0]["credited_owners"].remove(additional)
    record("incomplete-multi-owner-credit", lambda: context._pairs(incomplete,before,{str(k):v for k,v in p["outputs"].items()},multi_source), "native credited owner set differs")
    origin_plan, origin_source = copy.deepcopy(plan), dict(source)
    pair = origin_plan["pairs"][0]; name = pair["source_owner"]["path"]
    owner = yaml.safe_load(origin_source[name]); owner.setdefault("synonyms", []).append({"synonym_text":pair["baseline_row"]["token"]})
    origin_source[name] = yaml.safe_dump(owner,allow_unicode=True,sort_keys=False).encode()
    pair["source_owner"]["sha256"] = op.digest(origin_source[name])
    record("new-yaml-origin", lambda: context._pairs(origin_plan,before,{str(k):v for k,v in p["outputs"].items()},origin_source), "fresh YAML origin requires new scope")
    # A private file is read through a pointer to the producer's Git metadata.
    # No Git metadata is written: HEAD/show are read-only and use the actual pin.
    producer_fixture = C / "producer-drift-fixture"
    producer_fixture.mkdir()
    gitdir = op.git(p["producer"], "rev-parse", "--absolute-git-dir").decode().strip()
    write_new(producer_fixture / ".git", ("gitdir: " + gitdir + "\n").encode())
    producer_policy = "src/kg_microbe_utils/owned_name_policy.py"
    write_new(producer_fixture / producer_policy, op.regular(p["producer"] / producer_policy) + b"\n# private drift control\n")
    record("producer-source-drift-at-same-head", lambda: op.render_events([], producer_fixture), "differs from pinned source")
    no_git = C / "wrong-producer-fixture";no_git.mkdir()
    # The native pin cannot be obtained from an arbitrary directory inside another repo.
    record("wrong-producer-head", lambda: op.render_events([], no_git), "wrong producer revision")
    fixture = C / "publication-fixture"
    fixture.mkdir()
    fp = dict(p);fp["root"] = fixture
    fp["inputs"] = {fixture/path.relative_to(W) if path.is_relative_to(W) else path:raw for path,raw in p["inputs"].items()}
    for path, raw in fp["inputs"].items():
        if path.is_relative_to(fixture):
            write_new(path, raw)
    for name, raw in before.items():
        write_new(fixture/name,raw)
    (fixture/op.LOG).parent.mkdir(parents=True)
    def outputs_unchanged():
        assert all(op.regular(fixture/name)==raw for name,raw in before.items())
        assert not os.path.lexists(fixture/op.RECEIPT)
    record("private-dry-run", lambda: {k:v for k,v in op.publish_prepared(fp).items() if k in {"applied","changed","output_sha256"}})
    outputs_unchanged()
    assert not os.path.lexists(fixture/op.LOG)
    marker = b"occupied private output; must remain intact\n"
    write_new(fixture/op.LOG, marker)
    record("occupied-publication-log", lambda: op.publish_prepared(fp,apply=True), "publication output already occupied")
    outputs_unchanged();assert (fixture/op.LOG).read_bytes()==marker
    (fixture/op.LOG).rename(C/"occupied-log-preserved.txt")
    write_new(fixture/op.RECEIPT, marker)
    record("occupied-new-receipt", lambda: op.publish_prepared(fp,apply=True), "publication output already occupied")
    assert all(op.regular(fixture/name)==raw for name,raw in before.items())
    (fixture/op.RECEIPT).rename(C/"occupied-receipt-preserved.txt")
    canonical = fixture/op.SSSOM
    canonical.rename(C/"canonical-symlink-target.tsv")
    canonical.symlink_to(C/"canonical-symlink-target.tsv")
    record("canonical-symlink-alias", lambda: op.publish_prepared(fp,apply=True), "aliased path")
    assert (C/"canonical-symlink-target.tsv").read_bytes()==before[op.SSSOM]
    canonical.unlink();(C/"canonical-symlink-target.tsv").rename(canonical)
    os.link(canonical,C/"canonical-hardlink-target.tsv")
    record("canonical-hardlink-alias",lambda: op.publish_prepared(fp,apply=True),"single regular file")
    (C/"canonical-hardlink-target.tsv").unlink();outputs_unchanged()
    # Occupy a backup after native preflight, immediately before held reservation.
    original_reserve = publication.guarded.reserve_receipt_outputs
    target_backup = next(iter(op.backups(fixture/op.LOG,before)))
    def occupied_reserve(*args,**kwargs):
        write_new(target_backup,marker)
        return original_reserve(*args,**kwargs)
    publication.guarded.reserve_receipt_outputs = occupied_reserve
    try:
        record("backup-reservation-race-before-first-write", lambda: op.publish_prepared(fp,apply=True), "exist")
    finally:
        publication.guarded.reserve_receipt_outputs = original_reserve
    outputs_unchanged();assert target_backup.read_bytes()==marker
    (fixture/op.LOG).parent.rename(C/"failed-reservation-application")
    (fixture/op.LOG).parent.mkdir()
    result = op.publish_prepared(fp,apply=True)
    record("private-apply",lambda: {k:v for k,v in result.items() if k in {"applied","changed","output_sha256","completed_verification"}})
    record("private-completed-verification",lambda:op.verify_completed(fp,fixture/op.LOG))
    saved = op.read_json(op.regular(fixture/op.LOG))
    journal = Path(saved["transaction"]["journal"])
    original_journal, original_log = journal.read_bytes(),(fixture/op.LOG).read_bytes()
    forged = json.loads(original_journal);forged["created"] = []
    forged_raw = json.dumps(forged,indent=2,sort_keys=True).encode();journal.write_bytes(forged_raw)
    saved["journal_sha256"] = op.digest(forged_raw);(fixture/op.LOG).write_bytes(op.encoded(saved))
    record("forged-empty-created-journal",lambda:op.verify_completed(fp,fixture/op.LOG),"native completed journal differs")
    write_new(C/"rejected-forged-journal.json",forged_raw)
    journal.write_bytes(original_journal);(fixture/op.LOG).write_bytes(original_log)
    record("completed-restored-exact-journal",lambda:op.verify_completed(fp,fixture/op.LOG))
    # Durable all-input/no-real-write verification, not merely an assertion about the fixture.
    assert {name:op.digest(op.regular(W/name)) for name in before} == real_outputs
    assert not os.path.lexists(W/op.RECEIPT) and not os.path.lexists(W/op.LOG)
    assert all(op.digest(op.regular(Path(name)))==sha for name,sha in real_inputs.items())
    result = {"schema_version":1,"operator_sha256":op.digest(OPERATOR.read_bytes()),
              "control_source_sha256":op.digest(Path(__file__).read_bytes()),"plan_sha256":PIN,
              "real_maintained_outputs_unchanged":True,"controls":rows,
              "passed_controls":len(rows),"private_fixture":str(fixture),
              "private_completed_log_sha256":op.digest(original_log),"private_completed_journal_sha256":op.digest(original_journal)}
    write_new(C/"results.json",op.encoded(result))
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
