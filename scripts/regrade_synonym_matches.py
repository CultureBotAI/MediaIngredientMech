#!/usr/bin/env python3
"""Re-grade overstated mappings using the evidence that established them (#317).

The schema defines the two grades unambiguously:

    EXACT_MATCH:    Direct exact match to ontology term
    SYNONYM_MATCH:  Matches known synonym in ontology
    CAS_RN_LOOKUP:  Mapping resolved via CAS Registry Number lookup

A record whose label matches a ChEBI *synonym* rather than the term's primary
label is `SYNONYM_MATCH` by that definition. Issue #317 originally counted 297
such records. The first pass re-graded 157, but selected the first match from an
unordered set; a circular enrichment synonym could therefore hide independent
evidence. Review then found that many records had actually been created through
an independently matching CAS RN. Calling those ``SYNONYM_MATCH`` would replace
one provenance error with another. This version therefore restores
``CAS_RN_LOOKUP`` where the creation history and target ChEBI xref agree, and
uses ``SYNONYM_MATCH`` only for independently supported lexical matches.

Scope, deliberately narrow:

* A CAS grade requires both a ``CREATED_FROM_CAS_LOOKUP`` history event and a
  current CAS RN that uniquely resolves to the current ChEBI target through
  ChEBI xrefs. Merely having a CAS number is not treated as provenance, and a
  CAS shared by multiple ChEBI entities is left for review.
* Identity-form guards run before either grade: concentration-qualified
  preparations and conflicting hydrate states need re-grounding, regardless of
  whether the original mapping happened to use CAS.
* Lexical re-grades require a matching ChEBI synonym that is independently
  supported, is not shared by another ChEBI term, and does not hide a preparation
  or hydrate-state conflict. No-match and ambiguous records are left for review.
* `ontology_id` is never changed. The term is right; only the claim about *how*
  it was matched is wrong.
* The own-identifier SSSOM predicate does not move: Rule D requires
  ``skos:exactMatch`` independently of mapping-quality provenance (#438).

Matching is case-insensitive and ignores presentation punctuation, while
preserving optical signs, charge, and prime locants that can change identity.

    python scripts/regrade_synonym_matches.py            # dry-run
    python scripts/regrade_synonym_matches.py --apply
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
CHEBI_DB = Path.home() / ".data" / "oaklib" / "chebi.db"
STAMP = "2026-08-24T00:00:00+00:00"
CURATOR = "regrade_synonym_matches"
ISSUE = "#317"


def norm(s: object) -> str:
    text = str(s or "").lower()
    # Most punctuation is presentation-only, but these marks can change a
    # chemical identity. Preserve them as stable tokens before stripping the
    # remaining separators: (+)-/(-)- optical forms, ionic charge, and prime
    # locants such as 5' versus 5.
    text = re.sub(r"\(\s*\+\s*\)", " opticalplus ", text)
    text = re.sub(r"\(\s*[-−]\s*\)", " opticalminus ", text)
    text = text.replace("±", " plusminus ")
    text = text.replace("+", " plus ").replace("−", " minus ")
    text = re.sub(
        r"(?<=\d)(['’′]+)",
        lambda match: " " + "prime" * len(match.group(1)) + " ",
        text,
    )
    # ``x`` is punctuation, rather than the letter x, in a hydrate formula.
    # Treat ``Na2S x 9 H2O`` and ChEBI's ``Na2S.9H2O`` as the same string while
    # retaining x everywhere else (e.g. xanthine).
    text = re.sub(r"(?<=\w)\s+x\s+(?=\d+(?:\.\d+)?\s*h2o\b)", "", text)
    return re.sub(r"[^a-z0-9]", "", text)


def chebi_synonyms(cur: sqlite3.Cursor, curie: str) -> dict[str, tuple[str, ...]]:
    """Return every ChEBI synonym, deterministically grouped by normalised text.

    Several verbatim ChEBI strings can collapse under :func:`norm`. Keeping all
    of them avoids depending on SQLite row order; sorting gives the audit trail
    a stable representative.
    """
    cur.execute(
        """SELECT value FROM statements
           WHERE subject=? AND predicate LIKE '%ynonym%'
           ORDER BY value""",
        (curie,),
    )
    grouped: dict[str, set[str]] = defaultdict(set)
    for (value,) in cur.fetchall():
        if value:
            grouped[norm(value)].add(value)
    return {
        key: tuple(sorted(values, key=lambda value: (value.casefold(), value)))
        for key, values in sorted(grouped.items())
    }


def synonym_subjects(cur: sqlite3.Cursor, values: list[str]) -> dict[str, set[str]]:
    """Return ChEBI subjects using each synonym's normalised surface.

    ``hasRelatedSynonym`` is sometimes shared by a general term and one or more
    stereospecific terms (for example, ``abscisic acid``). Such a surface does
    not independently select one target and must not be auto-regraded as if it
    did. The ambiguity lookup must use the same normalisation as candidate
    selection: punctuation variants such as ``alias-one`` and ``alias one`` are
    not independent evidence for different targets.
    """
    requested = {norm(value) for value in values if norm(value)}
    if not requested:
        return {}
    cur.execute(
        """SELECT subject, value FROM statements
           WHERE predicate = 'rdfs:label' OR predicate LIKE '%ynonym%'"""
    )
    grouped: dict[str, set[str]] = defaultdict(set)
    for subject, value in cur.fetchall():
        key = norm(value)
        if key in requested and str(subject).startswith("CHEBI:"):
            grouped[key].add(str(subject))
    return grouped


# These synonym lists were populated from the target ontology/graph after the
# mapping already existed. Matching one back to ChEBI is therefore circular.
# This applies to the second-stage ChEBI-synonym evidence below. The issue's
# defined cohort already excludes records where *any* stored local surface
# equals the primary ontology label, so that historical prefilter remains
# deliberately unchanged here.
DERIVED_SOURCES = ("chebi", "ols", "kg_microbe")

# A concentration- or solution-qualified label denotes a *preparation*, not the
# solute, so its mapping is wrong at the identity level (#324's neighbourhood),
# not merely mis-graded. Re-grading one would stamp "the term is correct" into
# its curation_history, which is a false statement — and would quietly remove it
# from anyone scanning EXACT_MATCH for problems. Those need re-grounding.
CONCENTRATION_LABEL = re.compile(
    r"(?<![a-z0-9])\d+(?:\.\d+)?\s*"
    r"(?:%|[mµμunp]?m(?![a-z])|m?g\s*/\s*m?l(?![a-z]))"
    r"|(?<![a-z])solution(?![a-z])|\bstock\b",
    re.I,
)

# Review found fifteen explicit source-label/target-form conflicts in the CAS
# cohort. Generic counterion and stereochemistry parsers would be unsafe here
# (ChEBI uses several valid ion, salt, historical-name, and underspecified-label
# conventions), so key the reviewed exceptions by all three identity-bearing
# values. Any later correction to the source label, target, or CAS automatically
# falls out of this list and is evaluated normally.
REVIEWED_IDENTITY_CONFLICTS = {
    ("Glycyrrhizic Acid, Ammonium Salt", "CHEBI:15939", "1405-86-3"): (
        "target is the free glycyrrhizinic acid and has no ammonium"
    ),
    ("Colistin sulfate salt", "CHEBI:37943", "1264-72-8"): (
        "target is colistin and its formula has no sulfate"
    ),
    ("Dimethylsulfoniopropionate hydrochloride", "CHEBI:16457", "7314-30-9"): (
        "target is zwitterionic DMSP and has no hydrochloride/chloride"
    ),
    ("potassium tellurate", "CHEBI:75248", "7790-58-1"): (
        "target is Te(IV) potassium tellurite, not bare Te(VI) tellurate"
    ),
    ("N-lauroylsarcosine sodium salt", "CHEBI:183704", "137-16-6"): (
        "target is the organic anion and has no sodium"
    ),
    ("Alpha-Toxicarol (Dl)", "CHEBI:9643", "82-09-7"): (
        "source denotes a racemate but target is a fixed stereoisomer"
    ),
    ("DL-2-Aminobutyric acid", "CHEBI:35621", "2835-81-6"): (
        "source denotes a racemate but target is stereo-unspecified"
    ),
    ("DL-3-Aminoisobutyric acid", "CHEBI:27389", "144-90-1"): (
        "source denotes a racemate but target is stereo-unspecified"
    ),
    ("DL-Glyceraldehyde 3-phosphate", "CHEBI:17138", "591-59-3"): (
        "source denotes a racemate but target is stereo-unspecified"
    ),
    ("DL-glyceraldehyde", "CHEBI:5445", "56-82-6"): (
        "source denotes a racemate but target is stereo-unspecified"
    ),
    ("methyl-cis-p-coumarate", "CHEBI:86904", "3943-97-3"): (
        "source is cis/Z while CAS denotes trans/E and target is stereo-unspecified"
    ),
    ("N-(3-oxohexanoyl)-DL-homoserine lactone", "CHEBI:29640", "76924-95-3"): (
        "source denotes a racemate but target is stereo-unspecified"
    ),
    ("Perillic Acid (-)", "CHEBI:36999", "7694-45-3"): (
        "source denotes one enantiomer but target is stereo-unspecified"
    ),
    ("rac-3-Hydroxypentanoic Acid", "CHEBI:139272", "10237-77-1"): (
        "source denotes a racemate but target is stereo-unspecified"
    ),
    ("Trans,Trans-Farnesol", "CHEBI:28600", "4602-84-0"): (
        "source is (2E,6E) but target and CAS are stereo-unspecified"
    ),
}


def _is_derived_source(source: object) -> bool:
    value = str(source or "").lower()
    return any(derived in value for derived in DERIVED_SOURCES)


def matching_surfaces(rec: dict, synonyms: dict[str, tuple[str, ...]]) -> list[dict]:
    """Return every local surface that matches a ChEBI synonym.

    The old implementation put all local strings in a set, selected the first
    hit, and then checked only that hit's provenance. Python hash randomisation
    therefore changed both the candidate count and which evidence was written
    to ``curation_history``. Here every surface is evaluated, and the result is
    sorted with ``preferred_term`` first, then independently sourced synonyms,
    then derived/circular synonyms.
    """
    surfaces = [
        {
            "surface_kind": "preferred_term",
            "surface_text": str(rec.get("preferred_term") or ""),
            "surface_source": None,
            "independent": True,
        }
    ]
    for synonym in rec.get("synonyms") or []:
        source = synonym.get("source")
        surfaces.append(
            {
                "surface_kind": "synonym",
                "surface_text": str(synonym.get("synonym_text") or ""),
                "surface_source": source,
                "independent": not _is_derived_source(source),
            }
        )

    matches: list[dict] = []
    for surface in surfaces:
        for chebi_text in synonyms.get(norm(surface["surface_text"]), ()):
            matches.append({**surface, "matched_synonym": chebi_text})
    return sorted(
        matches,
        key=lambda match: (
            match["surface_kind"] != "preferred_term",
            not match["independent"],
            match["surface_text"].casefold(),
            str(match["surface_source"] or "").casefold(),
            match["matched_synonym"].casefold(),
            match["matched_synonym"],
        ),
    )


_HYDRATE_WORD_COUNTS = {
    "hemihydrate": 0.5,
    "monohydrate": 1.0,
    "dihydrate": 2.0,
    "trihydrate": 3.0,
    "tetrahydrate": 4.0,
    "pentahydrate": 5.0,
    "hexahydrate": 6.0,
    "heptahydrate": 7.0,
    "octahydrate": 8.0,
    "nonahydrate": 9.0,
    "decahydrate": 10.0,
    "undecahydrate": 11.0,
    "dodecahydrate": 12.0,
}
_FORMULA_HYDRATE = re.compile(
    r"(?:\s+x\s+|[×·⋅∙・])\s*" r"(?:(\d+(?:\.\d+)?)|n)?\s*h2o\b",
    re.I,
)


def hydration_state(value: object) -> tuple[bool, float | None]:
    """Return ``(mentions_hydrate, stated_water_count)`` for a label.

    ``None`` as the count means that the label says only ``hydrate`` or
    ``x n H2O``. A bare ``x H2O``/middle-dot-H2O is the monohydrate convention.
    """
    text = str(value or "").lower()
    # Ceftriaxone labels use both ``hemi(heptahydrate)`` and the contracted
    # ``hemiheptahydrate``. Both mean 7 waters per 2 formula units (3.5 each),
    # rather than a seven-water-vs-unhydrated conflict.
    if re.search(r"\bhemi\s*(?:\(\s*)?heptahydrate\s*\)?", text):
        return True, 3.5
    for word, count in _HYDRATE_WORD_COUNTS.items():
        if re.search(rf"\b{word}\b", text):
            return True, count
    if re.search(r"\bhydrate\b", text):
        return True, None
    match = _FORMULA_HYDRATE.search(text)
    if match:
        if match.group(1):
            return True, float(match.group(1))
        if re.search(r"\bn\b", match.group(0), re.I):
            return True, None
        return True, 1.0
    return False, None


def hydration_states_conflict(preferred_term: object, ontology_label: object) -> bool:
    """True when record and target state incompatible hydration identities."""
    preferred_hydrate, preferred_count = hydration_state(preferred_term)
    target_hydrate, target_count = hydration_state(ontology_label)
    if preferred_hydrate != target_hydrate:
        return True
    return bool(
        preferred_hydrate
        and preferred_count is not None
        and target_count is not None
        and preferred_count != target_count
    )


def was_created_from_cas_lookup(rec: dict) -> bool:
    """True only for an explicit historical CAS-to-ontology resolution."""
    return any(
        event.get("action") == "CREATED_FROM_CAS_LOOKUP"
        for event in (rec.get("curation_history") or [])
    )


def record_cas(rec: dict) -> str:
    """Return the record's current CAS RN, stripped for exact xref lookup."""
    return str((rec.get("chemical_properties") or {}).get("cas_rn") or "").strip()


