"""The CHEBI accession ceiling in `conf/id_label_targets.yaml` (#210).

`max_accession` decides which of two FATAL verdicts a curator is shown for an
id that already failed to resolve: `ID_OUT_OF_RANGE` ("beyond anything this
ontology mints — most likely from another registry") or the plain
`ID_NOT_FOUND`. Nothing passes or fails because of it; only the diagnosis
changes.

That makes it look cosmetic, and it is not. The ceiling was `CHEBI: 300000`,
below ChEBI's own range — the local semsql build already reaches accession
747618 — so every real term newer than the local build was reported as an
identifier wearing someone else's prefix. #193 acted on that wording and demoted
17 real ChEBI terms; 11 of them resolved locally the whole time (#197, #205).

These tests live HERE rather than in `tests/test_id_label_plausibility.py`
because that file is governed byte-identically from canonical claw (see
`scripts/check_vendored_sync.sh`); adding to it forks the vendored copy. They
assert properties of MIM's OWN config, which is not vendored, so this is the
right home for them regardless.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

_REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "validate_id_label_correspondence",
    _REPO / "scripts" / "validate_id_label_correspondence.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

# The highest accession present in the local semsql ChEBI build (release 252),
# measured directly against `~/.data/oaklib/chebi.db`. Recorded as a literal so
# the tests do not need the 3.9 GB artifact, which CI does not have.
LOCAL_BUILD_MAX_ACCESSION = 747618

# The six OLS4-verified antibiotics #193 demoted and #205/#207 had to untangle.
# Every one sits above the retired 300000 ceiling.
RESTORED_ANTIBIOTICS = {
    "CHEBI:753395": "lysostaphin",
    "CHEBI:756054": "carbomycin",
    "CHEBI:748901": "netilmicin",
    "CHEBI:759883": "colistin sulfate",
    "CHEBI:759086": "polymyxin B",
    "CHEBI:759884": "gentamicin",
}


class _FakeAdapter:
    """Minimal OAK stand-in: resolves only the terms it is given."""

    def __init__(self, terms: dict[str, str]):
        self._terms = terms

    def label(self, curie: str):
        return self._terms.get(curie)

    def entity_alias_map(self, curie: str):
        return {"oio:hasExactSynonym": []}

    def entity_metadata_map(self, curie: str):
        return {}


# gepotidacin is real, recent, and present in the local build — the case the old
# ceiling would have called foreign had it merely failed to resolve.
ADAPTER = _FakeAdapter({"CHEBI:747127": "gepotidacin"})


def _config() -> dict:
    return yaml.safe_load((_REPO / "conf" / "id_label_targets.yaml").read_text())


def _ceiling() -> int:
    """The CHEBI ceiling as actually shipped, never a literal repeated here.

    A test that hard-codes the number passes just as happily once the config
    drifts away from it — which is how 300000 survived being wrong.
    """
    return int(_config()["max_accession"]["CHEBI"])


def _classify(label: str, curie: str, ceiling: int | None = None) -> str:
    return mod.classify(
        curie=curie, label=label, adapter=ADAPTER,
        policy="canonical_or_synonym", scope="exact_related",
        label_waived=True, waiver_mode="plausible",
        max_accession=_ceiling() if ceiling is None else ceiling,
    )["verdict"]


def test_ceiling_clears_chebi_real_accession_range():
    """The ceiling must sit ABOVE ChEBI's range, not inside it.

    This is the defect itself: at 300000 the ceiling described neither ChEBI's
    accession space nor anything else, and terms ChEBI genuinely minted were
    reported as coming from another registry.
    """
    ceiling = _ceiling()
    assert ceiling > LOCAL_BUILD_MAX_ACCESSION, (
        f"ceiling {ceiling} is at or below the local build's own highest "
        f"accession ({LOCAL_BUILD_MAX_ACCESSION}) — every term newer than the "
        "build would be reported as a foreign identifier (#197)"
    )
    assert ceiling > max(int(c.split(":")[1]) for c in RESTORED_ANTIBIOTICS)


def test_ceiling_stays_below_pubchem_width():
    """It tracks the FOREIGN namespace's digit count, not ChEBI's growth.

    PubChem CIDs reach 8 digits. Raise the ceiling past that and
    `ID_OUT_OF_RANGE` can never fire, so the verdict becomes dead code rather
    than a lenient one.
    """
    assert _ceiling() < 10_000_000


@pytest.mark.parametrize("curie,label", sorted(RESTORED_ANTIBIOTICS.items()))
def test_restored_antibiotics_are_not_called_foreign(curie, label):
    """The six records #193 deleted must not be re-accused by the same rule.

    They do not resolve in the local build (it stops at 747618), so they still
    fail — as ID_NOT_FOUND, which says "not in this build". That is a fact about
    the build. ID_OUT_OF_RANGE asserts something about the identifier, and for
    these six that assertion is false: all six are real per OLS4.
    """
    assert _classify(label, curie) == "ID_NOT_FOUND"


def test_resolvable_above_old_ceiling_id_never_reaches_the_check():
    """The ceiling is a tie-breaker on ids that ALREADY failed to resolve.

    gepotidacin (CHEBI:747127) resolves and sits above the retired 300000, so it
    passes at either ceiling. Pinning the OLD value here too records that the
    ceiling was never what rejected these terms — a curator misreading a verdict
    was.
    """
    for ceiling in (300000, _ceiling()):
        assert _classify("gepotidacin", "CHEBI:747127", ceiling) == "OK_ID_ONLY"


def test_eight_digit_foreign_id_still_reports_out_of_range():
    """Raising the ceiling must not disarm the verdict it exists to produce."""
    assert _classify("Nicotinate", "CHEBI:10716816") == "ID_OUT_OF_RANGE"


def test_bogus_six_digit_id_is_still_fatal():
    """CHEBI:867561 (#170) is a genuine PubChem CID inside ChEBI's real range.

    A width heuristic cannot see it at ANY workable ceiling — which is the
    limitation #304 records. It must still fail, just under the other verdict.
    """
    verdict = _classify("Whatever", "CHEBI:867561")
    assert verdict == "ID_NOT_FOUND"
    assert verdict in mod._ERROR_VERDICTS


def test_both_ceiling_verdicts_are_fatal():
    """Neither diagnosis is advisory, so moving the ceiling cannot let data in.

    This is what makes the ceiling safe to raise: it selects wording, not
    outcome.
    """
    assert {"ID_NOT_FOUND", "ID_OUT_OF_RANGE"} <= mod._ERROR_VERDICTS


def test_config_ceilings_match_the_curie_module():
    """MIM carries two ceiling tables; they must not disagree.

    `src/mediaingredientmech/curie.py::MAX_ACCESSION` was corrected to 1_000_000
    while `conf/id_label_targets.yaml` stayed at 300000, so the same id could be
    called foreign by one gate and fine by the other (#210).
    """
    sys.path.insert(0, str(_REPO / "src"))
    try:
        from mediaingredientmech.curie import MAX_ACCESSION
    finally:
        sys.path.pop(0)
    conf = _config()["max_accession"]
    shared = set(conf) & set(MAX_ACCESSION)
    assert shared, "the two ceiling tables share no prefix — one has been renamed"
    for prefix in sorted(shared):
        assert int(conf[prefix]) == int(MAX_ACCESSION[prefix]), (
            f"{prefix} ceiling differs: conf/id_label_targets.yaml says "
            f"{conf[prefix]}, curie.py says {MAX_ACCESSION[prefix]}"
        )
