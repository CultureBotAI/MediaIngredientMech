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

# The report's own bolded verdict, in the several shapes the template produces.
VERDICT = re.compile(
    r"\*\*Recommend(?:ation|ed)?[^*\n]*\*\*[^\n]*|"
    r"\*\*Recommended interpretation:\*\*[^\n]*", re.I)
# A CURIE the report proposes, so the note can say whether one was found at all.
CURIE = re.compile(r"\b(CHEBI|NCIT|FOODON|ENVO|UBERON|MESH|MICRO):\d+\b")


def summarise(text: str) -> tuple[str, list[str]]:
    m = VERDICT.search(text)
    verdict = re.sub(r"\s+", " ", m.group(0)).strip() if m else ""
    # de-duplicate while preserving order
    seen, curies = set(), []
    for c in CURIE.findall(text):
        pass
    for c in CURIE.finditer(text):
        v = c.group(0)
        if v not in seen:
            seen.add(v)
            curies.append(v)
    return verdict, curies


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    doc = yaml.safe_load(UNMAPPED.read_text())
    touched = 0
    for rec in doc["ingredients"]:
        if rec.get("mapping_status") not in ("UNMAPPED", "NEEDS_EXPERT"):
            continue
        slug = sanitize_filename(rec.get("preferred_term") or "")
        report = RESEARCH / f"{slug}-edison-literature.md"
        if not report.exists():
            continue
        # idempotent: one provenance entry per record
        if any(h.get("curator") == "edison_literature_identity"
               for h in (rec.get("curation_history") or [])):
            continue

        verdict, curies = summarise(report.read_text())
        rel = report.relative_to(ROOT)
        note = (f"Edison LITERATURE (PaperQA3) identity research: {rel}. ")
        note += (f"Report verdict: {verdict} " if verdict
                 else "Report reached no single bolded verdict; see the report. ")
        note += (f"CURIEs discussed: {', '.join(curies[:6])}. "
                 if curies else "No ontology CURIE was proposed. ")
        note += ("Recorded as provenance only — no grounding applied from this run. "
                 "Edison's recommendations are deliberately conservative, and a "
                 "plausible identifier promoted by a mechanism that never decided "
                 "anything is what #203 and #263 exist to undo. Any CURIE above is "
                 "a curator's to accept or reject.")

        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP,
            "curator": "edison_literature_identity",
            "action": "ANNOTATED",
            "changes": note,
            "llm_assisted": True,
        })
        touched += 1
        print(f"  {rec.get('preferred_term')[:38]:40} "
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
