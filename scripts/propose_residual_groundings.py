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
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import yaml
from oaklib.datamodels.search import SearchConfiguration, SearchProperty

_REPO = Path(__file__).resolve().parent.parent
TRIAGE = _REPO / "reports" / "culturemech_residual_triage.tsv"
OUT = _REPO / "reports" / "culturemech_residual_groundings.tsv"

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


def exact_hits(adapter, query: str, prefix: str) -> list[tuple[str, str]]:
    """Return (curie, label) for terms whose label or exact synonym equals `query`."""
    wanted = comparison_key(query)
    if not wanted:
        return []
    # The default search config covers labels only. Most recipe surface forms are
    # synonyms rather than primary labels, so without ALIAS this finds almost nothing --
    # it reported 0 hits on the whole canary set.
    config = SearchConfiguration(properties=[SearchProperty.LABEL, SearchProperty.ALIAS])
    out = []
    for curie in list(adapter.basic_search(query, config=config))[:25]:
        if not str(curie).startswith(f"{prefix}:"):
            continue
        label = adapter.label(curie) or ""
        names = {comparison_key(label)}
        if prefix not in LABEL_ONLY:
            try:
                names.update(comparison_key(a) for a in adapter.entity_aliases(curie))
            except Exception:  # noqa: BLE001 - alias lookup is best-effort per term
                pass
        if wanted in names:
            out.append((str(curie), label))
    return out


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
    args = parser.parse_args(argv)

    if not args.triage.is_file():
        raise SystemExit(
            f"triage report not found: {args.triage}\n"
            "Run: python scripts/triage_culturemech_residual.py"
        )
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
    adapters = []
    for prefix in sources:
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
        for query in candidate_queries(label, triage.fold):
            for prefix, adapter in adapters:
                for curie, term_label in exact_hits(adapter, query, prefix):
                    hits.append((curie, term_label, query))
                if hits:
                    # First ontology in preference order that answers exactly wins; a
                    # lower-priority ontology carrying the same name adds no information.
                    break
            if hits:
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
