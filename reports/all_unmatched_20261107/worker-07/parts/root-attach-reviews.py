"""Attach actual cross-review receipts after exact input hashes have been verified."""
import hashlib
import json
from pathlib import Path

OUT = Path("reports/all_unmatched_20261107/worker-07")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    decisions_path, evidence_path = OUT / "decisions.json", OUT / "evidence.json"
    decisions = json.loads(decisions_path.read_text())
    evidence = json.loads(evidence_path.read_text())
    by_case = {d["case_id"]: d for d in decisions["decisions"]}
    expected = set(by_case)
    seen = set()
    sources = [
        ("A", "captures/c-review-a-final.json", "case_reviews", "primary_c reviewing primary_a"),
        ("B", "parts/a-review-b-final.json", "cases", "primary_a reviewing primary_b"),
        ("C", "parts/b-independent-c-review-final.json", "cases", "primary_b reviewing primary_c"),
    ]
    for part, name, case_key, author in sources:
        path = OUT / name
        review = json.loads(path.read_text())
        for relative, digest in review["input_hashes"].items():
            candidate = OUT / (relative if relative.startswith(("parts/", "captures/")) else "parts/" + relative)
            assert sha(candidate) == digest, f"Stale reviewer input {candidate}"
        case_ids = [c["case_id"] for c in review[case_key]]
        assert len(case_ids) == len(set(case_ids))
        assert not seen.intersection(case_ids)
        assert all(c.get("status", c.get("outcome")) not in {"pending", "findings_open", "open"} for c in review[case_key])
        assert all(f.get("status", "resolved") not in {"open", "findings_open"} for f in review.get("findings", []))
        seen.update(case_ids)
        eid = "W07-INDEPENDENT-" + part
        evidence["evidence"].append({"evidence_id": eid, "kind": "independent_review", "capture": {"root": "artifact", "path": name, "sha256": sha(path)}, "url": None, "locator": f"{case_key}: exact per-case scientific assessments, reviewed input hashes and proposal captures", "supports_or_contradicts": f"Actual in-process skeptical review by {author}. Scope limitations and resolved findings are retained. Shared payload authorship exceptions are covered by the separately identified reviewer; no inherited hold or publication approval is granted.", "case_ids": case_ids})
        for cid in case_ids:
            decision = by_case[cid]
            decision["evidence_ids"] = list(dict.fromkeys(decision["evidence_ids"] + [eid]))
            decision["independent_review"] = {"status": "complete", "evidence_ids": [eid]}
    assert seen == expected
    name = "captures/integration-stock-deltas-final.json"
    path = OUT / name
    review = json.loads(path.read_text())
    for relative, digest in review["input_hashes"].items():
        assert sha(OUT / relative) == digest
    ids = [c["case_id"] for c in review["cases"]]
    eid = "W07-INDEPENDENT-ROOT-STOCK-DELTAS"
    evidence["evidence"].append({"evidence_id": eid, "kind": "independent_review", "capture": {"root": "artifact", "path": name, "sha256": sha(path)}, "url": None, "locator": "Four root-authored final source-case deltas and exact nominal-stock payloads; shared Hutner source reconciliation", "supports_or_contradicts": "Independent integration reviewer assessed the four later root-authored decisions separately from C's original A review. Unknown percentage basis, solvent, stereo/hydrate and source unit conflicts remain explicit. The shared JCM900/JCM979 stock has independent exact primary-source comparison.", "case_ids": ids})
    for cid in ids:
        by_case[cid]["evidence_ids"].append(eid)
        by_case[cid]["independent_review"]["evidence_ids"].append(eid)
    proposals = json.loads((OUT / "proposals.json").read_text())["proposals"]
    hutner = next(p for p in proposals if p["proposal_id"] == "W07-COMBINED-JCM900-JCM979-Hutner")
    eid = "W07-INDEPENDENT-HUTNER-CONSOLIDATION"
    evidence["evidence"].append({"evidence_id": eid, "kind": "independent_review", "capture": {"root": "artifact", "path": name, "sha256": sha(path)}, "url": None, "locator": "proposals_checked: W07-COMBINED-JCM900-JCM979-Hutner and INTEGRATION-01 resolution", "supports_or_contradicts": "Independent primary-capture comparison establishes the same declared JCM900/JCM979 nominal stock boundary. Original per-case applicability reviews still govern each source occurrence, and chemically unresolved component text remains literal.", "case_ids": hutner["case_ids"]})
    for cid in hutner["case_ids"]:
        by_case[cid]["evidence_ids"].append(eid)
        by_case[cid]["independent_review"]["evidence_ids"].append(eid)
    # Source-case applicability and a cross-author shared payload can have
    # different independent reviewers. Link both, without expanding either
    # receipt's declared full-case scope.
    for proposal in proposals:
        author_ids = proposal.get("author_proposal_ids", [proposal["proposal_id"]])
        payload_reviews = set()
        for pid in author_ids:
            if pid.startswith("A-PROPOSAL-"):
                payload_reviews.add("W07-INDEPENDENT-A")
            elif pid.startswith("B-PROPOSAL-"):
                payload_reviews.add("W07-INDEPENDENT-B")
            elif pid.startswith("C-P"):
                payload_reviews.add("W07-INDEPENDENT-C")
        for cid in proposal["case_ids"]:
            decision = by_case[cid]
            decision["evidence_ids"] = list(dict.fromkeys(decision["evidence_ids"] + sorted(payload_reviews)))
            decision["independent_review"]["evidence_ids"] = list(dict.fromkeys(decision["independent_review"]["evidence_ids"] + sorted(payload_reviews)))
            if payload_reviews:
                decision["independent_review"]["shared_payload_review_note"] = "Primary receipt reviews this source case; additional author-bundle receipts independently review the linked shared payload only, within their own declared scope."
    decisions_path.write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + "\n")
    evidence_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n")
    print(f"Attached distinct primary-author cross-reviews for {len(seen)} cases and independent root-delta review for {len(ids)} cases.")


if __name__ == "__main__":
    main()