def cas_subjects(cur: sqlite3.Cursor, cas_rns: list[str]) -> dict[str, set[str]]:
    """Return every ChEBI subject cross-referenced by each requested CAS RN.

    A CAS xref can be shared by a general molecule, a charge state, a tautomer,
    or a stereospecific form. Such an xref does not by itself select one target,
    so callers must require the returned subject set to equal ``{target}``.
    """
    values = sorted({f"cas:{cas_rn}".casefold() for cas_rn in cas_rns if cas_rn})
    if not values:
        return {}
    placeholders = ",".join("?" for _ in values)
    cur.execute(
        f"""SELECT subject, value FROM statements
            WHERE predicate LIKE '%xref%'
              AND lower(value) IN ({placeholders})""",
        values,
    )
    grouped: dict[str, set[str]] = defaultdict(set)
    for subject, value in cur.fetchall():
        if str(subject).startswith("CHEBI:"):
            grouped[str(value).casefold()].add(str(subject))
    return grouped


def plan(coll: dict, cur: sqlite3.Cursor) -> tuple[list[dict], dict[str, int]]:
    """Return the records to re-grade, plus a tally of why others were skipped."""
    cas_candidates: list[dict] = []
    synonym_candidates: list[dict] = []
    tally = {
        "not_mapped": 0,
        "not_exact_match": 0,
        "not_chebi": 0,
        "identity_conflict_skipped": 0,
        "cas_xref_mismatch": 0,
        "cas_ambiguous_skipped": 0,
        "label_matches": 0,
        "no_chebi_synonym_match": 0,
        "preparation_skipped": 0,
        "hydrate_mismatch_skipped": 0,
        "structureless_term_skipped": 0,
        "circular_evidence_only": 0,
        "ambiguous_synonym_skipped": 0,
        "cas_rn_lookup_regrade": 0,
        "synonym_regrade": 0,
        "regrade": 0,
    }
    # Terms with no structure at all are role/grouping/family classes (#322):
    # a label on one of those is a scope problem, again not a grading one.
    cur.execute("""SELECT DISTINCT subject FROM statements
                   WHERE predicate LIKE '%inchikey%' OR predicate LIKE '%smiles%'
                      OR predicate LIKE '%formula%'""")
    has_structure = {r[0] for r in cur.fetchall()}
    subjects_by_cas = cas_subjects(
        cur,
        [
            record_cas(rec)
            for rec in coll.get("ingredients", [])
            if was_created_from_cas_lookup(rec)
        ],
    )
    for rec in coll.get("ingredients", []):
        if rec.get("mapping_status") != "MAPPED":
            tally["not_mapped"] += 1
            continue
        om = rec.get("ontology_mapping") or {}
        old_quality = om.get("mapping_quality")
        if old_quality not in {"EXACT_MATCH", "SYNONYM_MATCH"}:
            tally["not_exact_match"] += 1
            continue
        curie = str(om.get("ontology_id") or "")
        if not curie.startswith("CHEBI:"):
            tally["not_chebi"] += 1
            continue
        onto_label = om.get("ontology_label")
        identity_key = (str(rec.get("preferred_term") or ""), curie, record_cas(rec))
        if identity_key in REVIEWED_IDENTITY_CONFLICTS:
            tally["identity_conflict_skipped"] += 1
            continue
        # These are identity conflicts, not evidence-grade defects. Apply the
        # guards before CAS as well as lexical re-grading: a matching CAS does
        # not turn a preparation into its solute or one hydrate into another.
        if CONCENTRATION_LABEL.search(str(rec.get("preferred_term") or "")):
            tally["preparation_skipped"] += 1
            continue
        if hydration_states_conflict(rec.get("preferred_term"), onto_label):
            tally["hydrate_mismatch_skipped"] += 1
            continue
        if was_created_from_cas_lookup(rec):
            cas_rn = record_cas(rec)
            subjects = subjects_by_cas.get(f"cas:{cas_rn}".casefold(), set())
            if curie not in subjects:
                tally["cas_xref_mismatch"] += 1
                continue
            if subjects != {curie}:
                tally["cas_ambiguous_skipped"] += 1
                continue
            cas_candidates.append(
                {
                    "rec": rec,
                    "curie": curie,
                    "onto_label": onto_label,
                    "old_quality": old_quality,
                    "target_quality": "CAS_RN_LOOKUP",
                    "cas_rn": cas_rn,
                }
            )
            continue
        if old_quality != "EXACT_MATCH":
            tally["not_exact_match"] += 1
            continue
        local = {norm(rec.get("preferred_term"))}
        local |= {norm(s.get("synonym_text")) for s in (rec.get("synonyms") or [])}
        if norm(onto_label) in local:
            tally["label_matches"] += 1  # genuinely exact; leave it
            continue
        syns = chebi_synonyms(cur, curie)
        matches = matching_surfaces(rec, syns)
        if not matches:
            tally["no_chebi_synonym_match"] += 1  # needs individual judgement
            continue
        if curie not in has_structure:
            tally["structureless_term_skipped"] += 1
            continue
        independent_matches = [match for match in matches if match["independent"]]
        if not independent_matches:
            tally["circular_evidence_only"] += 1  # also needs judgement
            continue
        hit = independent_matches[0]
        synonym_candidates.append(
            {
                "rec": rec,
                "curie": curie,
                "onto_label": onto_label,
                "old_quality": old_quality,
                "target_quality": "SYNONYM_MATCH",
                **hit,
            }
        )

    subjects_by_synonym = synonym_subjects(
        cur, [item["matched_synonym"] for item in synonym_candidates]
    )
    lexical_todo: list[dict] = []
    for item in synonym_candidates:
        subjects = subjects_by_synonym.get(norm(item["matched_synonym"]), set())
        if subjects - {item["curie"]}:
            tally["ambiguous_synonym_skipped"] += 1
            continue
        lexical_todo.append(item)

    tally["cas_rn_lookup_regrade"] = len(cas_candidates)
    tally["synonym_regrade"] = len(lexical_todo)
    tally["regrade"] = len(cas_candidates) + len(lexical_todo)
    return cas_candidates + lexical_todo, tally


