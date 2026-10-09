---
name: review-round-issues
description: "Turn MediaIngredientMech YAML review report outputs into a timestamped review-round ledger, bundle findings into a small GitHub issue plan, deduplicate the plan against existing issues, and track created issues, fixing PRs, and finding retirements. Use when asked to make issues from review reports or to track review/issue/fix rounds."
allowed-tools: Bash, Read, Grep, Glob, Write
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review Rounds to Issues

## Scope

For new structured bundles, start with [Structured Review Inputs](#structured-review-inputs)
below. The legacy manifest-based round builder only consumes historical prose
reports; it is not an adapter for the new YAML contract.

Use this skill after `review-yaml-record` or `review-yaml-category` has written
Markdown review reports and you need to promote their findings into a durable,
bundled GitHub issue backlog.

The workflow tracks this lifecycle:

```text
review reports
  -> reports/review_rounds/<round-id>/input_reports.tsv
  -> normalized findings.tsv
  -> category bundles.tsv
  -> deduplicated issue_plan.tsv and issue_bodies/*.md
  -> issues.tsv after approved GitHub creation or updates
  -> fixes.tsv after PRs merge
  -> retirements.tsv after re-review proves findings are gone
```

Do not use this skill to fix records directly. Review-output triage owns report
ledgering and GitHub issue planning only.

## Round IDs

Name each round with a UTC timestamp and the source report family:

```text
<YYYYMMDDTHHMMSSZ>-yaml-review-issues
<YYYYMMDDTHHMMSSZ>-category-review-issues
```

The timestamp marks when the issue-planning round was built, not when every
individual report was written. Individual report timestamps and
`record_sha256` values stay in `input_reports.tsv`.

## Build the Ledger

From the repository root, build a round from the current YAML record review
manifest:

```bash
uv run python scripts/build_review_round.py \
  --round-id <YYYYMMDDTHHMMSSZ>-yaml-review-issues
```

This writes:

- `round.yaml` — round metadata, source manifest, base commit, and row counts.
- `input_reports.tsv` — exact reports snapshotted from the review manifest,
  their `record_sha256` values, review timestamps, and report SHA-256 digests.
- `findings.tsv` — one normalized finding per actionable report finding.
- `bundles.tsv` — category-level bundles that intentionally group multiple
  related findings into a small issue set.
- `issue_plan.tsv` — default issue actions; every row starts as `create` until
  a dedupe pass proves otherwise.
- `issue_bodies/*.md` — draft Markdown bodies with embedded
  `mim-review-round`, `mim-review-bundle`, and `mim-fingerprints` footer
  comments for future dedupe.
- `issues.tsv`, `fixes.tsv`, `retirements.tsv` — empty ledgers for later issue
  creation, merge, and re-review proof.
- `validation.tsv` — counts and sanity checks for the generated round.

Commit the generated round only after reviewing `issue_plan.md`, not merely
because the builder exited zero.

## Dedupe Before GitHub Mutation

Before opening an issue for a bundle:

1. Fetch open issues:

   ```bash
   gh issue list --state open --limit 500 \
     --json number,title,body,labels,createdAt,updatedAt
   ```

2. Search for the bundle category, owner area, affected record names, and any
   existing `mim-fingerprints` footer.
3. Edit `issue_plan.tsv`:
   - keep `action=create` for genuinely new bundles;
   - set `action=append_to_existing` and `issue_number=<N>` when an issue
     exists but lacks some fingerprints;
   - set `action=skip_duplicate` and `issue_number=<N>` when an existing issue
     already covers the full bundle;
   - set `action=skip_minor` for noisy minor-only bundles that should stay in
     the round ledger but not become GitHub issues yet;
   - set `action=needs_human_split` when the bundle is too broad to be a useful
     issue.

Do not open one issue per report. If a bundle is too large, split it into a
smaller number of root-cause clusters and keep the fingerprints in the bodies.

## GitHub Issue Creation

Only create or update issues for explicitly approved `bundle_id` values from
`issue_plan.tsv`.

For each approved `create` row:

1. Read the matching `issue_bodies/<bundle_id>.md`.
2. Create one issue whose title is the `issue_plan.tsv` title and whose body is
   that Markdown.
3. Append a row to `issues.tsv` with `round_id`, `bundle_id`, `issue_number`,
   `issue_url`, `action=create`, the UTC creation time, and the comma-joined
   `finding_ids` from `bundles.tsv`.

For approved `append_to_existing` rows, comment on the existing issue with the
new affected records and the missing `mim-fingerprints`, then append an
`issues.tsv` row with `action=append_to_existing`.

Never bulk-create the full plan unattended. Review-output runs can surface
hundreds of minor findings, and the whole point of this skill is to prevent
issue spam.

## Tracking Fixes

When a PR claims to fix a bundle:

1. Verify the PR actually edited the maintained owner paths from
   `findings.tsv`.
2. Verify the post-fix validators named in `followup_check` ran or record why a
   narrower equivalent proves the fix.
3. After merge, add one `fixes.tsv` row per issue:

   ```text
   issue_number
   bundle_id
   pr_number
   merge_commit
   fixed_paths
   fixed_at
   validation
   ```

Mentioning an issue number in a PR is not enough. The row needs the merge
commit and the validation evidence that closed the specific bundle.

## Structured Review Inputs

New scientific reviews use [docs/record-reviews.md](../../../docs/record-reviews.md).
Validate bundles with `uv run python scripts/record_review.py check`; use their
authoritative YAML finding IDs and stable issue keys, not parsed Markdown.
The legacy `scripts/build_review_round.py` and manifest examples below are
for historical prose reports only. Do not feed a structured bundle to that
parser or infer closure from a newer clean report. For new observations, retain
`issue_key`, cite exact `previous_occurrences`, and record inspected evidence
and the disposition reason through the shared saver. GitHub writes still
require the task's outbound authorization.

## Retiring Findings

Retire findings only after a later review report inspects the changed
`record_sha256`.

For each old fingerprint:

1. Find the new report for the same record in the latest
   `reports/yaml_record_review/manifest.tsv`.
2. Require an explicit evidence-backed disposition of the old finding.
   Omission or `severity=none` alone does not establish that it was resolved.
3. Add a `retirements.tsv` row with:
   - `old_finding_id`
   - `fingerprint`
   - `issue_number`
   - `retired_by_report`
   - `retired_record_sha256`
   - `retired_at`
   - `retirement_reason`

Use these retirement reasons:

```text
fixed
superseded
duplicate_of
not_reproducible
narrower_residual_opened
```

Close the GitHub issue only when every fingerprint in that bundle is retired
or intentionally moved to a narrower residual issue.

## Mutation Boundaries

- Do not edit `data/ingredients/**`, `data/curated/**`, or `mappings/**` as
  part of issue planning.
- Do not create, comment on, or close GitHub issues until the exact bundle IDs
  and target issue numbers have been reviewed.
- Do not drop minor findings from the ledger just because they are too noisy
  for GitHub. Mark them `skip_minor` in `issue_plan.tsv`.
- Do not trust issue titles alone during dedupe. Search existing bodies for
  the machine-readable `mim-fingerprints` comments first.

## Final Summary

Report:

- round ID and base commit
- number of input reports snapshotted
- number of normalized findings
- number of issue bundles by severity
- bundles created, appended, skipped as duplicates, skipped as minor-only, and
  left for human splitting
- any GitHub issue numbers created or updated
