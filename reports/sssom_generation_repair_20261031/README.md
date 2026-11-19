# SSSOM generator repair evidence

This bundle records mechanical validation of the CLAW SSSOM builder repairs for
[registry conflicts (#679)](https://github.com/CultureBotAI/culturebotai-claw/issues/679),
[inherited target aliases (#680)](https://github.com/CultureBotAI/culturebotai-claw/issues/680),
[header dates (#681)](https://github.com/CultureBotAI/culturebotai-claw/issues/681), and
[Unicode date rejection (#682)](https://github.com/CultureBotAI/culturebotai-claw/issues/682).

Generator fix: [CLAW PR #683](https://github.com/CultureBotAI/culturebotai-claw/pull/683).
This directory and the two linked review bundles form the MIM evidence-only companion.

The maintained canonical mapping remains **2,987 rows** with SHA-256
`89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9`.
The diagnostic candidate has **2,980 rows**, SHA-256
`04159ba36b221d1c8ebf6e281972c846a333cf4fe5e868b06bb5326f2b02e3a7`.
It was not promoted. Ingredient YAML, aggregate collections, the unified mapping,
and the pinned scientific release review were not edited.

## Review and exact outcomes

- [Original observation, YAML](../../reviews/structured/20261031T214143Z-sssom-current-inputs-mechanical/review.yaml)
  and [Markdown](../../reviews/structured/20261031T214143Z-sssom-current-inputs-mechanical/review.md)
  are preserved byte-for-byte.
- [Successor review, YAML](../../reviews/structured/20261031T233012Z-sssom-native-repair-mechanical/review.yaml)
  and [Markdown](../../reviews/structured/20261031T233012Z-sssom-native-repair-mechanical/review.md)
  resolve the three prior mechanical findings with `pass_with_limitations` and
  `scientific_review: false`. Native inspection, validation, guarded save and the
  complete 978-bundle review check passed.
- [All 41 original diagnostics](original-41-remediation.json) retain exact row or
  header selectors and dispositions: 14 maintained primary identities retained,
  14 competing generated identities removed, 11 Rule K aliases removed, and two
  header dates corrected to the newest row date, `2026-10-15`.
- [All changed `other` fields](other-field-changes.json) show 17 removed inherited
  aliases across 17 rows. No curated subject synonym was removed. Relative to the
  previous raw candidate, no row was added and no retained-row predicate changed.
- [Separate comparisons](candidate-comparison.json) distinguish the old raw
  candidate from the maintained canonical mapping. The repaired candidate still
  differs substantially from canonical: 2,366 shared pairs have payload changes,
  nine pairs are absent, and two pairs are added. These are not new release
  approvals.

## Native checks and limits

The diagnostic candidate passed strict native SSSOM invariants, SSSOM JSON Schema,
prefix/CURIE checks, configured ID-label validation, and native reconciliation
(zero GAP, ORPHAN, STALE, PREDICATE or GRADE findings). The maintained canonical
source separately passed `just qc`, CURIE, reconciliation and product-label
checks. Actual command arguments, times, exit codes and log hashes are in
[`logs/`](logs/); setup/helper failures and successful retries are retained.
The local Git attributes preserve verbatim log, patch and captured-label bytes,
including terminal spacing and TSV line endings, so recorded hashes survive checkout.

Native limitations remain visible: 101 nonblocking full-product label warnings,
5,314 canonical-run and 3,736 candidate-run no-adapter skips, 18 non-gating
subject-slug warnings, and missing BTO/MICRO transforms in best-effort Rule B4.
Actual-path B4 found zero defects using the available read-only KG transforms.
The [candidate label configuration](candidate-id-label-config.yaml) preserves
the native adapters, policies, exceptions and settings, changing only target
selection and the diagnostic input path.

[Historical scientific holds](historical-rule-k-holds.json) remain in force for
all 11 corresponding canonical non-exact mappings. Resolving generator defects
does not establish their scientific relation or full synonym scope, change
curation status, calibrate confidence, or renew historical validation stamps.
CultureMech outputs and KG Mediadive nodes remain comparison inputs; the builder
uses maintained MIM records and its native KG unified mapping/residual inputs.

## Final code and provenance

The [input manifest](validation-inputs.json) hashes 2,985 current files and records
repository revisions, working-tree state, copied residual data, KG inputs and
ontology database snapshots. [B4 evidence](candidate-b4-actual.json) separately
records the exact ontology transform files and hashes.

The initial generation loaded a version preceding removal of an unused import.
[Generator identities](generator-revisions.json) and the
[first final-code replay](final-code-replay.json) preserve that distinction.
An independent review then found the Unicode date edge case. The appended
[code-only supplement](code-review-supplement-r2.json) records the ASCII guard
fix at CLAW commit `8f837d505b948a25965b0b2a001a4c7691c840fc`, two regression
failures before the fix, 66 passing focused tests afterward, and passing lint.
The [second final-code replay](final-code-replay-r2.json) proves byte-identical
candidate output at that final commit. The saved review and its inspected inputs
were not rewritten for this later code change.

Both replay runs reuse [exact emitted-object label values](resolved-label-values.tsv). They make no new
ontology/provider calls and establish output equivalence rather than fresh
ontology validation. Forty-eight requested CHEBI IDs absent from the emitted
output are explicitly recorded in the replay receipts. The full CLAW suite is
reported separately by the fix PR; this bundle does not attest a full-suite pass.

[Independent review round 1](adversarial-review-round1.md) found one minor defect:
Unicode years bypassed the new date guard. It was filed as issue #682 before
repair. [Round 2](adversarial-review-round2.md) checked final code head
`8f837d505b948a25965b0b2a001a4c7691c840fc`, confirmed that finding resolved and
found no new code defects. The JSON reports retain tested heads, commands,
counterexamples, scope and limitations.

## Reproduction

Use Python 3.13 and the native repository environments, with the exact source
revisions, data bytes and ontology caches in the manifest. Resolve the MIM and KG
roots explicitly; keep KG read-only. The run receipts preserve the executed
commands and absolute input paths. The core native sequence is:

```bash
export MEDIAINGREDIENTMECH_ROOT="$MIM_REVIEW_ROOT"
export KGMICROBE_ROOT="$KG_REVIEW_ROOT"
# Set PYSTOW_HOME to the retained ontology-cache root from the input manifest.
python "$CLAW_REVIEW_ROOT/scripts/build_mim_ingredient_sssom.py" \
  --output "$MIM_REVIEW_ROOT/output/sssom-repair/ingredient_mappings.sssom.tsv" \
  --prior-stamps-from "$MIM_REVIEW_ROOT/mappings/ingredient_mappings.sssom.tsv"
cd "$MIM_REVIEW_ROOT"
uv run python scripts/validate_sssom_invariants.py \
  output/sssom-repair/ingredient_mappings.sssom.tsv \
  --reject-tsv output/sssom-repair/rejected-rows-current.tsv
sssom validate -V JsonSchema -V PrefixMapCompleteness -V StrictCurieFormat \
  output/sssom-repair/ingredient_mappings.sssom.tsv
uv run python scripts/validate_published_curies.py \
  output/sssom-repair/ingredient_mappings.sssom.tsv
uv run python scripts/validate_id_label_correspondence.py \
  --config reports/sssom_generation_repair_20261031/candidate-id-label-config.yaml
just check-record-reviews
```

The generation run also used native repository identity validation and the CLAW
repository lock before writing its diagnostic output. Reproduction should retain
those controls. Current external ontology responses may change; use the captured
labels and retained input hashes for byte-level replay. Full mapping outputs and
large data/cache inputs remain local diagnostic artifacts, outside this tracked
evidence bundle.
