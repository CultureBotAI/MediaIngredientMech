#!/usr/bin/env python3
"""Make merge tombstones point at their merge target (#360).

A merged record is tombstoned REJECTED and takes the WINNER's identifier, so a
downstream lookup on the loser still resolves. Two ways that breaks, both fixed
here, and both now matter more because #260 makes MIM the resolution source for
CultureMech.

**Stale `ontology_id` (25 records).** The merge scripts set `identifier` and
`mapping_status` and leave `ontology_mapping` untouched, so a tombstone keeps
advertising the term it used to assert — `D` still offers `L-aspartic acid
residue`, `glucose` still offers `aldehydo-D-glucose`. Anything indexing by
`ontology_id` routes through a record that no longer claims it. That is how
`D-Glucose` (589 occurrences) was mis-routed to generic glucose.

**Identifier never updated (6 records).** Older merges tombstoned the loser
without giving it the winner's identifier, so it points at nothing live:

    Bacto Soytone        CHEBI:8150                      -> FOODON:03315720
    Sodium L-lactate     CHEBI:867561 (dead, OLS4 404)   -> CHEBI:232798
    Na2S2O4              CHEBI:61278                     -> CHEBI:66870
    Na-Phosphate-Buffer  ...na-phosphate-buffer          -> ...na-phosphate_buffer
    Vitamins-solution    ...vitamins-solution            -> ...vitamins_solution
    Deoxyribonucleic acid from herring sperm             -> Fish-Sperm DNA

Each target is named in the record's own MERGED_INTO history entry, so nothing is
inferred. `Sodium L-lactate` is the sharpest: its identifier is a dead accession
that OLS4 404s, recorded as such on the record itself, and still published.

**Chains are followed.** `Deoxyribonucleic acid from herring sperm` merges into
`Fish-Sperm DNA`, which was itself later tombstoned — so the pointer is followed
to the first live record rather than left one hop short.

**Retired-invalid records are left alone.** REJECTED covers both "duplicate" and
"invalid"; the 7 assay/splice labels retired in #373 keep their `UNMAPPED_NNNN`
identifiers, because they were never merged and there is no target to point at.
Only records carrying a MERGED_INTO event are touched.

    python scripts/fix_tombstone_pointers.py            # dry-run
    python scripts/fix_tombstone_pointers.py --apply
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
STAMP = "2026-08-15T00:00:00+00:00"
CURATOR = "fix_tombstone_pointers"
ISSUE = "#360"

# Nothing is hardcoded: a dangling tombstone is repointed at whichever LIVE
# record its own fields already name. Three shapes occur, and a table would have
# missed two of them:
#
#   * identifier stale, ontology_id already corrected — `Bacto Soytone` (an
#     obsolete CHEBI id) and `Sodium L-lactate` (a dead one that OLS4 404s).
#     Someone fixed the mapping and left the primary key.
#   * both stale — the ordinary case.
#   * the WINNER moved after the merge — `Fish-Sperm DNA` was re-minted from
#     CHEBI:16991 to a kgmicrobe.ingredient id by #322, stranding the tombstone
#     that pointed at its old identifier. Merging does not pin the winner.
MERGE_ACTIONS = {"MERGED_INTO", "MERGED", "REJECTED"}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    colls = {p: (yaml.safe_load(p.read_text(encoding="utf-8", errors="replace")) or {})
             for p in (MAPPED, UNMAPPED)}
    records = [r for coll in colls.values() for r in (coll.get("ingredients") or [])]
    by_ident: dict[str, list[dict]] = {}
    for r in records:
        by_ident.setdefault(str(r.get("identifier")), []).append(r)

    def live_for(ident: str, seen: set[str] | None = None) -> dict | None:
        """First LIVE record holding `ident`, following tombstone chains."""
        seen = seen or set()
        if ident in seen:
            return None
        seen.add(ident)
        holders = by_ident.get(ident) or []
        for h in holders:
            if h.get("mapping_status") != "REJECTED":
                return h
        for h in holders:
            nxt = str(h.get("identifier"))
            if nxt != ident:
                found = live_for(nxt, seen)
                if found:
                    return found
        return None

    def merged_into(rec: dict) -> bool:
        return any(h.get("action") in MERGE_ACTIONS
                   for h in rec.get("curation_history", []))

    def winner_for(rec: dict) -> dict | None:
        """The live record this tombstone should resolve to.

        Tries, in order: its identifier, its ontology_id, and any live record
        whose OWN ontology_id equals either — which is what finds a winner that
        was re-minted after the merge.
        """
        om = rec.get("ontology_mapping") or {}
        cands = [str(rec.get("identifier") or ""), str(om.get("ontology_id") or "")]
        for c in filter(None, cands):
            w = live_for(c)
            if w is not None and w is not rec:
                return w
        for c in filter(None, cands):
            for other in records:
                if other is rec or other.get("mapping_status") == "REJECTED":
                    continue
                if str((other.get("ontology_mapping") or {}).get("ontology_id")) == c:
                    return other
        # Last resort: the record's own history names the target in prose. Needed
        # where BOTH fields are stale — `Na2S2O4` carries CHEBI:61278 in each and
        # the winner CHEBI:66870 appears only in the MERGED_INTO text.
        for h in rec.get("curation_history", []):
            # NOT `[\s.,;]` as the terminator: a dot ends the match inside
            # `kgmicrobe.ingredient:...`, truncating it to `kgmicrobe`. CHEBI
            # CURIEs survived that because they contain no dot.
            m = re.search(r"[Mm]erged (?:into|there)[: ]*([^\s'\"]+)",
                          str(h.get("changes") or ""))
            if m:
                w = live_for(m.group(1).rstrip(".,;'\""))
                if w is not None and w is not rec:
                    return w
        return None

    repointed, refreshed, skipped = [], [], []

    for rec in records:
        if rec.get("mapping_status") != "REJECTED" or not merged_into(rec):
            continue
        label = str(rec.get("preferred_term") or "")
        ident = str(rec.get("identifier") or "")

        # 1. identifier must name a LIVE merge target
        if live_for(ident) is None:
            win = winner_for(rec)
            if win is None:
                skipped.append(f"{label}: identifier {ident} resolves to nothing and no "
                               f"live record claims its term")
            elif str(win.get("identifier")) != ident:
                new = str(win.get("identifier"))
                rec["identifier"] = new
                rec.setdefault("curation_history", []).append({
                    "timestamp": STAMP, "curator": CURATOR,
                    "action": "REPOINTED_TOMBSTONE_IDENTIFIER",
                    "changes": (
                        f"identifier {ident} -> {new} ({ISSUE}). This record was merged "
                        f"into {win.get('preferred_term')!r} but kept its own old "
                        f"identifier, so a downstream lookup on this label resolved to "
                        f"nothing live. The target is the one named in this record's own "
                        f"MERGED_INTO entry; the chain was followed to the first live "
                        f"record. A tombstone exists to keep the loser resolvable."),
                    "llm_assisted": False})
                repointed.append(f"{label[:34]:<36} {ident[:26]:<28} -> {new}")
                ident = new

        # 2. ontology_mapping must not advertise a term the record no longer asserts
        om = rec.get("ontology_mapping") or {}
        cur = str(om.get("ontology_id") or "")
        win = live_for(ident)
        if win is None or not cur:
            continue
        wom = win.get("ontology_mapping") or {}
        want, want_label = str(wom.get("ontology_id") or ""), wom.get("ontology_label")
        if want and cur != want:
            om["ontology_id"] = want
            om["ontology_label"] = want_label
            om["ontology_source"] = wom.get("ontology_source") or om.get("ontology_source")
            rec["ontology_mapping"] = om
            rec.setdefault("curation_history", []).append({
                "timestamp": STAMP, "curator": CURATOR,
                "action": "REFRESHED_TOMBSTONE_ONTOLOGY_ID",
                "changes": (
                    f"ontology_id {cur} -> {want} ({ISSUE}). The merge set identifier and "
                    f"status but left ontology_mapping untouched, so this tombstone kept "
                    f"advertising a term it no longer asserts — anything indexing by "
                    f"ontology_id routed through it. Now agrees with the merge target "
                    f"{win.get('preferred_term')!r}. Provenance is unaffected: what the "
                    f"record used to assert is in this history."),
                "llm_assisted": False})
            refreshed.append(f"{label[:34]:<36} {cur[:22]:<24} -> {want}")

    if args.apply and (repointed or refreshed):
        for path, coll in colls.items():
            save_yaml(coll, path)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(repointed)} identifier(s) repointed, {len(refreshed)} ontology_id(s) refreshed\n")
    print(f"  identifier repointed to the merge target ({len(repointed)}):")
    for r in repointed:
        print(f"     {r}")
    print(f"\n  ontology_id refreshed to the target's term ({len(refreshed)}):")
    for r in refreshed[:30]:
        print(f"     {r}")
    if len(refreshed) > 30:
        print(f"     ... {len(refreshed) - 30} more")
    for s in skipped:
        print(f"  SKIPPED {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
