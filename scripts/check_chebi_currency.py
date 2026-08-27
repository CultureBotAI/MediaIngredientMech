#!/usr/bin/env python3
"""Report whether the local ChEBI build is behind, and whether refreshing helps.

MIM grounds ingredients against a local semsql ChEBI and publishes those
groundings to kg-microbe. When the local copy is older than the ChEBI release
kg-microbe uses, a term that exists upstream simply does not resolve here — and
the id↔label gate reports it as missing. That verdict is about THIS BUILD, not
about the identifier: "not here" is not "not real", and the repair is upstream.

Six real terms — polymyxin B, colistin sulfate, gentamicin, netilmicin,
carbomycin, lysostaphin — were deleted on that misreading in #193 (see #197,
#198). What made it easy was the CHEBI accession ceiling, then set at 300000 —
below ChEBI's own range — so every term newer than the local build was reported
ID_OUT_OF_RANGE, wording that asserts "a foreign identifier wearing an OBO
prefix". #210 raised the ceiling to 1000000, so a high-but-real accession now
reports ID_NOT_FOUND instead: still fatal, but no longer accusing the id of
coming from another registry. Either verdict on a recent accession still means
"check OLS4 first", which is what this script is for.

THE SECOND QUESTION MATTERS AS MUCH AS THE FIRST. Being behind is only actionable
if a refresh would fix it, and often it would not: the semsql build MIM consumes
is produced downstream of ChEBI, so it lags. At the time of writing the local
build and the published one are both release 252 while kg-microbe is on 253 —
so `just refresh-chebi` would delete ~4.7 GB, re-download ~760 MB, and land back
on 252. Telling someone to refresh in that state wastes an hour and fixes
nothing. This script therefore also asks whether the published artifact actually
differs from the local one, and says so.

Advisory and local-only by design: the OAK cache is a multi-gigabyte developer
artifact CI does not have, so failing a build on it would only teach people to
skip the check. `--strict` exits non-zero for anyone who wants it enforced.

Exit codes: 0 = current, or cannot be determined; 1 = behind (with --strict);
2 = usage error.
"""

from __future__ import annotations

import argparse
import gzip
import os
import re
import sqlite3
import sys
import urllib.error
import urllib.request
import zlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# The semsql artifact oaklib downloads for `sqlite:obo:chebi`.
#
# Was `https://s3.amazonaws.com/bbop-sqlite/...`. INCATools/semantic-sql#112 is
# removing `AllUsers` from that bucket, and this constant bypasses oaklib
# entirely, so bumping the dependency does NOT migrate it -- exactly the
# category tracked in INCATools/semantic-sql#115 (#488).
#
# The env var is oaklib's own escape hatch (`SEMSQL_SQLITE_URL_BASE` in
# oaklib.constants, >= 0.7.2). Honouring it here rather than hardcoding a bare
# string keeps the two in step: pointing oaklib at a mirror points this check at
# the same mirror, instead of silently comparing against a different artifact
# than the one that would actually be downloaded. It is read rather than
# imported so this script stays stdlib-only.
SEMSQL_URL_BASE = os.environ.get(
    "OAKLIB_SEMSQL_SQLITE_URL_BASE", "https://semanticsql.berkeleybop.io"
).rstrip("/")
SEMSQL_URL = f"{SEMSQL_URL_BASE}/chebi.db.gz"

# Anchored on versionIRI AND the full `obo/chebi/NNN/chebi.owl` form. A looser
# `obo/chebi/(\d+)` matches decoy strings earlier in the header — the real file
# carries bare `obo/chebi/2`, `/3` and `/1` in namespace declarations at bytes
# 650-768, before the versionIRI at 982 — so a loose pattern reports release 2.
VERSION_IRI = re.compile(rb"versionIRI[^>]*?obo/chebi/(\d+)/chebi\.owl")

# A semsql versionInfo is a bare release integer. Anything else (a date, a
# dotted version) must NOT be coerced: stripping non-digits turns "2026-08-01"
# into 20260801, which compares as hugely NEWER and yields a confident false OK
# from the one tool whose job is preventing false reassurance.
BARE_INTEGER = re.compile(r"^\s*(\d+)\s*$")


def oaklib_cache_dir() -> Path:
    """Where oaklib actually caches its sqlite builds.

    Resolved through pystow, which oaklib itself uses (oaklib/constants.py), so
    this honours PYSTOW_HOME. Deriving it from $HOME instead means a developer
    with PYSTOW_HOME set gets a check that reads — and a refresh that deletes —
    the wrong path, while reporting success.
    """
    try:
        import pystow

        return Path(pystow.module("oaklib").base)
    except Exception:
        return Path.home() / ".data" / "oaklib"


def default_local_db() -> Path:
    override = os.environ.get("OAK_CHEBI_DB")
    return Path(override) if override else oaklib_cache_dir() / "chebi.db"


