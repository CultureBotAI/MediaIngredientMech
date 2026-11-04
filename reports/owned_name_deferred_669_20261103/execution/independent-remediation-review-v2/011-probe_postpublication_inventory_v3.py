"""Private fault injection; never publishes to the maintained worktree."""
from pathlib import Path
import datetime
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
W = RUN / "step8-aliases"
OPERATOR = HERE.parent / "promote_deferred_aliases_v2.py"
OUT = HERE / "postpublication-inventory-probe-v3"
assert not OUT.exists()
OUT.mkdir()
spec = importlib.util.spec_from_file_location("independent_deferred_publisher", OPERATOR)
op = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = op
exec(compile(OPERATOR.read_bytes(), str(OPERATOR), "exec"), op.__dict__)
assert op.digest(OPERATOR.read_bytes()) == "e2494b967f377ed1ce9053e0260a3e04a2aa0d374111b96e992bd92a332ae921"
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
    try:
        result = op.publish_prepared(private, apply=True)
    except ValueError as exc:
        rejected = str(exc)
    else:
        raise AssertionError("late source membership drift was accepted")
finally:
    publication.publish = original_publish
assert hook_called == [True]
fresh_inventory = context.source_inventory(fixture)
assert fresh_inventory != private["source_paths"]
assert late_owner.relative_to(fixture).as_posix() in fresh_inventory["data/ingredients"]
assert rejected == "Deferred owned-name publication: completed source membership changed"
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
    "immediate_completion_rejected": True,
    "rejection": rejected,
    "context_sha256": op.digest((W / "src/mediaingredientmech/owned_name_suppression_refresh.py").read_bytes()),
    "real_maintained_outputs_and_source_inventory_unchanged": True,
    "finding": "The exact independent late-owner counterexample is rejected immediately by corrected writer v2; original failure evidence remains immutable.",
    "scope": "Private reproduction of a completion-verification omission. The standalone CLI re-runs prepare and would catch later drift; that does not establish the immediate post-publication claim.",
}
(OUT / "result.json").write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
print("result_sha256", op.digest((OUT / "result.json").read_bytes()))
