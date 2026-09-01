#!/usr/bin/env python3
"""Triage CultureMech ingredient labels that MIM's published index cannot resolve.

CultureMech resolves recipe ingredient labels against MIM's *literal* label index
(`docs/data/label_index.csv`, vendored at a pinned commit). A surface form that
differs from an indexed label only by punctuation, a parenthetical qualifier, a
concentration annotation, or a hydrate spelling therefore fails to resolve even
though MIM already holds the compound. Those are alias gaps, not grounding gaps,
and they are the exact-match head of the residual.

This tool buckets every unresolved label so the grounding effort is spent only on
what actually needs it:

    ALIAS       normalizes onto an existing MAPPED MIM record -> add a synonym
    UNMAPPED    normalizes onto an existing UNMAPPED MIM record -> ground that record
    NOISE       parse damage (bare numbers, truncated quoted fragments) -> fix upstream
    RESIDUAL    genuinely absent from MIM -> Tier-0 CHEBI cascade, then research

Input is CultureMech's `output/ingredient_occurrences.tsv` (uncapped occurrence
table, one row per ingredient mention). Read-only: writes a report, edits nothing.

Usage:
    python scripts/triage_culturemech_residual.py \
        --occurrences ../CultureMech/output/ingredient_occurrences.tsv \
        --out reports/culturemech_residual_triage.tsv
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
LABEL_INDEX = _REPO / "docs" / "data" / "label_index.csv"

# Hydration state is identity, not decoration: `CaCl2 (anhydrous)` and `CaCl2 x 2 H2O`
# are 110.98 and 147.01 g/mol, which is exactly what a recipe depends on
# (MAPPING_SEMANTICS.md Section 3). A parenthetical matching this is never stripped,
# so such a label falls to RESIDUAL and gets its own grounding decision rather than
# silently inheriting a sibling hydrate's identifier.
_HYDRATION_STATE = re.compile(
    r"anhyd|hydrat|\d\s*h2o|[xn]\s*h2o|water of crystall", re.IGNORECASE
)

# Surface decorations that never change which compound is meant. Stripped before
# the normalized comparison so `Agar (if needed)` can reach `Agar`.
#
# The leading `(?<=\s)` matters: it confines stripping to a standalone qualifier and
# keeps the pattern away from a parenthesis inside a formula token. Without it
# `AlK(SO4)2 (anhydrous)` folds to `alk 2` and collides with an unrelated record.
# For the same reason the vendor branch is case-SENSITIVE — under re.IGNORECASE it
# degenerates into a catch-all that eats every parenthetical in the corpus.
_PARENTHETICAL = re.compile(
    r"\s*(?<=\s)\((?:"
    r"(?i:if needed|if required|if desired|optional|omit[^)]*)|"
    r"(?i:see [^)]*|note[^)]*|for [^)]*)|"
    r"(?i:[^)]*\d[^)]*%[^)]*)|"
    r"(?i:[\d.,;:\s]*(?:[unmµμ]?g\s*/\s*[unmµμ]?l|mm?|nm?|m|w/v|v/v|g/l|mg/l|ph\s*[\d.]+)[^)]*)|"
    r"[A-Z][\w.-]*(?:[- ][\w.-]+)*"  # vendor/catalog tags: (BD-Difco), (Sigma A1296)
    r")\)"
)
_TRAILING_QUALIFIER = re.compile(
    r"[,;]\s*(?:anhydrous|hydrated|solution|soln\.?|powder|crystals?|"
    r"tech(?:nical)?|reagent grade|acs|usp|p\.?a\.?)\s*$",
    re.IGNORECASE,
)
_WS = re.compile(r"\s+")
_PUNCT = re.compile(r"[^\w]+")

# Unicode forms that occur in scraped recipe text but never in ontology labels.
_UNICODE_FOLD = {
    "·": ".", "•": ".", "×": "x", "′": "'", "’": "'",
    "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-",
    "−": "-", " ": " ",
}
_SUBSCRIPTS = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")

# Ontologies spell Greek letters out in ASCII -- CHEBI stores `beta-D-glucose` and
# `alpha-tocopherol` -- while recipe text uses the letter itself. Without this the two
# never meet: `beta-NAD` resolves to CHEBI:15846 and `β-NAD` resolves to nothing.
# Transliteration is applied for BOTH searching and comparison, so a surface form
# written either way reaches the same term.
_GREEK = {
    "\u03b1": "alpha", "β": "beta", "\u03b3": "gamma", "\u03b4": "delta",
    "\u03b5": "epsilon", "\u03b6": "zeta", "\u03b7": "eta", "\u03b8": "theta",
    "\u03ba": "kappa", "\u03bb": "lambda", "\u03c0": "pi", "\u03c1": "rho",
    "\u03c3": "sigma", "\u03c4": "tau", "\u03c9": "omega",
    "\u0391": "alpha", "\u0392": "beta", "\u0393": "gamma", "\u0394": "delta",
}


# Parse damage, not ingredient names.
_BARE_NUMBER = re.compile(r"^[\d.,;:%\s+-]+$")
_UNBALANCED_QUOTE = re.compile(r"^['\"]|['\"]$")


def fold(text: str) -> str:
    """Fold a surface form to its comparison key (lossy, comparison-only)."""
    text = unicodedata.normalize("NFKC", text)
    for src, dst in _UNICODE_FOLD.items():
        text = text.replace(src, dst)
    text = text.translate(_SUBSCRIPTS)
    for src, dst in _GREEK.items():
        text = text.replace(src, dst)
    if not _HYDRATION_STATE.search(text):
        text = _PARENTHETICAL.sub(" ", text)
        text = _TRAILING_QUALIFIER.sub("", text)
    text = _PUNCT.sub(" ", text.lower())
    return _WS.sub(" ", text).strip()


def is_noise(label: str) -> str | None:
    """Return a reason when the label is parse damage rather than an ingredient."""
    stripped = label.strip()
    if not stripped:
        return "empty"
    if _BARE_NUMBER.match(stripped):
        return "bare_number"
    if len(stripped) <= 2 and not any(c.isalpha() for c in stripped):
        # A short token needs a letter to be a formula. `O2` and `N2` are real
        # ingredients; requiring `.isalpha()` rejected them as parse damage.
        return "too_short"
    quotes = stripped.count("'") + stripped.count('"')
    if quotes % 2 == 1 and _UNBALANCED_QUOTE.search(stripped):
        return "truncated_quote"
    if stripped.endswith(("(", "[", ",", ";")):
        return "truncated_tail"
    return None


def load_index(path: Path) -> dict[str, list[dict[str, str]]]:
    """Index MIM's published labels by folded key."""
    if not path.is_file():
        raise SystemExit(f"MIM label index not found: {path}")
    by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            key = fold(row["label"])
            if key:
                by_key[key].append(row)
    if not by_key:
        raise SystemExit(f"MIM label index is empty: {path}")
    return by_key