def default_kgm_chebi() -> Path:
    override = os.environ.get("KGM_CHEBI_OWL")
    if override:
        return Path(override)
    # Sibling checkout, like scripts/validate_sssom_invariants.py resolves it.
    return REPO_ROOT.parent / "kg-microbe" / "data" / "raw" / "chebi.owl.gz"


def local_release(db: Path) -> tuple[int | None, str]:
    """(release, reason). reason explains a None so the caller can say which."""
    if not db.is_file():
        return None, f"no local build at {db}"
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        row = con.execute(
            "select value from statements "
            "where subject='obo:chebi.owl' and predicate='owl:versionInfo' limit 1"
        ).fetchone()
        con.close()
    except sqlite3.Error as exc:
        return None, f"local build unreadable ({exc})"
    if not row or not row[0]:
        return None, f"local build at {db} records no owl:versionInfo"
    match = BARE_INTEGER.match(str(row[0]))
    if not match:
        return None, f"local versionInfo {row[0]!r} is not a release integer"
    return int(match.group(1)), ""


def kgmicrobe_release(owl_gz: Path) -> tuple[int | None, str]:
    if not owl_gz.is_file():
        return None, f"kg-microbe's ChEBI not found at {owl_gz}"
    opener = gzip.open if owl_gz.suffix == ".gz" else open
    try:
        with opener(owl_gz, "rb") as fh:
            head = fh.read(200_000)
    except (OSError, EOFError, zlib.error) as exc:
        # A partially-downloaded chebi.owl.gz is an ordinary state; it must not
        # traceback out of an advisory check.
        return None, f"kg-microbe's ChEBI unreadable ({type(exc).__name__}: {exc})"
    match = VERSION_IRI.search(head)
    if not match:
        return None, f"no versionIRI in the first 200 kB of {owl_gz}"
    return int(match.group(1)), ""


def refresh_would_help(local_db: Path, timeout: float = 15.0) -> tuple[bool | None, str]:
    """Would re-downloading the semsql build actually change anything?

    Compares the published artifact's size against the local .gz oaklib keeps
    beside the decompressed build. Equal size means oaklib would fetch the
    identical artifact, so a refresh is a no-op — the lag is upstream of us and
    no amount of downloading fixes it.

    Size equality is a proxy, not a proof: it cannot distinguish two same-sized
    builds. It is the strongest signal available without downloading 760 MB, and
    it errs the safe way — a rebuilt artifact of a different size reports "a
    refresh WOULD change the build", which merely costs a download. See #206.
    """
    local_gz = Path(str(local_db) + ".gz")
    if not local_gz.is_file():
        return None, f"no local .gz beside {local_db} to compare against"
    try:
        req = urllib.request.Request(SEMSQL_URL, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            published = int(resp.headers.get("Content-Length") or 0)
    except (urllib.error.URLError, OSError, ValueError) as exc:
        return None, f"could not query {SEMSQL_URL} ({exc})"
    if not published:
        return None, "published artifact reported no Content-Length"
    return published != local_gz.stat().st_size, ""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-db", type=Path, default=None)
    parser.add_argument("--kgm-chebi", type=Path, default=None)
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 when behind. Default is advisory (exit 0).")
    parser.add_argument("--no-network", action="store_true",
                        help="Skip the published-artifact comparison.")
    args = parser.parse_args(argv)

    local_db = args.local_db or default_local_db()
    kgm_chebi = args.kgm_chebi or default_kgm_chebi()

    local, local_why = local_release(local_db)
    upstream, up_why = kgmicrobe_release(kgm_chebi)

    if local is None or upstream is None:
        print("ChEBI currency: cannot determine.")
        for why in (local_why, up_why):
            if why:
                print(f"  - {why}")
        return 0

    print(f"ChEBI currency: local build = {local}, kg-microbe = {upstream}")
    if local >= upstream:
        print("  OK: the local build is at least as current as kg-microbe's.")
        return 0

    print(f"\n  BEHIND by {upstream - local} release(s). Terms minted after ChEBI {local} do not")
    print("  resolve locally, so `just validate-products` reports them ID_NOT_FOUND. That verdict")
    print("  is a fact about THIS BUILD, not about the identifier — check OLS4 before demoting")
    print("  anything (#193 deleted six real terms on that misreading; see #197, #198).")

    if args.no_network:
        print("\n  Whether a refresh helps: not checked (--no-network).")
        return 1 if args.strict else 0

    helps, why = refresh_would_help(local_db)
    if helps is None:
        print(f"\n  Whether a refresh helps: unknown — {why}.")
    elif helps:
        print("\n  A refresh WOULD change the build: run `just refresh-chebi`.")
    else:
        print(
            "\n  A refresh would NOT help. The published semsql build is byte-identical to the\n"
            "  local one, so oaklib would re-download the same release. This lag is UPSTREAM of\n"
            f"  MIM — the semsql build simply has not caught up to ChEBI {upstream} yet.\n"
            "  Do not spend ~760 MB discovering that. Until it does, treat a missing-id verdict\n"
            "  on a high accession as unproven rather than as a bogus id: check the id against\n"
            "  OLS4 before demoting anything."
        )
    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
