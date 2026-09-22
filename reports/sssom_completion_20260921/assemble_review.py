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
# Updated by each link in the chain, in order: the trait-phrase refresh (#703),
# the parent-name refresh (#232), then every mapping-change receipt under
# mapping_changes/ in sequence order (#312 ...). Each link records its own
# before/after pair, so the chain is auditable link by link, and no link can
# turn a prior approval into an approval of a changed row.
REVIEWED_SOURCE = "c418f8062967e772911978cc51b680d031228019dfe744773a6307d51b87f0e0"
WEAK_EXACT_GRADES = {"CLOSE_MATCH", "NARROW_MATCH", "BROAD_MATCH", "PLACEHOLDER", "LEXICAL_MATCH"}
REGISTRIES = ("kgmicrobe.ingredient:", "kgmicrobe.compound:", "cas:")


def read(name):
    return json.loads((HERE / name).read_text())


def relative(path):
    return str(path.relative_to(ROOT))


def walk_mapping_changes(receipts, *, start_sha256, reviewed_sha256, baseline_rows, refreshed_rows):
    """Verify the mapping-change receipts as one chain and replay them over the rows.

    ``receipts`` are the ``mapping_changes/*.json`` documents (any order);
    ``start_sha256`` is the SSSOM digest the last synonym refresh produced;
    ``refreshed_rows`` maps a baseline position to the row as the synonym
    refreshes left it. Every receipt must chain by digest, be numbered without
    gaps, carry no approval, and describe each touched row's ``before`` exactly
    as the previous link left it -- a row corrected twice chains through its
    first correction, not back to the baseline (#742).

    Returns ``(forward, last, state)``: the baseline-to-current position map
    (``None`` for removed rows), the last receipt change per current position
    for rows a receipt changed or added, and the replayed rows, which the caller
    compares to the current source.
    """
    receipts = sorted(receipts, key=lambda receipt: receipt["sequence"])
    if [r["sequence"] for r in receipts] != list(range(1, len(receipts) + 1)):
        raise ValueError("Mapping-change receipts must be numbered 1..n without gaps")
    state = [dict(refreshed_rows.get(position, row)) for position, row in enumerate(baseline_rows, 1)]
    forward = list(range(1, len(baseline_rows) + 1))
    last = {}
    link = start_sha256
    for receipt in receipts:
        batch = receipt.get("batch")
        if receipt.get("schema_version") != 1 or str(receipt.get("approval", "")).split(":")[0] != "NONE":
            raise ValueError(f"Mapping-change receipt {batch} is not an approval-free link")
        if receipt["before_sha256"] != link:
            raise ValueError(f"Mapping-change receipt {batch} does not chain from the previous link")
        link = receipt["after_sha256"]
        position_map = receipt["position_map"]
        if len(position_map) != receipt["before_row_count"] or receipt["before_row_count"] != len(state):
            raise ValueError(f"Mapping-change receipt {batch} position map is incomplete")
        after_count = receipt["after_row_count"]
        new_state = [None] * after_count
        for position, row in enumerate(state, 1):
            target = position_map[position - 1]
            if target is None:
                continue
            if not 1 <= target <= after_count or new_state[target - 1] is not None:
                raise ValueError(f"Mapping-change receipt {batch} position map is not injective")
            new_state[target - 1] = row
        moved = {}
        for current, change in last.items():
            target = position_map[current - 1]
            if target is not None:
                moved[target] = change
        for change in receipt["changes"]:
            kind = change["kind"]
            if kind in {"changed", "removed"}:
                before = change["before_position"]
                if state[before - 1] != change["before"]:
                    raise ValueError(f"Mapping-change receipt {batch} does not chain from the reviewed row")
                target = position_map[before - 1]
                if kind == "removed":
                    if target is not None:
                        raise ValueError(f"Mapping-change receipt {batch} removes a row its position map keeps")
                    continue
                if target != change["after_position"]:
                    raise ValueError(f"Mapping-change receipt {batch} moves a changed row inconsistently")
            elif kind == "added":
                target = change["after_position"]
                if not 1 <= target <= after_count or new_state[target - 1] is not None:
                    raise ValueError(f"Mapping-change receipt {batch} adds a row onto an occupied position")
            else:
                raise ValueError(f"Mapping-change receipt {batch} has an unknown change kind {kind!r}")
            new_state[target - 1] = change["after"]
            moved[target] = dict(change, receipt=batch)
        if any(row is None for row in new_state):
            raise ValueError(f"Mapping-change receipt {batch} leaves a hole in the row order")
        forward = [position_map[p - 1] if p is not None else None for p in forward]
        last, state = moved, new_state
    if link != reviewed_sha256:
        raise ValueError("The last chain link does not produce the reviewed source")
    return forward, last, state


