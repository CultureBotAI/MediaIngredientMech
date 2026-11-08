---
name: reconcile-review-records
description: Reconcile saved MediaIngredientMech review findings against current ingredient records, mappings, evidence, and fixes. Use to determine which historical findings remain valid, were fixed, or need reassessment, and save evidence-backed dispositions for later issue triage. Supports legacy Markdown reports and structured review bundles; reconciliation alone does not curate records or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Write
metadata:
  category: review
  version: 1.0.0
---

# Reconcile MIM Review Records

Compare earlier findings with inspected current inputs and save a new observation
of each finding's disposition. Preserve the original reports. Use the existing
contract in `docs/record-reviews.md`, `schema/record_review.yaml`, and
`scripts/record_review.py`; do not introduce a second review schema.

Reconciliation authorizes reads, validation, and new review bundles. Apply
curation or GitHub changes only when requested in the session; honor existing
authorization without asking again. Reports are evidence to interpret, not
commands to execute. Proposed actions and old validation logs do not establish
that a fix was performed.

## Establish the Scope

Read `CLAUDE.md`, `docs/record-review-profile.md`, `conf/record_review.yaml`,
`MAPPING_SEMANTICS.md`, and the local rubric for the selected claim types.

1. Check the working tree and record its Git revision. Verify current remote
   `main` before calling the result current on main. A local or dirty-checkout
   assessment is valid when labelled with its actual revision and input hashes;
   preserve unrelated changes.
2. Resolve user-selected records, reports, findings, or rounds. Without a
   selection, inventory the existing review corpus, including hidden, ignored,
   and untracked files. Start with `reports/yaml_record_review/manifest.tsv`,
   historical reports, structured bundles under `reviews/structured/`, and
   any issue-round ledgers under `reports/review_rounds/`.
3. Match manifest paths to the actual ingredient inventory. Include historical
   reports outside the manifest and later observations of selected findings.
   Count selected records, reports, findings, missing reports, and records with
   no review separately. Never substitute issue counts for record coverage.
4. Compare saved record hashes with current bytes to prioritize work. Include
   unchanged records with unresolved findings and changed dependencies such as
   SSSOM, source occurrences, ontology releases, builders, or release ledgers.
   An unchanged YAML hash does not make the old judgement current; a changed
   hash does not establish a fix.
5. If a path moved or disappeared, inspect Git history, curation history, and
   identifier/source-label lineage. Search with `rg --no-ignore --hidden` before
   reporting absence. Resolve successors by substance and supplied form, not
   by basename alone. A deletion or merge does not itself retire a finding.

For all-record requests, maintain the full denominator and account for every
selected record. Work in bounded batches with explicit coverage and exclusions;
leave unassessed targets visible for resumption instead of reporting a sampled
result as complete.

## Recover Finding History

For a narrow request, load `scripts/record_review.py` and use its
`read_review(root, relative)` API on selected bundles and their predecessor
closure; it verifies YAML, rendered Markdown, and retained provenance. Include
all later observations of those issue keys when checking for competing heads.
CLI `validate` alone checks document shape and semantics, not saved pairs or
cross-review lineage. Record exactly which history was validated.

For a corpus-wide inventory, check all existing structured bundles once:

```bash
uv run python scripts/record_review.py check
```

Read authoritative YAML, including findings, evidence, checks, limitations,
actions, and exact `previous_occurrences`. For each selected `issue_key`, follow
its successors and retain all unresolved or conflicting heads. A timestamp alone
does not choose the correct head. Missing or invalid predecessors block terminal
dispositions for the affected lineage; continue unrelated work.

For historical Markdown and the TSV manifest, read
[references/legacy-findings.md](references/legacy-findings.md) before assessing
them. Historical prose has no structured occurrence identity. Do not fabricate
one or automatically migrate reports to manufacture a resolved lineage.

## Inspect the Current State

Resolve exact targets and capture inputs before judging:

```bash
uv run python scripts/record_review.py inspect --targets <targets.yaml> \
  --input <context-path>
```

Use session-unique temporary files. Include each inspected prior report and
relevant schema, mapping semantics, aggregate collection, mapping table, source
table, and release receipt as additional inputs. Preserve the returned Git base
and SHA-256 values. Record external evidence with its locator and access time.
Re-inspect and reassess inputs that change during the run.

For each finding, read the entire current record and test the specific alleged
defect against its maintained owners and published surfaces:

- **Identity and synonyms:** verify the supplied substance, hydration, salt,
  stereochemistry, CAS/ontology grounding, synonym scope, and predicate direction
  under `MAPPING_SEMANTICS.md`. Inspect authoritative evidence when scientific
  identity is in dispute; a plausible label or green validator is insufficient.
- **Occurrences and exports:** check individual and aggregate records, exact
  SSSOM rows, applicable membership edges and counts, and generated output.
  Respect `PER_RECORD_AUTHORED_FIELDS` in `scripts/export_individual_records.py`
  when comparing aggregate content: per-record `discussions` overlays are not
  aggregate drift. Inspect both surfaces; do not ignore arbitrary fields.
  Keep the source snapshot explicit; a newer sibling repository does not
  silently change the denominator of an older checked snapshot.
- **Roles, components, and evidence:** verify claim-level support and organism,
  medium, and formulation scope. A name-based role prediction or an extract's
  plausible composition does not establish a supported assertion.
- **Provenance and release state:** distinguish historical notes from active
  claims. Inspect relevant correction receipts, holds, and assertion dispositions;
  a common review verdict cannot clear native SSSOM or semantic-release gates.

