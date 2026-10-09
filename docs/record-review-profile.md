# MediaIngredientMech Record Review Profile

Passing verdicts require positive evidence-linked assessments of the reviewed
targets. Terminal finding dispositions require those targets to have actually
been reviewed and assessed, with completion other than failed. Every
supersession must preserve all affected targets from the cited prior finding,
including multi-record findings; a narrower observation cannot silently drop
unassessed members or close their issues. Keep their remaining scope explicit.

Follow [Structured Record Reviews](record-reviews.md). Active routes and
local rubrics are enumerated in `conf/record_review.yaml`.

## Routes And Native Rubrics

- `review-yaml-record`: exact ingredient identity and claim review.
- `review-yaml-category`: coherent substance/form cohorts, explicit boundaries,
  evidence for lump/split decisions, and declared sample coverage.
- `review-ingredients`: focused or batch P1-P4 mapping/quality review.
- `review-sssom-output`: published mapping rows, predicates, registry siblings,
  labels, synonym payloads and GAP/ORPHAN/STALE drift.
- `curate-yaml-record`: audit-only review of one resolved ingredient.
- `schema-gap-analysis`: diagnostic schema / instances / process scans;
  delegate interpreted findings to registered `review-yaml-record` or
  `review-yaml-category` and save using that assessment route. Retain
  `audit_axis`, current error counts/denominators, aggregate and individual
  selectors, and writer ownership. Schema/process-only assessments are
  `scientific_review: false`; scans cannot grant scientific or release approval.
  Audit-only work does not apply the skill's proposed fixes or synchronize data.

`MAPPING_SEMANTICS.md` remains the authority for identity and mapping.
One record denotes one distinct substance: hydration, salt, stereochemistry,
purity, supplied form and mixture boundaries survive normalization. A generic
parent is not an exact identity for a specific form. Keep form-specific IDs or
the documented CAS/registry identity and asymmetric parent mapping.
Keep synonym types, mapping quality, source occurrence, roles and evidence
context in assessments and evidence-linked dimensions. Preserve P1-P4 rule IDs
and native severity, with impact-based normalization reasons (normally P1
blocker, P2 major, P3 minor, P4 informational). Native confidence and quality
scores retain their own definitions and scales.

For SSSOM, identify exact rows with stable subject/object/predicate selectors
and hashed TSV input. Retain `predicate_semantics: skos`, NARROW_MATCH to
`skos:broadMatch`, exact identity/registry sibling rules, canonical-or-synonym
labels, and genuine same-substance `other` tokens. A failed slug lookup remains
a reported issue under the native contract, not a newly invented release gate.

## Maintained And Generated Ownership

Record owners are `data/ingredients/{mapped,unmapped}/*.yaml` and their matching
`data/curated/{mapped,unmapped}_ingredients.yaml` entries. Name the actual
maintained owner and exact selector, plus corresponding mapping rows where
relevant. Per-record edits synchronize with `just sync-curated`; aggregate
edits use `just sync-individual` only after protecting unsynced individual
changes. Review alone runs neither mutator.

SSSOM, docs CSV/JSON and `UNIFIED_INGREDIENT_MAPPING.tsv` may expose source
or builder errors. Record generated targets with their YAML owners and the
actual builder (including its repository if external). Do not propose editing
generated Pages as a scientific fix. Hash schema, mapping semantics and source
tables used in the assessment with `inspect --input`.

## Commands And Saving

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
just validate-strict <record-path>
just validate-terms <record-path>
uv run python scripts/reconcile_sssom.py
just qc-sssom
just curie-validate
uv run python scripts/check_sssom_subject_files.py
just validate-products
uv run python scripts/record_review.py validate /tmp/completed-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-review.yaml
just check-record-reviews
just test-record-reviews
```

Select actual checks for the declared scope and record real exit codes.
`qc-sssom` can write the rejected-row diagnostic TSV; it does not apply repairs.
Use session-unique temporary paths. Save new YAML plus derived Markdown only
under `reviews/structured/<timestamp>-<slug>/` and link both.

`uv run python scripts/batch_review.py --limit 10 --dry-run` and
`uv run python scripts/review_ingredient.py "sodium chloride"` are diagnostic
validators, not primary-source scientific review. Batch output retains rule
IDs and diagnostic issue counts; counts of issues are not counts of reviewed
records. A priority filter can hide issues, so it cannot support an unqualified
pass. Save the assessed final content via the shared saver, recording exact
selection/population, failed targets and unavailable checks. Diagnostic-only
reviews use `scientific_review: false`; provider drafts remain unassessed leads.

## Retained Status And Release Gates

`mapping_status: MAPPED` means an ontology mapping exists, not that the record
passed scientific review. Keep `just validate-all`, `just qc-sssom`,
`just qc-roundtrip`, `just qc-flat-coverage`, `just qc-evidence` and
`just audit-writers` when applicable. The content-bound semantic release,
supported KGX and reviewed SSSOM contracts keep their existing assertion
dispositions, source/evidence hashes, negative holds and excluded-claim backlog.
A common review bundle does not replace those native release inputs or clear
their blockers; do not convert its verdict into an APPROVED disposition.
No old review reports, release ledgers or history are migrated.

The shared schema/helper/docs/test are CLAW-owned byte-identical artifacts.
Local profiles, mapping rules and domain assessments remain repository-owned.
