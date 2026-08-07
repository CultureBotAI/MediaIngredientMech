#!/usr/bin/env python3
"""Record Edison identity-research findings on the records they describe.

The Edison literature runs produce a report per ingredient under
``research/ingredients/{slug}-edison-literature.md``. Most of them conclude
"retain UNMAPPED" with a reasoned justification rather than proposing a
grounding — which is the correct outcome for ambiguous family labels
(``Amphotericin`` is the family, not Amphotericin B) and for compounds no
ontology covers.

That conclusion is worth keeping. Without it the record looks identical to one
nobody has ever examined; with it, the next curator knows the search was done,
what it found, and why no CURIE was asserted.

This does NOT auto-apply groundings. Edison's own recommendations are
deliberately conservative, and #203/#263 are what happens when a plausible
identifier is promoted by a mechanism that never decided anything. Any CURIE it
suggests is surfaced in the report for a curator; only the provenance is written
here.

    python scripts/apply_edison_identity_findings.py            # dry-run
    python scripts/apply_edison_identity_findings.py --apply
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import yaml
from mediaingredientmech.utils.yaml_handler import save_yaml
from export_individual_records import sanitize_filename

UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
RESEARCH = ROOT / "research" / "ingredients"
STAMP = "2026-08-06T00:00:00+00:00"

# The report's own verdict. The agent does not use one template, and requiring a
# bolded `**Recommend...**` run missed 49 of 240 reports that state a verdict
# plainly in another shape:
#
#   | Recommended status | **UNMAPPED** ... |   <- a table cell (BHI)
#   ## Executive recommendation             <- a heading (Whole egg)
#   ### Recommended mapping status          <- a heading (Amphotericin)
#
# Those notes then read "Report reached no single bolded verdict; see the report"
# and deferred to a gitignored path -- the one outcome the inline quoting exists
# to prevent. Ordered most-specific first; `search` takes the earliest match, so
# each alternative must be self-delimiting.
VERDICT = re.compile(
    r"\*\*Recommend(?:ation|ed)?[^*\n]*\*\*[^\n]*"          # **Recommended X:** ...
    r"|\|\s*Recommend(?:ation|ed)?[^|\n]*\|[^\n]*"          # | Recommended ... | ... |
    r"|^#{2,4}\s*(?:Executive |Curation )?Recommend[^\n]*"  # ## Executive recommendation
    r"|^\s*[-*]\s*\*\*Recommend[^\n]*",                     # - **Recommended status:** ...
    re.I | re.M)
# A CURIE the report proposes, so the note can say whether one was found at all.
#
# The local part is NOT uniformly numeric. MeSH descriptors are a letter then
# digits (MESH:D012313) and NCIT accessions are C-prefixed (NCIT:C68610), so a
# `\d+` local part silently drops both -- from the two ontologies that supplied
# this project's RNA, Filipin and Polymyxin B groundings. A report proposing only
# a MeSH term would have been summarised as "No ontology CURIE was proposed."
CURIE = re.compile(
    r"\b(?:CHEBI|FOODON|ENVO|UBERON|MICRO):\d+\b"
    r"|\b(?:MESH|NCIT):[A-Z]?\d+\b", re.I)


def report_index() -> dict[str, Path]:
    """Case-folded slug -> report path.

    `sanitize_filename` and the Edison runner disagree about case on 13 of these
    records: the record computes `adeninyl_cobamide` while the report on disk is
    `Adeninyl_Cobamide`, and `FeSO43_x_n_H2O` lands as `Feso43_X_N_H2o`. An exact
    stem lookup skips those silently — the report is present and paid for, the
    record just never receives it. Same drift as #293, different consumer.
    """
    idx: dict[str, Path] = {}
    for p in RESEARCH.glob("*-edison-literature.md"):
        idx.setdefault(p.name[: -len("-edison-literature.md")].lower(), p)
    return idx


def summarise(text: str) -> tuple[str, list[str]]:
    m = VERDICT.search(text)
    verdict = ""
    if m:
        verdict = re.sub(r"\s+", " ", m.group(0)).strip()
        # A heading is only a pointer -- "## Executive recommendation" quoted on
        # its own tells a curator nothing. Carry the first non-empty line under
        # it, which is where that shape puts the actual verdict.
        if verdict.startswith("#"):
            rest = text[m.end():].lstrip("\n")
            follow = next((ln for ln in rest.split("\n") if ln.strip()), "")
            if follow:
                verdict = f"{verdict} — {re.sub(r'\s+', ' ', follow).strip()}"
    verdict = verdict[:400]
    # De-duplicate on the case-folded CURIE, keeping the spelling first used.
    # Reports mix `MeSH:D001812` and `MESH:D001812` in one document; matching
    # case-insensitively without folding the key lists the same term twice and
    # reads as two independent candidates.
    # De-duplicate case-folded, and emit the CANONICAL prefix spelling rather
    # than whatever the report used. Reports write `ChEBI:2682` and `MeSH:D000666`;
    # quoting those verbatim puts strings into curation history that a curator
    # would reasonably copy-paste and that fail this repo's own CURIE pattern.
    seen: dict[str, str] = {}
    for m in CURIE.finditer(text):
        prefix, local = m.group(0).split(":", 1)
        seen.setdefault(m.group(0).upper(), f"{prefix.upper()}:{local.upper()}")
    return verdict, list(seen.values())


def build_note(report: Path, verdict: str, curies: list[str]) -> str:
    # `research/` is gitignored (NEXT_TASKS.md documents this), so the path is a
    # pointer to a LOCAL artifact, not a repo file — say so, or a reader who
    # cannot open it concludes the provenance is broken rather than uncommitted.
    # The verdict and CURIEs are therefore inlined below: the note has to stand
    # on its own for anyone working from a fresh clone.
    note = (f"Edison LITERATURE (PaperQA3) identity research; report at "
            f"{report.relative_to(ROOT)} (local artifact — research/ is "
            f"gitignored, so the findings are quoted here rather than linked). ")
    note += (f"Report verdict: {verdict} " if verdict
             else "Report reached no single bolded verdict; see the report. ")
    note += (f"CURIEs discussed: {', '.join(curies[:6])}. "
             if curies else "No ontology CURIE was proposed. ")
    note += ("Recorded as provenance only — no grounding applied from this run. "
             "Edison's recommendations are deliberately conservative, and a "
             "plausible identifier promoted by a mechanism that never decided "
             "anything is what #203 and #263 exist to undo. Any CURIE above is "
             "a curator's to accept or reject.")
    return note


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument(
        "--refresh", action="store_true",
        help="Rewrite existing notes whose text no longer matches the report. "
             "The first run of this tool used a CURIE pattern with a numeric "
             "local part, so reports proposing only a MeSH or NCIT term were "
             "summarised as 'No ontology CURIE was proposed' — the opposite of "
             "what they say. Those notes are wrong until refreshed.")
    args = ap.parse_args()

    doc = yaml.safe_load(UNMAPPED.read_text())
    index = report_index()
    touched = 0
    for rec in doc["ingredients"]:
        if rec.get("mapping_status") not in ("UNMAPPED", "NEEDS_EXPERT"):
            continue
        slug = sanitize_filename(rec.get("preferred_term") or "")
        # Resolve ONLY through the index. Trying `RESEARCH / f"{slug}-..."` first
        # looks equivalent but is not: on macOS's case-insensitive APFS that path
        # `.exists()` even when the real filename differs in case, so the note
        # embeds a path that does not exist on Linux, and the two platforms write
        # different text for the same record. 13 notes were in that state.
        report = index.get(slug.lower())
        if report is None:
            continue
        verdict, curies = summarise(report.read_text())
        note = build_note(report, verdict, curies)

        # idempotent: one provenance entry per record
        existing = [h for h in (rec.get("curation_history") or [])
                    if h.get("curator") == "edison_literature_identity"]
        if existing:
            if not args.refresh or existing[-1].get("changes") == note:
                continue
            existing[-1]["changes"] = note
            existing[-1]["timestamp"] = STAMP
            action = "REFRESHED"
        else:
            rec.setdefault("curation_history", []).append({
                "timestamp": STAMP,
                "curator": "edison_literature_identity",
                "action": "ANNOTATED",
                "changes": note,
                "llm_assisted": True,
            })
            action = "annotated"

        touched += 1
        print(f"  {action:10} {rec.get('preferred_term')[:34]:36} "
              f"{'verdict' if verdict else 'no-verdict':11} "
              f"{len(curies)} CURIE(s)")

    if args.apply and touched:
        save_yaml(doc, UNMAPPED, validate=True, target_class="IngredientCollection")
        print(f"\nannotated {touched} record(s)")
    else:
        print(f"\n{touched} record(s) would be annotated (dry-run)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