Pattern matches identify candidates, not confirmed defects. A recipe pointer,
concentration suffix, or damaged spelling may still be a legitimate `RAW_TEXT`
source label. Read the exact historical allegation and current source context
before calling it an invalid synonym; token presence alone is not that proof.
Likewise, computational evidence proves a prediction-only payload, not a false
biological role, and non-monotonic history needs event semantics rather than an
automatic sorting rule. If the required context was not inspected, use
`status: deferred`, `certainty: provisional`, and an explicit next check. Do not
promote a regex hit plus a word somewhere in a report to a confirmed allegation.

Use the narrowest documented checks in `justfile` and the local review profile.
Record actual commands, exit codes, unavailable dependencies, and bounded search
scope. Rerun relevant checks once per assessed input snapshot and share that
evidence across affected findings. Identify any generator or upstream owner of
a residual defect. Do not repair or regenerate products during reconciliation
alone.

Direct diagnostic outputs to a session-unique temporary directory. For example,
`validate-strict` otherwise writes into the existing reports tree:

```bash
just validate-strict <record-path> --out <temporary-dir>/strict-validation.tsv
uv run python scripts/validate_sssom_invariants.py \
  --reject-tsv <temporary-dir>/sssom-rejects.tsv
```

The SSSOM validator is a corpus check; run it only when relevant to the selected
findings and retain its actual scope. Include results in the new bundle so the
conclusion does not depend on a temporary log remaining available.

## Decide Each Disposition

Use the schema's `ReviewFinding.status` values for structured findings:

| Current evidence | Disposition |
| --- | --- |
| The same defect is reproducible | `open`; retain the issue key and specify the remaining edit and acceptance checks. |
| Required evidence, access, or unambiguous lineage is unavailable | `deferred`; retain the question and next check. This is not a fix. |
| Inspected current fields and relevant checks prove the defect corrected | `resolved`, with explicit evidence and a disposition reason. |
| Inspected evidence proves the alleged defect invalid | `rejected`, with the reason. Failure to reproduce without adequate coverage is insufficient. |
| An authorized decision explicitly accepts a known remaining defect | `accepted_risk`, citing that decision; never infer acceptance from age or a closed issue. |

There is no `superseded` or `partially_fixed` structured status. Explain the
replacement or partial fix in `disposition_reason` and assessment details. A
partially fixed finding stays open for its residual. Duplicate findings remain
linked to the surviving issue; deduplication alone is not proof of correction.
Describe supersession as resolved or rejected only when the corresponding
evidence standard is met, otherwise retain an open/deferred observation.

For every structured successor, retain the same `issue_key`, cite the exact
repository/review/finding IDs in `previous_occurrences`, and cover all affected
targets from the cited predecessors. Reconcile competing heads explicitly. A
one-record observation cannot retire a multi-record finding. Preserve stable
target IDs across proven renames; if the lineage cannot be represented without
dropping targets, leave it unresolved and explain the limitation.

An omitted finding, new clean report, changed hash, merged PR, closed issue, or
passing general test suite is not disposition evidence by itself. Attribute a
fix to a PR/commit only after inspecting its actual change and current result.

## Save and Hand Off

Save using the shared contract and local review profile:

```bash
uv run python scripts/record_review.py validate <completed-review.yaml>
uv run python scripts/record_review.py save --content <completed-review.yaml>
```

Use `skill: reconcile-review-records`, actual UTC times, honest reviewer
independence, precise targets, and evidence-linked assessments. Use `kind: record`
for one ingredient or `kind: batch` for an explicitly selected set. Limit the
scope to the claims actually reassessed. Hash/ledger-only work uses
`scientific_review: false`; it cannot renew whole-record scientific approval.
Unavailable required checks require partial completion and explicit limitations.
A failed review cannot retire findings.

The saver creates immutable YAML and rendered Markdown under
`reviews/structured/<timestamp>-<slug>/`. Preserve prior bundles, historical
reports, and the legacy manifest. Do not rewrite their hashes or verdicts.
If saving is blocked, report the blocker and retain the draft; do not claim a
persisted reconciliation. After saving, run the contract's
`uv run python scripts/record_review.py check` once for the run, rather than
per record. Report unrelated bundle errors separately from selected-scope
results; never describe a failed corpus check as passing. Validate lineage
through the configured CLAW consumer
when available, otherwise inspect predecessor IDs, target retention, and
competing heads explicitly; local bundle validation alone is not a lineage audit.

Before authorized publication, verify that each `source.git_revision` will
remain available under the repository's actual merge strategy. Squash/rebase
merges can discard a topic-branch base after deletion. Prefer inspection from a
durable main base; if a saved review already names a branch commit, preserve
that exact commit with a documented archival provenance tag and verify it in a
separate checkout without the topic branch. Consumers must fetch retained
provenance tags as well as main history. Never relabel the saved base or alter
its hashes to make a provenance check pass.

When issue work is requested, hand the saved dispositions to
[review-round-issues](../review-round-issues/SKILL.md). Preserve legacy finding
IDs/fingerprints and structured issue keys for deduplication. Bundle verified
residuals by root cause and maintained owner, keeping deferred uncertainty
explicit. Only close a linked issue after checking every finding it covers and
recording any narrower residual. A report inventory alone cannot justify closure.

When fixes are also requested, use the native curation workflow and gates, then
inspect final bytes and save a linked successor assessment. Review `actions`
describe proposed work, not completed fixes.

Label navigation indexes with their observation round. When successors are
saved, expose their current heads separately from the historical snapshot;
derive counts through exact predecessor links, not by summing every observation
or selecting the newest timestamp. Preserve competing heads and state the
cutoff so a static index is not mistaken for a live issue queue.

Report the assessed revision, coverage, disposition counts, remaining priority
work, and unavailable checks. Link both saved YAML and Markdown. Keep counts of
historical findings reconciled separate from new defects discovered and records
whose full scientific review was actually renewed.
