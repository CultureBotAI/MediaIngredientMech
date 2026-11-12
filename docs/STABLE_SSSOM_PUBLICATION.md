# Guarded stable SSSOM publication

Issue #1335 adds a canonical **candidate** installation step after native stable
ID adoption. It does not approve the whole table for consumers. The ordinary
current whole-row SSSOM review and the separate source-binding review still
determine supported and withheld release products. A concept's CREATE/BIND
decision does not approve its external mappings, roles, components, or subclass
relationships.

Use an isolated checkout, the maintained Python 3.13 environment and the actual
reviewed Claw producer. No dependency, workflow, lease duration, or threshold is
selected implicitly. Keep every generation, prepared set, report pair, fit and
application receipt in durable storage under the checkout. Never reuse an old
output directory, overwrite a failed receipt, or copy the TSV alone.

## Generation and inspection

First complete and verify native `adoption-*`. Then run:

```bash
just stable-sssom-generate /absolute/claw /absolute/read-only/kg-microbe \
  .temp/adoption/prepared .temp/adoption/applied/application.json \
  .temp/publication/generation
```

This invokes Claw's actual stable CLI, with validation enabled and legacy stamp
replay disabled. It records the actual interpreter runtime, command, selected
roots, revisions, output hashes and stdout/stderr. The original diagnostic TSV,
suppression sidecar and generation manifest remain together and immutable.
Generation failure retains its diagnostic files and `FAILED.json`; no canonical
files are changed. Ontology label lookup follows the native producer's ordinary
configuration; this command grants no provider expenditure authorization.

