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
from mediaingredientmech.form_mapping_review import FormFollowups
from mediaingredientmech.record_refresh import RecordRefreshes
from mediaingredientmech.validation.mapping_change_receipts import (
    record_supersession,
    verify_mapping_chain,
)
from mediaingredientmech.validation.mapping_change_receipts import (
    walk_mapping_changes as walk_mapping_changes,
)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SOURCE = "mappings/ingredient_mappings.sssom.tsv"
# Updated by each link in the chain, in order: the trait-phrase refresh (#703),
# the parent-name refresh (#232), then every mapping-change receipt under
# mapping_changes/ in sequence order (#312 ...). Each link records its own
# before/after pair, so the chain is auditable link by link, and no link can
# turn a prior approval into an approval of a changed row.
REVIEWED_SOURCE = "38173b2206a3d60615fca7d6d7861e777bd9905c58ec9d0b55d6a89a8c325b1c"
WEAK_EXACT_GRADES = {"CLOSE_MATCH", "NARROW_MATCH", "BROAD_MATCH", "PLACEHOLDER", "LEXICAL_MATCH"}
REGISTRIES = ("kgmicrobe.ingredient:", "kgmicrobe.compound:", "cas:")
# Admission is explicit; discovering an arbitrary report never grants authority.
FORM_FOLLOWUP_FILES = ()


def read(name):
    return json.loads((HERE / name).read_text())


def relative(path):
    return str(path.relative_to(ROOT))


def require_unique_source_positions(positions, cohort):
    """Reject duplicate cohort keys before they can discard an archived claim."""
    seen = set()
    for position in positions:
        if position in seen:
            raise ValueError(f"Duplicate source position in {cohort}: {position}")
        seen.add(position)


def withdraw_stale_cohort(entry, mapping, owner, owner_hash, chain, baseline, *, current_position):
    """Withdraw a scoped decision only from its exact archived owner and row."""
    reviewed_owner = entry.get("owner_record", entry.get("owner"))
    reviewed_hash = entry.get("owner_record_sha256")
    historical = entry.get("decision", {})
    position = entry.get("source_position", historical.get("source_position"))
    source_sha = entry.get("source_sssom_sha256", historical.get("source_record_sha256"))
    try:
        position = int(position)
    except (TypeError, ValueError) as exc:
        raise ValueError("Scoped review has no archived row position") from exc
    if (
        reviewed_owner != owner or not reviewed_hash or not owner_hash
        or source_sha != baseline["source_sha256"]
        or not 1 <= position <= len(chain["baseline_rows"])
        or chain["baseline_rows"][position - 1] != entry.get("mapping")
        or chain["forward"][position - 1] != current_position
        or chain["state"][current_position - 1] != mapping
    ):
        raise ValueError("Scoped review does not bind the verified archived row and owner")
    owner_proof = record_supersession(
        chain, owner=owner, reviewed_sha256=reviewed_hash, current_sha256=owner_hash,
    )
    if reviewed_hash != owner_hash and owner_proof is None:
        raise ValueError("Scoped review owner has no exact byte-chain supersession")
    return {
        "owner_record": owner, "reviewed_sha256": reviewed_hash,
        "current_sha256": owner_hash, "baseline_position": position,
        "current_position": current_position, "owner_supersession": owner_proof,
        "receipt_inputs": chain["receipt_inputs"],
        "reason": "Archived scoped approval withdrawn after verified correction; no approval renewed",
    }


def apply_followup(entry, mapping, owner, owner_hash, negative_reviews, root, *, safeguards=()):
    """Bind a decision to the exact current row, owner bytes and archived evidence."""
    if (
        entry["mapping"] != mapping
        or entry["row_sha256"] != row_sha256(mapping)
        or entry["owner_record"] != owner
        or not owner_hash
        or entry["owner_record_sha256"] != owner_hash
    ):
        raise ValueError("Mapping follow-up has stale row or owner")
    if entry["disposition"] not in {"SUPPORTED", "WITHHOLD"}:
        raise ValueError("Invalid mapping follow-up disposition")
    for path, expected in entry["evidence_inputs"].items():
        relative_path = Path(path)
        if relative_path.is_absolute() or ".." in relative_path.parts:
            raise ValueError("Follow-up evidence must stay within repository")
        if digest(root / relative_path) != expected:
            raise ValueError("Mapping follow-up evidence changed")
    if not entry["evidence_inputs"] or not entry["identity_review"] or not entry["reason"]:
        raise ValueError("Mapping follow-up requires explicit scientific evidence")
    if entry["disposition"] == "SUPPORTED":
        if safeguards:
            raise ValueError("Mapping follow-up cannot override relation, grade or preparation safeguards")
        if mapping["predicate_id"] != "skos:exactMatch":
            raise ValueError("This follow-up does not approve non-exact relations")
        tokens = {token for token in mapping["other"].split("|") if token}
        if set(entry["token_reviews"]) != tokens or any(
            not review for review in entry["token_reviews"].values()
        ):
            raise ValueError("Mapping follow-up does not review every synonym token")
        if entry.get("resolved_negative_reviews", []) != negative_reviews:
            raise ValueError("Mapping follow-up does not resolve the exact prior negative reviews")
    return entry["disposition"], entry["reason"]


