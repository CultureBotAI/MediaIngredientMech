"""Tests for the canonical CURIE normalizer (issue #119).

Each test pins a failure mode that has actually occurred in this codebase, so a
regression here is a regression of something we already paid for once.
"""

from __future__ import annotations

import csv

import pytest

from mediaingredientmech.curie import CurieNormalizer, Verdict


@pytest.fixture(scope="module")
def n() -> CurieNormalizer:
    return CurieNormalizer()


# ---- syntax and prefix registry -------------------------------------------

def test_typoed_prefix_is_rejected_not_ignored(n):
    """CHBEI: must fail loudly; silently skipping it is how drift hides."""
    v = n.normalize("CHBEI:15377")
    assert not v and v.problem == "UNKNOWN_PREFIX"


def test_prefix_case_is_canonicalised(n):
    v = n.normalize("chebi:15377")
    assert v and v.curie == "CHEBI:15377"


@pytest.mark.parametrize("curie", ["", "notacurie", ":15377", "CHEBI:"])
def test_malformed_curies_rejected(n, curie):
    assert not n.normalize(curie)


# ---- foreign identifiers wearing an OBO prefix ----------------------------

def test_pubchem_cid_as_chebi_is_caught(n):
    """CHEBI:10716816 was asserted for 'Nicotinate'.

    Real CHEBI accessions reach ~747k, so this 8-digit value is well outside the
    range; note the ceiling only catches egregious cases (some PubChem CIDs are
    6-digit and sit inside the real CHEBI range).
    """
    v = n.normalize("CHEBI:10716816")
    assert not v and v.problem == "ACCESSION_OUT_OF_RANGE"


def test_real_chebi_accession_passes(n):
    assert n.normalize("CHEBI:15377")


# ---- MicrO malformed-IRI guard --------------------------------------------

def test_unverified_micro_id_is_blocked(n):
    """MICRO:0002390 is minted under …/obo/MicrO.owl/… and will not round-trip."""
    v = n.normalize("MICRO:0002390")
    assert not v and v.problem == "MICRO_UNVERIFIED"


def test_verified_micro_id_passes(n):
    assert n.normalize("MICRO:0000182")


# ---- rename resolution -----------------------------------------------------

def test_renamed_mim_curie_still_resolves(n):
    """The exact case from issue #119: a case-only rename retired a CURIE."""
    v = n.resolve("MIM:1-Naphtylacetic_Acid")
    assert v and v.curie == "MIM:1-naphtylacetic_Acid"
    assert "renamed" in v.note


def test_unknown_mim_subject_is_rejected(n):
    v = n.resolve("MIM:Does_Not_Exist_Anywhere")
    assert not v and v.problem == "UNKNOWN_SUBJECT"


def test_alias_map_targets_are_all_live(n):
    """Every published alias must point at a RECORD that exists today.

    Checked against records on disk, not SSSOM subjects: an unmapped ingredient
    is a legitimate rename target but carries no mapping, so it never appears as
    an SSSOM subject.
    """
    dangling = [(old, new) for old, new in n._aliases.items()
                if new not in n._records]
    assert not dangling, f"alias map points at missing records: {dangling[:5]}"


def test_alias_map_has_no_cycles(n):
    for old in n._aliases:
        seen, cur, hops = {old}, old, 0
        while cur in n._aliases and hops < 20:
            cur = n._aliases[cur]
            assert cur not in seen or cur == old, f"cycle through {old}"
            seen.add(cur); hops += 1
        assert hops < 20, f"alias chain from {old} does not terminate"


# ---- the selection rule ----------------------------------------------------

def test_equivalent_term_picks_highest_ranked_exact_match(n):
    """Selection ranks among exactMatch candidates only.

    It must NOT reach past the exactMatch set to grab a better-ranked prefix that
    is only a close/narrow match — that is the generalisation bug this rule
    exists to prevent. So the assertion is "best of what is eligible", not
    "always an ontology term".
    """
    from mediaingredientmech.curie import PREFIX_RANK
    multi = [s for s, rows in n._mappings.items()
             if len({o.split(":", 1)[0] for o, p in rows
                     if p == "skos:exactMatch"}) > 1]
    if not multi:
        pytest.skip("no multi-prefix exactMatch subject in this SSSOM")
    for subj in multi[:25]:
        v = n.equivalent_term(subj)
        assert v
        eligible = [o for o, p in n._mappings[subj] if p == "skos:exactMatch"]
        best = min(eligible, key=lambda o: (PREFIX_RANK.get(o.split(":", 1)[0], 99), o))
        assert v.curie == best, f"{subj}: picked {v.curie}, best eligible was {best}"


def test_narrow_match_is_not_offered_as_equivalent(n):
    """narrowMatch means MIM is MORE specific — citing it as equal generalises."""
    narrow_only = [
        s for s, rows in n._mappings.items()
        if rows and all(p != "skos:exactMatch" for _, p in rows)
    ]
    if not narrow_only:
        pytest.skip("every subject has an exactMatch")
    v = n.equivalent_term(narrow_only[0])
    assert not v and v.problem == "NO_EXACT_MATCH"


def test_verdict_is_falsy_on_failure():
    assert not Verdict(False, problem="X")
    assert Verdict(True, curie="CHEBI:1")


# ---- the published SSSOM itself -------------------------------------------

KNOWN_BAD_MICRO = {"MICRO:0002250", "MICRO:0002392", "MICRO:0002393"}


def test_every_published_object_id_normalises(n):
    """The artifact we publish must satisfy our own standard.

    Three MICRO ids are known-bad (malformed upstream IRI) and are excluded here
    so this test guards against NEW breakage; re-grounding them is tracked
    separately. If that list ever shrinks to empty, delete the exclusion.
    """
    bad = []
    for rows in n._mappings.values():
        for obj, _ in rows:
            if obj in KNOWN_BAD_MICRO:
                continue
            v = n.normalize(obj)
            if not v:
                bad.append((obj, v.problem))
    assert not bad, (f"{len(bad)} published object_ids fail normalisation: "
                     f"{sorted(set(bad))[:10]}")


def test_known_bad_micro_ids_are_still_bad(n):
    """The exclusion above must not outlive the defect it works around."""
    for c in KNOWN_BAD_MICRO:
        assert not n.normalize(c), f"{c} now passes — remove it from KNOWN_BAD_MICRO"
