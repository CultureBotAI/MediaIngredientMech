"""Count native disposition reasons without issuing new scientific decisions."""
from __future__ import annotations

import collections
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "mim"
PHASE = sys.argv[1] if len(sys.argv) > 1 else "baseline"
OUT = ROOT / "audit718" / PHASE
OUT.mkdir(parents=True, exist_ok=False)
EXPORTED = REPO / "output/mim-reviewed-sssom"

RULES = [
    ("changed_or_new_receipt", "Review no longer binds changed/new row or owner", ("Mapping corrected by receipt", "Row added by mapping-change receipt")),
    ("nonexact_relation_scope", "Prior review does not establish current non-exact relation and synonym scope", ("The prior record review does not settle this non-exact relation",)),
    ("record_specific_concern", "Existing record-specific mapping, identity, alias or evidence concern", ("Current row requires resolution of this record-specific mapping/identity/alias/evidence concern:",)),
    ("synonym_payload_incomplete", "Complete other-token payload lacks individual same-subject documentation", ("The available report does not individually document every current other token",)),
    ("cross_record_obligation", "Cross-record baseline remains an explicit unresolved review obligation", ("Cross-record baseline is an unresolved review obligation",)),
    ("chemistry_conflict", "Label-index different-substance chemistry conflict needs per-record review", ("Different-substance chemistry conflict remains in label index",)),
    ("weak_grounding_grade", "Lexical or close grounding does not establish exact equivalence", ("The source grounding grade is",)),
    ("no_positive_mapping_disposition", "Assertion lacks mapping-specific positive disposition", ("This assertion lacks a mapping-specific positive disposition",)),
    ("preparation_synonym_scope", "Preparation/concentration/instruction tokens need same-subject review", ("Preparation/concentration/instruction tokens remain in the synonym channel",)),
]

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open() as handle:
        return list(csv.DictReader((line for line in handle if not line.startswith("#")), delimiter="\t"))

inputs = {}
for relative in [
    "output/mim-reviewed-sssom/manifest.json",
    "output/mim-reviewed-sssom/mapping-dispositions.tsv",
    "output/mim-reviewed-sssom/ingredient_mappings.sssom.tsv",
    "output/mim-reviewed-sssom/withheld_mappings.sssom.tsv",
    "mappings/ingredient_mappings.sssom.tsv",
    "reports/sssom_completion_20260921/review.json",
    "reports/sssom_completion_20260921/mapping-evidence.json",
    "docs/SSSOM_RELEASE.md",
]:
    source = REPO / relative
    destination = OUT / "inputs" / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    inputs[relative] = sha(destination)

manifest = json.loads((OUT / "inputs/output/mim-reviewed-sssom/manifest.json").read_text())
for name, digest in manifest["files"].items():
    assert digest == inputs["output/mim-reviewed-sssom/" + name], name
assert manifest["source_sha256"] == inputs["mappings/ingredient_mappings.sssom.tsv"]
assert manifest["review_sha256"] == inputs["reports/sssom_completion_20260921/review.json"]
rows = read_tsv(OUT / "inputs/output/mim-reviewed-sssom/mapping-dispositions.tsv")
withheld = [row for row in rows if row["disposition"] == "WITHHOLD"]
supported = [row for row in rows if row["disposition"] == "SUPPORTED"]
assert len(rows) == manifest["counts"]["source"]
assert len(withheld) == manifest["counts"]["withhold"]
assert len(supported) == manifest["counts"]["supported"]

counts = collections.Counter()
for row in withheld:
    row["reason_category"] = next((key for key, _, prefixes in RULES if row["review_reason"].startswith(prefixes)), "other_preserved_reason")
    counts[row["reason_category"]] += 1
with (OUT / "withheld-reason-classification.tsv").open("w") as handle:
    writer = csv.DictWriter(handle, fieldnames=["reason_category"] + [key for key in rows[0] if key != "reason_category"], delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(withheld)
reason_counts = collections.Counter(row["review_reason"] for row in withheld)
with (OUT / "exact-reason-counts.tsv").open("w") as handle:
    writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
    writer.writerow(["count", "review_reason"])
    writer.writerows(reason_counts.most_common())

summary = {
    "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    "phase": PHASE,
    "repository_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip(),
    "scientific_review": False,
    "scope": "All native mapping dispositions at the captured source and review hashes; reason classification only, without reassessing the archived scientific evidence or changing any disposition.",
    "excluded": ["Role and component assertions", "KGX or downstream media approval", "Scientific re-review of withheld or supported rows", "Any source data or native review mutation"],
    "counts": manifest["counts"],
    "withheld_owner_records": len({row["owner_record"] for row in withheld}),
    "withheld_predicates": dict(collections.Counter(row["predicate_id"] for row in withheld)),
    "supported_predicates": dict(collections.Counter(row["predicate_id"] for row in supported)),
    "exclusive_reason_categories": dict(counts),
    "classification_rules": [{"category": key, "definition": definition, "match": "first matching case-sensitive prefix in this order", "prefixes": prefixes} for key, definition, prefixes in RULES] + [{"category": "other_preserved_reason", "definition": "No listed prefix matches; exact native reason retained for individual interpretation"}],
    "unique_withheld_reasons": len(reason_counts),
    "manifest_verification": "Source, review and every published partition file match the native manifest; counts independently recomputed from all dispositions.",
    "input_sha256": inputs,
    "limitations": ["Categories reflect recorded reason text, not a new finding that the underlying assertion is false.", "A row can carry multiple concerns; exclusive categories use the first recorded leading reason. Full reasons remain available in the row-level TSV.", "Counts are snapshot-bound and will change when content-bound mapping receipts are assembled.", "This diagnostic is input for the root combined native structured review, not a separate native review bundle or scientific approval."],
}
(OUT / "classification.json").write_text(json.dumps(summary, indent=2) + "\n")
lines = ["# Withheld mapping disposition inventory", "", f"Captured {summary['created_at']} at MIM `{summary['repository_head']}`.", "", f"Source: **{len(rows):,}**; supported: **{len(supported):,}**; withheld: **{len(withheld):,}** across **{summary['withheld_owner_records']:,}** owner records.", "", "This is a deterministic classification of existing review reasons, not a new scientific review. No dispositions were changed. Roles, components, KGX and downstream media are outside scope.", "", "| Recorded leading reason | Rows |", "| --- | ---: |"]
labels = {key: definition for key, definition, _ in RULES}
for key, number in counts.most_common():
    lines.append(f"| {labels.get(key, 'Other preserved native reason')} | {number:,} |")
lines += ["", "Withheld predicates: " + ", ".join(f"`{key}` {value:,}" for key, value in summary["withheld_predicates"].items()) + ".", "", "Categories are disjoint by ordered leading-text rules. A full reason may include several concerns. Inspect `withheld-reason-classification.tsv` for exact selectors, owner hashes, reasons and evidence references; `exact-reason-counts.tsv` preserves every distinct native reason.", "", "Input bytes are retained under `inputs/`; `classification.json` records hashes and rule definitions. Native manifest hashes and counts were checked independently. This inventory does not establish that withheld rows are false, approve supported rows anew, or clear any scientific finding."]
(OUT / "classification.md").write_text("\n".join(lines) + "\n")
print(json.dumps({key: summary[key] for key in ["phase", "counts", "withheld_owner_records", "withheld_predicates", "supported_predicates", "exclusive_reason_categories", "unique_withheld_reasons"]}, indent=2))
