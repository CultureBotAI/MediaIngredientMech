"""`cas_rn` must reject EC/EINECS numbers (#287).

The two registries are distinguishable by shape alone:

    CAS-RN      NNNNNNN-NN-N   2-7 digits, exactly 2, exactly 1 check digit
    EC/EINECS   NNN-NNN-N      3-3-1

The original pattern `^\\d+-\\d+-\\d+$` matched BOTH, so thirteen EC numbers
reached `chemical_properties.cas_rn` — mostly via `fetch_cas_rn_from_pubchem`,
which reads records that carry both identifiers.

Six were caught in #114 by cross-checking against ChEBI CAS dbxrefs. The other
seven sit on terms that publish no dbxref, so **no semantic check could reach
them** — only the format could. That is the argument for validating shape rather
than meaning, and it is why this pattern is worth a test of its own.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

SCHEMA = (Path(__file__).resolve().parent.parent
          / "src" / "mediaingredientmech" / "schema" / "mediaingredientmech.yaml")


def _cas_patterns() -> list[str]:
    """Every `cas_rn` pattern in the schema — there is one per class that has the slot."""
    doc = yaml.safe_load(SCHEMA.read_text())
    found = []
    for cls in (doc.get("classes") or {}).values():
        for name, attr in (cls.get("attributes") or {}).items():
            if name == "cas_rn" and attr.get("pattern"):
                found.append(attr["pattern"])
    return found


def test_the_slot_is_constrained_everywhere_it_appears():
    """ChemicalProperties and the evidence row both carry cas_rn.

    Constraining one and not the other leaves a door open, and the evidence row
    is written by the CAS-RN cross-reference resolver — exactly the automated
    path that produced the bad values.
    """
    pats = _cas_patterns()
    assert len(pats) >= 2, f"expected a pattern on every cas_rn slot, found {len(pats)}"
    assert len(set(pats)) == 1, f"cas_rn patterns disagree: {set(pats)}"


@pytest.mark.parametrize("ec", [
    "200-059-4", "200-194-9", "200-400-7", "211-682-6", "215-794-6",
    "222-793-4", "231-153-3",   # the seven only the format could catch
    "226-214-6", "233-788-1", "219-452-7", "200-416-4", "203-742-5", "205-358-3",
])
def test_ec_numbers_are_rejected(ec):
    """Every EC number that actually reached the data must fail the pattern."""
    rx = re.compile(_cas_patterns()[0])
    assert not rx.match(ec), f"{ec} is an EC number and must not validate as a CAS-RN"


@pytest.mark.parametrize("cas", [
    "50-99-7",        # glucose — the 2-digit lower bound
    "110-16-7",       # maleic acid
    "7775-14-6",      # sodium dithionite
    "10361-37-2",     # barium chloride
    "6381-92-6",      # EDTA disodium dihydrate
    "1075236-89-3",   # gepotidacin — the 7-digit upper bound, from #114/PR #112
])
def test_real_cas_numbers_are_accepted(cas):
    """A tightened pattern is only worth having if it passes legitimate data.

    1075236-89-3 matters: it is 7 digits, so a stricter upper bound would break a
    grounding this repo already relies on.
    """
    rx = re.compile(_cas_patterns()[0])
    assert rx.match(cas), f"{cas} is a real CAS-RN and must validate"


def test_the_corpus_has_no_remaining_ec_numbers():
    """Guards the data, not just the schema — a fixture cannot drift from reality."""
    rx = re.compile(_cas_patterns()[0])
    root = SCHEMA.resolve().parent.parent.parent.parent
    offenders = []
    for coll in ("mapped", "unmapped"):
        doc = yaml.safe_load((root / "data" / "curated"
                              / f"{coll}_ingredients.yaml").read_text())
        for rec in doc.get("ingredients") or []:
            val = ((rec.get("chemical_properties") or {}).get("cas_rn") or "").strip()
            if val and not rx.match(val):
                offenders.append((rec.get("preferred_term"), val))
    assert not offenders, f"non-CAS values still in cas_rn: {offenders[:5]}"
