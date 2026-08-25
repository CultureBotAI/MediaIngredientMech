#!/usr/bin/env python3
"""Assert every CURIE in the published SSSOM satisfies the CURIE standard (#439).

`just curie-validate` was documented as *"Assert the published SSSOM satisfies
the CURIE standard"* while its body ran `pytest tests/test_curie_normalizer.py`
and opened no artifact. It passed 19/19 green on 2026-08-21 against a published
file carrying **11 subjects that violate `curie.py`'s own `_CURIE_RE`** —
unescaped parentheses, `MIM:(R)-lactate` and friends. The recipe tested the
implementation and called it a check on the data.

That is the #178 / #179 / #180 / #188 / #189 class: a guard reporting OK while
checking nothing. It is also part of why #236 went unnoticed for as long as it
did, since the one recipe named after this exact property could not see it.

What this checks, per row:

* ``subject_id`` and ``object_id`` are well-formed CURIEs by ``_CURIE_RE`` —
  the same pattern the unit tests exercise, now pointed at the artifact.
* every prefix is one MIM recognises (``PREFIX_RANK`` plus ``MIM`` itself),
  so a typo'd or newly-invented namespace cannot ship silently.

Deliberately NOT checked here, because another gate owns each:

* whether a subject resolves to a record — `tests/test_published_mim_subject_case.py`
* accession plausibility — ``CurieNormalizer`` (#303, #304)
* label correspondence — ``just validate-products``
* the SSSOM invariants A/B/C/D — ``scripts/validate_sssom_invariants.py``

Exit codes: 0 clean, 2 at least one bad CURIE.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mediaingredientmech.curie import _CURIE_RE, PREFIX_RANK  # noqa: E402

DEFAULT_SSSOM = REPO / "mappings" / "ingredient_mappings.sssom.tsv"

# `MIM` is the subject namespace and is not in PREFIX_RANK, which ranks
# *object* prefixes for the primary-term decision.
KNOWN_PREFIXES = frozenset(PREFIX_RANK) | {"MIM"}

CHECKED_COLUMNS = ("subject_id", "object_id")


def read_rows(path: Path) -> list[dict[str, str]]:
    """SSSOM TSV rows, minus the `#`-prefixed YAML preamble."""
    with path.open(encoding="utf-8") as f:
        body = [ln for ln in f if not ln.startswith("#") and ln.strip()]
    return list(csv.DictReader(body, delimiter="\t"))


def check(rows: list[dict[str, str]]) -> list[tuple[int, str, str, str]]:
    """[(row_number, column, value, problem)] for every offending cell."""
    bad: list[tuple[int, str, str, str]] = []
    for num, row in enumerate(rows, start=1):
        for col in CHECKED_COLUMNS:
            value = (row.get(col) or "").strip()
            if not value:
                bad.append((num, col, value, "empty"))
                continue
            m = _CURIE_RE.match(value)
            if not m:
                bad.append((
                    num, col, value,
                    "does not match curie.py::_CURIE_RE — a character outside "
                    "[A-Za-z0-9_.~%-] is unescaped (escape it as ~HEX)",
                ))
                continue
            prefix = m.group(1)
            if prefix not in KNOWN_PREFIXES:
                bad.append((
                    num, col, value,
                    f"unrecognised prefix {prefix!r} — add it to "
                    f"curie.py::PREFIX_RANK or fix the CURIE",
                ))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("sssom_path", nargs="?", type=Path, default=DEFAULT_SSSOM)
    args = ap.parse_args()

    if not args.sssom_path.exists():
        print(f"No such SSSOM: {args.sssom_path}", file=sys.stderr)
        return 2

    rows = read_rows(args.sssom_path)
    bad = check(rows)

    if not bad:
        print(
            f"OK: {len(rows)} rows, {len(CHECKED_COLUMNS) * len(rows)} CURIEs in "
            f"{args.sssom_path.name} match _CURIE_RE and use a known prefix."
        )
        return 0

    print(f"{len(bad)} bad CURIE(s) in {args.sssom_path.name}:", file=sys.stderr)
    for num, col, value, problem in bad[:40]:
        print(f"  row {num} {col}={value!r}: {problem}", file=sys.stderr)
    if len(bad) > 40:
        print(f"  ... and {len(bad) - 40} more", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
