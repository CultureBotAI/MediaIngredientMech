"""Pin the asymmetric-predicate direction now that both repos have moved (#390).

Until #390 this file asserted something wrong by the SKOS spec, on purpose. MIM
wrote `skos:narrowMatch` for *"MIM:X is a kind-of Y"*, which is the inverse of
the spec -- `skos:narrowMatch` is a sub-property of `skos:narrower`, so
`A narrowMatch B` asserts **B is narrower than A** -- and kg-microbe read it the
same inverted way, so every row still produced a correct `biolink:subclass_of`
edge. A one-sided fix would have inverted every one of them, silently, so the
old test refused `broadMatch` and asked whoever tripped it one question: *is the
kg-microbe half landing too?*

It has landed (Knowledge-Graph-Hub/kg-microbe#822, `97d458f75`), and not as the
branch-swap this file once anticipated but as something order-independent: the
mapping set declares its own semantics in its header,

    # predicate_semantics: skos

and a reader treats absence as the legacy convention. The consolidator reads the
declaration and re-emits it into the unified set, so the whole chain follows it.
Verified with kg-microbe's own indexer at the cutover: the legacy file under the
legacy reading and the flipped file under the SKOS reading yield identical
parent edges, 166 of 166 -- and the flipped file with the declaration stripped
inverts all of them. The header line is load-bearing, which is why Rule L and
the tests below pin the rows and the declaration *together*.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).parent.parent
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"

ASYMMETRIC = {"skos:narrowMatch", "skos:broadMatch"}


def _rows():
    with SSSOM.open(encoding="utf-8") as fh:
        return list(csv.DictReader(
            (l for l in fh if not l.startswith("#")), delimiter="\t"))


def _header():
    with SSSOM.open(encoding="utf-8") as fh:
        return [line for line in fh if line.startswith("#")]


def test_parent_anchoring_rows_are_broadmatch():
    """ "MIM:X is a kind-of Y" is `skos:broadMatch`: Y is the broader concept."""
    rows = _rows()
    asym = [r for r in rows if r["predicate_id"] in ASYMMETRIC]
    narrow = [r for r in asym if r["predicate_id"] == "skos:narrowMatch"]
    assert asym, "no asymmetric rows at all — has the corpus changed shape?"
    assert not narrow, (
        f"{len(narrow)} skos:narrowMatch row(s) found, e.g. "
        f"{[(r['subject_label'], r['object_id']) for r in narrow[:3]]}.\n"
        f"Since #390 the set declares SKOS semantics, under which narrowMatch "
        f"asserts the OBJECT is narrower. For a MIM record anchored to an OBO "
        f"parent that is backwards: kg-microbe would index the ontology term as "
        f"a child of the MIM record. Use skos:broadMatch. A genuine narrowMatch "
        f"(the MIM record is the broader concept) is possible but was absent from "
        f"the corpus at the cutover, so check it is not a legacy-convention row."
    )


def test_the_set_declares_skos_semantics_at_the_top_level():
    """The declaration is load-bearing: without it every parent edge inverts."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "validate_sssom_invariants", ROOT / "scripts" / "validate_sssom_invariants.py"
    )
    validator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validator)
    assert validator.declared_predicate_semantics(_header()) == "skos"


def test_a_nested_key_does_not_count_as_the_declaration():
    """SSSOM headers are nested YAML; kg-microbe reads top-level keys only (#831)."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "validate_sssom_invariants", ROOT / "scripts" / "validate_sssom_invariants.py"
    )
    validator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validator)
    nested = ["# extension_definitions:\n", "#   predicate_semantics: skos\n"]
    assert validator.declared_predicate_semantics(nested) == ""
    assert validator.declared_predicate_semantics(["# predicate_semantics: skos\n"]) == "skos"
    assert validator.declared_predicate_semantics(['# predicate_semantics: "skos"\n']) == "skos"


def test_rule_l_rejects_a_flipped_set_with_no_declaration():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "validate_sssom_invariants", ROOT / "scripts" / "validate_sssom_invariants.py"
    )
    validator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validator)
    rows = [{"predicate_id": "skos:broadMatch"}]
    assert list(validator.evaluate_rule_l([], rows)), "absence must not pass"
    assert list(validator.evaluate_rule_l(["# predicate_semantics: legacy\n"], rows))
    assert list(validator.evaluate_rule_l(["# predicate_semantics: skos\n"], rows)) == []


def test_no_script_emits_the_legacy_literal():
    """A writer that hardcodes `skos:narrowMatch` would put a legacy-convention
    row into a SKOS-declared set -- an inverted edge nothing else would catch.
    Parent-anchoring writers take PREDICATE_BROAD from sssom_grading instead.
    """
    allowed_fragments = ('"skos:narrowMatch", "skos:broadMatch"',)  # direction-agnostic sets
    offenders = []
    for folder in ("scripts", "src"):
        for path in (ROOT / folder).rglob("*.py"):
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if '"skos:narrowMatch"' not in line or line.lstrip().startswith("#"):
                    continue
                if any(fragment in line for fragment in allowed_fragments):
                    continue
                offenders.append(f"{path.relative_to(ROOT)}:{number}")
    assert not offenders, (
        f"hardcoded legacy predicate literal at {offenders}. Import PREDICATE_BROAD "
        f"from mediaingredientmech.sssom_grading for a parent-anchoring row (#390)."
    )


def test_every_asymmetric_subject_has_its_registry_row():
    """Rule B1, restated as a test.

    The parent-index translates `MIM:<slug>` to a kg-microbe primary using the
    sibling registry exactMatch row. Without it the asymmetric row still parses
    but the subject never resolves, so the edge is dropped rather than inverted —
    a different failure, equally silent.
    """
    rows = _rows()
    by_subject = {}
    for r in rows:
        by_subject.setdefault(r["subject_id"], []).append(r)

    missing = []
    for r in rows:
        if r["predicate_id"] not in ASYMMETRIC:
            continue
        subject = r["subject_id"]
        if not subject.startswith("MIM:"):
            continue
        slug = subject[4:].lower()
        ok = any(
            s["predicate_id"] == "skos:exactMatch"
            and s["object_id"].startswith(("kgmicrobe.ingredient:", "kgmicrobe.compound:"))
            and s["object_id"].split(":", 1)[1] == slug
            for s in by_subject[subject]
        )
        if not ok:
            missing.append(subject)
    assert not missing, (
        f"{len(missing)} asymmetric subject(s) lack the registry exactMatch row "
        f"whose object local-part equals the subject slug: {sorted(set(missing))[:5]}. "
        f"Note the local part must match the slug EXACTLY, hyphens included — "
        f"`MIM:Dry_Cow-manure` needs `kgmicrobe.ingredient:dry_cow-manure`, not "
        f"`dry_cow_manure`.")
