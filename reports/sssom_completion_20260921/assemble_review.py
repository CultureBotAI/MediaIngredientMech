"""Assemble the completed mapping dispositions from explicit reviewed evidence.

The frozen input boundary prevents rerunning this dated assembler from granting
approval to a changed source. --check independently reproduces the decisions
and catches overrides of the negative scientific reviews (#729, #730).
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

from mediaingredientmech.export.reviewed_sssom import _owners, digest, read_sssom, row_sha256

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SOURCE = "mappings/ingredient_mappings.sssom.tsv"
REVIEWED_SOURCE = "761b7dee1e7eef7ecd999a848f6188fe1a0d394c79a8b53b957c2e477cec9f3f"
WEAK_EXACT_GRADES = {"CLOSE_MATCH", "NARROW_MATCH", "BROAD_MATCH", "PLACEHOLDER", "LEXICAL_MATCH"}
REGISTRIES = ("kgmicrobe.ingredient:", "kgmicrobe.compound:", "cas:")


def read(name):
    return json.loads((HERE / name).read_text())


def relative(path):
    return str(path.relative_to(ROOT))


def assemble():
    if digest(ROOT / SOURCE) != REVIEWED_SOURCE:
        raise ValueError("SSSOM differs from this completed scientific review; review it again")
    baseline = read("baseline-mapping-review.json")
    traits = read("trait_synonyms/decisions.json")
    refresh = read("trait-synonym-refresh.json")
    expected_hashes = dict(baseline["record_inputs"])
    for entry in traits["records"]:
        if expected_hashes[entry["source_record"]] != entry["before_yaml_sha256"]:
            raise ValueError("Trait correction no longer extends the reviewed baseline")
        expected_hashes[entry["source_record"]] = entry["after_yaml_sha256"]
    _, _, mappings = read_sssom(ROOT / SOURCE)
    owners, records = _owners(ROOT, mappings)
    record_hashes = {owner: digest(ROOT / owner) for owner in set(owners)}
    if any(record_hashes[owner] != expected_hashes[owner] for owner in record_hashes):
        raise ValueError("Owner changed after scientific review; do not restamp its approval")
    prior = {int(d["source_position"]): d for d in baseline["decisions"]}
    changed_rows = {item["source_position"]: item for item in refresh["changes"]}
    original_records = {
        r["source_record"]: r
        for r in csv.DictReader(
            (ROOT / "reports/semantic_review_20260921/records.tsv").open(), delimiter="\t"
        )
    }
    concerns = {
        r["source_position"]: r for r in read("mapping_review/concern_cohorts.json")["rows"]
    }
    candidates = {
        r["source_position"]: r for r in read("mapping_review/nonmapping_cohorts.json")["rows"]
    }
    changed = {
        int(r["decision"]["source_position"]): r
        for r in read("mapping_review/changed-owner-review.json")["rows"]
    }
    for cohort in (concerns, candidates, changed):
        for position, entry in cohort.items():
            owner = entry.get("owner_record", entry.get("owner", entry.get("source_record")))
            if entry["mapping"] != baseline["rows"][position - 1] or owner != owners[position - 1]:
                raise ValueError("Scoped review was moved to another mapping or owner")
    intersections = read("mapping_review/issue-intersections.json")
    explicit_holds = {}

    def hold(position, reason, proof, detail):
        explicit_holds.setdefault(int(position), []).append(
            {"reason": reason, "evidence": proof, "detail": detail}
        )

    for group in (
        "issue_669_all_baseline_intersections",
        "issue_232_conflicting_label_intersections",
    ):
        for item in intersections[group]:
            reason = (
                item.get("reason")
                or "This current synonym collides across different substance identities (#232); a shared label does not establish chemical equivalence."
            )
            for row in item["sssom_rows"]:
                hold(
                    row["source_position"], reason, "mapping_review/issue-intersections.json", group
                )
    for finding in intersections["findings"]:
        if finding["status"].startswith(("CONFIRMED", "WITHHOLD")):
            for row in finding["record"]["sssom_rows"]:
                hold(
                    row["source_position"],
                    finding["reason"],
                    "mapping_review/issue-intersections.json",
                    finding["id"],
                )
    for filename in (
        "mapping_review/adversarial-findings.json",
        "mapping_review/synonym-adversarial-findings.json",
    ):
        for finding in read(filename)["findings"]:
            hold(
                finding["source_position"],
                finding["reason"],
                filename,
                finding.get("id", finding.get("subject_id")),
            )

    entries, decisions = {}, []
    for position, (mapping, owner) in enumerate(zip(mappings, owners, strict=True), 1):
        previous_mapping = baseline["rows"][position - 1]
        if mapping != previous_mapping:
            correction = changed_rows.get(position, {})
            if correction.get("before") != previous_mapping or correction.get("after") != mapping:
                raise ValueError("Mapping changed outside the reviewed synonym correction")
        original = prior[position]
        disposition = "WITHHOLD"
        reason = "This assertion lacks a mapping-specific positive disposition. Its full unchanged claim is preserved for source review."
        basis = {
            "baseline_position": position,
            "previous_decision": original,
            "historical_record_review": original_records.get(owner, {}).get("review_report"),
        }
        # These are previously completed scientific reviews, not inference from
        # passing structural checks or matching ontology labels.
        if (
            original["resolution_status"] == "APPROVED"
            and mapping == previous_mapping
            and record_hashes[owner] == baseline["record_inputs"][owner]
        ):
            disposition = "SUPPORTED"
            reason = (
                "Retain the existing explicit scientific approval for the identical owner and complete mapping payload, subject to this review's independent negative findings and relation/alias-scope safeguards. "
                + original["review_reason"]
            )
        elif position in changed_rows:
            reason = "The trait-phrase rejection corrects a non-name token, but does not itself approve the record's remaining identity and aliases. Preserve this changed row pending a complete mapping-specific decision."
            basis["trait_correction"] = "trait-synonym-refresh.json"
        if position in concerns:
            entry = concerns[position]
            disposition, reason = "WITHHOLD", entry["reason"]
            basis["scoped_review"] = {
                "file": "mapping_review/concern_cohorts.json",
                "position": position,
            }
        if position in candidates:
            entry = candidates[position]
            disposition, reason = entry["disposition"], entry["reason"]
            if disposition == "SUPPORTED" and (
                entry["mapping"] != mapping or entry["owner_record_sha256"] != record_hashes[owner]
            ):
                raise ValueError("Nonmapping-cohort approval has stale owner or row")
            basis["scoped_review"] = {
                "file": "mapping_review/nonmapping_cohorts.json",
                "position": position,
            }
        if position in changed:
            entry = changed[position]
            disposition, reason = entry["disposition"], entry["reason"]
            if disposition == "SUPPORTED" and (
                entry["mapping"] != mapping
                or entry["owner"] != owner
                or entry["owner_record_sha256"] != record_hashes[owner]
            ):
                raise ValueError("Changed-owner approval has stale row or owner")
            basis["scoped_review"] = {
                "file": "mapping_review/changed-owner-review.json",
                "position": position,
            }
        if position in {437, 439}:
            expected = {
                437: (
                    "MIM:Aromatic_Compound",
                    "CHEBI:33655",
                    "aromatic compounds|aromatic molecular entity",
                ),
                439: (
                    "MIM:Arsenate",
                    "CHEBI:29125",
                    "Arsenate ion|arsorate|tetraoxoarsenate(V)|tetraoxidoarsenate(3-)|tetraoxoarsenate(3-)|CAS:15584-04-0",
                ),
            }[position]
            if tuple(mapping[k] for k in ("subject_id", "object_id", "other")) != expected:
                raise ValueError("Explicit corrected identity or synonym set changed")
            disposition = "SUPPORTED"
            reason = "The archived ChEBI identity review explicitly verifies this exact target and every remaining synonym/CAS token. The source correction preserves the complete activity phrase as REJECTED_LABEL and the pinned producer excludes it. Earlier wrong arsenite aliases, where applicable, remain rejected. This decision approves only the corrected mapping."
            basis["scoped_review"] = {
                "file": "trait-synonym-refresh.json",
                "position": position,
                "historical_report": original_records[owner]["review_report"],
            }
        # Absence of proof for a precise SKOS relation remains an explicit hold.
        # exactMatch to the record's own identifier is a serialization rule,
        # and cannot strengthen an uncertain ontology grounding scientifically.
        if mapping["predicate_id"] != "skos:exactMatch":
            disposition = "WITHHOLD"
            reason = (
                "The prior record review does not settle this non-exact relation and its complete synonym scope under the current mapping-only release standard. Preserve the precise parent/close claim for explicit relation review. "
                + reason
            )
            basis["policy"] = (
                "Non-exact relations require fresh claim-level review; no inherited whole-record approval."
            )
        elif (
            not mapping["object_id"].startswith(REGISTRIES)
            and (records[owner].get("ontology_mapping") or {}).get("mapping_quality")
            in WEAK_EXACT_GRADES
        ):
            disposition = "WITHHOLD"
            reason = (
                "The source grounding grade is "
                + records[owner]["ontology_mapping"]["mapping_quality"]
                + "; identity with its own identifier does not substantiate an exact ontology equivalence. A source-scoped exact-relation review is required. "
                + reason
            )
            basis["policy"] = (
                "Do not infer exact scientific equivalence from primary-identifier equality (#730)."
            )
        # Specific preparation or instruction tokens need individual curation;
        # this is a conservative hold, not an automated assertion of falsity.
        suspect = [
            t
            for t in mapping["other"].split("|")
            if re.search(
                r"(?i)\d\s*%|\d\s*(?:mg/ml|g/l)|autoclave|\bif needed\b|\bstock solution\b", t
            )
        ]
        if suspect:
            disposition = "WITHHOLD"
            reason = (
                "Preparation/concentration/instruction tokens remain in the synonym channel and need individual same-subject review: "
                + "; ".join(suspect)
                + ". "
                + reason
            )
            basis["preparation_tokens"] = suspect
        if position in explicit_holds:
            disposition = "WITHHOLD"
            reason = " ".join(dict.fromkeys(item["reason"] for item in explicit_holds[position]))
            basis["negative_reviews"] = explicit_holds[position]
        key = str(position)
        entry = {
            "row_sha256": row_sha256(mapping),
            "owner_record": owner,
            "owner_record_sha256": record_hashes[owner],
            "disposition": disposition,
            "review_reason": reason,
            "basis": basis,
        }
        entries[key] = entry
        decisions.append(
            {
                "source_position": position,
                "row_sha256": entry["row_sha256"],
                "owner_record": owner,
                "disposition": disposition,
                "review_reason": reason,
                "review_evidence": relative(HERE / "mapping-evidence.json"),
                "evidence_key": key,
            }
        )
    evidence = {
        "schema_version": 1,
        "scope": "Completed mapping-only disposition review; WITHHOLD preserves a review obligation and does not assert that every withheld triple is false. No role/component approval.",
        "entries": entries,
    }
    evidence_bytes = (json.dumps(evidence, indent=2) + "\n").encode()
    import hashlib

    inputs = {
        relative(p): digest(p)
        for p in HERE.rglob("*")
        if p.is_file()
        and p.suffix in {".json", ".py", ".tsv", ".md"}
        and p.name not in {"review.json", "mapping-evidence.json", "README.md"}
    }
    for p in (
        ROOT / "MAPPING_SEMANTICS.md",
        ROOT / "src/mediaingredientmech/export/reviewed_sssom.py",
        ROOT / "src/mediaingredientmech/synonym_policy.py",
        ROOT / "scripts/validate_reviewed_sssom_schema.py",
        ROOT / "reports/semantic_review_20260921/records.tsv",
        ROOT / "reports/semantic_review_20260921/resolution/historical-review-evidence.json",
    ):
        inputs[relative(p)] = digest(p)
    for decision in baseline["decisions"]:
        if decision["resolution_status"] == "APPROVED":
            path = ROOT / decision["review_evidence"]
            inputs[relative(path)] = digest(path)
    inputs[relative(HERE / "mapping-evidence.json")] = hashlib.sha256(evidence_bytes).hexdigest()
    review = {
        "schema_version": 1,
        "scope": "MIM SSSOM mappings only; supported subset plus complete withheld backlog",
        "source_sssom": SOURCE,
        "source_sha256": REVIEWED_SOURCE,
        "inputs": dict(sorted(inputs.items())),
        "record_inputs": dict(sorted(record_hashes.items())),
        "decisions": decisions,
    }
    return {
        "mapping-evidence.json": evidence_bytes,
        "review.json": (json.dumps(review, indent=2) + "\n").encode(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    products = assemble()
    for name, content in products.items():
        path = HERE / name
        if args.check:
            if not path.is_file() or path.read_bytes() != content:
                raise ValueError("Reviewed decision drift: " + name)
        else:
            path.write_bytes(content)
    decisions = json.loads(products["review.json"])["decisions"]
    print(
        json.dumps(
            {
                "mapping_rows": len(decisions),
                "dispositions": dict(Counter(d["disposition"] for d in decisions)),
                "reproduced": args.check,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
