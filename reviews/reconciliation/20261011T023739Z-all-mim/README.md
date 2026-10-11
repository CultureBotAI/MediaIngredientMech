# All-MIM Review Reconciliation

**Partial reconciliation; complete record inventory. No scientific approvals renewed.**

## Current Head Snapshot

As of `2026-10-11T03:08:52Z`, the initial 13 batches plus one linked successor
contain **616 open and 35 deferred heads** across the same 651 issue keys.
Use [current-findings.tsv](current-findings.tsv), not the initial counts below,
for this corrected observation snapshot. This is not a live issue queue; later
reviews must be reconciled through exact predecessor links.

Adversarial self-review in [PR #860](https://github.com/CultureBotAI/MediaIngredientMech/pull/860)
found that the recipe-token heuristic overstated certainty
([#861](https://github.com/CultureBotAI/MediaIngredientMech/issues/861)).
All 17 token observations now have deferred/provisional successors:
[YAML](../../structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml),
[Markdown](../../structured/20261011T030852Z-mim-token-scope-reassessment/review.md).
In particular, the Artificial seawater and DL vitamins historical reports
explicitly accept their raw source labels; they did not allege the token defect
attributed to them by the initial extraction. No ingredient label was changed
or scientifically approved by this correction. Other identity allegations,
including trace-mineral labels on 4-vinylphenol, remain unadjudicated here.

The successor's inspected base is retained by the archival tag
`review-source/20261011-0cc2b4e3` because the merge queue squashes topic commits
([#862](https://github.com/CultureBotAI/MediaIngredientMech/issues/862)).
[provenance-bases.tsv](provenance-bases.tsv) records its exact revision.
Keep this tag after branch cleanup. A consumer that fetches only main should
also run `git fetch origin tag review-source/20261011-0cc2b4e3` before validating
the successor. This preserves the original source attestation, not a rewritten
Git base. The first 13 batches use the existing main-history base below.

Correction checks:

- `scripts/record_review.py check --base origin/main --require-reviews`: 14 valid bundles, declared scopes only; the original pairs remain byte-identical.
- `tests/test_record_review_routes.py` and `tests/test_reconciliation_indexes.py`: six tests passed, including exact predecessor/target/head accounting and retained-tag agreement.
- A separate main-only object database could not resolve the successor's base before fetching the archival tag. After fetching that tag, all 14 source attestations verified without any topic-branch ref.
- Skill validation, instruction-reference checks, Black, Ruff, and `git diff --check` passed. Ingredient, mapping, and native release-gate bytes were not changed.

## Initial Round

- Assessed Git base: `378d733d51f6d66cbc936bf17c56821a1f7030fe` (remote main verified before review).
- Started: 2026-10-11T02:37:39.999012Z; finished: 2026-10-11T02:46:40Z.
- Scope: all 2,953 current IngredientRecord files, including 81 rejected tombstones, 260 unmapped records and one AMBIGUOUS record; 2,611 are MAPPED.
- Historical inputs: 2,953 manifest rows and 3,135 Markdown reports, including older originals behind refresh reports. Ignored/untracked files were included. No missing manifest target/report or unresolved report-to-record lineage was found.
- Nine record hashes differ from their latest legacy manifest entries. Hash equality/change was not used as a finding disposition.
- Saved 13 disjoint structured batches. Every target has a current-surface assessment and retained historical-review evidence.
- This is bounded, primarily deterministic reconciliation. All report text was loaded and retained by hash, but the run does not complete independent scientific interpretation of every historical allegation. Remaining narrative groups are explicitly `needs_reassessment`.

## Initial Results

| Finding Category | Open | Deferred |
| --- | ---: | ---: |
| cas-source | 0 | 1 |
| exported-context-tokens | 17 | 0 |
| history-order | 19 | 0 |
| receipt-id | 1 | 0 |
| role-support | 595 | 17 |
| source-count | 1 | 0 |
| **Total** | **633** | **18** |

The counts above are the initial structured observations, not current heads or proposed GitHub issue counts. Bundle by root cause/owner, reuse the existing [scientific curation backlog #718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718), and inspect residual scope before creating anything new. The initial run performed no GitHub mutation; the later PR self-review opened the two process issues linked above.

| Scoped Legacy Disposition Assessments | Count |
| --- | ---: |
| already_fixed | 9 |
| needs_reassessment | 1931 |
| still_open | 632 |
| superseded | 1 |

These are **bounded assessment groups, not distinct historical allegations**. They can overlap on one record. Refresh carry-forward reports are retained as history, not counted as new defects. Fixed dispositions do not close the entire older report.

Verified narrow corrections include six tombstone ontology/identifier pointers, Furaltadone hydrochloride's exact NCIT row shape, and the calcium nitrate label/three-occurrence transfer (assessed from both affected records). The old CMC/PY/horse-serum note-edit recommendation is superseded by withdrawal of that mixture representation; its current source-context ambiguity remains.

Initial observations include prediction-only role payloads, reported context-dependent or truncated SSSOM tokens, timestamp-order problems, the missing direct D-lyxose source-count row, and a calcium-nitrate correction receipt naming CHEBI:31348 instead of the actual CHEBI:86159. The token conclusions are superseded by the certainty correction above; they require source-scope adjudication, not automatic removal. Furaltadone CAS verification remains deferred. These observations do not establish that all asserted biological roles are false.

## Verification

- Strict closed-schema validation: 2,960 YAML documents, zero errors.
- SSSOM currency: zero GAP, ORPHAN, STALE, PREDICATE or GRADE drift.
- SSSOM available invariants: passed. B4 was unavailable because the validator's default sibling ontology transforms were absent for BTO, CHEBI, ENVO, FOODON, MICRO and UBERON.
- Export freshness: eight generated artifacts match their producers; all 8,312 curated labels are indexed/resolvable.
- Aggregate comparison: all 2,953 records agree after applying the exporter-declared per-record overlay exclusions. Eight raw `discussions` differences are intentional, not defects (#786).
- Merge-tombstone regression tests: nine passed.
- Pre-save audit: exact disjoint target coverage, all historical reports represented, unique issue keys, no invented predecessors/terminal statuses, and all captured inputs unchanged.
- Shared structured-contract corpus check: `.venv/bin/python scripts/record_review.py check --require-reviews` exited 0 with `valid_reviews: 13` and `coverage: declared_scopes_only`. This validates the saved pairs/provenance, not unassessed science. Native release gates, holds and prior reports were not altered.

## Files

- [Per-record index](records.tsv): each current record, hashes, prior severity, saved bundle and finding counts.
- [Findings index](findings.tsv): exact stable issue keys, owner paths and existing issue links.
- [Scoped dispositions index](dispositions.tsv): exact assessment IDs and bounded rationale.

These three TSVs describe the initial round only. The separately linked current-findings index incorporates the successor. All TSVs are navigation indexes only. The immutable structured YAML is authoritative; Markdown is rendered by the shared saver.

| Batch | Records | YAML | Markdown |
| --- | ---: | --- | --- |
| 1 | 26 | [YAML](../../../reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml) | [Markdown](../../../reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.md) |
| 2 | 250 | [YAML](../../../reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml) | [Markdown](../../../reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.md) |
| 3 | 250 | [YAML](../../../reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml) | [Markdown](../../../reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.md) |
| 4 | 250 | [YAML](../../../reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml) | [Markdown](../../../reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.md) |
| 5 | 250 | [YAML](../../../reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml) | [Markdown](../../../reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.md) |
| 6 | 250 | [YAML](../../../reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml) | [Markdown](../../../reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.md) |
| 7 | 250 | [YAML](../../../reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml) | [Markdown](../../../reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.md) |
| 8 | 250 | [YAML](../../../reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml) | [Markdown](../../../reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.md) |
| 9 | 250 | [YAML](../../../reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml) | [Markdown](../../../reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.md) |
| 10 | 250 | [YAML](../../../reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml) | [Markdown](../../../reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.md) |
| 11 | 250 | [YAML](../../../reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml) | [Markdown](../../../reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.md) |
| 12 | 250 | [YAML](../../../reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml) | [Markdown](../../../reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.md) |
| 13 | 177 | [YAML](../../../reviews/structured/20261011T024640Z-mim-reconcile-all-batch-13/review.yaml) | [Markdown](../../../reviews/structured/20261011T024640Z-mim-reconcile-all-batch-13/review.md) |

## Next Round

Read these saved bundles before using the older manifest as an issue source. Follow exact issue keys and assessment IDs; do not rebuild a legacy round and rediscover already-addressed subclaims. Address supported fixes only when authorized, then save successor observations with real previous_occurrences. For deferred narrative groups, inspect the complete original report and current source/ontology evidence before deciding a disposition.