def assemble():
    if digest(ROOT / SOURCE) != REVIEWED_SOURCE:
        raise ValueError("SSSOM differs from this completed scientific review; review it again")
    baseline = read("baseline-mapping-review.json")
    traits = read("trait_synonyms/decisions.json")
    refresh = read("trait-synonym-refresh.json")
    parents = read("parent_names/decisions.json")
    parent_refresh = read("parent-name-refresh.json")
    if parent_refresh["before_sha256"] != refresh["after_sha256"]:
        raise ValueError("Parent-name refresh does not chain from the trait refresh")
    # Mapping-change receipts (identity, parent, grade, merge, mint) follow the
    # synonym refreshes. They are explicit links, never approvals: every row a
    # receipt touches is withheld below, and every owner it touches loses the
    # byte-identical carry-forward.
    mapping_changes = [
        json.loads(path.read_text()) for path in sorted((HERE / "mapping_changes").glob("*.json"))
    ]
    expected_hashes = dict(baseline["record_inputs"])
    plans = [("Trait", traits), ("Parent-name", parents)] + [
        (f"Mapping-change {receipt['batch']}", receipt)
        for receipt in sorted(mapping_changes, key=lambda receipt: receipt["sequence"])
    ]
    for label, plan in plans:
        for entry in plan["records"]:
            # A record first touched by a mapping change may be new to the reviewed
            # set (a registry mint) or a tombstone outside it; both start from
            # whatever the receipt recorded.
            known = expected_hashes.get(entry["source_record"], entry["before_yaml_sha256"])
            if known != entry["before_yaml_sha256"]:
                raise ValueError(f"{label} correction no longer extends the reviewed baseline")
            expected_hashes[entry["source_record"]] = entry["after_yaml_sha256"]
    _, _, mappings = read_sssom(ROOT / SOURCE)
    owners, records = _owners(ROOT, mappings)
    record_hashes = {owner: digest(ROOT / owner) for owner in set(owners)}
    if any(record_hashes[owner] != expected_hashes.get(owner) for owner in record_hashes):
        raise ValueError("Owner changed after scientific review; do not restamp its approval")
    prior = {int(d["source_position"]): d for d in baseline["decisions"]}
    changed_rows = {item["source_position"]: dict(item, receipt="trait-synonym-refresh.json") for item in refresh["changes"]}
    for item in parent_refresh["changes"]:
        position = item["source_position"]
        # A row corrected twice must chain: the parent-name "before" is the trait "after".
        if position in changed_rows and changed_rows[position]["after"] != item["before"]:
            raise ValueError("Parent-name refresh does not chain from the trait refresh on a shared row")
        merged = dict(item, receipt="parent-name-refresh.json")
        if position in changed_rows:
            merged["before"] = changed_rows[position]["before"]
            merged["removed_tokens"] = sorted(set(changed_rows[position]["removed_tokens"]) | set(item["removed_tokens"]))
        changed_rows[position] = merged
    forward, mapping_changed_rows, replayed = walk_mapping_changes(
        mapping_changes,
        start_sha256=parent_refresh["after_sha256"],
        reviewed_sha256=REVIEWED_SOURCE,
        baseline_rows=baseline["rows"],
        refreshed_rows={position: item["after"] for position, item in changed_rows.items()},
    )
    if replayed != mappings:
        raise ValueError("Current source rows differ from the reviewed chain's replay")
    baseline_of = {current: bp for bp, current in enumerate(forward, 1) if current is not None}
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
            current = forward[position - 1]
            if entry["mapping"] != baseline["rows"][position - 1] or (
                current is not None and owner != owners[current - 1]
            ):
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
    for current_position, (mapping, owner) in enumerate(zip(mappings, owners, strict=True), 1):
        # ``position`` is the baseline position every cohort, hold and prior
        # decision is keyed by; ``current_position`` is where the row sits now.
        position = baseline_of.get(current_position)
        mapping_change = mapping_changed_rows.get(current_position)
        if position is None:
            # A row a mapping-change receipt added: it has no baseline decision and
            # no prior review to inherit. Withhold it with the receipt as basis.
            if not mapping_change or mapping_change["kind"] != "added" or mapping_change["after"] != mapping:
                raise ValueError("Row added outside a mapping-change receipt")
            key = str(current_position)
            reason = (
                f"Row added by mapping-change receipt {mapping_change['receipt']} ({mapping_change.get('kind')}). "
                "It has no prior scientific review; preserve the claim pending a mapping-specific decision."
            )
            entry = {
                "row_sha256": row_sha256(mapping),
                "owner_record": owner,
                "owner_record_sha256": record_hashes[owner],
                "disposition": "WITHHOLD",
                "review_reason": reason,
                "basis": {"baseline_position": None, "mapping_change": mapping_change["receipt"]},
            }
            entries[key] = entry
            decisions.append(
                {
                    "source_position": current_position,
                    "row_sha256": entry["row_sha256"],
                    "owner_record": owner,
                    "disposition": "WITHHOLD",
                    "review_reason": reason,
                    "review_evidence": relative(HERE / "mapping-evidence.json"),
                    "evidence_key": key,
                }
            )
            continue
        previous_mapping = baseline["rows"][position - 1]
        if mapping != previous_mapping and not mapping_change:
            # Not touched by any receipt, so the only admissible difference is the
            # reviewed synonym correction (the replay above already proved a
            # receipt-touched row matches its receipt).
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
            and record_hashes[owner] == baseline["record_inputs"].get(owner)
        ):
            disposition = "SUPPORTED"
            reason = (
                "Retain the existing explicit scientific approval for the identical owner and complete mapping payload, subject to this review's independent negative findings and relation/alias-scope safeguards. "
                + original["review_reason"]
            )
        elif mapping_change:
            reason = (
                f"Mapping corrected by receipt {mapping_change['receipt']}: the row payload or its owner record changed after the "
                "prior review, which therefore does not carry. The correction's verification is recorded in the receipt; "
                "preserve the corrected claim pending a mapping-specific decision."
            )
            basis["mapping_change"] = mapping_change["receipt"]
        elif position in changed_rows:
            reason = "The synonym rejection corrects a token that is not a name of this substance, but does not itself approve the record's remaining identity and aliases. Preserve this changed row pending a complete mapping-specific decision."
            basis["synonym_correction"] = changed_rows[position]["receipt"]
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
        key = str(current_position)
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
                "source_position": current_position,
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
