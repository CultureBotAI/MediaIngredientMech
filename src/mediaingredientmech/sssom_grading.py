"""How a mapping's quality becomes its SSSOM `confidence` and `mapping_justification`.

Two things can write these columns: MIM's own promotion helpers, and claw's
`build_mim_ingredient_sssom.py`, which regenerates the whole file. When they disagree,
whichever ran last wins and the columns flip back and forth across rebuilds with nothing
gating or reporting it -- measured on one promotion as 205 rows moving 0.99 -> 0.9, 49
moving 0.95 -> 0.99, and 189 justification flips, on a diff that otherwise showed zero
identity changes (#519).

**claw's rules are canonical here**, because claw is the generator: it rebuilds every row
from the records, so any value MIM writes that disagrees survives only until the next
build. Mirroring its rules is what makes a rebuild a no-op instead of a rewrite.

The two rules, and why they are what they are:

`SYNONYM_MATCH` is graded 0.99, not 0.95. MIM's schema glosses it "Matches known synonym
in ontology", which says how the term was *located*, not that the identity is
approximate -- `CLOSE_MATCH` is the value reserved for "semantically close but not
exact". A row found through an exact synonym is an exact identity claim, and it already
carries `skos:exactMatch`, so grading it below a label match contradicted its own
predicate.

Justification is derived, not asserted. A row found by string equality is
`semapv:LexicalMatching`; anything that needed a judgement is
`semapv:ManualMappingCuration`. MIM's writers used to hardcode the latter, which
described 107 records created by exact string matching as hand-curated.

Kept in step with claw by `tests/test_sssom_grading.py`, which reads claw's own constants
when the sibling checkout is present and skips when it is not -- the same shape as the
SSSOM validator's Rule B4.
"""

from __future__ import annotations

# Qualities that denote an exact identity, and so earn exact-match confidence.
EXACT_QUALITIES = frozenset({"EXACT_MATCH", "SYNONYM_MATCH"})

# Qualities reached by string equality rather than by a curator's judgement.
LEXICAL_QUALITIES = frozenset({"EXACT_MATCH", "LEXICAL_MATCH", ""})

CONFIDENCE_EXACT = "0.99"
CONFIDENCE_OTHER = "0.9"

JUSTIFICATION_LEXICAL = "semapv:LexicalMatching"
JUSTIFICATION_MANUAL = "semapv:ManualMappingCuration"


def confidence_for(quality: str | None) -> str:
    """SSSOM `confidence` for a record's `mapping_quality`."""
    return CONFIDENCE_EXACT if (quality or "") in EXACT_QUALITIES else CONFIDENCE_OTHER


def justification_for(quality: str | None) -> str:
    """SSSOM `mapping_justification` for a record's `mapping_quality`."""
    return JUSTIFICATION_LEXICAL if (quality or "") in LEXICAL_QUALITIES else JUSTIFICATION_MANUAL


# Dict view for the writers that index by grade. Every grade the corpus uses must be
# present: a KeyError here is a write that never happens, so a missing key is worse than
# a wrong value. Derived from the rule above so the two cannot disagree.
KNOWN_QUALITIES = (
    "EXACT_MATCH",
    "SYNONYM_MATCH",
    "CLOSE_MATCH",
    "NARROW_MATCH",
    "BROAD_MATCH",
    "LEXICAL_MATCH",
    "CAS_RN_LOOKUP",
    "MANUAL_CURATION",
    "LLM_ASSISTED",
    "PROVISIONAL",
    "FALLBACK_REGISTRY",
)

CONFIDENCE = {quality: confidence_for(quality) for quality in KNOWN_QUALITIES}
JUSTIFICATION = {quality: justification_for(quality) for quality in KNOWN_QUALITIES}
