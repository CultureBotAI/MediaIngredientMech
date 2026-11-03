# Step 7d external mapping promotion operator

`promote_step7d_mapping.py` is a single-batch operator for the owned `step7d`
checkout. It defaults to dry-run and grants no scientific or release approval.
The science author prepared this operator; the final independent review remains
required. The operator has not been applied by its author.

Fixed bindings:

- MIM base: `467aa319a06ef992035f509f66fe251082b44ae1`.
- Isolated Claw producer: `3022b8738dcc9e01c7464a8d5c95aa9be2eef141`.
- Canonical preimage SHA256:
  `62fd37c2ed8ace9b9295618d44e251d11fc35feb711053b66d322e5a7bce14f1`.
- Historical receipt prefix: 24 receipts; this operation creates exactly one
  sequence-25 receipt, `issue901-step7d-reviewed-owner-forms.json`.
- Source groups, in order: `1117-carbonate`, `1117-maltose`, `901`.

## Required sequence

Freeze the source operator before the source transactions. Freeze the explicit
owner plan, including all evidence, before/after hashes and operations. The
source operator bytes are inputs to every source log, so changing that operator
afterward invalidates replay.

Apply each source group with the native guarded source operator and retain its
completed log, backups and native transaction journal. Commit each group as
directed by the approved plan. After source commits, generate and capture the
native candidate with the pinned isolated producer. Generation requires clean
MIM and producer checkpoints. Construct and review the explicit projection
config against that exact candidate and the unchanged canonical preimage.

Run mapping promotion before the separately authorized unified rebuild. At
promotion time, the unified snapshot pair must still equal the base files. The
mapping operator writes only canonical SSSOM and the sequence-25 receipt through
one native guarded transaction. After promotion, the source surfaces and exports
still require the approved synchronization, companion review, unified rebuild,
QC, full suite, independent review and CI workflow; this operator does not
perform those later steps.

## Owner plan and auxiliary reference contract

The owner plan uses the exact contract of `apply_reviewed_owners.py`: nonempty
`owners` keyed by flat mapped YAML paths; `all_owner_sha256`; `base_revision`;
`timestamp`; `evidence_sha256`; `protected_sha256`; and
`scientific_approval_added: false`. Every selected owner occurs in exactly one
of the three groups. All other ingredient files must retain their base bytes.
New primary identifiers cannot case-insensitively collide with another owner
in either the base or current inventory, even if that other owner also changed.

Optional `auxiliary` is a mapping from each of the two allowed relative paths
to an ordered list of stages:

```json
{
  "mappings/culturemech_recipe_membership.tsv": [
    {
      "group": "1117-maltose",
      "before_sha256": "<base hash>",
      "after_sha256": "<first stage hash>",
      "migrations": ["<explicit migration objects>"]
    },
    {
      "group": "901",
      "before_sha256": "<first stage hash>",
      "after_sha256": "<final hash>",
      "migrations": ["<explicit migration objects>"]
    }
  ]
}
```

The other allowed path is `mappings/unified_mapping_rejections.tsv`, with the
same staged hash contract. Each migration binds `owner_path`,
`before_identifier`, `after_identifier` and the exact membership cohort, or
the exact `before_row` and `after_reason` for the rejection ledger. Only the
three transitions allowed by the source operator are admitted: maltose CAS to
NCIT, cerium local identity to CAS, and copper local identity to CAS. Each
migration must belong to the selected owner in that exact group. These varying
auxiliary paths must not also appear in the plan's constant evidence/protected
input maps. Other cells remain unchanged except the source operator's permitted
membership sorting and ledger rationale changes.

The mapping operator reconstructs the entire phase input state, replays every
owner and auxiliary output, and verifies each completed source log, preimage
backup and journal. Reordered phases or unlogged reference edits are rejected.

## Explicit projection config

The config has exactly these top-level fields:

