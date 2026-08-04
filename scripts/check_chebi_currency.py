#!/usr/bin/env python3
"""Warn when the local ChEBI build is older than kg-microbe's.

MIM grounds ingredients against a local semsql ChEBI (`sqlite:obo:chebi`, cached
at ~/.data/oaklib/chebi.db) and publishes those groundings to kg-microbe. When
the local copy is older than the ChEBI release kg-microbe itself uses, a term
that exists upstream simply does not resolve here — and the id↔label gate then
reports it as ID_OUT_OF_RANGE, whose wording ("a foreign identifier wearing an
OBO prefix") invites deleting a perfectly good mapping.

That is not hypothetical. In #193 six real ChEBI terms — polymyxin B, colistin
sulfate, gentamicin, netilmicin, carbomycin, lysostaphin — were demoted to
UNMAPPED on exactly this reasoning. They were minted in ChEBI 253; the local
build was 252. Issue #197.

The check is a comparison of two release numbers:

    local        owl:versionInfo on obo:chebi.owl in ~/.data/oaklib/chebi.db
    kg-microbe   versionIRI in its data/raw/chebi.owl.gz

It is DELIBERATELY LOCAL-ONLY and advisory. The OAK cache is a multi-gigabyte
developer artifact that CI does not have, so failing a build on it would only
teach people to skip the check. It belongs in the `next-tasks` reconcile, where
"is the backlog current?" already means "is anything quietly out of date?".

Exit codes: 0 = current, or cannot be determined (nothing to compare);
1 = local is behind kg-microbe (with --strict); 2 = usage error.
"""

from __future__ import annotations

import argparse
import gzip
import os
import re
import sqlite3
import sys
from pathlib import Path

DEFAULT_LOCAL_DB = Path(os.environ.get("OAK_CHEBI_DB", Path.home() / ".data/oaklib/chebi.db"))
DEFAULT_KGM_CHEBI = Path(
    os.environ.get(
        "KGM_CHEBI_OWL",
        "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/chebi.owl.gz",
    )
)

# Anchored on versionIRI and the full `obo/chebi/NNN/chebi.owl` form. A looser
# `obo/chebi/(\d+)` matches decoy strings that appear EARLIER in the header —
# the file contains bare `obo/chebi/2`, `/3` and `/1` before the real versionIRI,
# so a loose pattern silently reports release 2.
VERSION_IRI = re.compile(rb"versionIRI[^>]*?obo/chebi/(\d+)/")


def local_release(db: Path) -> int | None:
    """ChEBI release number recorded in the local semsql build."""
    if not db.is_file():
        return None
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        row = con.execute(
            "select value from statements "
            "where subject='obo:chebi.owl' and predicate='owl:versionInfo' limit 1"
        ).fetchone()
        con.close()
    except sqlite3.Error:
        return None
    if not row or not row[0]:
        return None
    digits = re.sub(r"\D", "", str(row[0]))
    return int(digits) if digits else None


def kgmicrobe_release(owl_gz: Path) -> int | None:
    """ChEBI release number kg-microbe downloaded.

    Reads only the head of the file: the versionIRI sits in the ontology header,
    and this is a ~63 MB gzip of an 826 MB document.
    """
    if not owl_gz.is_file():
        return None
    opener = gzip.open if owl_gz.suffix == ".gz" else open
    try:
        with opener(owl_gz, "rb") as fh:
            head = fh.read(200_000)
    except OSError:
        return None
    match = VERSION_IRI.search(head)
    return int(match.group(1)) if match else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-db", type=Path, default=DEFAULT_LOCAL_DB)
    parser.add_argument("--kgm-chebi", type=Path, default=DEFAULT_KGM_CHEBI)
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit 1 when the local build is behind. Default is advisory (exit 0).",
    )
    args = parser.parse_args(argv)

    local = local_release(args.local_db)
    upstream = kgmicrobe_release(args.kgm_chebi)

    if local is None:
        print(f"ChEBI currency: local build not readable at {args.local_db} — nothing to compare.")
        print("  (OAK downloads it on first use; this check is a developer aid, not a gate.)")
        return 0
    if upstream is None:
        print(f"ChEBI currency: kg-microbe's ChEBI not readable at {args.kgm_chebi}.")
        print(f"  Local build is release {local}; cannot tell whether that is current.")
        return 0

    print(f"ChEBI currency: local build = {local}, kg-microbe = {upstream}")
    if local >= upstream:
        print("  OK: the local build is at least as current as kg-microbe's.")
        return 0

    print(
        f"\n  BEHIND by {upstream - local} release(s). Terms minted after ChEBI {local} do not\n"
        "  resolve locally, so `just validate-products` reports them ID_OUT_OF_RANGE — whose\n"
        "  wording suggests a bogus identifier and invites demoting a valid mapping. That is\n"
        "  what happened to six real terms in #193 (see #197, #198).\n\n"
        "  Refresh:  just refresh-chebi\n"
        "  Then re-run `just validate-products` before acting on any ID_OUT_OF_RANGE finding."
    )
    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
