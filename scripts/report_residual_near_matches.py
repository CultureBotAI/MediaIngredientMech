#!/usr/bin/env python3
"""Near-match review report for the residual that has no exact ontology match.

`propose_residual_groundings.py` proposes only exact matches, because a wrong
grounding is worse than an honest UNMAPPED. That leaves ~1,200 CultureMech surface
forms with no proposal at all. Many of them are close to a real term and a curator
could settle them in seconds -- but "close" is exactly where the dangerous mistakes
live, so this tool **reports and never applies**.

The similarity score is the least useful column. The `risks` column is the point:
it names *what differs* between the surface form and the candidate, because in this
domain the small differences are the ones that change the compound.

    HYDRATION_STATE   `MgSO4 x 7 H2O` vs `magnesium sulfate` -- 246.47 vs 120.37 g/mol.
                      MAPPING_SEMANTICS.md Section 3: these are different compounds and
                      must not share an identifier.
    FORMULA_DIGITS    `H3BO4` vs `H3BO3`. Usually a transcription error, sometimes a
                      genuinely different species. Never decidable from the string.
    STEREOCHEMISTRY   `DL-Serine` vs `serine`. A racemate is not the stereo-unspecified
                      parent; the corpus grades these CLOSE_MATCH, not EXACT.
    SALT_OR_ION_FORM  `Sodium glycerophosphate` vs `glycerophosphate`, `citrate` vs
                      `citric acid`. Different formula weight, often different solubility.
    PHYSICAL_STATE    `N2 gas` vs `dinitrogen`; `... solution` vs the solute.
    CONCENTRATION     a percentage or molarity survived into the comparison.
    TOKEN_DIFFERENCE  plain extra or missing words -- the residual category.

A row carrying no risk flag is a spelling or word-order difference only, and is the
safest thing on the list. A row carrying HYDRATION_STATE or FORMULA_DIGITS should be
assumed wrong until a curator confirms otherwise.

Read-only. Writes a TSV; edits nothing.

Usage:
    python scripts/report_residual_near_matches.py --limit 20        # canary
    python scripts/report_residual_near_matches.py
"""

from __future__ import annotations

import argparse
import csv
import difflib
import importlib.util
import re
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
GROUNDINGS = _REPO / "reports" / "culturemech_residual_groundings_final.tsv"
OUT = _REPO / "reports" / "culturemech_residual_near_matches.tsv"

# Only a candidate at least this similar is worth a curator's attention; below it the
# report becomes noise and stops being read, which is its own failure mode.
MIN_SIMILARITY = 0.62
MAX_CANDIDATES = 3

_HYDRATE = re.compile(
    r"(\d+\s*h2o|[xn·•.]\s*\d*\s*h2o|hydrate|anhydrous|anhyd)", re.IGNORECASE
)
_STEREO = re.compile(r"(?:^|[^a-z])(d|l|dl|r|s|rs|\(\+\)|\(-\))[- ]", re.IGNORECASE)
_SALT_OR_ION = re.compile(
    r"\b(sodium|potassium|calcium|magnesium|ammonium|lithium|ferrous|ferric|"
    r"disodium|dipotassium|monosodium|hydrochloride|sulfate|sulphate|acid|"
    r"[a-z]+ate|[a-z]+ide)\b",
    re.IGNORECASE,
)
_PHYSICAL = re.compile(
    r"\b(gas|gaseous|solution|soln|powder|crystals?|liquid|solid|dehydrated|"
    r"anhydrous|aqueous|slurry|paste|flakes)\b",
    re.IGNORECASE,
)
_CONCENTRATION = re.compile(r"\d\s*(%|mm?\b|molar|m\b|g/l|mg/l|w/v|v/v|n\b)", re.IGNORECASE)
_FORMULA_TOKEN = re.compile(r"^[A-Z][a-z]?\d*(?:[A-Z(][\w()]*\d*)*$")
_DIGITS = re.compile(r"\d+")
_WORD = re.compile(r"[a-z0-9]+")
# Tokens as written, so formula lookups see `MgSO4` rather than `mgso` plus `4`.
_RAW_TOKEN = re.compile(r"[A-Za-z0-9()·•]+")


def _tokens(text: str) -> set[str]:
    return set(_WORD.findall(text.lower()))


