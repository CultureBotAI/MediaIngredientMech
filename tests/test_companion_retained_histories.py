"""#1150: older typed successors retain later history without bypassing append checks."""

from copy import deepcopy
from pathlib import Path

import pytest

from mediaingredientmech import ingredient_bundle_refresh as refresh
from mediaingredientmech.ingredient_bundle_contract import content_sha256, read_json

ROOT = Path(__file__).resolve().parents[1]
CONTEXTS = (
    (refresh.FormProjectionContext, refresh.verify_form_projection),
    (refresh.RegistryCorrectionContext, refresh.verify_registry_correction),
    (refresh.StockCasRemovalContext, refresh.verify_stock_cas_removal),
)
HISTORIES = ("owned_name_suppression_updates", "source_alias_addition_updates")


def documents():
    old = read_json((ROOT / refresh.POLICY_MANIFEST).read_bytes())
    for key in HISTORIES:
        old[key] = [{"sequence": 1, "approval": "NONE"}, {"sequence": 2, "approval": "NONE"}]
    return old, deepcopy(old)


def invoke(context, verifier, old, new):
    before, current = refresh.encode(old), refresh.encode(new)
    execution = context(ROOT, "0dac278466699129a083343a921c2e0ca18a9ab4", content_sha256(current))
    return verifier(
        {}, {refresh.POLICY_MANIFEST: before}, {refresh.POLICY_MANIFEST: current}, execution
    )


@pytest.mark.parametrize("context,verifier", CONTEXTS)
def test_stable_histories_reach_the_still_required_native_append_guard(context, verifier):
    old, new = documents()
    # This deliberately incomplete fixture must NOT pass a full transition.
    # It proves that retained histories no longer fail the unrelated shape gate.
    with pytest.raises(ValueError, match="expected exactly one append with preserved history"):
        invoke(context, verifier, old, new)


@pytest.mark.parametrize("context,verifier", CONTEXTS)
@pytest.mark.parametrize("history", HISTORIES)
@pytest.mark.parametrize("mutation", ["delete", "introduce", "alter", "reorder", "bool", "type"])
def test_other_history_cannot_change(context, verifier, history, mutation):
    old, new = documents()
    if mutation == "delete":
        del new[history]
    elif mutation == "introduce":
        del old[history]
    elif mutation == "alter":
        new[history][0]["approval"] = "SUPPORTED"
    elif mutation == "reorder":
        new[history].reverse()
    elif mutation == "bool":
        new[history][0]["sequence"] = True
    else:
        old[history] = new[history] = {"invalid": "not a list"}
    with pytest.raises(ValueError, match="other typed update history changed"):
        invoke(context, verifier, old, new)
