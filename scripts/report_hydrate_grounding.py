"""Report records whose label is a hydrate but whose term is not (#238).

MAPPING_SEMANTICS.md Section 3 makes a hydration state a distinct substance: it
takes a hydrate-specific ontology term if one exists, else its own `cas:` id with
a narrowMatch to the anhydrous parent. Grounding a hydrate directly onto the
anhydrous term is the identity collapse that produced the 32 families of #218.

The id-label gate cannot see this. Its `plausible` waiver compares
`ontology_id` against `ontology_label` -- the *term's own* label -- and hydrate
names live in `preferred_term`. Adding that pair to the gate surfaces 50
unrelated IMPLAUSIBLE_LABEL findings and still no hydrates, so this reports the
population directly instead: report-then-enforce, without breaking a gate first.

Compares each record's hydrate-notated preferred_term against its term's formula
from the local chebi.db. Exits 0 -- it is a measurement, not a gate.
"""

from __future__ import annotations

import argparse
import collections
import csv
import os
import re
import sqlite3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
REPORT = ROOT / "reports" / "hydrate_grounding.tsv"
SYN_REPORT = ROOT / "reports" / "hydrate_synonyms.tsv"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
CHEBI_DB = Path(os.path.expanduser("~/.data/oaklib/chebi.db"))


