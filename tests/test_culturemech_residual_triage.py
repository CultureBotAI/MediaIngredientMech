"""Pin the CultureMech residual triage and its alias backfill.

Every case here failed at least once while the tools were being written, and each
failure would have shipped a wrong identity claim or an unreviewable diff.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml

_REPO = Path(__file__).resolve().parent.parent


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, _REPO / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


triage = _load("triage_culturemech_residual")
aliases = _load("apply_culturemech_aliases")


class TestFoldPreservesIdentity:
    """The fold may drop decoration. It may never drop chemistry."""

    @pytest.mark.parametrize(
        "label",
        [
            "CaCl2 (anhydrous)",
            "MgCl2 (anhydrous)",
            "K2HPO4 (anhydrous base)",
            "Na2SeO3 (anhydrous)",
            "AlK(SO4)2 (anhydrous)",
            "Sodium acetate (hydrated)",
        ],
    )
    def test_hydration_state_is_never_folded_away(self, label):
        """A hydration state is identity (MAPPING_SEMANTICS.md Section 3).

        `CaCl2` and `CaCl2 x 2 H2O` are 110.98 and 147.01 g/mol. Folding
        `(anhydrous)` away lets an anhydrous surface form inherit a hydrate's
        identifier, which is a wrong mapping rather than a missing one.
        """
        folded = triage.fold(label)
        assert "anhyd" in folded or "hydrat" in folded, (
            f"{label!r} folded to {folded!r}, dropping its hydration state"
        )

    def test_a_parenthesis_inside_a_formula_survives(self):
        """`AlK(SO4)2` must keep its sulfate group.

        With re.IGNORECASE the vendor-tag branch matches any parenthetical, so
        this folded to 'alk 2' and collided with an unrelated record.
        """
        assert "so4" in triage.fold("AlK(SO4)2 (anhydrous)")

    def test_a_qualifier_attached_without_a_space_survives(self):
        """`EDTA(Disodium salt)` names the salt; only a standalone tag is decoration."""
        assert "disodium" in triage.fold("EDTA(Disodium salt)")


class TestFoldStripsDecoration:
    @pytest.mark.parametrize(
        "label,expected",
        [
            ("Agar (if needed)", "agar"),
            ("Agar (If needed)", "agar"),
            ("HCl (25%; 7.7 M)", "hcl"),
            ("Casamino acids (BD-Difco)", "casamino acids"),
            ("Sodium phosphate buffer (10 mM; pH7.1)", "sodium phosphate buffer"),
            ("Trace element solution (see Medium No. 187 )", "trace element solution"),
        ],
    )
    def test_decoration_folds_away(self, label, expected):
        assert triage.fold(label) == expected

    def test_unicode_middots_and_subscripts_normalise(self):
        """Scraped recipe text uses codepoints ontology labels never carry."""
        assert triage.fold("MnSO4·xH2O") == triage.fold("MnSO4・xH2O")
        assert triage.fold("H₃BO₃") == triage.fold("H3BO3")


class TestNoiseDetection:
    @pytest.mark.parametrize("label", ["1", "2", "  7 ", "0.5", "%"])
    def test_bare_numbers_are_noise(self, label):
        assert triage.is_noise(label) is not None

    @pytest.mark.parametrize("label", ["'Iron(III", '"Sodium'])
    def test_truncated_quotes_are_noise(self, label):
        assert triage.is_noise(label) == "truncated_quote"

    @pytest.mark.parametrize("label", ["Agar", "NaCl", "L-Cysteine . HCl"])
    def test_real_ingredients_are_not_noise(self, label):
        assert triage.is_noise(label) is None


class TestClassify:
    @pytest.fixture
    def index(self):
        return {
            triage.fold("Agar"): [
                {"label": "Agar", "identifier": "CHEBI:2509", "mapping_status": "MAPPED"}
            ],
            triage.fold("Whole egg"): [
                {"label": "Whole egg", "identifier": "UNMAPPED_0577", "mapping_status": "UNMAPPED"}
            ],
            triage.fold("Casamino acids"): [
                {"label": "Casamino acids", "identifier": "FOODON:03315719", "mapping_status": "MAPPED"},
                {"label": "Casamino acids", "identifier": "mesh:C017721", "mapping_status": "MAPPED"},
            ],
        }

    def test_mapped_hit_is_alias(self, index):
        assert triage.classify("Agar (if needed)", index)[:2] == ("ALIAS", "CHEBI:2509")

    def test_unmapped_hit_is_reported_separately(self, index):
        """An UNMAPPED holder is a grounding opportunity, not an alias fix."""
        assert triage.classify("Whole egg", index)[0] == "UNMAPPED"

    def test_two_holders_are_ambiguous_not_arbitrary(self, index):
        """Picking one of two holders would assert an identity nobody curated."""
        assert triage.classify("Casamino acids (BD-Difco)", index)[0] == "AMBIGUOUS"

    def test_absent_label_is_residual(self, index):
        assert triage.classify("Fictional compound XYZ", index)[0] == "RESIDUAL"

    def test_anhydrous_form_does_not_borrow_the_base_record(self, index):
        """The whole point of the hydration guard, stated as a classification."""
        assert triage.classify("Agar (anhydrous)", index)[0] == "RESIDUAL"


class TestAliasApplyGuards:
    def test_rejected_labels_are_never_promoted(self):
        """#477 stopped rejected labels resolving as synonyms.

        Re-adding one as RAW_TEXT would silently undo that, so the guard reads the
        existing synonym_type rather than only checking for presence.
        """
        record = {
            "preferred_term": "Agar",
            "synonyms": [{"synonym_text": "Agar-agar", "synonym_type": "REJECTED_LABEL"}],
        }
        assert aliases.existing_texts(record)["agar-agar"] == "REJECTED_LABEL"

    def test_preferred_term_counts_as_already_present(self):
        record = {"preferred_term": "Agar", "synonyms": []}
        assert aliases.existing_texts(record)["agar"] == "PREFERRED_TERM"

    @pytest.mark.parametrize(
        "label,expected",
        [
            ("agar (BD-Difco)", "CATALOG_VARIANT"),
            ("MOPS buffer (SIGMA)", "CATALOG_VARIANT"),
            ("Agar (if needed)", "RAW_TEXT"),
        ],
    )
    def test_vendor_tagged_forms_are_typed_as_catalog_variants(self, label, expected):
        matched = aliases._VENDOR.search(label)
        assert ("CATALOG_VARIANT" if matched else "RAW_TEXT") == expected


class TestWrittenRecordsStayCanonical:
    def test_dump_settings_round_trip_the_corpus_byte_for_byte(self):
        """A `width=` on the dump reflows every long string in the file.

        The two added lines then arrive buried under dozens of spurious ones, and
        the batch diff stops being reviewable. Pin the exact dump settings.
        """
        sampled = sorted((_REPO / "data" / "ingredients").rglob("*.yaml"))[:40]
        assert sampled, "no ingredient records found"
        for path in sampled:
            original = path.read_text(encoding="utf-8")
            redumped = yaml.dump(
                yaml.safe_load(original),
                sort_keys=False,
                allow_unicode=True,
                default_flow_style=False,
            )
            assert redumped == original, f"{path.name} is not in the canonical dump format"

    def test_backfill_timestamps_are_date_time_not_date(self):
        """CurationEvent.timestamp is `date-time`; a bare date fails validate-strict."""
        offenders = []
        for path in (_REPO / "data" / "ingredients").rglob("*.yaml"):
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            for event in (data or {}).get("curation_history") or []:
                if not isinstance(event, dict):
                    continue
                if event.get("curator") == aliases.CURATOR and "T" not in str(event.get("timestamp", "")):
                    offenders.append(path.name)
        assert not offenders, f"bare-date timestamps on {offenders[:5]}"


class TestShortFormulaeAreNotNoise:
    @pytest.mark.parametrize("label", ["O2", "N2", "H2"])
    def test_two_character_formulae_survive(self, label):
        """`O2` is a real ingredient with 10 recipe mentions.

        The first rule rejected any <=2-character token that was not pure alpha,
        which discards every short formula along with the parse damage.
        """
        assert triage.is_noise(label) is None


class TestGroundingProposerGuards:
    """The proposer's job is to refuse a match it cannot justify."""

    @pytest.fixture
    def proposer(self):
        return _load("propose_residual_groundings")

    def test_ncit_and_mesh_are_label_only(self, proposer):
        """NCIT synonyms carry gene symbols: `B12` resolved to `TNFAIP1 wt Allele`."""
        assert "NCIT" in proposer.LABEL_ONLY
        assert "MESH" in proposer.LABEL_ONLY

    def test_chebi_and_foodon_may_match_on_synonyms(self, proposer):
        """Most recipe surface forms are synonyms, so these must not be label-only."""
        assert "CHEBI" not in proposer.LABEL_ONLY
        assert "FOODON" not in proposer.LABEL_ONLY

    @pytest.mark.parametrize("query", ["X", "Ca", "B"])
    def test_very_short_names_are_never_matched(self, proposer, query):
        """`X` matched UBERON's "area X of ventral lateral nucleus"."""

        class _Boom:
            def basic_search(self, *a, **k):
                raise AssertionError("short query should not reach the ontology")

        assert proposer.exact_hits(_Boom(), query, "CHEBI") == []

    def test_prime_and_subscripts_normalise_for_comparison(self, proposer):
        """CHEBI writes an ASCII apostrophe where recipe text writes U+2032 PRIME."""
        assert proposer.comparison_key("[1,1′-Biphenyl]-2-ol") == "[1,1'-biphenyl]-2-ol"
        assert proposer.comparison_key("H₃BO₃") == "h3bo3"

    def test_punctuation_is_not_stripped_for_comparison(self, proposer):
        """Stripping it would make EDTA and EDTA-2Na compare equal."""
        assert proposer.comparison_key("EDTA") != proposer.comparison_key("EDTA-2Na")