def load_unresolved(path: Path) -> dict[str, dict[str, object]]:
    """Collect distinct unresolved labels and their occurrence counts."""
    if not path.is_file():
        raise SystemExit(
            f"CultureMech occurrence table not found: {path}\n"
            "Generate it in CultureMech with `just ingredient-occurrences`."
        )
    terms: dict[str, dict[str, object]] = {}
    csv.field_size_limit(10_000_000)
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if (row.get("resolved_identifier") or "").strip() not in ("", "NA"):
                continue
            label = (row.get("preferred_term") or "").strip()
            if not label:
                continue
            entry = terms.setdefault(
                label,
                {"occurrences": 0, "recipes": set(), "reason": row.get("grounding_reason", "")},
            )
            entry["occurrences"] = int(entry["occurrences"]) + 1
            recipes = entry["recipes"]
            assert isinstance(recipes, set)
            recipes.add(row.get("recipe_id", ""))
    if not terms:
        raise SystemExit(f"no unresolved labels found in {path}")
    return terms


def classify(label: str, index: dict[str, list[dict[str, str]]]) -> tuple[str, str, str]:
    """Return (bucket, matched_identifier, matched_label) for one surface form."""
    noise = is_noise(label)
    if noise:
        return f"NOISE:{noise}", "", ""
    key = fold(label)
    if not key:
        return "NOISE:empty_after_fold", "", ""
    hits = index.get(key)
    if not hits:
        return "RESIDUAL", "", ""
    mapped = [h for h in hits if h.get("mapping_status") == "MAPPED"]
    pool = mapped or hits
    identifiers = {h["identifier"] for h in pool}
    if len(identifiers) > 1:
        return "AMBIGUOUS", "|".join(sorted(identifiers)), pool[0]["label"]
    hit = pool[0]
    bucket = "ALIAS" if mapped else "UNMAPPED"
    return bucket, hit["identifier"], hit["label"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--occurrences",
        type=Path,
        default=_REPO.parent / "CultureMech" / "output" / "ingredient_occurrences.tsv",
    )
    parser.add_argument("--index", type=Path, default=LABEL_INDEX)
    parser.add_argument("--out", type=Path, default=_REPO / "reports" / "culturemech_residual_triage.tsv")
    parser.add_argument("--label", action="append", help="classify only these labels (canary mode)")
    args = parser.parse_args(argv)

    index = load_index(args.index)

    if args.label:
        for label in args.label:
            bucket, ident, matched = classify(label, index)
            print(f"{label!r}\n  fold   -> {fold(label)!r}\n  bucket -> {bucket}\n  match  -> {ident} ({matched})")
        return 0

    terms = load_unresolved(args.occurrences)
    rows = []
    for label, entry in terms.items():
        bucket, ident, matched = classify(label, index)
        recipes = entry["recipes"]
        assert isinstance(recipes, set)
        rows.append(
            {
                "bucket": bucket,
                "label": label,
                "occurrences": entry["occurrences"],
                "recipes": len(recipes),
                "folded": fold(label),
                "mim_identifier": ident,
                "mim_label": matched,
                "culturemech_reason": entry["reason"],
            }
        )
    rows.sort(key=lambda r: (r["bucket"], -int(r["occurrences"]), r["label"]))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for row in rows:
        head = row["bucket"].split(":")[0]
        counts[head][0] += 1
        counts[head][1] += int(row["occurrences"])
    print(f"distinct unresolved labels: {len(rows)}")
    for bucket in sorted(counts):
        terms_n, occ_n = counts[bucket]
        print(f"  {bucket:<10} {terms_n:5d} labels  {occ_n:6d} occurrences")
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
