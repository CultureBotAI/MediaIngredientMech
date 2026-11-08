# Structural worker outcome contract — 2026-11-07

This private contract implements the accounting portion of `../WORKER-CONTRACT.md`.
It does not supersede repository semantics, perform scientific review, approve
hold removal, or replace independent review. No real decisions are supplied here.
The auditor is `audit_worker_outcomes_v1.py`; synthetic controls are in
`test_audit_worker_outcomes_v1.py`.

Inputs are explicit and read-only. Evidence captures must already exist under one
of two declared roots: `artifact` (the worker evidence directory) or `source`
(the frozen queue directory). A capture is an object with `root`, a normalized
relative POSIX `path`, and lowercase `sha256`. Symlinks, traversal, missing files,
duplicate JSON object keys, and differing hashes fail. The output receipt must
be a new file inside the worker artifact root.

## Decisions

`decisions.json` is an object with:

- `schema_version`: `1`.
- `worker_slot`: the integer from the exact shard.
- `shard_sha256`: SHA256 of the entire exact shard file.
- `phase`: `shard`, or `canary` only with the explicit CLI `--canary-case ID`.
- `decisions`: a list of decision objects, exactly once per assigned case. The
  explicit canary scope requires exactly that one assigned case; it reports the
  other shard cases as still outside the canary scope, never completed.

Every decision has:

- `case_id`: unchanged shard case ID.
- `case_input_sha256`: SHA256 of the complete original case object serialized
  with `json.dumps(case, sort_keys=True, separators=(",", ":"),
  ensure_ascii=False, allow_nan=False).encode("utf-8")`, without a newline. The
  auditor exposes this exact function as `case_digest`.
- `source`: an object containing exactly the original `source`,
  `source_case_id`, `source_label`, and `raw_source_label`. Blank labels remain
  blank; proposed interpretations belong in reasoning/proposals, not here.
- `occurrence_ids`: every original `occurrences[].occurrence_id`, once. For KG
  cases this is `[]`: their frozen case does not expose per-recipe occurrence IDs.
  The complete case digest binds the KG raw record, original occurrence-count
  definition, source IDs, and every embedded downstream hold. An empty list
  does not assert that KG has no observations. Workers must still review the
  complete source contexts in the queue and cited source audit.
- `disposition`: one of `existing_identity_or_alias`,
  `new_distinct_ingredient_proposal`, `supplied_form_correction`,
  `broad_parent_relation_only`, `stock_product_mixture_context`,
  `malformed_or_nonchemical_token`, or `unresolved`.
- `reasoning` and `applicability`: nonempty scientific reasoning and an explicit
  explanation of how the evidence applies to this exact source case.
- `evidence_ids`: nonempty references to captured evidence below.
- `proposal_ids`: references to proposals below, or `[]`.
- `no_change_reason`: a nonempty reason when no proposal exists; otherwise null.
- `missing_requirement`: a precise, case-specific next requirement for
  `unresolved`; null or text for other dispositions. The checker can establish
  presence, not whether a requirement is scientifically precise or sufficient.
- `owner_records`: `[]` if none is identified; otherwise objects containing
  `path` and `sha256` for actual direct-child
  `data/ingredients/{mapped,unmapped}/*.yaml` records. The auditor then requires
  `--mim-root` and verifies actual current bytes. Do not invent an owner to make a
  source-only case fit native record-review tooling.
- `issue_refs`: `[]` or exact GitHub issue URLs, optionally with a comment anchor.
- `independent_review`: an object with `status` (`pending`, `findings_open`, or
  `complete`) and `evidence_ids`. A nonpending state requires an actual capture
  of kind `independent_review`. The auditor does not authenticate authorship or
  determine reviewer independence or adequacy.

## Evidence

`evidence.json` has `schema_version: 1` and an `evidence` list. Each entry has a
unique `evidence_id`, a `capture` object, nonempty `locator` and
`supports_or_contradicts`, and `kind`: `primary_source`, `source_snapshot`,
`ontology`, `native_record_review`, `independent_review`, `unsuccessful_search`,
or `local_validation`. Include `url` (HTTP(S), or null for local-only evidence).
URL-bearing evidence includes truthful `accessed_at`; primary-source/ontology
evidence requires a URL. Reused captures must retain their true provenance;
never invent a retrieval date. Optional `case_ids` may claim only cases within
the explicit audit scope. Shared captures may include broader source context;
that does not claim those cases were reviewed.

The checker validates file and reference integrity. It does not treat a URL,
file hash, `kind`, or nonempty sentence as scientific substantiation. The worker
contract's primary-source applicability and independent review remain required.

## Proposals

`proposals.json` has `schema_version: 1` and a `proposals` list, which may be empty.
Each proposal has a unique `proposal_id`, nonempty in-scope `case_ids`,
`description`, `evidence_ids`, an intended direct-child `owner_path`, `kind`
(`edit_existing_owner` or `new_owner`), and an `after_capture` referring to the
exact proposed owner payload. `before_sha256` is null for a proposed new owner;
for an existing owner it must match verified `owner_records` bytes. Every case
reference and proposal reference must have the corresponding backlink.

This file proposes bytes only; it never authorizes their application. Identity,
form, predicate, complete published payload, curation history, guarded-writer
and native record-review obligations remain the coordinator's integration work.
Any additional explanatory fields are retained by the worker, but they do not
substitute for these required fields or create scientific authority.

## Invocation

Run with the maintained offline Python environment, substituting real paths:

```text
python audit_worker_outcomes_v1.py \
  --shard /absolute/frozen/queue/shards/shard-01.json \
  --decisions /absolute/worker/artifacts/decisions.json \
  --evidence /absolute/worker/artifacts/evidence.json \
  --proposals /absolute/worker/artifacts/proposals.json \
  --artifact-root /absolute/worker/artifacts \
  --source-root /absolute/frozen/queue \
  --output /absolute/worker/artifacts/structural-audit-new.json \
  --canary-case EXACT_ASSIGNED_CASE_ID
```

Omit `--canary-case` for the complete shard, and add `--mim-root` whenever owner
references are present. A structural PASS explicitly reports
`scientific_adequacy_or_approval_established: false`, review statuses, accounted
case IDs/counts, unaccounted canary remainder, and all input hashes. It is an
independent-review aid, not a generic-holds generator or completion shortcut.
