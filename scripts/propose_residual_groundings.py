#!/usr/bin/env python3
"""Propose exact ontology groundings for the CultureMech residual.

`triage_culturemech_residual.py` leaves a RESIDUAL bucket: surface forms genuinely
absent from MIM. This tool searches them against CHEBI and reports only what it can
justify as an *exact* match -- the query equals the term's label or one of its exact
synonyms, case-insensitively. Nothing fuzzy is proposed, because a wrong grounding is
worse than an honest miss.

Every hit is then routed by whether MIM already holds the CURIE, which is the finding
that reshaped the #260 pass:

    SYNONYM_ONTO_EXISTING   a record already holds this CURIE. In MIM the `identifier`
                            IS the ontology CURIE, so minting a second record on it is a
                            duplicate by construction (the `Butane-1,4-diol` defect).
                            The fix is to add the surface form as a synonym.
    NEW_RECORD              the CURIE is free; a record can be created for it.

Read-only. Writes a review TSV; applies nothing. Groundings are applied by
`apply_culturemech_aliases.py` (synonyms) or the collection-edit path (new records).

Usage:
    python scripts/propose_residual_groundings.py --limit 10     # canary
    python scripts/propose_residual_groundings.py
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

import yaml
from oaklib.datamodels.search import SearchConfiguration, SearchProperty

_REPO = Path(__file__).resolve().parent.parent
TRIAGE = _REPO / "mappings" / "culturemech_residual_triage.tsv"
OUT = _REPO / "mappings" / "culturemech_residual_groundings.tsv"

# Shared with the triage fold: the codepoints recipe text uses and ontologies do not.
_UNICODE_FOLD = {
    "\u00b7": ".", "\u2022": ".", "\u00d7": "x", "\u2032": "'", "\u2019": "'",
    "\u2018": "'", "\u201c": '"', "\u201d": '"', "\u2013": "-", "\u2014": "-",
    "\u2212": "-", "\u3000": " ", "\uff65": ".",
}
_SUBSCRIPTS = str.maketrans("\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089", "0123456789")


def _triage_module():
    spec = importlib.util.spec_from_file_location(
        "triage", _REPO / "scripts" / "triage_culturemech_residual.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def held_curies() -> dict[str, str]:
    """Map every CURIE MIM already holds as a record identifier -> preferred term."""
    held: dict[str, str] = {}
    for path in (_REPO / "data" / "ingredients").rglob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data.get("identifier"):
            held[str(data["identifier"])] = str(data.get("preferred_term") or "")
    if not held:
        raise SystemExit("no ingredient records found")
    return held


def mim_unmapped_rows(ingredient_type: str | None) -> list[dict[str, str]]:
    """MIM's own UNMAPPED records as a worklist, newest-first by occurrence.

    Restricting to SINGLE_INGREDIENT matters. Of 269 UNMAPPED records, 102 are
    NAMED_MEDIUM -- whole culture media rather than ingredients, whose home is a
    `CultureMechReference` link (#489), not an ontology term; grounding one as an
    ingredient is a category error. Another 91 are UNDEFINED_MIXTURE, for which
    staying UNMAPPED is the correct outcome. Only the remainder is a grounding backlog.
    """
    rows = []
    for path in sorted((_REPO / "data" / "ingredients" / "unmapped").glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("mapping_status") != "UNMAPPED":
            continue
        if ingredient_type and data.get("ingredient_type") != ingredient_type:
            continue
        stats = data.get("occurrence_statistics") or {}
        rows.append(
            {
                "bucket": "MIM_UNMAPPED",
                "label": str(data.get("preferred_term") or ""),
                "occurrences": str(stats.get("total_occurrences") or 0),
                "recipes": str(stats.get("media_count") or 0),
                "folded": "",
                "mim_identifier": str(data.get("identifier") or ""),
                "mim_label": str(data.get("preferred_term") or ""),
                "culturemech_reason": str(data.get("ingredient_type") or ""),
            }
        )
    if not rows:
        raise SystemExit("no matching UNMAPPED records found")
    return rows


def candidate_queries(label: str, fold_decoration) -> list[str]:
    """Conservative query variants: the label itself, and the label without decoration.

    Deliberately no hydrate stripping. `strip_hydrate_notation` truncates every
    spelled-out hydrate to a meaningless stem (#503), and more importantly a hydration
    state is identity (MAPPING_SEMANTICS.md Section 3) -- searching the anhydrous parent
    for a hydrate surface form is how a wrong grounding gets proposed.
    """
    queries = [label]
    # The codepoint-normalised form must be SEARCHED, not merely compared against:
    # oaklib returns nothing for a query carrying U+2032 PRIME or subscript digits, so
    # `[1,1<PRIME>-Biphenyl]-2-ol` found no hit even though CHEBI:17043 lists it verbatim.
    normalised = comparison_key(label)
    if normalised and normalised != label:
        queries.append(normalised)
    stripped = fold_decoration(label)
    if stripped and stripped.casefold() not in {q.casefold() for q in queries}:
        queries.append(stripped)
    return queries


def comparison_key(text: str) -> str:
    """Casefold a name for equality testing, without discarding chemistry.

    Only codepoint variation is folded -- recipe text writes U+2032 PRIME where CHEBI
    writes an ASCII apostrophe, and subscript digits where CHEBI writes ASCII, so
    `[1,1′-Biphenyl]-2-ol` and `[1,1'-biphenyl]-2-ol` are the same name. Punctuation
    is deliberately NOT stripped: that would make `EDTA` and `EDTA-2Na` compare equal.
    """
    text = unicodedata.normalize("NFKC", text)
    for src, dst in _UNICODE_FOLD.items():
        text = text.replace(src, dst)
    return " ".join(text.translate(_SUBSCRIPTS).casefold().split())


# Ontologies whose alias space collides with ingredient names, so only a primary-label
# match is trustworthy. NCIT carries gene symbols and clinical concepts as synonyms: `B12`
# resolves through them to `TNFAIP1 wt Allele`, which would assert that vitamin B12 is a
# gene allele. Requiring the primary label removes that class of hit entirely.
LABEL_ONLY = frozenset({"NCIT", "MESH"})

# Below this length a name carries too little information for an exact match to mean
# anything: ontologies use short strings as formula and abbreviation synonyms across
# unrelated branches. `X` matched UBERON's "area X of ventral lateral nucleus" and `Ca`
# matched through a formula alias. Short labels are reported for curation, not proposed.
MIN_QUERY_LENGTH = 3

# An exact string match says nothing about whether the term denotes a *substance*.
# `Dissolve` matches NCIT:C64929 ("Dissolve", a procedure) and `Stock A` matches
# NCIT:C14643 -- both perfect label matches, neither an ingredient. That is the defect
# class of #356, where `X` was published as EXACT_MATCH against the 24th letter of the
# alphabet on a record with 101 occurrences. For ontologies broad enough to contain
# non-substances, require the term to descend from a substance root.
SUBSTANCE_ROOTS = {
    "NCIT": frozenset({"NCIT:C1908"}),  # Drug, Food, Chemical or Biomedical Material
}

# Prefixes whose accessions must be confirmed to round-trip before a proposal on them can
# be published. `promote_resolved_unmapped.canonical_label` performs the check and refuses
# `is_defining_ontology=false`.
ROUND_TRIP_CHECKED = frozenset({"MICRO"})


@lru_cache(maxsize=1)
def promoter():
    """The promotion helper, loaded lazily so the common path pays nothing for it."""
    spec = importlib.util.spec_from_file_location(
        "promote_resolved_unmapped", _REPO / "scripts" / "promote_resolved_unmapped.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["promote_resolved_unmapped"] = module
    spec.loader.exec_module(module)
    return module


def denotes_a_substance(adapter, curie: str, prefix: str) -> bool:
    """Whether `curie` descends from one of its ontology's substance roots.

    Only consulted for ontologies in SUBSTANCE_ROOTS. Anything else is assumed to be
    substance-scoped already (CHEBI, FOODON) or narrow enough not to need it.
    """
    roots = SUBSTANCE_ROOTS.get(prefix)
    if not roots:
        return True
    try:
        from oaklib.datamodels.vocabulary import IS_A  # noqa: PLC0415

        ancestors = set(adapter.ancestors([curie], predicates=[IS_A]))
    except Exception:  # noqa: BLE001 - an unavailable hierarchy must not silently pass
        return False
    return bool(ancestors & roots)


def exact_hits(adapter, query: str, prefix: str) -> list[tuple[str, str]]:
    """Return (curie, label) for terms whose label or exact synonym equals `query`."""
    wanted = comparison_key(query)
    if len(wanted) < MIN_QUERY_LENGTH:
        return []
    if not wanted:
        return []
    # The default search config covers labels only. Most recipe surface forms are
    # synonyms rather than primary labels, so without ALIAS this finds almost nothing --
    # it reported 0 hits on the whole canary set.
    config = SearchConfiguration(properties=[SearchProperty.LABEL, SearchProperty.ALIAS])
    trusted = getattr(adapter, "server_side_exact", False)
    out = []
    for curie in list(adapter.basic_search(query, config=config))[:25]:
        if not str(curie).startswith(f"{prefix}:"):
            continue
        label = adapter.label(curie) or ""
        if trusted:
            if denotes_a_substance(adapter, str(curie), prefix):
                out.append((str(curie), label))
            continue
        names = {comparison_key(label)}
        if prefix not in LABEL_ONLY:
            try:
                names.update(comparison_key(a) for a in adapter.entity_aliases(curie))
            except Exception:  # noqa: BLE001 - alias lookup is best-effort per term
                pass
        if wanted in names and denotes_a_substance(adapter, str(curie), prefix):
            out.append((str(curie), label))
    return out


class OlsAdapter:
    """Minimal exact-search backend for an ontology with no local semantic-sql build.

    MICRO ships as a 0-byte stub locally, and it is the ontology that actually models
    named growth media -- so without this every commercial broth and agar falls to
    NO_EXACT_HIT and looks like it needs minting when MAPPING_SEMANTICS Section 3 step 1
    would have grounded it.

    `queryFields` is not optional: without it OLS4's default search returned 0 hits for
    `MRS agar` and `nutrient broth`, both of which MICRO carries verbatim. The
    `ontology=` filter is also not trusted -- it leaks CHEBI rows -- so results are
    filtered on the CURIE prefix here.
    """

    BASE = "https://www.ebi.ac.uk/ols4/api/search"

    # OLS4 is asked for `exact=true` over `label,synonym`, so a returned term already
    # matched the query exactly on one of them. Re-checking client-side against the label
    # alone would discard every synonym match: `Christensen's urea agar` is an exact MICRO
    # synonym of `urea agar` (MICRO:0000643), and the check threw it away. That made the
    # whole MICRO pass label-only without saying so.
    server_side_exact = True

    def __init__(self, prefix: str, pause: float = 0.34) -> None:
        self.prefix = prefix
        self.pause = pause
        self._labels: dict[str, str] = {}

    def basic_search(self, query: str, config=None):  # noqa: ARG002 - adapter protocol
        params = urllib.parse.urlencode(
            {
                "q": query,
                "ontology": self.prefix.lower(),
                "queryFields": "label,synonym",
                "exact": "true",
                "rows": 10,
            }
        )
        request = urllib.request.Request(
            f"{self.BASE}?{params}", headers={"User-Agent": "MediaIngredientMech-grounding"}
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.load(response)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            print(f"  (OLS4 lookup failed for {query!r}: {exc})", file=sys.stderr)
            return []
        finally:
            time.sleep(self.pause)
        out = []
        for doc in payload.get("response", {}).get("docs", []):
            curie = str(doc.get("obo_id") or "")
            if curie.startswith(f"{self.prefix}:"):
                self._labels[curie] = str(doc.get("label") or "")
                out.append(curie)
        return out

    def label(self, curie: str) -> str:
        return self._labels.get(curie, "")

    def entity_aliases(self, curie: str):  # noqa: ARG002 - adapter protocol
        # Never consulted: `server_side_exact` short-circuits the client-side check.
        # Re-deriving real aliases would cost one request per term for no added trust.
        return [self._labels.get(curie, "")]


def recheck(report: Path, out: Path) -> int:
    """Re-apply the current guards to an existing proposals report.

    A full pass is expensive, so when a guard is added after a run the proposals it
    would now reject are removed here rather than by re-searching every label. Only
    rejects: a row this cannot re-validate is dropped, never upgraded, so recheck can
    never introduce a proposal the run did not make.
    """
    from oaklib import get_adapter  # noqa: PLC0415

    with report.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    adapters: dict[str, object] = {}
    kept, dropped = [], []
    for row in rows:
        curie, verdict = row.get("curie", ""), row.get("verdict", "")
        if verdict not in ("NEW_RECORD", "SYNONYM_ONTO_EXISTING") or not curie:
            kept.append(row)
            continue
        if len(comparison_key(row["label"])) < MIN_QUERY_LENGTH:
            dropped.append((row["label"], curie, "label shorter than MIN_QUERY_LENGTH"))
            continue
        prefix = curie.split(":", 1)[0]
        if prefix in ROUND_TRIP_CHECKED:
            # MicrO has ~1,472 classes under a malformed IRI that do not round-trip:
            # kg-microbe's ontology transform never produces them, so a published row
            # would dangle. curie.py gates MICRO behind MICRO_VERIFIED for this reason,
            # and a proposal on such an id is unpublishable however good the label match.
            try:
                promoter().canonical_label(curie)
            except SystemExit as exc:
                dropped.append((row["label"], curie, str(exc).split(" (IRI")[0]))
                continue
        if prefix in SUBSTANCE_ROOTS:
            if prefix not in adapters:
                adapters[prefix] = get_adapter(f"sqlite:obo:{prefix.lower()}")
            if not denotes_a_substance(adapters[prefix], curie, prefix):
                dropped.append((row["label"], curie, f"outside the {prefix} substance branch"))
                continue
        kept.append(row)

    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(kept)
    print(f"rechecked {len(rows)} rows; dropped {len(dropped)} proposal(s)")
    for label, curie, why in dropped:
        print(f"  - {label!r} -> {curie}: {why}")
    print(f"\nwrote {out}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--triage", type=Path, default=TRIAGE)
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--limit", type=int, help="only the N highest-occurrence labels (canary)")
    parser.add_argument("--bucket", default="RESIDUAL")
    parser.add_argument(
        "--sources",
        default="CHEBI,FOODON,ENVO,UBERON,BTO,NCIT",
        help="ontology prefixes to search, in preference order",
    )
    parser.add_argument(
        "--ols-sources",
        default="MICRO",
        help="of --sources, which to query over OLS4 rather than a local build",
    )
    parser.add_argument(
        "--from-mim-unmapped",
        action="store_true",
        help="work MIM's own UNMAPPED records instead of the CultureMech triage",
    )
    parser.add_argument(
        "--ingredient-type",
        default="SINGLE_INGREDIENT",
        help="with --from-mim-unmapped, restrict to this ingredient_type ( for all)",
    )
    parser.add_argument(
        "--recheck",
        type=Path,
        help="re-apply current guards to an existing report instead of searching",
    )
    args = parser.parse_args(argv)

    if args.recheck:
        return recheck(args.recheck, args.out)

    if args.from_mim_unmapped:
        rows = mim_unmapped_rows(args.ingredient_type)
    elif not args.triage.is_file():
        raise SystemExit(
            f"triage report not found: {args.triage}\n"
            "Run: python scripts/triage_culturemech_residual.py"
        )
    else:
        with args.triage.open(encoding="utf-8", newline="") as handle:
            rows = [r for r in csv.DictReader(handle, delimiter="\t") if r["bucket"] == args.bucket]
        if not rows:
            raise SystemExit(f"no {args.bucket} rows in {args.triage}")
    rows.sort(key=lambda r: -int(r["occurrences"]))
    if args.limit:
        rows = rows[: args.limit]

    triage = _triage_module()
    held = held_curies()

    from oaklib import get_adapter

    # Preference order when more than one ontology carries the same exact name. It follows
    # the routing table in the map-media-ingredients skill: chemical identity first, then
    # food/biological material, then clinical reagent, then environmental and anatomical.
    # MICRO is absent because its local semantic-sql build is a 0-byte stub; named media
    # therefore stay in NO_EXACT_HIT rather than being silently routed elsewhere.
    sources = [s.strip().upper() for s in args.sources.split(",") if s.strip()]
    via_ols = {s.strip().upper() for s in args.ols_sources.split(",") if s.strip()}
    adapters = []
    for prefix in sources:
        if prefix in via_ols:
            adapters.append((prefix, OlsAdapter(prefix)))
            continue
        try:
            adapters.append((prefix, get_adapter(f"sqlite:obo:{prefix.lower()}")))
        except Exception as exc:  # noqa: BLE001 - a missing build must not kill the run
            print(f"  (skipping {prefix}: {exc})", file=sys.stderr)
    if not adapters:
        raise SystemExit("no ontology adapters available")

    results = []
    for row in rows:
        label = row["label"]
        hits: list[tuple[str, str, str]] = []
        queries = candidate_queries(label, triage.fold)
        # Ontology preference has to dominate the query variants, not the other way round.
        # With queries outer, the RAW query found a match at a low-priority ontology before
        # the NORMALISED query ever reached a high-priority one -- oaklib's search is
        # case-sensitive, so `Air` missed ENVO's `air` and landed on NCIT while the
        # lowercase surface form `air` resolved to ENVO. The same substance took two
        # different ontologies based on nothing but capitalisation.
        for prefix, adapter in adapters:
            for query in queries:
                for curie, term_label in exact_hits(adapter, query, prefix):
                    hits.append((curie, term_label, query))
                if hits:
                    break
            if hits:
                # First ontology in preference order that answers exactly wins; a
                # lower-priority ontology carrying the same name adds no information.
                break
        if not hits:
            results.append({**row, "verdict": "NO_EXACT_HIT", "curie": "", "term_label": "", "matched_query": "", "holder": ""})
            continue
        curies = {h[0] for h in hits}
        if len(curies) > 1:
            results.append({**row, "verdict": "MULTIPLE_EXACT", "curie": "|".join(sorted(curies)),
                            "term_label": hits[0][1], "matched_query": hits[0][2], "holder": ""})
            continue
        curie, term_label, query = hits[0]
        holder = held.get(curie, "")
        verdict = "SYNONYM_ONTO_EXISTING" if holder else "NEW_RECORD"
        results.append({**row, "verdict": verdict, "curie": curie, "term_label": term_label,
                        "matched_query": query, "holder": holder})

    args.out.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) + ["verdict", "curie", "term_label", "matched_query", "holder"]
    with args.out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(results)

    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for r in results:
        counts[r["verdict"]][0] += 1
        counts[r["verdict"]][1] += int(r["occurrences"])
    print(f"{args.bucket} labels searched: {len(results)}")
    for verdict in sorted(counts):
        n, occ = counts[verdict]
        print(f"  {verdict:<22} {n:5d} labels  {occ:5d} occurrences")
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
