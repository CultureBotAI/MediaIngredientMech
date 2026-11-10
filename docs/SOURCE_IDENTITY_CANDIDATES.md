# Reviewed source identity candidates

Issue [#1299](https://github.com/CultureBotAI/MediaIngredientMech/issues/1299)
adds a separate product on top of the permanent-ID contract. It does not modify
the canonical MIM-to-external table, mint IDs, change records, waive scientific
holds, authorize publication or invoke a KG rebuild.

The native entry point is `mediaingredientmech.export.source_bindings`. Run:

```bash
just inspect-source-bindings path/to/source-review.json
just export-source-bindings path/to/source-review.json output/new-unique-candidate
just qc-source-bindings path/to/source-review.json output/new-unique-candidate
```

Inspection returns exact native targets, complete payloads and input hashes.
It grants no approval. Export requires two actually authored native scientific
reviews of each target. The same module supports `--root`, `--review`,
`--inspect`, `--output` and `--validate-only` for explicit isolated roots.

## Input contract

The closed top-level JSON object has these fields (version 1):

| Field | Value |
| --- | --- |
| `schema_version` | Integer `1` |
| `capability` | `reviewed-source-bindings-v1` |
| `source` | Table paths/hashes, column selectors and explicit source CURIE prefixes, below |
| `record_inputs` | Exact repository-relative path → SHA256 for **all** current mapped and unmapped ingredient YAML records |
| `ledger_inputs` | Exact paths/hashes for `data/ids/mim_id_registry.tsv` and `data/ids/mim_id_lifecycle.tsv` |
| `inputs` | Exact paths/hashes for both authoritative native `review.yaml` / derived `review.md` pairs and any additional captured evidence |
| `external_review` | `{ "path": "…", "sha256": "…" }` identifying an ordinary current complete review of this root's `mappings/ingredient_mappings.sssom.tsv` |
| `cases` | One case per source row, in original order; no omissions or duplicate positions |

`source` has exactly `nodes`, `nodes_sha256`, `occurrences`,
`occurrences_sha256`, `id_column`, `label_column`, `occurrence_id_column`,
and `curie_map`. Both inputs are UTF-8 TSVs with unique header names. All
columns and physical row positions are retained. The nodes file must have one
unique original CURIE per row; the occurrence file must join only to those
IDs. Zero occurrences are allowed and explicitly represented. Prefix URIs
must be supplied, never guessed. Reserved MIM, MIM.ingredient, SKOS and SEMAPV
expansions cannot be overridden. These declarations are part of the reviewed
payload, so changing a namespace or column selector withdraws prior support.

This is complete accounting of the **declared files**, not proof that the
upstream provider supplied its entire database. Upstream extraction provenance
and selection boundaries belong in the captured evidence and review scope.
Preserve the original files and scope; do not make a passing cohort by dropping
unresolved rows. Multiple preparations or alternatives sharing a raw ID are
all reviewed together. If they cannot share one identity, WITHHOLD the source
entity. This version cannot split it into invented occurrence subjects.

Each case has exactly:

```json
{
  "source_position": 1,
  "owner_record": "data/ingredients/unmapped/Existing_material.yaml",
  "holds": [],
  "primary": {
    "path": "reviews/structured/TIMESTAMP-primary/review.yaml",
    "target_id": "source-1",
    "assessment_id": "identity-1"
  },
  "skeptic": {
    "path": "reviews/structured/TIMESTAMP-skeptic/review.yaml",
    "target_id": "source-1",
    "assessment_id": "identity-1"
  }
}
```

An unresolved case can have `owner_record: null`. For inspection only, the
two report references can be null; author and pin the actual reports before
export. `holds` is an explicit list of unresolved scientific obligations and
is itself reviewed. Existing holds cannot be removed merely to get a pass.
No owner is selected by label, filename, external ID or legacy alias. The
record's existing registered `mim_id` identifies the proposed owner. Retired,
merged, split or deprecated IDs do not silently redirect this assertion.

## Native scientific admission

Use `scripts/record_review.py inspect`, author the assessments, then its native
`validate` and `save` workflow. Use the exact targets and input paths returned
by `inspect-source-bindings`; add captured primary evidence to the inspection.
The exporter validates the native schema, authoritative YAML/Markdown pair,
retained Git provenance, current input hashes and target/assessment links.
It does not generate a review or turn a checksum into scientific approval.

Each native target is a `snapshot_row` in the original nodes TSV. Its selector
is the compact sorted JSON of `source_position` and `source_id`. Its semantic
digest uses `mim-source-identity-sha256-v1` and the full payload from inspection:
source declarations and row, every occurrence and position, owner path/hash,
permanent ID, actual mapping status and holds. Keep the exact digest description
returned by inspection. The target owner path is the proposed record, or the
source table for an ownerless withheld case.

Each referenced assessment covers exactly this target, uses `area: identity`,
and includes these native `dimensions` (with descriptions/evidence IDs):

- `source_identity_scope`: `all_source_occurrences`.
- `source_identity_disposition`: `same_material` or `withhold`.

Both reports must be completed scientific reviews; the skeptical reviewer must
declare `independence: independent` with a nonblank native independence basis,
and have a different reviewer identity and report path. These are accountable
reviewer attestations, not cryptographic proof of who authored the science.

A positive identity requires both `same_material` decisions, supported native
assessments, hash-bound supporting primary-source/database/authority evidence,
and no open/deferred finding on that target. The reports must bind current
nodes, occurrences, owner and both ID ledgers. All other declared native inputs
must also remain current. A report's overall `needs_curation` verdict can
coexist with a supported individual target; this does not clear another target's
holds. `blocked`/unassessed reports cannot approve a target. Any source with a
remaining hold, no owner, or an AMBIGUOUS/REJECTED owner cannot be supported.
An UNMAPPED owner can support source identity only: no external mapping or
MAPPED status is manufactured.

## Outputs and consumer contract

`manifest.json` declares `REVIEWED_CANDIDATE_ONLY`, `production_authorized:
false`, the required capability, complete input hashes, exact product hashes
and separate source/occurrence/external counts. The products are:

- `source-bindings.sssom.tsv`: positively reviewed source-to-MIM identities.
- `withheld-source-bindings.sssom.tsv`: proposed identities with an owner that
  remain WITHHOLD; these are backlog, not approved mappings.
- `source-decisions.json`: **every** source case, including ownerless cases,
  all occurrence payloads, original CURIEs, holds, exact review references,
  complete native assessments, reviewer attestations and dispositions.
- `producer.json`: the generating implementation's captured source/dependency
  bytes, runtime versions, selected-root Git context and original generation
  origin attestation (#1305).
- `external-*`: the ordinary native external review's complete supported and
  withheld SSSOM files, dispositions and manifest, retained byte-for-byte.

Ownerless cases have no SSSOM row because no object identity exists to assert;
`withheld_without_owner` and the full JSON ledger account for every such case.
The two identity SSSOM partitions carry explicit manual-curation justification,
candidate scope, payload digests and native report locators. Validation uses
the maintained SSSOM parser/schema and checks that no identities or rows vanish.

An arbitrary smaller external TSV is refused: the external partition must cover
the supplied root's entire current canonical SSSOM. An isolated candidate root
can be reviewed in its own right; this exporter does not promote it.

Source approval and external approval are independent. Exact, broad, close and
narrow external rows retain their actual predicates and evidence. A supported
source identity can coexist with no external row or withheld external rows.
Conversely, a supported external mapping never rescues an unsupported source
identity. No source row is appended to the canonical external table or admitted
through `identity-projection-v1`.

Consumers must explicitly accept `reviewed-source-bindings-v1` and run
`validate_candidate(root, review_path, output)` against the actual maintained
root and exact review. Hash-checking an output manifest alone is insufficient:
validation reconstructs all products from source and evidence. The helper
`consumer_claims(..., capabilities={...})` returns only supported candidate
source assertions, with MIM graph spelling plus original subject/object CURIEs
and payload digests. It never collapses different MIM concepts that share an
external target and never projects mappings to `subclass_of`.

`MIM:0000001` and `MIM.ingredient:0000001` expand to the identical permanent
ingredient URL. A graph prefix change is a spelling projection only; preserve
original CURIEs. Unsupported capability, stale evidence, substituted outputs,
incomplete accounting, ambiguous aliases and self-loops fail closed.

Output must be a new directory; inputs and symlink aliases cannot be overwritten.
All bytes are staged and validated before the directory is reserved. The
manifest is written last and the final candidate is revalidated. A caught
failure after reservation retains diagnostic bytes and adds `FAILED.json`,
which makes native validation refuse that directory. Abrupt interruption may
leave an incomplete directory. This is not an atomic production publication;
consumers must validate it and recheck current inputs at their own acceptance
boundary. Use a new output path for a retry, retaining failed evidence.

## Executing producer provenance (#1305)

The producer and its bounded MIM dependency closure run in a private module
namespace compiled from captured source bytes. This includes the conditional
historical identity-projection reader, without changing what that reader can
admit. Existing public Python modules are neither reused nor reloaded. In
particular, hashing a dependency's current disk file after an older version was
already cached is insufficient; the regression from #1195 is covered explicitly.
The native structured-review helper also executes the exact captured bytes.

Every selected-root producer file must equal the captured bytes that execute.
The receipt also binds `uv.lock`, `pyproject.toml`, `.python-version`, native
review schema/helper and actual Python/library versions. Generation and
validation check original file identities/bytes, selected bytes, membership and
Git HEAD before/after their work. A changed producer, lock or endpoint invalidates
an old computational candidate; rebuilding never repairs a stale scientific
review or grants an identity decision.

The selected-root Git context describes the exact protected inputs relative to
HEAD. Modified and untracked inputs, including explicitly supplied ignored
files, are `working_tree` observations. Writing the candidate output itself does
not change this protected-input scope. Original generation paths and Git context
are retained as `GENERATION_CONTEXT_ATTESTATION`; they are descriptive original
provenance, not cryptographic proof of authorship. A later validator can execute
identical captured code at another owned location. It verifies the same code,
dependency, runtime and selected-input context while retaining the original
generation origin rather than falsely replacing it with the validator's path.
Consumers should pin the complete candidate manifest at their acceptance
boundary; descriptive origin strings are never read or executed as input paths.

The old filename-based MIM addresses remain historical aliases, not new source
identity approvals. This candidate contract neither rewrites those historical
reviews nor makes a minted record address equivalent to an unreviewed material.
An entirely empty canonical external table is supported when its ordinary native
review accounts for zero rows: independently reviewed source-to-MIM identities
still survive, and nothing fabricates ontology grounding. Real KG consumer
adoption remains a separate candidate-only adapter/release decision.

## Campaign adoption remains separate

This code framework does not migrate or approve the unmatched campaign.
[Issue #1303](https://github.com/CultureBotAI/MediaIngredientMech/issues/1303)
tracks that pending data/provenance adoption after the permanent-ID and export
prerequisites. Reuse authenticated existing IDs across record moves and label
changes. Proposed new records require distinct-concept eligibility and duplicate
boundary review before the existing guarded allocator can mint an ID; a source
name alone is not a new concept. Retain the completed legacy evidence, original
source-case obligations and scientific holds. The fixed historical
`identity-projection-v1` proof is not extended to changed campaign records.