def _load_hydrate_notation():
    """Load the shared regexes WITHOUT importing the package.

    `mediaingredientmech.curation.__init__` imports ingredient_curator, which
    imports linkml_runtime — so a plain package import would turn this
    stdlib+PyYAML script into one that needs the full dependency set, and this
    repo has four CI jobs that deliberately run scripts with only pyyaml (and
    click/rich). hydrate_guard itself imports nothing but `re` and `typing`.
    """
    import importlib.util

    path = ROOT / "src" / "mediaingredientmech" / "curation" / "hydrate_guard.py"
    spec = importlib.util.spec_from_file_location("_hydrate_guard", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return (
        mod.HYDRATE_NOTATION,
        mod.FORMULA_WATER,
        mod.water_multiplicity,
        mod.implausible_water_counts,
    )


HYDRATE, FORMULA_WATER, water_multiplicity, implausible_water_counts = _load_hydrate_notation()

# Machine-readable classification for the hydrate-synonym rows. Separate from
# the `detail` prose so the two cannot drift apart (#259).
DIFFERENT_STATE = "different_state"
ANHYDROUS_TERM = "anhydrous_term"
MALFORMED_NOTATION = "malformed_notation"
HYDRATE_FIELDS = [
    "identifier",
    "preferred_term",
    "ontology_id",
    "ontology_label",
    "term_formula",
    "status",
]
OK_LOCAL_REGISTRY_ID = "OK_LOCAL_REGISTRY_ID"
SYNONYM_FIELDS = [
    "identifier",
    "preferred_term",
    "ontology_id",
    "kind",
    "detail",
    "hydrate_synonyms",
]


def term_is_hydrate(
    ontology_id: str,
    ontology_label: str,
    form: dict[str, str],
) -> bool:
    """Water as its own formula component, or the term's own label saying so.

    Both tests come from hydrate_guard so they cannot drift: a bare "H2O"
    substring matches `H2O4P` (dihydrogenphosphate, no water), and a bare
    /hydrate/ matches `borohydrate` and `carbohydrate` — two live MIM targets
    (`CHEBI:195690` monochlorohydrate, `cas:9036-88-8` b-Mannan borohydrate)
    would otherwise be called hydrate terms.
    """
    return bool(
        FORMULA_WATER.search(form.get(ontology_id, "")) or HYDRATE.search(str(ontology_label or ""))
    )


def formula_known(ontology_id: str, form: dict[str, str]) -> bool:
    return bool(form.get(ontology_id))


def classify_hydrate_rows(
    records: list[dict],
    form: dict[str, str],
    cas_anchored: set[str],
    local_anchored: set[str] | None = None,
) -> list[dict]:
    if local_anchored is None:
        local_anchored = cas_anchored
    rows = []
    for rec in records:
        if rec.get("mapping_status") == "REJECTED":
            continue
        term = str(rec.get("preferred_term") or "")
        if not HYDRATE.search(term):
            continue
        ident = str(rec.get("identifier") or "")
        om = rec.get("ontology_mapping") or {}
        target = str(om.get("ontology_id") or "")
        f = form.get(target, "")
        is_hydrate = term_is_hydrate(target, om.get("ontology_label"), form)
        if ident.startswith("cas:"):
            status = "OK_OWN_CAS_ID" if term in cas_anchored else "CAS_MISSING_ANCHOR_ROWS"
        elif ident.startswith("kgmicrobe.") and term in local_anchored:
            status = OK_LOCAL_REGISTRY_ID
        elif is_hydrate:
            status = "OK_HYDRATE_TERM"
        elif target.startswith("CHEBI:") and f:
            status = "HYDRATE_ON_ANHYDROUS_TERM"
        else:
            status = "UNKNOWN_NO_FORMULA"
        rows.append(
            {
                "identifier": ident,
                "preferred_term": term,
                "ontology_id": target,
                "ontology_label": om.get("ontology_label") or "",
                "term_formula": f,
                "status": status,
            }
        )
    return rows


def hydrate_synonyms(rec: dict) -> list[str]:
    return [
        str(sy.get("synonym_text") or "")
        for sy in (rec.get("synonyms") or [])
        if is_resolving_synonym(sy or {}) and HYDRATE.search(str(sy.get("synonym_text") or ""))
    ]


def classify_synonym_rows(records: list[dict], form: dict[str, str]) -> list[dict]:
    syn_rows = []
    for rec in records:
        if rec.get("mapping_status") == "REJECTED":
            continue
        term = str(rec.get("preferred_term") or "")
        om = rec.get("ontology_mapping") or {}
        target = str(om.get("ontology_id") or "")
        hyd = hydrate_synonyms(rec)
        if not hyd:
            continue
        malformed = [syn for syn in hyd if implausible_water_counts(syn)]
        if malformed:
            counts = sorted(
                {count for synonym in malformed for count in implausible_water_counts(synonym)},
                key=int,
            )
            syn_rows.append(
                {
                    "identifier": str(rec.get("identifier") or ""),
                    "preferred_term": term,
                    "ontology_id": target,
                    "kind": MALFORMED_NOTATION,
                    "detail": "water count above plausible ceiling: " + ", ".join(counts),
                    "hydrate_synonyms": " | ".join(malformed),
                }
            )
        if HYDRATE.search(term):
            # The record's own label is a hydrate, but a synonym may name a
            # DIFFERENT state (`MgSO4·7H2O` with `MgSO4 x 6 H2O`) — the same
            # Section 3 collapse, and one the mapped bucket calls clean.
            # water_multiplicity returns None for "unspecified", which must not
            # count as a mismatch (#254).
            here = water_multiplicity(term)
            if here is None:
                continue
            other = sorted(
                {w for w in (water_multiplicity(h) for h in hyd) if w is not None and w != here},
                key=float,
            )
            if not other:
                continue  # same state, just respelled
            syn_rows.append(
                {
                    "identifier": str(rec.get("identifier") or ""),
                    "preferred_term": term,
                    "ontology_id": target,
                    # `kind` is the machine key; `detail` is prose for a
                    # human and may be reworded freely (#259).
                    "kind": DIFFERENT_STATE,
                    "detail": f"record states {here} H2O; synonyms state " + ", ".join(other),
                    "hydrate_synonyms": " | ".join(hyd),
                }
            )
            continue
        if term_is_hydrate(target, om.get("ontology_label"), form):
            continue  # the term itself is the hydrate
        if not formula_known(target, form):
            continue  # cannot tell; do not assert either way
        syn_rows.append(
            {
                "identifier": str(rec.get("identifier") or ""),
                "preferred_term": term,
                "ontology_id": target,
                "kind": ANHYDROUS_TERM,
                "detail": "term formula has no water",
                "hydrate_synonyms": " | ".join(hyd),
            }
        )
    return syn_rows


def split_synonym_buckets(rows: list[dict]) -> dict[str, list[dict]]:
    # Key on `kind`, not on a substring of `detail`. The split used to test
    # `"states" in r["detail"]`, so rewording the human-readable sentence -- or
    # a term label that happens to contain "states" -- silently reclassified
    # rows between the two buckets the summary reports (#259).
    out: dict[str, list[dict]] = collections.defaultdict(list)
    for row in rows:
        out[row["kind"]].append(row)
    return out


def formulas() -> dict[str, str]:
    if not CHEBI_DB.exists():
        # exit 2, not 0: "cannot measure" must not be indistinguishable from
        # "measured, nothing found" to anyone reading exit codes.
        print(f"ERROR: no chebi.db at {CHEBI_DB}; cannot compare formulas")
        raise SystemExit(2)
    con = sqlite3.connect(CHEBI_DB)
    q = (
        "select subject, value from statements "
        "where predicate like '%formula%' and subject like 'CHEBI:%'"
    )
    return dict(con.execute(q))


def anchored_subjects() -> tuple[set[str], set[str]]:
    """Return subject_labels with Section 3 anchors and local registry anchors.

    `cas:` records still require BOTH a parent narrow/broadMatch and the Rule B1
    kgmicrobe registry row — Section 3 step 2 requires both, not just a cas: id.
    Local kgmicrobe identities may use closeMatch for malformed or unresolved
    hydrate labels whose anhydrous parent is related but not a subclass (#342,
    #344).
    """
    labels: dict[str, str] = {}
    cas_parents: set[str] = set()
    local_parents: set[str] = set()
    registry: set[str] = set()
    # the file opens with a commented YAML curie_map preamble; DictReader would
    # otherwise take the first comment line as the header and match nothing
    lines = SSSOM.read_text().splitlines(keepends=True)
    start = next(i for i, ln in enumerate(lines) if ln.startswith("subject_id"))
    with __import__("io").StringIO("".join(lines[start:])) as fh:
        r = csv.DictReader(fh, delimiter="\t")
        for row in r:
            sid, lab, pred, obj = (
                row.get("subject_id"),
                row.get("subject_label"),
                row.get("predicate_id", ""),
                row.get("object_id", ""),
            )
            if not sid or not lab:
                continue
            labels[sid] = lab
            if pred in ("skos:narrowMatch", "skos:broadMatch"):
                cas_parents.add(sid)
                local_parents.add(sid)
            elif pred == "skos:closeMatch" and not obj.startswith("kgmicrobe."):
                local_parents.add(sid)
            elif pred == "skos:exactMatch" and obj.startswith("kgmicrobe."):
                registry.add(sid)

    return (
        {labels[sid] for sid in cas_parents & registry},
        {labels[sid] for sid in local_parents & registry},
    )


def baseline_identifiers() -> set[str]:
    """Identifiers already tracked in the duplicate-identifier baseline, so the
    report can say which findings are genuinely new to tooling rather than
    claiming no gate sees any of them."""
    path = ROOT / "mappings" / "duplicate_identifier_baseline.tsv"
    if not path.exists():
        return set()
    with path.open() as fh:
        return {r["identifier"] for r in csv.DictReader(fh, delimiter="\t")}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=25, help="cap the violations list")
    ap.add_argument(
        "--queue-limit", type=int, default=25, help="cap the UNMAPPED pending-queue list"
    )
    ap.add_argument("--synonym-limit", type=int, default=15, help="cap the hydrate-synonym list")
    args = ap.parse_args()

    form = formulas()
    cas_anchored, local_anchored = anchored_subjects()

    # parsed once: re-reading this 6.7 MB / 2308-record file for the second scan
    # cost +55% wall clock
    mapped_records = yaml.safe_load(MAPPED.read_text())["ingredients"]
    baseline_ids = baseline_identifiers()
    rows = classify_hydrate_rows(mapped_records, form, cas_anchored, local_anchored)

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=HYDRATE_FIELDS,
            delimiter="\t",
            lineterminator="\n",
        )
        w.writeheader()
        w.writerows(rows)
    if not rows:
        print("no mapped record carries hydrate notation")

    c = collections.Counter(r["status"] for r in rows)
    print(f"{len(rows)} record(s) whose preferred_term carries hydrate notation\n")
    for k in (
        "HYDRATE_ON_ANHYDROUS_TERM",
        "CAS_MISSING_ANCHOR_ROWS",
        "OK_HYDRATE_TERM",
        "OK_OWN_CAS_ID",
        OK_LOCAL_REGISTRY_ID,
        "UNKNOWN_NO_FORMULA",
    ):
        if c.get(k):
            print(f"  {k:28} {c[k]}")
    bad = [r for r in rows if r["status"] == "HYDRATE_ON_ANHYDROUS_TERM"]
    if bad:
        print("\nGrounded onto a term whose formula has no water (Section 3 violations):")
        for r in bad[: args.limit]:
            print(
                f"  {r['preferred_term'][:34]:34} -> {r['ontology_id']:14} "
                f"{r['ontology_label'][:26]:26} [{r['term_formula']}]"
            )
        if len(bad) > args.limit:
            print(f"  ... and {len(bad) - args.limit} more")
    # The guard added in #246 refuses these rather than mis-filing them, so they
    # stay UNMAPPED. Without a worklist the hydrate residual grows invisibly
    # instead of visibly, which is only an improvement if someone can see it (#247).
    # A merge folds the hydrate in as a synonym rather than giving it its own
    # identifier, so the #218 collapse survives post-merge where the mapped
    # bucket cannot see it -- that bucket keys on preferred_term. Two shapes:
    #   ANHYDROUS_TERM   preferred_term is not a hydrate at all
    #   HYDRATION_STATE  preferred_term IS a hydrate, but a synonym names a
    #                    DIFFERENT one (MgSO4·7H2O carrying MgSO4 x 6 H2O).
    #                    These land in OK_HYDRATE_TERM above, i.e. reported clean.
    #   MALFORMED        a synonym's digit count is parse damage, not a real
    #                    hydration state (MgCl2 x 76 H2O).
    # Issue #251.
    syn_rows = classify_synonym_rows(mapped_records, form)
    buckets = split_synonym_buckets(syn_rows)
    mismatched = buckets[DIFFERENT_STATE]
    anhydrous = buckets[ANHYDROUS_TERM]
    malformed = buckets[MALFORMED_NOTATION]
    print(
        f"\n{len(syn_rows)} hydrate-synonym finding(s) their own term does "
        f"not account for\n  {len(anhydrous)} on an anhydrous term, "
        f"{len(mismatched)} naming a different hydration state, "
        f"{len(malformed)} with malformed notation."
    )
    if syn_rows:
        known = {r["identifier"] for r in syn_rows} & baseline_ids
        print(
            f"\n{len(known)} of these identifiers are already tracked in "
            "mappings/duplicate_identifier_baseline.tsv\n(as HYDRATE_FAMILY_UNREVIEWED); "
            f"the other {len({r['identifier'] for r in syn_rows}) - len(known)} are not "
            "tracked by any existing check."
        )
        for r in syn_rows[: args.synonym_limit]:
            print(
                f"  {r['identifier']:16} {r['preferred_term'][:22]:22} "
                f"<- {r['hydrate_synonyms'][:44]}"
            )
        if len(syn_rows) > args.synonym_limit:
            print(
                f"  ... and {len(syn_rows) - args.synonym_limit} more "
                f"(full list in {SYN_REPORT.relative_to(ROOT)})"
            )
    SYN_REPORT.parent.mkdir(parents=True, exist_ok=True)
    with SYN_REPORT.open("w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            delimiter="\t",
            fieldnames=SYNONYM_FIELDS,
            lineterminator="\n",
        )
        w.writeheader()
        w.writerows(syn_rows)

    if not UNMAPPED.exists():
        print(f"\nERROR: {UNMAPPED.relative_to(ROOT)} is missing; cannot report the pending queue")
        return 2
    doc = yaml.safe_load(UNMAPPED.read_text()) or {}
    if not isinstance(doc.get("ingredients"), list):
        print(f"\nERROR: {UNMAPPED.relative_to(ROOT)} has no 'ingredients' list")
        return 2
    # 'MES Hydrat' is the German spelling and its own history action is
    # REVIEWED_HYDRATE_AMBIGUITY -- the one record whose audit trail says "this is
    # the hydrate problem" was the one the \bhydrate\b anchor dropped.
    pending = [
        r
        for r in doc["ingredients"]
        if r.get("mapping_status") == "UNMAPPED"
        and (
            HYDRATE.search(str(r.get("preferred_term") or ""))
            or re.search(r"(?<![a-z])hydrat\b", str(r.get("preferred_term") or ""), re.IGNORECASE)
        )
    ]

    def occ(r: dict) -> int:
        return (r.get("occurrence_statistics") or {}).get("total_occurrences") or 0

    pending.sort(key=occ, reverse=True)  # a 4-medium record is not a 0-medium one
    print(f"\n{len(pending)} UNMAPPED record(s) whose label carries hydrate notation.")
    if pending:
        print(
            "This is the queue the #246 guard refuses into; it also holds records that "
            "predate\nthe guard. Each needs MAPPING_SEMANTICS.md Section 3: a "
            "hydrate-specific ontology term\nif one exists, else its own cas:<hydrate CAS> "
            "with a narrowMatch to the parent plus\nthe Rule B1 registry row."
        )
        for r in pending[: args.queue_limit]:
            print(
                f"  {str(r.get('identifier')):16} occ={occ(r):<4} "
                f"{str(r.get('preferred_term'))[:48]}"
            )
        if len(pending) > args.queue_limit:
            print(f"  ... and {len(pending) - args.queue_limit} more")

    print(f"\nreport: {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
