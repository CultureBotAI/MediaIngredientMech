"""Read-only proof of the old typed-context history-schema obstruction."""
from pathlib import Path
import copy
import hashlib
import json
from mediaingredientmech.ingredient_bundle_refresh import (
    FormProjectionContext, RegistryCorrectionContext, StockCasRemovalContext,
    POLICY_MANIFEST, verify_form_projection, verify_registry_correction,
    verify_stock_cas_removal,
)

R = Path(__file__).resolve().parent
W = R.parent / "worktree"
raw = (W / POLICY_MANIFEST).read_bytes()
manifest = json.loads(raw)
assert "owned_name_suppression_updates" in manifest
head = "0dac278466699129a083343a921c2e0ca18a9ab4"
outcomes = []
for cls, verifier in [
    (FormProjectionContext, verify_form_projection),
    (RegistryCorrectionContext, verify_registry_correction),
    (StockCasRemovalContext, verify_stock_cas_removal),
]:
    for mode in ("actual_current_history", "private_control_without_owned_history"):
        value = copy.deepcopy(manifest)
        if mode != "actual_current_history":
            del value["owned_name_suppression_updates"]
        content = json.dumps(value).encode()
        context = cls(W, head, hashlib.sha256(content).hexdigest())
        try:
            verifier({}, {POLICY_MANIFEST: content}, {POLICY_MANIFEST: content}, context)
        except ValueError as exc:
            outcome = str(exc)
        else:
            raise AssertionError("Incomplete fixture unexpectedly accepted")
        expected = ("Form projection: unknown manifest shape" if mode == "actual_current_history"
                    else "Form projection: expected exactly one append with preserved history")
        assert outcome == expected, (cls.__name__, mode, outcome)
        outcomes.append({"context": cls.__name__, "mode": mode, "result": outcome})
result = {
    "source_sha256": hashlib.sha256((W / "src/mediaingredientmech/ingredient_bundle_refresh.py").read_bytes()).hexdigest(),
    "current_manifest_sha256": hashlib.sha256(raw).hexdigest(),
    "outcomes": outcomes,
    "scope": "The private control is diagnostic only. Removing retained history is not a proposed remedy. No complete successor transition or scientific review is claimed.",
    "maintained_manifest_unchanged": (W / POLICY_MANIFEST).read_bytes() == raw,
}
with (R / "typed-history-proof-v1.json").open("x") as stream:
    json.dump(result, stream, indent=2)
print(json.dumps(result, indent=2))