Generation and every subsequent load also replay the exact native producer's
pure transformations in a fresh child from the captured input bytes and recorded
label-resolution map (#1339). The replay compares every byte of the TSV,
suppression sidecar and manifest, including complete present/absent source
membership, registry compatibility and owner accounting. Rehashing edited output
or dropping an optional input cannot make it generated output. Replay calls no
ontology provider and does not treat recorded labels as new ontology verification.
It is a deterministic source/input proof, not cryptographic runtime attestation;
current scientific review of evidence and labels remains mandatory. Native replay
warnings go to stderr rather than the JSON transport (#1342); the original
invocation stdout/stderr remain captured inputs. A diagnostic row with an empty
date can therefore retain the native Rule F warning without a transport error.
The later strict publication validator still refuses that undated row.

A request is a closed JSON object:

```json
{
  "schema_version": 1,
  "capability": "reviewed-stable-sssom-publication-v1",
  "head": "ACTUAL_SELECTED_COMMIT",
  "generation": {"path": ".temp/publication/generation/receipt.json", "sha256": "ACTUAL_SHA256"},
  "selection": null,
  "reviews": [],
  "review_inputs": {},
  "historical_reviews": [
    {
      "root": "/absolute/frozen-original-review-checkout",
      "head": "ACTUAL_HISTORICAL_CHECKOUT_HEAD",
      "review": {"path": "reviews/structured/ORIGINAL/review.yaml", "sha256": "ACTUAL_SHA256"},
      "markdown_sha256": "ACTUAL_SHA256"
    }
  ],
  "operational_policy": {"path": ".temp/publication/policy.json", "sha256": "ACTUAL_SHA256"}
}
```

The operational policy has the same four explicit fields as native adoption:
`lease_seconds`, `evidence_max_age_seconds`, `safety_factor`, and
`additional_overhead_seconds`. This operator reuses the native lease namespace,
global conflict, forecast model and deadline checks. It does not renew leases or
increase an insufficient budget automatically.

`just stable-sssom-inspect REQUEST` returns the complete unassessed selection.
It covers all old rows and all generated rows, their exact full cell payloads,
the current owners, and old/generated/proposed/retired suppression payloads.
Owner lookup uses the current permanent-ID registry and explicit aliases, never
filenames. Unknown or ambiguous historical aliases stop the operation.

For matching stable subject/predicate/object triples, the proposed row retains
every prior source token and the original comment, then adds current generated
provenance. Original validation stamps stay in history and are never replayed
as approval. Every old row and suppression payload is preserved in publication
provenance, including rows that no longer occur in the generator's candidate.
An old suppression that the new table republishes is a failure requiring a
source/generator correction; it is not silently discarded.

## Explicit diagnostic compatibility-retirement proposal (Claw #1189)

A historical canonical registry row may compete with the current owner's
curated registry namespace. The default generator still refuses that conflict.
Do not edit the canonical table to get generation through. A separately authored,
checksum-bound `stable-registry-retirement-proposal-v1` may identify exact old
rows to omit from the **diagnostic compatibility view**. It cannot remove a
current curated primary, invent an identity, hide an unknown or ambiguous owner,
or grant scientific, canonical, or release approval.

Use the native module's additive options when this reviewed proposal is needed:

```bash
python -m mediaingredientmech.curate.stable_sssom_publication generate \
  --root /absolute/mim --claw-root /absolute/reviewed-claw \
  --kg-root /absolute/read-only/kg --adoption-stage .temp/adoption/prepared \
  --adoption-receipt .temp/adoption/applied/application.json \
  --stage .temp/publication/fresh-generation \
  --registry-retirement-proposal .temp/retirement/proposal.json \
  --registry-retirement-proposal-sha256 ACTUAL_PROPOSAL_SHA256
```

Both proposal arguments are mandatory together. Use the recorded native runtime
spelling, not an interchangeable interpreter alias. The closed proposal contains
`schema_version: 1`, `capability: stable-registry-retirement-proposal-v1`,
`scope: diagnostic_candidate_only`, a nonempty `author`, and
`scientific_approval: false`. It binds `canonical: {path, sha256}` to the complete
original `mappings/ingredient_mappings.sssom.tsv`, nonempty `evidence_inputs`
(relative path to SHA256), and nonempty `entries`. Each entry contains:

- `row_position`: one-based data-row position, excluding comments and header;
- `row`: every exact original column and cell, including comments, source tokens
  and validation history;
- `owner: {path, sha256, mim_id}`: the actual current distinct owner;
- `reason`: the author's nonempty rationale;
- `evidence`: a nonempty list of the declared evidence-input paths.

The selected row must be an exact local-registry compatibility row in the
opposing namespace from that owner's current curated primary. All unselected
rows and legitimate same-namespace aliases remain inputs. The original full
canonical bytes, proposal, owner and every evidence input are captured and
rechecked, then replayed using the same native producer. The revised Claw
manifest records the complete proposal or explicit null when absent. Historical
c1 generation receipts remain replayable with their original manifest format.

A valid proposal is an input to diagnosis, **not a vote**. Obtain genuine current
primary and independent skeptical assessment before using it in a reviewed
campaign. After generation the omitted row remains an unassessed historical row
in the ordinary complete publication selection. It still requires
`REMOVE_WITH_HISTORY`, the complete primary/skeptical native publication reviews,
and independent exact-prepared technical acceptance. A rehashed proposal or a
successful generation never supplies those decisions. The ordinary supported/
withheld external partition and source-binding reviews remain separate.

## Scientific selection and independent acceptance

Save the inspection result as an immutable selection file. Set only each row's
`disposition` and nonempty `reason`: `INSTALL_SUPPORTED` or `INSTALL_WITHHOLD`
for candidate rows, `REMOVE_WITH_HISTORY` for old rows absent from the candidate.
These are explicit installation decisions, not the ordinary release partition.
Any edit to the derived row, provenance, owner or suppression payload is refused,
even when its checksum is updated and reports are regenerated.

The nonempty `historical_reviews` list names genuine original or independently
frozen historical Git checkouts. The operator parses each unchanged native
YAML/Markdown pair, verifies original source provenance and every direct input,
and includes the full report, assessments and holds in the derived selection.
The historical root must be physically distinct from the publication root,
including case aliases on a case-insensitive filesystem (#1337). Its pinned HEAD and
input bytes remain read-only and current throughout the operation. An archived
acquisition is labeled historical; it is never re-saved as a stable-row review.

Obtain native completed primary and separate skeptical reports, saved through
`scripts/record_review.py`, with one exact `snapshot_row` target per `entry_id`
and a `suppressions` target, plus one target for each `history-NNN` entry. Each target's path is the selection file; its
semantic digest is `sha256-canonical-json-v1` of the complete corresponding
payload, described as `Complete stable publication selection`. Assessments
must state `publication_action` and
`publication_scope: canonical_installation_not_release_approval`. History targets
must explicitly state `PRESERVE_HISTORICAL_OBLIGATIONS`; this assesses preservation
of the complete prior evidence, not renewed approval of its assertions. They require
current captured evidence and completed checks, not a hash-only sign-off.
Reports bind the complete owner inventory, stable registry/lifecycle/contract,
generation receipt, actual adoption receipt, selection and mapping semantics.
Historic mapping decisions must be considered as historic evidence, never
restamped or relabeled as current scientific approval.

Set `selection` to its path/hash, `reviews` to the two report YAML path/hash
references, and `review_inputs` to the exact YAML and Markdown hashes. Then:

```bash
just stable-sssom-prepare REQUEST .temp/publication/prepared
```

Preparation runs native strict `qc-sssom` on the staged table against current
owners, measures real full guards and backup work, and refuses a forecast that
does not fit the explicit policy. It writes four staged outputs: canonical TSV,
canonical suppressions, the original generation manifest, and complete
publication provenance. Nothing maintained is installed yet.

A third, independent technical reviewer accepts the exact prepared manifest
using a native report with `scientific_review: false`. Its target selector is
`prepared`; its digest is `sha256` of exact manifest bytes, described as
`Exact prepared manifest bytes`. A supported assessment must bind:

- `publication_action: apply_exact_prepared_set`
- `operational_budget_sha256`: canonical-JSON digest of `operational_budget`
- `lease_seconds`: the exact reviewed duration as text
- `lease_namespace_sha256`: canonical-JSON digest of the namespace
- `lease_scheduling: mediaingredientmech_and_global_conflict_reviewed`

An acceptance JSON envelope names `manifest_sha256`, the native `review`
path/hash, and `markdown_sha256`. It is insufficient to provide the manifest
hash without that current, completed, independent native report.

## Installation and verification

```bash
just stable-sssom-apply .temp/publication/prepared ACCEPTANCE .temp/publication/applied
just stable-sssom-apply .temp/publication/prepared ACCEPTANCE .temp/publication/applied --apply
just stable-sssom-verify .temp/publication/prepared .temp/publication/applied/application.json
```

The first command is a dry-run. Explicit application reserves all recovery
outputs before any maintained write, archives exact existing beforeimages and
records absent outputs explicitly. It installs through native alias-resistant
guarded writers under the real `mediaingredientmech` lease. The sequence is
recoverable, not a multi-file atomic transaction. A failure records observed
partial outputs and `recovery_required: true`; it never claims success or
automatically rolls back. A lease expiry/loss or post-write input change stops
the operation and preserves evidence. The exact KG input revision is rechecked
after the expensive terminal guards as well as at entry (#1338). A completed rerun must verify the actual
current endpoint and the original acceptance.

The four maintained outputs are:

- `mappings/ingredient_mappings.sssom.tsv`
- `mappings/suppressed_aliases.tsv`
- `mappings/stable_sssom_generation.json`
- `mappings/stable_sssom_publication.json`

After installation, run repository QC and the separately reviewed ordinary
whole-row and source-binding exports. Do not use diagnostic paths to bypass the
ordinary canonical-path route. No KG rebuild, Git merge, scientific status
promotion, owner merge, or ontology-parent/subclass inference occurs here.
