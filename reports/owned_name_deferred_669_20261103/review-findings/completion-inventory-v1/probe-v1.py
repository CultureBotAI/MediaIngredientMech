"""Private fault injection; never publishes to the maintained worktree."""
from pathlib import Path
import datetime
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
W = RUN / "step8-aliases"
OPERATOR = HERE.parent / "promote_deferred_aliases_v1.py"
OUT = HERE / "postpublication-inventory-probe-v1"
assert not OUT.exists()
OUT.mkdir()
spec = importlib.util.spec_from_file_location("independent_deferred_publisher", OPERATOR)
op = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = op
exec(compile(OPERATOR.read_bytes(), str(OPERATOR), "exec"), op.__dict__)
assert op.digest(OPERATOR.read_bytes()) == "4c31a61fabda38cbb848bc636d9e42349283f2302ca2694419b546c707ef1a3e"
prepared = op.prepare(W, W / "output/next23-native-candidate-v1", RUN / "step7c-claw", "112e2303176db3530f88469f220367f14041d7ae9a84d879efe8623255e6fa34")
native, publication, context, chain = prepared["modules"]
original_source_inventory = context.source_inventory(W)
real_artifacts = {name: op.digest((W / name).read_bytes()) for name in prepared["before"]}
fixture = OUT / "private-fixture"
fixture.mkdir()
private = dict(prepared)
private["root"] = fixture
private["inputs"] = {
    fixture / path.relative_to(W) if path.is_relative_to(W) else path: raw
    for path, raw in prepared["inputs"].items()
}


def write_new(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(raw)


for path, raw in private["inputs"].items():
    if path.is_relative_to(fixture):
        write_new(path, raw)
for name, raw in private["before"].items():
    write_new(fixture / name, raw)
(fixture / op.LOG).parent.mkdir(parents=True)
late_owner = fixture / "data/ingredients/mapped/.late-independent-owner.yaml"
original_publish = publication.publish
hook_called = []


def add_owner_after_native_publication(*args, **kwargs):
    result = original_publish(*args, **kwargs)
    assert args[0] == fixture and kwargs.get("apply") is True
    write_new(late_owner, b"preferred_term: 2-deoxyadenosine\nidentifier: kgmicrobe.ingredient:late-independent-owner\nmapping_status: MAPPED\n")
    hook_called.append(True)
    return result


publication.publish = add_owner_after_native_publication
try:
    result = op.publish_prepared(private, apply=True)
finally:
    publication.publish = original_publish
assert hook_called == [True]
fresh_inventory = context.source_inventory(fixture)
assert fresh_inventory != private["source_paths"]
assert late_owner.relative_to(fixture).as_posix() in fresh_inventory["data/ingredients"]
assert result["completed_verification"]["state"] == "verified-complete"
assert context.source_inventory(W) == original_source_inventory
assert all(op.digest((W / name).read_bytes()) == expected for name, expected in real_artifacts.items())
assert not (W / op.LOG).exists() and not (W / op.RECEIPT).exists()
output = {
    "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "reviewer": "/root/step7d_independent_review",
    "operator_sha256": op.digest(OPERATOR.read_bytes()),
    "fault": "One ignored/hidden YAML owner appears after the native publication returns and before the operator's immediate verify_completed call.",
    "private_fixture": str(fixture),
    "late_owner": str(late_owner),
    "captured_ingredient_count": len(private["source_paths"]["data/ingredients"]),
    "actual_ingredient_count": len(fresh_inventory["data/ingredients"]),
    "source_inventory_changed": True,
    "immediate_completion_result": result["completed_verification"],
    "real_maintained_outputs_and_source_inventory_unchanged": True,
    "finding": "The immediate completion verifier returns verified-complete without checking the source path inventory after publication. Existing captured files and the receipt chain remain valid, so those checks do not detect the newly added owner.",
    "scope": "Private reproduction of a completion-verification omission. The standalone CLI re-runs prepare and would catch later drift; that does not establish the immediate post-publication claim.",
}
(OUT / "result.json").write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
print("result_sha256", op.digest((OUT / "result.json").read_bytes()))