```json
{
  "schema_version": 2,
  "base_revision": "467aa319a06ef992035f509f66fe251082b44ae1",
  "producer_revision": "3022b8738dcc9e01c7464a8d5c95aa9be2eef141",
  "candidate_sha256": "<captured native candidate>",
  "generation_manifest_sha256": "<captured native manifest>",
  "canonical_after_sha256": "<reviewed full projection>",
  "owner_plan_sha256": "<frozen owner plan>",
  "source_operator_sha256": "<frozen source operator>",
  "scientific_approval_added": false,
  "supervisor_binding": null,
  "rows": [],
  "removed": []
}
```

Every selected native candidate row must appear exactly once in `rows`:

```json
{
  "candidate_position": 1,
  "candidate": {"<every SSSOM column>": "<exact native cell>"},
  "output": {"<every SSSOM column>": "<exact reviewed projected cell>"},
  "before_position": 1,
  "insert_after_position": null,
  "output_position": 1,
  "basis": "Specific reviewed evidence and row change"
}
```

All positions are one-based data-row positions, excluding header/comment lines.
Candidate positions refer to the whole native candidate. An existing slot keeps
its old position relative to the remaining old rows. A new slot has
`before_position: null` and must be inserted after that subject's last old row.
Every output position and the final file hash must be declared correctly.

Each removed row is declared as
`{"before_position": 1, "before": {"<complete old row>": "..."}, "basis": "..."}`.
Only an obsolete CAS/local slot absent from the native candidate can be removed,
and only when that subject's complete native output is one exact ontology row.
No unrelated rows can be removed. Removal cannot discard a deferred alias
occurrence. Removed-row provenance remains in the historical canonical preimage
and native mapping-change receipt; it is not reassigned to a different row.

The output must exactly equal `output_from_candidate`: native scientific cells;
existing source tokens plus new native `MIM:` tokens; existing and native comment
texts; old validation stamp only for unchanged object and predicate; and native
aliases plus deferred tokens previously present on that same existing row.
New rows gain no historical stamp or invented provenance. Across the complete
canonical file, all baseline deferred-token occurrences remain unchanged. No
suppression sidecar claim is added. All unrelated row bytes and order stay exact.

## Invocation and verification

Use the native runner and fresh external log paths. With `RUN` and `D` set to
their actual resolved locations, the command shape is:

```sh
python3 "$RUN/run_step7d_mim.py" step7d step7d-mapping-dry-v1 -- \
  python -B "$D/promote_step7d_mapping.py" \
  --bundle "<native generation bundle>" \
  --producer "$RUN/step7c-claw" \
  --plan "$D/owner-plan.json" --plan-sha256 "<plan hash>" \
  --config "<reviewed projection config>" --config-sha256 "<config hash>" \
  --source-log "<completed carbonate log>" \
  --source-log "<completed maltose log>" \
  --source-log "<completed 901 log>" \
  --log "<new external dry-run log>" --dry-run
```

Apply requires an explicit `--apply` and a new unused log path. Inputs, absence
claims, native code at base, producer code/import inventory, captured label
responses and native offline generation replay are checked before publication.
The native maker is executed only inside a temporary tree to construct receipt25
and verify the full historical chain; maintained files are changed only by the
reserved native guarded transaction. Completed publication is verified again.

`promotion_external_controls.py` passed 29 controls under
`step7d-promotion-controls-v5`. It exercises projection and identity-boundary
guards plus real base/prefix pins; it is not a substitute for the full actual
source-journal/generation-bundle dry run. Earlier v1 failed because the synthetic
fixture omitted the native quoted header date; the fixture was corrected and
the failure evidence retained. No maintained test or assertion was edited.

`cas-local-registry-probe.json` records a read-only probe of the pinned native
row builder: the proposed cerium and copper CAS identities preserve their
existing local compound handles and add CAS rows. No namespace is synthesized
by the mapping projection.

`build_promotion_operator.py` and `patch_promotion_aux.py` are construction
provenance, not runnable workflow entrypoints. Do not rerun them over the final
operator. The handoff JSON binds the current executable and control files.