class TestServerSideExactMatchesAreTrusted:
    """A backend that already matched exactly must not be re-checked against the label.

    OLS4 is queried with `exact=true` over `label,synonym`, so a returned term matched
    one of them exactly. Re-checking client-side against the label alone discarded every
    synonym match -- `Christensen's urea agar` is an exact MICRO synonym of `urea agar`
    (MICRO:0000643) and was thrown away, making the whole MICRO pass label-only without
    reporting that it had.
    """

    @pytest.fixture
    def proposer(self):
        return _load("propose_residual_groundings")

    class _ServerExact:
        server_side_exact = True

        def basic_search(self, query, config=None):  # noqa: ARG002
            return ["MICRO:0000643"]

        def label(self, curie):  # noqa: ARG002
            return "urea agar"

    class _ClientChecked:
        def basic_search(self, query, config=None):  # noqa: ARG002
            return ["MICRO:0000643"]

        def label(self, curie):  # noqa: ARG002
            return "urea agar"

        def entity_aliases(self, curie):  # noqa: ARG002
            return ["urea agar"]

    def test_synonym_match_survives_when_backend_is_trusted(self, proposer):
        hits = proposer.exact_hits(self._ServerExact(), "Christensen's urea agar", "MICRO")
        assert hits == [("MICRO:0000643", "urea agar")]

    def test_untrusted_backend_still_requires_a_local_name_match(self, proposer):
        """The trust must be opt-in, or a local adapter would stop being checked."""
        hits = proposer.exact_hits(self._ClientChecked(), "Christensen's urea agar", "MICRO")
        assert hits == []

    def test_ols_adapter_declares_itself_trusted(self, proposer):
        assert proposer.OlsAdapter("MICRO").server_side_exact is True


