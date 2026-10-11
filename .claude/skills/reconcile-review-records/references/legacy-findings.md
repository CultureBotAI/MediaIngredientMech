# Reconciling Historical MIM Reports

Use this path for Markdown in `reports/yaml_record_review/`, its TSV manifest,
and historical issue-round ledgers. Save new observations with the shared
structured-review contract; preserve every historical input.

## Recover the Actual Claim

Read the entire selected report, including Evidence, Recommended Edits,
Follow-up Checks, conditional language, and limitations. Some older reports
lack a Findings heading. Some timestamped refreshes merely carry an earlier
severity forward; follow their cited report to the original claim. Neither a
carried-forward blocker nor a stale summary is a fresh scientific judgement.

For each distinct allegation retain:

- original report path and SHA-256, exact heading/paragraph or line locator;
- record path, reviewed timestamp and record hash from the manifest when known;
- the claim, affected fields, original severity, maintained owner, and proposed
  proof of correction;
- existing issue-round `finding_id`, `fingerprint`, bundle, issue, fix, and
  retirement links, when present.

Recover every distinct claim even when the manifest notes summarize only one.
Do not count a refresh's carried-forward claim as an additional independent
defect. Preserve conflicting reports until the current assessment addresses
the disagreement.

`scripts/build_review_round.py` offers parsing and fingerprint helpers for
historical reports. Its fallback may reduce reports without Findings to one
manifest note, so extracted rows are an index to inspect, not the complete
claim inventory. Do not run the builder with `--force` over an existing round:
it replaces fix/retirement ledgers. Do not feed structured YAML to its parser.

## Represent Current Evidence Honestly

For a resolved current ingredient, use that ingredient as the review target and
hash the historical reports and relevant current inputs with `inspect --input`.
For a deleted or ambiguous historical record whose successor cannot be resolved,
an exact historical report can be a `source` target in a bounded provenance
assessment. State the unresolved record lineage and use
`scientific_review: false`; this does not count as reviewing a current ingredient.

For each historical allegation, write an evidence-linked assessment with:

- `topic` identifying the original defect;
- prior-review evidence containing its exact report locator and hash;
- current evidence containing exact fields/rows, inspected sources, and relevant
  check results;
- `details` stating the before/current comparison and disposition rationale;
- a `legacy-disposition` dimension with value `still_open`, `already_fixed`,
  `rejected`, `superseded`, or `needs_reassessment`, a definition, and supporting
  evidence IDs. These are assessment labels, not `ReviewFinding.status` values.

Use additional dimensions or details to retain legacy IDs/fingerprints and the
reviewed/current hashes. For `superseded`, identify the replacement claim or
record and whether a residual remains. A partial fix stays `still_open` with
its narrowed scope. Use `outcome: concern` for a remaining defect, `unknown` for
insufficient evidence, and `supported` only for an inspected conclusion. A
supported conclusion about an old finding is not a blanket record pass.

A verified unresolved defect gets a new structured `open` finding and proposed
action. Search existing structured observations and issue links before assigning
its stable `issue_key`; reuse a key only for the same defect and preserve exact
structured predecessor references when they exist. If a later run fixes that
finding, it can save a genuine `resolved` successor.

Already-fixed or disproven legacy claims belong in current assessments with
evidence. Do not invent structured `previous_occurrences`, backdate a baseline,
or create an open/resolved pair merely to represent a historical fix. Legacy
`RF-`/`RFP-` identifiers are not structured review/finding references. In later
rounds, cite these new assessments as evidence and trace the original allegation
so it is not repeatedly introduced as new work.

## Issue-Round Handoff

When issue/ledger maintenance is requested, attach the saved reconciliation
bundle and exact assessment/finding IDs to the existing round. Keep original
IDs/fingerprints when appending fix or retirement evidence; use the legacy
ledger field names and reasons defined by `scripts/build_review_round.py` and
the `review-round-issues` skill. Do not infer a retirement because the manifest
now omits a finding, or replace the old manifest row with a partial assessment.

The legacy builder does not consume these structured dispositions. Review and
apply the handoff explicitly; rerunning it on the old manifest will rediscover
historical findings. Keep new structured observations on the structured issue
triage route. Check current issue bodies and all linked findings before any
authorized GitHub mutation, and keep unresolved residuals visible.