def assess_risks(surface: str, candidate: str) -> list[str]:
    """Name every difference that could mean these are not the same compound."""
    risks: list[str] = []

    surface_hydrate = {m.group(0).lower().replace(" ", "") for m in _HYDRATE.finditer(surface)}
    candidate_hydrate = {m.group(0).lower().replace(" ", "") for m in _HYDRATE.finditer(candidate)}
    if surface_hydrate != candidate_hydrate:
        risks.append("HYDRATION_STATE")

    surface_stereo = {m.group(1).lower() for m in _STEREO.finditer(surface)}
    candidate_stereo = {m.group(1).lower() for m in _STEREO.finditer(candidate)}
    if surface_stereo != candidate_stereo:
        risks.append("STEREOCHEMISTRY")

    # Digits inside a formula-shaped token: H3BO4 vs H3BO3 is one character and a
    # different species, and no similarity score will ever separate them.
    for token in surface.split():
        if _FORMULA_TOKEN.match(token):
            for other in candidate.split():
                if _FORMULA_TOKEN.match(other) and token.lower() != other.lower():
                    if _WORD.findall(token.lower())[:1] == _WORD.findall(other.lower())[:1]:
                        continue
                    if _DIGITS.findall(token) != _DIGITS.findall(other):
                        risks.append("FORMULA_DIGITS")
                        break
            if "FORMULA_DIGITS" in risks:
                break

    surface_salt = {m.group(0).lower() for m in _SALT_OR_ION.finditer(surface)}
    candidate_salt = {m.group(0).lower() for m in _SALT_OR_ION.finditer(candidate)}
    if surface_salt != candidate_salt:
        risks.append("SALT_OR_ION_FORM")

    surface_phys = {m.group(0).lower() for m in _PHYSICAL.finditer(surface)}
    candidate_phys = {m.group(0).lower() for m in _PHYSICAL.finditer(candidate)}
    if surface_phys != candidate_phys:
        risks.append("PHYSICAL_STATE")

    if _CONCENTRATION.search(surface) and not _CONCENTRATION.search(candidate):
        risks.append("CONCENTRATION")

    if not risks and _tokens(surface) != _tokens(candidate):
        risks.append("TOKEN_DIFFERENCE")
    return risks


# Words that describe presentation rather than identity. As a *query* each one is
# useless -- searching `solution` returns thousands of unrelated terms -- so they are
# dropped from candidate generation. They are still compared against, via PHYSICAL_STATE.
_UNINFORMATIVE = frozenset({
    "gas", "gaseous", "solution", "soln", "powder", "crystal", "crystals", "liquid",
    "solid", "aqueous", "slurry", "paste", "flakes", "dehydrated", "see", "medium",
    "media", "no", "if", "needed", "necessary", "optional", "below", "above", "stock",
    "conc", "concentrated", "sterile", "filtered", "autoclaved", "final", "added",
    "per", "and", "or", "the", "of", "in", "for", "with", "from", "grade", "pure",
})


