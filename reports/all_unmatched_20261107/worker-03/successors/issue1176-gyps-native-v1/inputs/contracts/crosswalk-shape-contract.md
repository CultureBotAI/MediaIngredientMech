# Closed future application crosswalk — issue 1247

This immutable successor corrects the unused future crosswalk helper. It does **not** rematerialize the campaign, select new worker heads, accept science, build a real native plan, or apply owners. The predecessor's observer-v4 counts remain historical. The current campaign's moving selectors need a separately frozen intake.

`accounting.py` retains the prior case/origin accounting functions and delegates only `validate_resolution_crosswalk` to `crosswalk.py`. The original source, original 35-test file, prior handoff and manifest remain byte-identical under `historical/`. The successor retains all original test cases; the formerly permissive retirement positive now uses actual published fixture evidence. Its unchanged old body is preserved in `historical/test_accounting.py`, not misrepresented as still valid under the corrected contract.

The function rejects duplicate denominator rows, closes every retirement over a separately declared and verified published successor universe, rejects self-links and cycles, binds actual evidence bytes, and compares every apply origin/operation/payload to a fresh native `campaign_owner_apply.prepare` result. The native writer is never called. Its final input/inventory recheck remains active.

## API

Call from Python 3.13 with the maintained integration `src` on `PYTHONPATH` and this directory on the import path:

```python
from accounting import validate_resolution_crosswalk

result = validate_resolution_crosswalk(
    original_origin_rows,
    explicit_resolution_rows,
    root=explicit_application_root,
    origin_bindings=exact_published_origin_bindings,
    successor_origins=additional_explicit_published_successor_rows,
    native_plan={"plan": plan_file_reference, "acceptance": acceptance_file_reference},
)
```

Those variables must contain real final evidence. No such real campaign crosswalk or native plan is supplied by this packet. Use `native_plan=None` if no row is `apply`; a caller cannot use that omission to hide a native operation. The native plan, when supplied, must be the exact set of applied origins and operations. All declared additional successors also need their own explicit resolution rows; the function reports their count separately.

Each original/successor origin retains `origin_id` (`wNN::proposal_id`), integer `worker_slot`, exact `published_head`, complete `proposal`, `proposal_object_sha256`, original `payload_sha256`, and source `case_hashes`. Rich existing accounting rows may keep other fields. The exact complete proposal is compared to its real committed JSON object, not merely an ID or payload hash.

Each origin binding is closed:

```json
{
  "origin_id": "wNN::actual-proposal-id",
  "proposal_ledger": {"path": "captured/proposals.json", "sha256": "64 lowercase hex", "published_path": "actual/committed/proposals.json"},
  "payload": {"path": "captured/owner.yaml", "sha256": "64 lowercase hex", "published_path": "actual/committed/owner.yaml"}
}
```

All references are relative to the explicit root, use canonical paths and must be actual regular files with exact hashes. Published references must match regular Git blobs at the declared source head; symlinks and aliases are refused. The entire declared origin universe needs bindings. A plain nonempty receipt string is no longer evidence.

Every resolution has exactly `origin_id`, `status`, `evidence_refs`, plus the status-specific keys below. Evidence references are closed `{path, sha256}` objects. Unknown keys, duplicate references and noncanonical paths are rejected.

| Status | Required additional fields and verification |
| --- | --- |
| `pending`, `deferred` | `missing_requirement`, nonempty; real bound evidence. These outcomes remain unresolved science/application work. |
| `retired` | `successor_origin_ids`, `retirement_reason`, `retirement_bridge`. Every successor exists in the verified universe and is separately classified. Empty successor lists represent an explicitly documented withdrawal, not an invented successor. |
| `already_satisfied` | `satisfied_owner` exact direct-owner file reference and `independent_review_refs`; current owner bytes must match. This records no-write accounting, not scientific equality inferred by code. |
| `apply` | `operation_id`, `payload_sha256`, `independent_review_refs`; exact match to real native prepare result, accepted review binding set, source head/case hashes, complete before/after inventories and artifact evidence. |

The retirement bridge has exactly `{capture, published_head}`. `capture` is a published reference. Its actual JSON statement has exactly `schema_version: 1`, `kind: "source_origin_retirement"`, `origin_id`, `origin_proposal_sha256`, `successors` (origin ID to complete proposal-object hash), and `reason`. It must equal the declared crosswalk claim and be included in `evidence_refs`. The bridge head is one of the selected successors' published heads, or the original selected head for a documented withdrawal with no successor. Existing differently shaped historical receipts remain immutable evidence; they are **not** automatically parsed or relabelled as this normalized statement. A future author/coordinator must provide an honest published normalization referencing the genuine lineage, with the required review, before this API is used for that case. This requirement cannot fabricate a new owner origin or supersede a source decision.

## Actual native verification and limits

For apply rows the helper calls the current native `prepare(root, plan, acceptance)`. This validates exact source inputs, real Git-published origins, the native case hashes, current preimages, producer bindings, native schema, owner-chain endpoint, complete inventory transition and explicit edit/create/promotion lineage. The helper verifies all selected native origins are consumed once and all native operations are covered. Two origins may legitimately share one operation only with the same exact native payload. A conflicting payload or operation is rejected. It calls the native recheck again at the final boundary and rechecks every additional path/byte proof.

Returned `native_prepare_proof` includes plan/acceptance hashes, exact input hashes and complete owner inventories. It is derived from actual execution, not a caller-supplied “PASS” JSON. The result always says `scientific_approval: false` and `application_authorized: false`. A structural pass does not authenticate a researcher's scientific judgment, establish reviewer independence, interpret the adequacy of a missing-requirement explanation, prove a current remote branch has not advanced, or make source-only acceptance into whole-owner approval. The coordinator still binds those separate exact reviews and the current published-intake cutoff.

## Verification and preserved diagnostics

The focused suite exercises all six original counterexamples with meaningful real publication/native fixtures: unknown successor, self-link, retirement cycle, duplicate origin denominator, conflicting shared operation and malformed digest. Additional controls cover changed published objects, stale evidence, missing proof roles/resolutions, unbound review, incomplete native operation coverage, incorrect source cases/promotion preimage, leaf/parent/late aliases and late direct-owner membership. Positive controls use the actual native prepare path for edit/create/promotion, legitimate shared-origin union, a real published retirement and explicit unresolved accounting. No fixture applies maintained source data.

Run with a fresh private output location; do not reuse a basetemp:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$C/integration/worktree/src" \
  "$T/env/bin/python" -B -m pytest -q --noconftest -o addopts='' \
  --basetemp=NEW_PRIVATE_FIXTURE_DIR test_accounting.py test_crosswalk.py
```

Initial failures remain in `pytest-v1.log`, `executed-producer-v1/`, and `initial-run-limitations.json`; they involved the new helper's native method spelling and an obsolete positive-fixture preparation command. Later Ruff import-order failures and all subsequent runs are preserved. The initial run used pytest's system temporary directory; subsequent fixtures use durable packet-local directories. No original evidence or worker files were restored, deleted or overwritten.