def apply_one(item: dict) -> str:
    rec, om = item["rec"], item["rec"]["ontology_mapping"]
    old_quality = item["old_quality"]
    target_quality = item["target_quality"]
    om["mapping_quality"] = target_quality
    if target_quality == "CAS_RN_LOOKUP":
        rec.setdefault("curation_history", []).append(
            {
                "timestamp": STAMP,
                "curator": CURATOR,
                "action": "REGRADED_TO_CAS_RN_LOOKUP",
                "changes": (
                    f"mapping_quality {old_quality} -> CAS_RN_LOOKUP ({ISSUE}). The record "
                    f"was created by an explicit CAS-to-ChEBI lookup and its current CAS RN "
                    f"{item['cas_rn']} uniquely resolves by ChEBI xref to {item['curie']} "
                    f"{item['onto_label']!r}. CAS_RN_LOOKUP records the method that established "
                    f"this mapping; a lexical grade would discard that provenance. ontology_id "
                    f"is unchanged. The own-identifier SSSOM predicate remains skos:exactMatch "
                    f"under Rule D (#438), independently of mapping quality."
                ),
                "llm_assisted": False,
            }
        )
        return (
            f"{str(rec.get('preferred_term'))[:34]:<34} {item['curie']:<16} "
            f"via CAS {item['cas_rn']}"
        )

    if item["surface_kind"] == "preferred_term":
        match_note = (
            f"preferred_term {item['surface_text']!r} matches the ChEBI synonym "
            f"{item['matched_synonym']!r}"
        )
    else:
        match_note = (
            f"the record's independently sourced synonym {item['surface_text']!r} "
            f"(source {item['surface_source']!r}) matches the ChEBI synonym "
            f"{item['matched_synonym']!r}"
        )
    rec.setdefault("curation_history", []).append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "REGRADED_EXACT_TO_SYNONYM",
            "changes": (
                f"mapping_quality {old_quality} -> SYNONYM_MATCH ({ISSUE}). The record's label "
                f"does not equal the term's primary label {item['onto_label']!r}; {match_note} "
                f"on {item['curie']}. The schema "
                f"defines EXACT_MATCH as a direct match to the term and SYNONYM_MATCH as a "
                f"match to a known synonym, so the recorded grade overstated. ontology_id is "
                f"unchanged — the term is correct. The own-identifier SSSOM predicate remains "
                f"skos:exactMatch under Rule D (#438), independently of mapping quality."
            ),
            "llm_assisted": False,
        }
    )
    return (
        f"{str(rec.get('preferred_term'))[:34]:<34} {item['curie']:<16} "
        f"via synonym {item['matched_synonym'][:34]!r}"
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true", help="Write changes (default: dry-run).")
    ap.add_argument("--limit", type=int, help="Show only N examples in the dry-run output.")
    args = ap.parse_args(argv)

    if not CHEBI_DB.exists():
        raise SystemExit(f"chebi.db not found at {CHEBI_DB} — needed to verify synonyms.")

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    db = sqlite3.connect(f"file:{CHEBI_DB}?mode=ro", uri=True)
    try:
        todo, tally = plan(coll, db.cursor())
    finally:
        db.close()

    lines = [apply_one(i) for i in todo]
    if args.apply and todo:
        save_yaml(coll, COLLECTION)

    print(
        f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
        f"{len(todo)} record(s) re-graded\n"
    )
    for ln in lines[: args.limit or 15]:
        print(f"  {ln}")
    if len(lines) > (args.limit or 15):
        print(f"  ... {len(lines) - (args.limit or 15)} more")
    print("\nskip tally:")
    for k, v in tally.items():
        print(f"  {k:<24} {v}")
    print(
        "\nNot touched: no-match, circular-evidence, shared-synonym, ambiguous-CAS, "
        "CAS-xref conflict, and reviewed identity-conflict records need per-record "
        "judgement; preparations and hydrate-state conflicts need re-grounding, not "
        "a re-grade."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
