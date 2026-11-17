#!/usr/bin/env python3
"""Record independently inspected fixes for #1535/#1536, 2026-11-17.

Inputs: exact prior native review and both frozen decision snapshots.
Outputs: new durable successor bytes, native inspection and linked review draft.
No scientific decisions, old reviews, ingredient records or canonical rows change.
"""

import argparse
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml
from record_review import assert_current_source, inspect_source, validate_review

ROOT = Path(__file__).resolve().parents[2]
PRIOR = "reviews/structured/20261117T013626Z-culturemech-intake-second-cross-review/review.yaml"
PRIOR_PIN = "35ce19f2e0fac754f22e47332ddeb43a75782f591009e303c25b84350f21a7cc"
BEFORE_PIN = "a309fe8b6a841afea0d0b4463a205fe322a2722fced2797930bd0cbfe815791b"
AFTER_PIN = "b846c03927bd2d0e5e09bbb4b6911295761c4e11f743c1e223d67bd5eac731ef"


def pinned(path, expected):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError("Unexpected input: " + str(path))
    return raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", type=Path, required=True)
    parser.add_argument("--after", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    prior_raw = pinned(ROOT / PRIOR, PRIOR_PIN)
    before_raw = pinned(args.before, BEFORE_PIN)
    after_raw = pinned(args.after, AFTER_PIN)
    before, after = json.loads(before_raw), json.loads(after_raw)
    expected = copy.deepcopy(before)
    changes = []
    for row in expected["decisions"]:
        if row["case_id"] == "b198a7c5e3164e5112e16cb10007008ceb321feeff7a7c4bc2f2dcad109d6e3d":
            row["evidence_locators"][0] = "owner-0273.json: descriptor d300b6526d61bfef904b8c9ca20b96a7c020a0bb686b85b9f007dc74079a07f8 and specialized/alp_defined_chlorate.yaml"
            changes.append("chlorate-locator")
        if row["case_id"] == "d0c8d3c8ab968b81703d7291e78c7bbb018c735fd3e2cd11b342b18b11d1be20":
            row["blocking_witnesses"][0]["reason"] = "The literal KOMODO source calls the material sodium sulfide hydrate, while the selected candidate owner denotes anhydrous CHEBI:76208; this witness itself contains no term or MIM-derived term field."
            changes.append("sulfide-witness-wording")
    if expected != after or set(changes) != {"chlorate-locator", "sulfide-witness-wording"}:
        raise ValueError("Successor differs beyond the independently inspected two fields")
    output = args.output_dir.resolve()
    output.relative_to(ROOT / "reports")
    output.mkdir(parents=True, exist_ok=False)
    successor = output / "second-219-284-v2.json"
    successor.write_bytes(after_raw)
    rel = successor.relative_to(ROOT).as_posix()
    review = yaml.safe_load(prior_raw)
    previous_id = review["review_id"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    review.update({
        "review_id": now.replace("-", "").replace(":", "") + "-culturemech-second-provenance-followup",
        "title": "Independent two-field provenance reconciliation for the second intake review",
        "started_at": now, "finished_at": now, "verdict": "pass_with_limitations",
        "summary": "Independently inspected the exact successor diff: only the chlorate narrative digest and sodium-sulfide witness explanation changed. All scientific dispositions, case pins and payload membership remain byte-equivalent at the parsed-field level. The two prior minor findings are resolved; the original bounded scientific sample and its limitations remain unchanged.",
    })
    review["evidence"].append({
        "evidence_id": "successor-two-field-diff", "kind": "record_content",
        "reference": rel, "accessed_at": now, "support": "supports",
        "summary": "Exact pinned successor equals the original document with only the two independently inspected narrative corrections. The corrected digest matches its inspected member; the hydrate explanation correctly distinguishes source wording from the selected anhydrous owner.",
        "snapshot_sha256": AFTER_PIN,
    })
    for assessment in review["assessments"]:
        assessment["outcome"] = "supported"
        assessment["summary"] += " Successor independently checked: both minor narrative findings corrected with no scientific decision changes."
        assessment["evidence_ids"].append("successor-two-field-diff")
    for finding in review["findings"]:
        finding["status"] = "resolved"
        finding["previous_occurrences"] = [{
            "repository": review["repository"], "review_id": previous_id,
            "finding_id": finding["finding_id"],
        }]
        finding["evidence_ids"].append("successor-two-field-diff")
        finding["disposition_reason"] = "The exact successor changes only the documented narrative error. Original targets and evidence remain retained; scientific identity judgments and machine payload pins are unchanged."
    review["actions"] = []
    review["related_reviews"] = [{"repository": review["repository"], "review_id": previous_id, "relationship": "Resolves both minor provenance findings after exact independent two-field successor inspection; retains all prior targets and scope limits."}]
    contexts = sorted({item["path"] for item in review["source"]["inputs"]} | {PRIOR, rel})
    inspection = inspect_source(ROOT, review["targets"], contexts)
    review["source"] = inspection["source"]
    assert_current_source(ROOT, review)
    pinned(ROOT / PRIOR, PRIOR_PIN)
    pinned(args.before, BEFORE_PIN)
    pinned(args.after, AFTER_PIN)
    validate_review(review, ROOT / "schema/record_review.yaml")
    draft = output / "review-draft.json"
    draft.write_text(json.dumps(review, indent=2) + "\n")
    (output / "inspection.json").write_text(json.dumps(inspection, indent=2) + "\n")
    print(draft.relative_to(ROOT))


if __name__ == "__main__":
    main()