def search_queries(label: str, key: str, folded: str, formula_names) -> list[str]:
    """Query strings likely to reach the right term, most specific first.

    The full label is rarely a substring of any ontology label -- `DI Water` and
    `N2 gas` return nothing from a whole-string search, partial and fuzzy included --
    so the informative tokens are searched and candidates are scored against the full
    label afterwards.

    Formula expansion is what reaches the answers no string measure can: `N2 gas` and
    `dinitrogen` have almost no characters in common, and only MIM's own formula table
    connects them.
    """
    queries: list[str] = [key]
    if folded and folded != key:
        queries.append(folded)

    tokens = [t for t in _WORD.findall(key) if len(t) > 2 and t not in _UNINFORMATIVE]
    for first, second in zip(tokens, tokens[1:]):
        queries.append(f"{first} {second}")
    queries.extend(tokens)

    # Case-preserving: `_WORD` is lowercase-only, so it cannot see `N2` or `MgSO4` in
    # the original label at all, and the formula table is keyed on the real casing.
    for token in _RAW_TOKEN.findall(label):
        expanded = formula_names(token)
        if expanded:
            queries.append(expanded.lower())
    # Preserve order (most specific first) while removing duplicates.
    return list(dict.fromkeys(q for q in queries if q))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--groundings", type=Path, default=GROUNDINGS)
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--limit", type=int, help="only the N highest-occurrence labels")
    parser.add_argument("--sources", default="CHEBI,FOODON,ENVO,UBERON,BTO,NCIT")
    parser.add_argument("--min-similarity", type=float, default=MIN_SIMILARITY)
    args = parser.parse_args(argv)

    if not args.groundings.is_file():
        raise SystemExit(
            f"groundings report not found: {args.groundings}\n"
            "Run: python scripts/propose_residual_groundings.py"
        )
    with args.groundings.open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t") if r["verdict"] == "NO_EXACT_HIT"]
    if not rows:
        raise SystemExit(f"no NO_EXACT_HIT rows in {args.groundings}")
    rows.sort(key=lambda r: -int(r["occurrences"]))
    if args.limit:
        rows = rows[: args.limit]

    proposer = _load("proposer", _REPO / "scripts" / "propose_residual_groundings.py")
    triage = _load("triage", _REPO / "scripts" / "triage_culturemech_residual.py")

    from oaklib import get_adapter
    from oaklib.datamodels.search import SearchConfiguration, SearchProperty

    config = SearchConfiguration(
        properties=[SearchProperty.LABEL, SearchProperty.ALIAS], force_case_insensitive=True
    )

    # MIM's own formula table, so this tool and the curation path agree on what `N2`
    # or `MgSO4` expands to.
    normalizer = _load(
        "chemical_normalizer",
        _REPO / "src" / "mediaingredientmech" / "utils" / "chemical_normalizer.py",
    )

    def formula_names(token: str) -> str | None:
        return normalizer.formula_to_common_name(token)
    adapters = []
    for prefix in (s.strip().upper() for s in args.sources.split(",") if s.strip()):
        try:
            adapters.append((prefix, get_adapter(f"sqlite:obo:{prefix.lower()}")))
        except Exception as exc:  # noqa: BLE001
            print(f"  (skipping {prefix}: {exc})", file=sys.stderr)

    results = []
    for row in rows:
        label = row["label"]
        key = proposer.comparison_key(label)
        if len(key) < proposer.MIN_QUERY_LENGTH:
            continue
        queries = search_queries(
            label, key, proposer.comparison_key(triage.fold(label)), formula_names
        )
        seen: dict[str, tuple[float, str, str]] = {}
        for prefix, adapter in adapters:
            for query in queries:
                try:
                    hits = list(adapter.basic_search(query, config=config))[:20]
                except Exception:  # noqa: BLE001
                    continue
                for curie in hits:
                    curie = str(curie)
                    if not curie.startswith(f"{prefix}:"):
                        continue
                    if not proposer.denotes_a_substance(adapter, curie, prefix):
                        continue
                    term = adapter.label(curie) or ""
                    if not term:
                        continue
                    score = difflib.SequenceMatcher(
                        None, key, proposer.comparison_key(term)
                    ).ratio()
                    if score >= args.min_similarity and score > seen.get(curie, (0,))[0]:
                        seen[curie] = (score, term, prefix)
        for curie, (score, term, prefix) in sorted(
            seen.items(), key=lambda kv: -kv[1][0]
        )[:MAX_CANDIDATES]:
            risks = assess_risks(label, term)
            results.append(
                {
                    "occurrences": row["occurrences"],
                    "label": label,
                    "candidate_curie": curie,
                    "candidate_label": term,
                    "ontology": prefix,
                    "similarity": f"{score:.3f}",
                    "risks": ";".join(risks) or "NONE",
                    "verdict": "",
                }
            )

    if not results:
        print("no candidates above the similarity threshold")
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(results[0]), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(results)

    labels = {r["label"] for r in results}
    clean = [r for r in results if r["risks"] == "NONE"]
    print(f"labels searched:            {len(rows)}")
    print(f"labels with a candidate:    {len(labels)}")
    print(f"candidate rows:             {len(results)}")
    print(f"  no risk flag (safest):    {len(clean)}")
    risk_counts: dict[str, int] = {}
    for r in results:
        for risk in r["risks"].split(";"):
            risk_counts[risk] = risk_counts.get(risk, 0) + 1
    for risk, n in sorted(risk_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {risk:<20} {n}")
    print(f"\nwrote {args.out}")
    print("Review only. The `verdict` column is for a curator; nothing here is applied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