class TestOntologyPreferenceDominatesQueryVariants:
    """Preference order must not be decided by the surface form's capitalisation.

    oaklib's `basic_search` is case-sensitive: ENVO answers `air` but not `Air`. With
    the query variants as the outer loop, the raw `Air` reached NCIT before the
    normalised `air` ever reached ENVO, so `Air` and `air` -- the same substance --
    were grounded to two different ontologies.
    """

    @pytest.fixture
    def proposer(self):
        return _load("propose_residual_groundings")

    def test_normalised_query_reaches_the_preferred_ontology_first(self, proposer):
        class _CaseSensitive:
            """Answers only the lowercase form, like ENVO."""

            def __init__(self, curie, label):
                self.curie, self._label = curie, label

            def basic_search(self, query, config=None):  # noqa: ARG002
                return [self.curie] if query == self._label else []

            def label(self, curie):  # noqa: ARG002
                return self._label

            def entity_aliases(self, curie):  # noqa: ARG002
                return [self._label]

        preferred = _CaseSensitive("ENVO:00002005", "air")
        # The raw surface form matches nothing here, the normalised one does.
        assert proposer.exact_hits(preferred, "Air", "ENVO") == []
        assert proposer.exact_hits(preferred, proposer.comparison_key("Air"), "ENVO") == [
            ("ENVO:00002005", "air")
        ]

    def test_candidate_queries_include_the_normalised_form(self, proposer):
        queries = proposer.candidate_queries("Air", lambda s: s)
        assert "air" in queries, "the lowercase form must be searched, not only compared"
