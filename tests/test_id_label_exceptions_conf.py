"""Guard: the curator-accepted MeSH-SCR exceptions stay wired on every gated
surface in conf/id_label_targets.yaml.

These four are valid MeSH supplementary-concept records absent from the cached
sqlite:obo:mesh adapter (see the conf comment). With the id↔label gate now
BLOCKING (label-correspondence workflow → `just validate-products`), dropping an
exception would turn the gate red on correct data. This pins the wiring without
touching OAK (pure YAML/load_config — CI-safe).
"""

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "validate_id_label_correspondence",
    Path(__file__).parent.parent / "scripts" / "validate_id_label_correspondence.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

CONF = Path(__file__).parent.parent / "conf" / "id_label_targets.yaml"

# (id, label) pairs that must be accepted as OK_EXCEPTION on every gated surface.
EXPECTED = {
    ("mesh:C000709627", "avocatin b"),
    ("mesh:C000655964", "cholinium lysinate"),
    ("mesh:C000730144", "sodium glutarate"),
    ("mesh:C000633628", "plicacetin"),
}
GATED_TARGETS = {"curated_yaml", "sssom", "mapped_csv"}


def _targets():
    cfg = mod.load_config(CONF)
    return {t.get("name"): t for t in cfg["targets"]}


def test_gated_targets_declare_all_mesh_scr_exceptions():
    targets = _targets()
    for name in GATED_TARGETS:
        assert name in targets, f"gated target {name!r} missing from conf"
        got = mod.load_exceptions(targets[name])
        missing = EXPECTED - got
        assert not missing, f"{name} is missing exception(s): {sorted(missing)}"


def test_exception_label_matching_is_normalized():
    # load_exceptions normalizes labels, so a different casing/spacing still
    # matches the same id — but a *different* label is not silently accepted.
    ex = mod.load_exceptions(_targets()["sssom"])
    assert ("mesh:C000709627", mod.normalize("Avocatin  B")) in ex
    assert ("mesh:C000709627", mod.normalize("not the label")) not in ex
