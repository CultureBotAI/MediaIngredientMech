"""No NEW ontology CURIE may be held by two live records (#414).

For a mapped MIM record the `identifier` **is** its ontology CURIE. Two live
records on one CURIE therefore assert that two different ingredients are the
same thing — the `Butane-1,4-diol` defect, generalised.

Nothing caught this before. `validate_sssom_invariants.py` checks Rules
A/B1/B2/B3/C over the SSSOM, none of which constrain identifier uniqueness among
records, and `check_visualization_currency.py` checks that every published node
names a record that exists — the converse. An identifier could be issued twice
and every gate stayed green; 32 had accumulated by the time #414 found them.

## Why an allow-list rather than a count

A bare threshold lets one collision be repaired and another introduced in the
same PR with no net change and no failure. Every currently-known collision is
named below with why it is still open, so a new one fails immediately and a
repaired one has to be struck off deliberately.

## Two shapes, needing opposite fixes

**Hydrate/anhydrous families** — `CuSO4` / `x 2 H2O` / `x 4 H2O`, `FeSO4` /
`x 5 H2O` / `x 6 H2O` and friends. These must NOT be merged: an anhydrous salt
and its hydrate have different formula weights and are ordered separately, and
`MAPPING_SEMANTICS` §"map to what you can order" says the orderability rule does
not license collapsing them. Each needs re-grounding to its own term or a mint.
They are detectable — the molecular formulas differ — and note the trap: the
records share a CAS because the anhydrous number was copied onto the hydrates.

**Distinct products sharing one term** — `Mannan from Saccharomyces cerevisiae`
against `b-Mannan ... carob seed`, `Mucin ... Type II` against `type III`,
Rhamnogalacturonan from soy against potato. These agree on CAS *and* formula
because the values were copied, so no chemistry test separates them. Human
reading does.
"""
from __future__ import annotations

import collections
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
COLLECTIONS = (
    REPO_ROOT / "data" / "curated" / "mapped_ingredients.yaml",
    REPO_ROOT / "data" / "curated" / "unmapped_ingredients.yaml",
)

# Known, unresolved collisions (#414). Each needs per-case curation; none may be
# merged blindly. Strike an entry off when it is fixed — never add one to make a
# test pass.
KNOWN = {
    # --- hydrate / anhydrous families: RE-GROUND, do not merge ---
    "CHEBI:23414",      # CuSO4 / x 2 H2O / x 4 H2O
    "CHEBI:31346",      # CaSO4 / x 7 H2O
    "CHEBI:31795",      # MgSO4 x 7 H2O / MgSO4·H2O
    "CHEBI:32036",      # K2SO4 / x 7 H2O
    "CHEBI:32599",      # Magnesium sulfate / MgSO4 x 6 H2O
    "CHEBI:6636",       # MgCl2 / MgCl2x 6 H2O  (records already carry DIFFERENT CAS)
    "CHEBI:75832",      # FeSO4 / x 5 H2O / x 6 H2O
    "CHEBI:86360",      # MnSO4 / x 7 H2O
    "CHEBI:86477",      # Na2SO3 / x 5 H2O
    "CHEBI:30769",      # Citric acid / Citric Acid·H2O
    # --- hydrate term holding an unqualified label: decide which the label means ---
    "CHEBI:86149",      # (NH4)2Ni(SO4)2 / x 6 H2O
    "CHEBI:86345",      # Magnesium chloride / MgCl2 x 6 H2O
    # --- a solution is not the solute ---
    "CHEBI:29377",      # Na2CO3 / Sodium carbonate solution
    # --- distinct products under one term: RE-GROUND or mint ---
    "FOODON:03315719",  # Casein peptone / Casamino acids
    "FOODON:03315720",  # Soy peptone / Soya peptone / Phytone / Soya pepton
    "MICRO:0000455",    # Algal / WC Trace Elements Solution
    "MICRO:0001363",    # Liver extract / concentrate / infusion
    "NCIT:C896",        # Trace element solution / SL-10 / Zeikus
    "cas:39280-21-2",   # Rhamnogalacturonan: soy bean vs potato
    "cas:84082-64-4",   # Mucin porcine stomach: Type II vs type III
    "cas:9036-88-8",    # Mannan: carob seed vs Saccharomyces cerevisiae
    "ENVO:00001998",    # CR1 Soil / Soil
    # --- brand-vs-generic: mergeable, but the brand may be worth keeping ---
    "ENVO:00002263",    # air-dried garden soil / Garden soil
    "MICRO:0000178",    # Bacto peptone / Peptone
    "MICRO:0000182",    # Bacto-tryptone / Tryptone / Tryptone peptone
    "MICRO:0000193",    # Bacto BHI / BHI / BHI broth
}


@pytest.fixture(scope="module")
def collisions() -> dict[str, list[str]]:
    live = collections.defaultdict(list)
    for path in COLLECTIONS:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for rec in data.get("ingredients", []):
            # REJECTED records are merge tombstones and deliberately carry the
            # WINNER's identifier, so they can never be a collision.
            if rec.get("mapping_status") != "MAPPED":
                continue
            identifier = str(rec.get("identifier") or "")
            if identifier and not identifier.startswith("UNMAPPED"):
                live[identifier].append(str(rec.get("preferred_term")))
    return {k: v for k, v in live.items() if len(v) > 1}


def test_no_new_identifier_collisions(collisions):
    """A CURIE held by two live records asserts two ingredients are one thing."""
    new = {k: v for k, v in collisions.items() if k not in KNOWN}
    assert not new, (
        f"{len(new)} ontology CURIE(s) are newly held by more than one live record "
        f"(#414). In MIM a mapped record's identifier IS its ontology CURIE, so this "
        f"asserts that different ingredients are the same thing.\n"
        f"{chr(10).join(f'  {k}: {v}' for k, v in list(new.items())[:5])}\n"
        f"Merge them if they are one substance, or re-ground one to its own term. "
        f"Do NOT add the identifier to KNOWN to make this pass."
    )


def test_the_known_backlog_does_not_grow(collisions):
    """The count may fall, never rise. 32 at #414; 26 after the first six merges."""
    assert len(collisions) <= 26, (
        f"{len(collisions)} identifier collisions, up from the recorded 26. "
        f"Something reintroduced one that was merged away."
    )


def test_known_entries_are_still_real(collisions):
    """Strike fixed entries off rather than letting the list rot.

    A stale allow-list is how a gate quietly stops covering what it names — the
    entry stays, the collision is gone, and nobody notices the list no longer
    describes the repo.
    """
    stale = sorted(KNOWN - set(collisions))
    assert not stale, (
        f"{len(stale)} entries in KNOWN are no longer collisions and should be "
        f"removed: {stale}"
    )
