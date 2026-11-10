# Reviewed campaign stable-ID adoption

Issue [#1303](https://github.com/CultureBotAI/MediaIngredientMech/issues/1303)
adds a bounded administrative transition for an already constructed legacy
campaign. It does not ingest a source name as a concept, approve an ontology
mapping or role, promote SSSOM, or authorize a KG rebuild. The original legacy
checkout is read-only. The maintained stable-ID registry, schema serializer,
aggregate/export producers, Claw write planner and write lease remain the native
implementations.

## Inputs and scientific boundary

The JSON request uses capability `reviewed-campaign-stable-id-adoption-v1` and
schema version `1`. It names the exact target Git baseline, the append-only
history base, explicit UTC timestamp, selected Claw checkout, complete target
owner inventory and both aggregate/ledger inputs, original migration receipt,
and every existing permanent-ID-to-current-legacy-owner join.

`legacy` names a disjoint read-only root and exact HEAD, original source plan,
completed application receipt and complete original case ledger. Every reference
has `path` and `sha256`. The case ledger must equal the plan's authentic
`full-case-ledger` binding. The complete original baseline owner inventory is
checked against actual Git blobs, including unchanged owners. The original
source-only acceptance, application records, beforeimages, current afterimages
and original plan operations must agree. This is a bounded adoption check, not
a replacement claim for the earlier full native source-application replay.

`origin_accounting` and `origin_proof` pin copied, immutable original crosswalk
and native preparation-proof artifacts in the target root. Their original
provenance remains explicit: the preparation proof conveys no scientific or
application approval. Original worker proposal and decision cores come from the
plan bindings. Every original origin must remain accounted for, including the
nonselected deferred and retired origins. Current applied origins must join the
completed original operation/payload exactly. Source cases, occurrences,
alternatives, retirement explanations and evidence remain in the context; the
selected adoption owners never replace these denominators.

Every original create operation has one explicit decision. An unassessed request
uses null `disposition`, review references, selection fields and unassessed
residual `identity_holds` / `other_holds`. The exact original
`eligibility_intake` reference binds every candidate object, including all literal
`known_conditions_and_holds`, source-case scope, comparisons and earlier review
scopes. These literals are not automatically classified as prohibitive holds.
An empty residual list is a review conclusion, never an intake default (#1317).
`inspect` performs no allocation or scientific review. It returns complete
current owner/source contexts and pre-ID target digests suitable for native
`record_review` inputs. Save those exact context and payload objects, then pin
their actual bytes in `context` and `payloads`.

The digest covers the owner, source context, original origins, current
MAPPING_SEMANTICS policy and complete original eligibility/hold evidence.
It deliberately excludes disposition, concept grouping, selected group owner,
an existing-ID choice and residual hold classifications. An author can state those conclusions without changing
the question being reviewed. They must occur explicitly in both native
primary and separate skeptical identity assessments:

- `CREATE_DISTINCT_CONCEPT`: `concept_key` and `concept_owner_operation` select
  one exact reviewed owner for a group. Each member's own assessment must agree.
- `BIND_EXISTING_CONCEPT_ONLY`: `concept_existing_mim_id` names the reviewed
  existing concept; the proposal is retained in accounting and no owner is added.
- `WITHHOLD_IDENTITY`: the proposal remains captured and accounted for, without
  selecting an owner or allocating an ID.

Both reviews bind the exact complete context, payload, eligibility-intake and
MAPPING_SEMANTICS files, target digest,
source evidence and explicit `concept_scope=complete_source_and_duplicate_boundary`.
Native matching Markdown/YAML, current source hashes, captured primary evidence,
completed target scope, separate reviewer identities, required target checks and
unresolved findings are checked. Both assessments explicitly state
`residual_identity_holds` and `residual_other_holds` as JSON-encoded native
dimension values. Positive CREATE/BIND requires an explicitly reviewed empty
identity-hold list. Other-scope classification can remain null; no role review
or role approval is inferred. Unknown original evidence remains in the question. Global checks explicitly enumerate their native
targets. Unknown/unassessed dispositions cannot prepare. Ontology mapping status,
shared external IDs, aliases, role support and prior copied report metadata are
not substitutes for these identity decisions. An identified UNMAPPED material
can be eligible while its ontology, role and export holds remain unchanged.

Successful native review-pair parsing is reused only within one loaded context
(#1347), bound to the exact captured pair, schema, producer and runtime. Cached
values are immutable serialized reports; each use receives a separate object.
Every target's scientific, source-provenance and current-input checks still run.
Nothing persists across loads, and failures never populate the cache. This
avoids repeated full parsing of shared reports without claiming a measured
speedup or changing lease, operational-fit or publication requirements.

## Prepare, apply and verification

Use the additive `adoption-inspect`, `adoption-prepare`, `adoption-apply` and
`adoption-verify` recipes. Paths belong to the selected isolated checkout;
preparation and recovery directories must be fresh children of its `.temp`.
No traversal, symlink, hardlink, occupied output or input substitution is accepted.
Set `CLAW_SRC` to the intended native Claw checkout for development tests; the
request itself pins its explicit Claw root and captures its revision/source bytes.

Preparation invokes the actual pure allocator only after all decisions pass.
It retains authenticated existing IDs, appends administrative history while
preserving original scientific and mint history, stages the complete selected
corpus through the native closed-schema serializer, regenerates both aggregates,
and exercises the native exporter with a guarded `record_sink`. The default
exporter remains unchanged. The callback receives each exact native filename
and fully restored record; it performs no native mkdir/unlink/save operation.
This allows validation/serialization in memory followed by guarded exclusive
private staging. Empty categories produce a closed-schema empty collection.
Both ledgers are staged together; the mint prefix is immutable and lifecycle
bytes remain identical. Claw validates the complete planned set in dry-run mode.

The prepared manifest is `PREPARED_CANDIDATE_ONLY`. It contains exact input,
producer, runtime, Git and Claw provenance, complete before/after inventories,
all decisions/source cases, output hashes, moves and native dry-run evidence.
A separate completed independent native technical review must accept these exact
manifest bytes with `adoption_action=apply_exact_prepared_set`. It cannot supply
missing scientific eligibility.

`adoption-apply` is dry-run by default. Explicit `--apply` rechecks the prepared
set, verifies the operational budget, takes the explicitly reviewed native write
lease, rechecks currentness and reserves the
receipt, every beforeimage and each recovery directory before managed writes.
Owners, explicit relocations, both aggregates and the append-only mint ledger
are published in recorded phases. Every transition rechecks source/target
currentness, producer bytes, accepted HEAD/index, receipt ownership and lease.
The native guarded retirement preserves the original inode in recovery.

This is a recoverable sequence, not an atomic multi-file transaction. A failure
records completed phases plus observed postimages and errors with
`recovery_required=true`. No rollback, deletion or automatic partial resume is attempted. An exact completed
rerun only verifies the existing result and returns unchanged.
Do not call Claw's `recover()` an automatic rollback. Preserve the failed receipt
and resolve its exact observed state before considering another operation.

`adoption-verify` rereads the completed receipt, original archived beforeimages,
accepted manifest, review and actual current endpoint. It verifies the exact
administrative transformation and phase log, including after an ordinary commit.
It grants no science/publication approval. Full data QC, generated products,
consumer acceptance, independent final-head review and the user's publication
workflow remain separate required gates. The historic identity-projection cohort
and its scientific proof are not extended by this operator.

## Implementation evidence

The producer uses the captured-module approach from #1305/#1195: exact native
source bytes are compiled privately, selected and executing bytes must agree,
and lock/runtime/revision provenance is explicit. Already imported public
modules are neither reloaded nor trusted as the selected producer.
The guarded filesystem helper and its recovery-directory repair are tracked in
[#1314](https://github.com/CultureBotAI/MediaIngredientMech/issues/1314).
Traversal rejection for preparation and receipt paths is tracked in
[#1315](https://github.com/CultureBotAI/MediaIngredientMech/issues/1315).
The synthetic tests are code-contract evidence only. They neither constitute
campaign eligibility decisions nor mint any actual campaign identifier.

The unclassified-intake admission defect and residual-conclusion correction are
tracked in [#1317](https://github.com/CultureBotAI/MediaIngredientMech/issues/1317).


## Operational fit and native lease (#1321)

`adoption-prepare REQUEST STAGE OPERATIONAL_POLICY` requires a separate JSON
policy file. It does not change the scientific request, context or pre-ID digest.
The closed policy has four explicit finite numeric fields:

| Field | Contract |
|---|---|
| `lease_seconds` | Positive duration explicitly offered for technical review; never increased automatically. |
| `evidence_max_age_seconds` | Positive maximum age measured from the start of the profiling scans. |
| `safety_factor` | Explicit factor greater than one applied to measured/estimated work. |
| `additional_overhead_seconds` | Positive explicit allowance for unmeasured publication, fsync, scheduling and final-validation costs. |

No actual campaign values or scheduling decision are selected by this code or
its synthetic tests. Long forecasts can remain operational blockers. The native
resource is `mediaingredientmech`; its lease also conflicts with Claw's `global`
resource. The effective namespace is resolved by the selected native Claw code
from `OPENCLAW_WORKSPACE` / `OPENCLAW_ORCHESTRATION_ROOT`, then recorded with the
resource and lock directory. The operator never chooses a private namespace to
avoid contention. Tests use their own explicit synthetic namespace.

The manifest's `operational_budget` binds the exact policy bytes, namespace,
complete prepared output/input context, native timing receipt, measured startup
work, future growth estimate and exact phase count. For N owner outputs, U
changed outputs at existing paths, V new installation paths and R retirements,
the successful full-recheck count is `N + 8 + 4U + 2V + 2R`. Unchanged owner
outputs still retain their full phase-entry check.

Profiling uses native exclusive receipt reservation and authentic copies of all
current beforeimages in a fresh `.temp/adoption-fit-...` directory. It measures
two complete current-state guards, including real reserved handles, backup,
staged and context bytes, all source/target inventories and evidence, producer
bytes, and Git checks. It acquires no lease and writes no maintained owner.
Measurements retain exact input hashes and state their scope. They do not label
current target bytes as the future endpoint. The forecast scales the measured
maximum by a conservative per-file `max(before, after)` plus-created-file
byte envelope and peak file count (so later shrinkage cannot cancel earlier
growth), the exact callback count and the explicit
safety factor, and includes measured startup/backup time plus explicit overhead.
This is a forecast, not a completion guarantee or a measured whole-batch runtime.
Prepare's own full duration is outside the apply lease and remains separate.

The independent native technical assessment accepting the exact manifest must
state all of these dimensions in the same supported prepared-set assessment:

- `adoption_action=apply_exact_prepared_set`;
- `operational_budget_sha256`: canonical-JSON digest of the complete budget;
- `lease_seconds`: exact string representation of the policy duration;
- `lease_namespace_sha256`: canonical-JSON digest of the namespace object;
- `lease_scheduling=mediaingredientmech_and_global_conflict_reviewed`.

Immediately before enabled apply, the operator checks policy, phase counts,
closure and age, then performs a **fresh** full recovery rehearsal after loading
the entire technical acceptance input closure. This uses a distinct diagnostic
directory, preserving the application's requested receipt path if a native lease
is busy. The fresh observed costs must also fit the same accepted duration. Age
and namespace are rechecked before acquisition. Failed fit evidence is retained;
no silent overwrite, longer timeout, lease renewal or partial retry is attempted.
An explicit duration is passed to native `LockManager.lock` only after fit passes.

Every original currentness/alias/reservation/identity check remains active.
Lease ownership is checked before **and after** each expensive full scan. The
initial token must match this manager's native acquired-token record under its
lease guard, rather than another owner observed on disk. The acquired aware
deadline cannot change or extend; native UTC must remain before
it, and monotonic elapsed time must remain within the reviewed duration. Expiry
during a scan therefore refuses the following guarded publication. This does
not claim a filesystem-wide atomic transaction or eliminate arbitrary process
suspension between individual system calls. Partial failures retain their native
recovery evidence; no automatic rollback or retry is introduced.

The completed application cites the fresh fit receipt and exact accepted budget.
Historical completion verification rechecks those contents without treating an
old, successfully used measurement as a new permission to apply. A new apply
requires fresh evidence again. The code and tests grant no actual campaign
concept eligibility, duration selection, scheduling authority or publication.
