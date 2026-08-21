"""Refuse to accept a hydrate label onto a non-hydrate term (#243).

The automated curation path normalises `MgSO4•7H2O` to `MgSO4`, searches on the
normalised string, and accepts whatever it finds — so a hydrate lands on its
anhydrous parent with the original filed as a `HYDRATE_FORM` synonym. That is
the identity collapse MAPPING_SEMANTICS.md Section 3 forbids: `MgSO4·7H2O` is
246.47 g/mol against 120.37, which is the number a medium recipe depends on. It
produced the 32 families of #218 and the 53 records `just
report-hydrate-grounding` still lists.

Stripping is still right — it is how you find the *family*. What must not happen
is accepting the family's parent as if it were the hydrate.

The check needs no ontology database: a candidate's own label and synonyms
almost always say whether it is a hydrate ("magnesium sulfate heptahydrate",
"ceftazidime pentahydrate").

Pass `formula_lookup` to catch terms whose LABEL is silent but whose formula
carries water -- `CHEBI:185255 Ammonium alum` is `Al.12H2O.H4N.2O4S`, and 181
ChEBI terms are like it. Without it those are refused wrongly. It is optional
because the guard must work where no ChEBI build exists.

The converse -- label says hydrate, formula does not (`CHEBI:182320 Glycocholic
acid hydrate`, C26H43NO6) -- is handled by the label check, and is usually a
COVALENT hydrate (chloral hydrate, sabinene hydrate), a different concept from
water of crystallisation that this guard does not try to distinguish.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Protocol

# Water of crystallisation in an ingredient label: 'x 7 H2O', 'x n H2O',
# '·7H2O', '7H2O', and hydrate words with or without a multiplier prefix.
# Deliberately NOT a bare /hydrate/ substring -- that matches 'borohydrate' in
# 'b-Mannan borohydrate reduced carob seed', which is not a hydrate.
# Separators seen in this corpus: x · • ・(U+30FB) ⋅(U+22C5) ∙(U+2219) ×(U+00D7)
# and a plain '.'. A separator is REQUIRED before H2O -- without one, 'H2O4P'
# (dihydrogenphosphate) and 'H2O2' would match.
_SEP = r"[x×·•・⋅∙.]"
HYDRATE_NOTATION = re.compile(
    rf"{_SEP}\s*(?:\d+|n)?\s*H2\s*O(?![0-9])"  # MgSO4·7H2O, NiCl2・H2O, FeSO4.H2O
    rf"|{_SEP}?\s*\(\s*H2\s*O\s*\)\s*[n\d]"  # VOSO4(H2O)n
    r"|\d\s*H2\s*O(?![0-9])"  # 7H2O with no separator
    r"|(?<![a-z])(?:hemi|sesqui|mono|di|tri|tetra|penta|hexa|hepta|octa|nona|deca|dodeca)*"
    r"hydrate\b",
    re.IGNORECASE,
)

# Water as its own component of a formula: 'Mg.O4S.7H2O', '(H2O)n.O5SV'.
# A bare 'H2O' substring would match 'H2O4P' -- dihydrogenphosphate, no water.
FORMULA_WATER = re.compile(r"(?:^|\.)\(?[\dn]*H2O\)?n?(?:\.|$)")


# Greek multipliers ChEBI and catalogues use, as numbers. `hexahydrate` and
# `6 H2O` are the same state; comparing raw tokens reports respellings as
# mismatches.
_MULTIPLIER = {
    "hemi": "0.5",
    "sesqui": "1.5",
    "mono": "1",
    "di": "2",
    "tri": "3",
    "tetra": "4",
    "penta": "5",
    "hexa": "6",
    "hepta": "7",
    "octa": "8",
    "nona": "9",
    "deca": "10",
    "undeca": "11",
    "dodeca": "12",
}

# A digit multiplier must be preceded by a separator, whitespace or the string
# start. Without that guard `AlCl3.6H2O` reads as "3.6" -- the aluminium
# subscript captured as part of the multiplier. The hyphen forms (`ZnSO4-7H2O`)
# occur in the corpus too, so `-` and the Unicode minus are separators (#256).
_DIGIT_WATER = re.compile(
    r"(?:^|[x\u00d7\u00b7\u2022\u30fb\u22c5\u2219.\-\u2212\s])(\d+)\s*H2\s*O(?![0-9])",
    re.IGNORECASE,
)
# `hemipentahydrate` is hemi x penta = 2.5 waters, so the fraction prefix is
# matched separately from the count rather than as one alternative.
_FRACTION = {"hemi": 0.5, "sesqui": 1.5}
_COUNT = {k: v for k, v in _MULTIPLIER.items() if k not in _FRACTION}
_WORD_WATER = re.compile(
    r"(?<![a-z])(hemi|sesqui)?(" + "|".join(sorted(_COUNT, key=len, reverse=True)) + r")?hydrate\b",
    re.IGNORECASE,
)


def water_multiplicity(text: str) -> str | None:
    """How many waters the label states, or None when it does not state one (#254).

    None means "unspecified", NOT monohydrate -- a bare `hydrate` or `x n H2O`
    says nothing, and treating it as 1 invents mismatches against records that
    genuinely say 6. It is also returned for genuinely ambiguous strings like
    `CaCl22H2O`, where nothing distinguishes the subscript from the multiplier.

    Word forms win over digits: `dihydrochloride pentahydrate` is a
    pentahydrate, and its digits belong to neither.

    Returns a decimal string so `hemi` (0.5) and `sesqui` (1.5) round-trip.
    """
    text = str(text or "")
    for word_match in _WORD_WATER.finditer(text):
        frac, count = word_match.group(1), word_match.group(2)
        if not frac and not count:
            continue  # a bare `hydrate` states nothing
        value = float(_COUNT[count.lower()]) if count else 1.0
        if frac:
            value *= _FRACTION[frac.lower()]
        return f"{value:g}"
    digit_match = _DIGIT_WATER.search(text)
    if digit_match:
        return digit_match.group(1)
    return None


class _Candidate(Protocol):
    ontology_id: str
    label: str
    synonyms: list[str]


class HydrateMismatch(ValueError):
    """Accepting this mapping would put a hydrate label on a non-hydrate term."""


def is_hydrate_label(text: str) -> bool:
    return bool(HYDRATE_NOTATION.search(str(text or "")))


def term_is_hydrate(
    candidate: _Candidate,
    formula_lookup: Callable[[str], str | None] | None = None,
) -> bool:
    """Does the candidate term itself denote a hydrate?"""
    if is_hydrate_label(candidate.label):
        return True
    if any(is_hydrate_label(s) for s in (getattr(candidate, "synonyms", None) or [])):
        return True
    if formula_lookup is not None:
        formula = formula_lookup(candidate.ontology_id)
        if formula and FORMULA_WATER.search(formula):
            return True
    return False


def hydrate_mismatch(
    record_label: str,
    candidate: _Candidate,
    formula_lookup: Callable[[str], str | None] | None = None,
) -> str | None:
    """Reason to refuse, or None if the mapping is fine.

    Only fires in one direction: a hydrate label onto a term that is not a
    hydrate. The reverse (an anhydrous label onto a hydrate term) is a different
    defect and is not this guard's job -- see #242.
    """
    if not is_hydrate_label(record_label):
        return None
    if term_is_hydrate(candidate, formula_lookup):
        return None
    return (
        f"{record_label!r} names a hydrate but {candidate.ontology_id} "
        f"({candidate.label!r}) does not. Accepting it would collapse a distinct "
        "substance onto its anhydrous parent — a different formula weight, which is "
        "what a medium recipe depends on. Per MAPPING_SEMANTICS.md Section 3: use a "
        "hydrate-specific term if one exists, else give the record its own "
        "cas:<hydrate CAS> with a narrowMatch to this term plus the Rule B1 registry "
        "row. Pass allow_hydrate_mismatch=True only if you have checked and this "
        "really is the right term."
    )
