"""Keep MIM's SSSOM grading in step with claw's, which is the generator.

Two things write `confidence` and `mapping_justification`: MIM's promotion helpers and
claw's `build_mim_ingredient_sssom.py`. claw rebuilds every row from the records, so any
value MIM writes that disagrees survives only until the next build and then flips back.
Measured on one promotion with zero identity changes: 205 rows 0.99 -> 0.9, 49 rows
0.95 -> 0.99, 189 justification flips (#519).

The cross-repo checks read claw at the sibling path and skip when it is absent — the
same shape as the SSSOM validator's Rule B4, which needs kg-microbe's transforms.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO / "src"))

from mediaingredientmech import sssom_grading as grading  # noqa: E402

CLAW_BUILDER = (
    _REPO.parent / "culturebotai-claw" / "scripts" / "build_mim_ingredient_sssom.py"
)


class TestTheRulesThemselves:
    def test_synonym_match_is_an_exact_identity_claim(self):
        """It already carries skos:exactMatch; grading it lower contradicted that.

        MIM's schema glosses SYNONYM_MATCH "Matches known synonym in ontology", which
        says how the term was located, not that the identity is approximate.
        CLOSE_MATCH is the value reserved for "close but not exact".
        """
        assert grading.confidence_for("SYNONYM_MATCH") == grading.CONFIDENCE_EXACT
        assert grading.confidence_for("EXACT_MATCH") == grading.CONFIDENCE_EXACT

    @pytest.mark.parametrize(
        "quality", ["CLOSE_MATCH", "NARROW_MATCH", "CAS_RN_LOOKUP", "FALLBACK_REGISTRY"]
    )
    def test_everything_else_is_graded_below_exact(self, quality):
        """CAS_RN_LOOKUP matters here: it identifies through a dbxref, not a label."""
        assert grading.confidence_for(quality) == grading.CONFIDENCE_OTHER

    def test_a_lexical_hit_is_not_described_as_hand_curated(self):
        """107 records created by exact string matching were published as manual."""
        assert grading.justification_for("EXACT_MATCH") == grading.JUSTIFICATION_LEXICAL

    def test_a_judgement_call_is_described_as_manual(self):
        assert grading.justification_for("CLOSE_MATCH") == grading.JUSTIFICATION_MANUAL

    def test_an_unknown_quality_does_not_earn_exact_confidence(self):
        """Fail low, not high: a grade nobody taught this module is not an exact match."""
        assert grading.confidence_for("SOMETHING_NEW") == grading.CONFIDENCE_OTHER
        assert grading.confidence_for(None) == grading.CONFIDENCE_OTHER

    def test_every_known_quality_has_an_entry(self):
        """A KeyError here is a row that never gets written -- worse than a wrong grade.

        `promote_microbedecoder_residual.py` carried a three-grade copy of the table and
        would have raised on NARROW_MATCH or FALLBACK_REGISTRY.
        """
        for quality in grading.KNOWN_QUALITIES:
            assert quality in grading.CONFIDENCE
            assert quality in grading.JUSTIFICATION


class TestMimWritersShareOneTable:
    """Three writers import from promote_resolved_unmapped; it must use the module."""

    def test_the_promotion_helper_does_not_declare_its_own(self):
        source = (_REPO / "scripts" / "promote_resolved_unmapped.py").read_text(encoding="utf-8")
        assert "from mediaingredientmech.sssom_grading import" in source
        assert not re.search(r"^CONFIDENCE = \{", source, re.M), (
            "a second table here re-opens the drift this module closes"
        )

    def test_the_microbedecoder_helper_does_not_declare_its_own(self):
        source = (_REPO / "scripts" / "promote_microbedecoder_residual.py").read_text(encoding="utf-8")
        assert "from mediaingredientmech.sssom_grading import" in source
        assert not re.search(r"^CONFIDENCE = \{", source, re.M)


@pytest.mark.skipif(not CLAW_BUILDER.is_file(), reason="claw not checked out at the sibling path")
class TestAgreesWithClaw:
    """claw is the generator, so its rules are the ones that survive a rebuild."""

    @pytest.fixture(scope="class")
    def claw(self):
        return CLAW_BUILDER.read_text(encoding="utf-8")

    def test_exact_qualities_match(self, claw):
        match = re.search(r"EXACT_QUALITIES = \{([^}]*)\}", claw)
        assert match, "claw's EXACT_QUALITIES not found -- the builder was restructured"
        theirs = set(re.findall(r'"([A-Z_]+)"', match.group(1)))
        assert theirs == set(grading.EXACT_QUALITIES), (
            f"claw grades {theirs} as exact; MIM grades {set(grading.EXACT_QUALITIES)}"
        )

    def test_exact_confidence_value_matches(self, claw):
        assert re.search(
            rf'confidence = "{re.escape(grading.CONFIDENCE_EXACT)}" if quality in EXACT_QUALITIES',
            claw,
        ), "claw's exact-match confidence differs from MIM's"

    def test_lexical_qualities_match(self, claw):
        match = re.search(r"if quality in \{([^}]*)\}\s*\n\s*else JUST_MANUAL", claw)
        assert match, "claw's justification rule not found -- the builder was restructured"
        theirs = set(re.findall(r'"([A-Z_]*)"', match.group(1)))
        assert theirs == set(grading.LEXICAL_QUALITIES), (
            f"claw treats {theirs} as lexical; MIM treats {set(grading.LEXICAL_QUALITIES)}"
        )


class TestTheTableIsTotal:
    """A KeyError is a row that never gets written -- worse than a conservative grade.

    `mapping_quality` is one of MIM's organically-growing enums, so any fixed key list
    goes stale. An enumerated table already shipped this bug once:
    `promote_microbedecoder_residual.py` knew three grades and raised on the rest, and
    the first cut of this module missed `PLACEHOLDER`, which 54 records use.
    """

    def test_every_quality_in_the_corpus_resolves(self):
        import glob

        import yaml

        seen = set()
        for path in glob.glob(str(_REPO / "data" / "ingredients" / "**" / "*.yaml"), recursive=True):
            data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
            quality = (data.get("ontology_mapping") or {}).get("mapping_quality")
            if quality:
                seen.add(quality)
        assert seen, "no mapping_quality values found -- the corpus check is vacuous"
        for quality in seen:
            assert grading.CONFIDENCE[quality]
            assert grading.JUSTIFICATION[quality]

    def test_an_unseen_grade_does_not_raise(self):
        assert grading.CONFIDENCE["A_GRADE_INVENTED_TOMORROW"] == grading.CONFIDENCE_OTHER
        assert grading.JUSTIFICATION["A_GRADE_INVENTED_TOMORROW"] == grading.JUSTIFICATION_MANUAL

    def test_an_unseen_grade_cannot_acquire_exact_confidence(self):
        """The rule fails low, so a new enum value cannot become exact by being unknown."""
        assert grading.CONFIDENCE["UNKNOWN"] != grading.CONFIDENCE_EXACT

    def test_placeholder_is_covered(self):
        """The specific grade the first enumerated list missed."""
        assert grading.CONFIDENCE["PLACEHOLDER"] == grading.CONFIDENCE_OTHER


class TestPredicateIsARuleNotATable:
    """The enumerated PREDICATE covered five grades; the corpus uses nine.

    `PLACEHOLDER`, `CAS_RN_LOOKUP`, `LEXICAL_MATCH` and `BROAD_MATCH` -- 339 records --
    raised KeyError on every write path that indexed it, which is a row that never gets
    written (#525). Four scripts index this table.
    """

    def test_the_five_previously_enumerated_grades_are_unchanged(self):
        """The rule must reproduce the old table exactly, or it rewrites history."""
        assert grading.predicate_for("EXACT_MATCH") == "skos:exactMatch"
        assert grading.predicate_for("SYNONYM_MATCH") == "skos:exactMatch"
        assert grading.predicate_for("NARROW_MATCH") == "skos:narrowMatch"
        assert grading.predicate_for("CLOSE_MATCH") == "skos:closeMatch"
        assert grading.predicate_for("FALLBACK_REGISTRY") == "skos:closeMatch"

    @pytest.mark.parametrize(
        "quality", ["PLACEHOLDER", "CAS_RN_LOOKUP", "LEXICAL_MATCH", "BROAD_MATCH"]
    )
    def test_the_grades_that_used_to_raise_now_resolve(self, quality):
        assert grading.PREDICATE[quality] == grading.PREDICATE_CLOSE

    def test_an_unknown_grade_does_not_claim_identity(self):
        """Fail weak: an unrecognised grade must not assert skos:exactMatch."""
        assert grading.PREDICATE["INVENTED_TOMORROW"] == grading.PREDICATE_CLOSE

    def test_every_corpus_quality_resolves(self):
        import glob

        import yaml

        for path in glob.glob(str(_REPO / "data" / "ingredients" / "**" / "*.yaml"), recursive=True):
            data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
            quality = (data.get("ontology_mapping") or {}).get("mapping_quality")
            if quality:
                assert grading.PREDICATE[quality]

    def test_the_promotion_helper_does_not_declare_its_own_predicate(self):
        source = (_REPO / "scripts" / "promote_resolved_unmapped.py").read_text(encoding="utf-8")
        assert not re.search(r"^PREDICATE = \{", source, re.M), (
            "a second predicate table re-opens the KeyError this rule closes"
        )


@pytest.mark.skipif(not CLAW_BUILDER.is_file(), reason="claw not checked out at the sibling path")
class TestPredicateAgreesWithClaw:
    def test_non_exact_qualities_get_close_match(self):
        claw = CLAW_BUILDER.read_text(encoding="utf-8")
        assert 'predicate = "skos:closeMatch"' in claw
        assert "if quality and quality not in EXACT_QUALITIES:" in claw

    def test_narrow_match_is_special_cased_the_same_way(self):
        claw = CLAW_BUILDER.read_text(encoding="utf-8")
        assert 'if quality == "NARROW_MATCH":' in claw
        assert 'predicate = "skos:narrowMatch"' in claw