def apply_added_identity_followup(entry, mapping, owner, owner_hash, record, root):
    """Review a newly minted local identity without approving an external grounding."""
    local_identity = (
        mapping["object_id"].startswith(("kgmicrobe.ingredient:", "kgmicrobe.compound:"))
        and mapping["object_id"] == record.get("identifier")
        and mapping["subject_label"] == mapping["object_label"] == record.get("preferred_term")
        and not mapping["other"]
    )
    return apply_followup(entry, mapping, owner, owner_hash, [], root,
                          safeguards=[] if local_identity else ["New rows require a separate external-mapping review"])


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
    chain = verify_mapping_chain(ROOT)
    mapping_changes = chain["receipts"]
    # Section receipts remain audit inputs, but every approval and chain link
    # binds exact record bytes. They cannot bridge a reviewed-hash mismatch.
    refreshes = RecordRefreshes(ROOT)
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
            known = refreshes.advance(
                entry["source_record"],
                expected_hashes.get(entry["source_record"], entry["before_yaml_sha256"]),
                entry["before_yaml_sha256"],
            )
            if known != entry["before_yaml_sha256"]:
                raise ValueError(f"{label} correction no longer extends the reviewed baseline")
            expected_hashes[entry["source_record"]] = entry["after_yaml_sha256"]
    _, _, mappings = read_sssom(ROOT / SOURCE)
    owners, records = _owners(ROOT, mappings)
    record_hashes = {owner: digest(ROOT / owner) for owner in set(owners)}
    if any(not refreshes.matches(owner, expected_hashes.get(owner)) for owner in record_hashes):
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
    forward, mapping_changed_rows, replayed = chain["forward"], chain["last"], chain["state"]
    if chain["refreshed_rows"] != {position: item["after"] for position, item in changed_rows.items()}:
        raise ValueError("Synonym-prefix replay differs from the verified receipt chain")
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
    candidate_entries = read("mapping_review/nonmapping_cohorts.json")["rows"]
    changed_owner_entries = read("mapping_review/changed-owner-review.json")["rows"]
    require_unique_source_positions(
        (entry["source_position"] for entry in candidate_entries), "nonmapping_cohorts.json",
    )
    require_unique_source_positions(
        (int(entry["decision"]["source_position"]) for entry in changed_owner_entries),
        "changed-owner-review.json",
    )
    candidates = {r["source_position"]: r for r in candidate_entries}
    changed = {int(r["decision"]["source_position"]): r for r in changed_owner_entries}
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

    followups = read("mapping_review/kgmicrobe-followup.json")["decisions"]
    followups_by_key = {}
    for item in followups:
        key = tuple(item["mapping"][field] for field in ("subject_id", "predicate_id", "object_id"))
        if key in followups_by_key:
            raise ValueError("Duplicate mapping follow-up")
        followups_by_key[key] = item
    used_followups = set()
    form_followups = FormFollowups(
        ROOT, FORM_FOLLOWUP_FILES, chain, mappings, owners, records, record_hashes,
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
            followup_key = tuple(mapping[field] for field in ("subject_id", "predicate_id", "object_id"))
            if followup_key in followups_by_key:
                followup = followups_by_key[followup_key]
                entry["disposition"], entry["review_reason"] = apply_added_identity_followup(
                    followup, mapping, owner, record_hashes[owner], records[owner], ROOT,
                )
                entry["basis"]["mapping_followup"] = {
                    "file": "mapping_review/kgmicrobe-followup.json",
                    "row_sha256": followup["row_sha256"],
                    "identity_review": followup["identity_review"],
                }
                used_followups.add(followup_key)
            form = form_followups.apply(
                mapping, owner, record_hashes[owner], records[owner],
                current_position=current_position,
                negative_reviews=[
                    negative
                    for old_position, old_row in enumerate(baseline["rows"], 1)
                    if old_row["subject_id"] == mapping["subject_id"]
                    for negative in explicit_holds.get(old_position, [])
                ],
            )
            if form:
                if followup_key in followups_by_key:
                    raise ValueError("Claim has both legacy and form review authorities")
                entry["disposition"], entry["review_reason"], entry["basis"]["form_followup"] = form
            entries[key] = entry
            decisions.append(
                {
                    "source_position": current_position,
                    "row_sha256": entry["row_sha256"],
                    "owner_record": owner,
                    "disposition": entry["disposition"],
                    "review_reason": entry["review_reason"],
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
        # Correction history is cumulative, even when the later mapping receipt
        # determines the current withholding reason (#1017).
        if position in changed_rows:
            basis["synonym_correction"] = changed_rows[position]["receipt"]
        if mapping_change:
            basis["mapping_change"] = mapping_change["receipt"]
        # These are previously completed scientific reviews, not inference from
        # passing structural checks or matching ontology labels.
        if (
            original["resolution_status"] == "APPROVED"
            and mapping == previous_mapping
            and refreshes.matches(owner, baseline["record_inputs"].get(owner))
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
        elif position in changed_rows:
            reason = "The synonym rejection corrects a token that is not a name of this substance, but does not itself approve the record's remaining identity and aliases. Preserve this changed row pending a complete mapping-specific decision."
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
                entry["mapping"] != mapping or entry["owner_record"] != owner
                or not refreshes.matches(owner, entry["owner_record_sha256"])
            ):
                basis["superseded_scoped_review"] = withdraw_stale_cohort(
                    entry, mapping, owner, record_hashes[owner], chain, baseline,
                    current_position=current_position,
                )
                disposition = "WITHHOLD"
                reason = "The exact archived cohort approval was superseded by a verified correction; fresh mapping-specific review is required."
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
                or not refreshes.matches(owner, entry["owner_record_sha256"])
            ):
                basis["superseded_scoped_review"] = withdraw_stale_cohort(
                    entry, mapping, owner, record_hashes[owner], chain, baseline,
                    current_position=current_position,
                )
                disposition = "WITHHOLD"
                reason = "The exact archived changed-owner approval was superseded by a verified correction; fresh mapping-specific review is required."
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
            reviewed_owner = next(
                (entry.get("after_yaml_sha256") for entry in traits["records"]
                 if entry["source_record"] == owner), None,
            )
            if not refreshes.matches(owner, reviewed_owner):
                raise ValueError("Explicit corrected identity review has stale owner bytes")
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
        followup_key = tuple(mapping[field] for field in ("subject_id", "predicate_id", "object_id"))
        if followup_key in followups_by_key:
            followup = followups_by_key[followup_key]
            disposition, reason = apply_followup(
                followup, mapping, owner, record_hashes[owner], explicit_holds.get(position, []), ROOT,
                safeguards=[basis[k] for k in ("policy", "preparation_tokens") if k in basis],
            )
            used_followups.add(followup_key)
            basis["mapping_followup"] = {
                "file": "mapping_review/kgmicrobe-followup.json",
                "row_sha256": followup["row_sha256"],
                "identity_review": followup["identity_review"],
            }
            if disposition == "SUPPORTED" and "negative_reviews" in basis:
                basis["resolved_prior_negative_reviews"] = basis.pop("negative_reviews")
        form = form_followups.apply(
            mapping, owner, record_hashes[owner], records[owner],
            current_position=current_position, negative_reviews=explicit_holds.get(position, []),
        )
        if form:
            if followup_key in followups_by_key:
                raise ValueError("Claim has both legacy and form review authorities")
            disposition, reason, basis["form_followup"] = form
            if disposition == "SUPPORTED":
                if "policy" in basis:
                    basis["resolved_relation_policy"] = basis.pop("policy")
                if "negative_reviews" in basis:
                    basis["resolved_prior_negative_reviews"] = basis.pop("negative_reviews")
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
    if used_followups != set(followups_by_key):
        raise ValueError("Mapping follow-up refers to a missing source assertion")
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
        ROOT / "src/mediaingredientmech/review_claims.py",
        ROOT / "src/mediaingredientmech/synonym_policy.py",
        ROOT / "src/mediaingredientmech/record_refresh.py",
        ROOT / "src/mediaingredientmech/form_mapping_review.py",
        ROOT / "src/mediaingredientmech/validation/mapping_change_receipts.py",
        ROOT / "scripts/validate_reviewed_sssom_schema.py",
        ROOT / "reports/semantic_review_20260921/records.tsv",
        ROOT / "reports/semantic_review_20260921/resolution/historical-review-evidence.json",
    ):
        inputs[relative(p)] = digest(p)
    inputs.update(chain["input_hashes"])
    inputs.update(form_followups.inputs)
    for decision in baseline["decisions"]:
        if decision["resolution_status"] == "APPROVED":
            path = ROOT / decision["review_evidence"]
            inputs[relative(path)] = digest(path)
    for followup in followups:
        # The standalone release verifier must check the same source evidence
        # even when the dated assembler is not run again.
        inputs.update(followup["evidence_inputs"])
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
    form_followups.finish()
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
