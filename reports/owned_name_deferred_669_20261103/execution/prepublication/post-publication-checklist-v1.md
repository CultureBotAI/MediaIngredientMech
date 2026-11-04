# Deferred23 post-publication native checklist

Read-only preparation; none of the commands below was executed by this checklist task. The root operator owns publication, maintained edits, commits and GitHub. Stop on the first failed command and preserve its output/receipt. No ontology/provider request or source/snapshot regeneration is part of this sequence.

The commands were checked against the current Step8 justfile, maintained refresh CLI and workflow bytes. Prior Step7d command receipts `logs/step7d-post1122-01-assemble-v1.json` through `...13-supported-schema-v1.json` all record exit0 and establish the native ordering. Those historical results do not count as validation of Step8.

## Preconditions and exact review edits

1. Independently reviewed publisher successfully applies the five-file transaction. Run its `--verify-completed` immediately, before changing any captured review input. Confirm the canonical SHA is `d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6`, the native receipt26 has 23 changes/0 additions/0 removals, historical receipts1–25 are byte-identical, and the journal has exactly4 changed files plus1 created receipt. No source/aggregate/label-index/unified bytes change.
2. Preserve the pre-refresh current review/semantic artifacts and the old companion bundle. The prior companion remains `reports/step7d_mapping_901_20261103/refresh-v2/companion-review.json`, from durable baseline `0ee56c11a2894ed50a476b331d56297be0a3ee12`.
3. Advance only the `REVIEWED_SOURCE` literal in `reports/sssom_completion_20260921/assemble_review.py`, from `d3030e6385a2659a0dbd2c64ad5581568eecd9c10023f4a58de667e8050f20ef` to the exact published canonical SHA above. Preserve every assertion/selection rule. Use the guarded publication helper with exact before/after bytes and retain its receipt, as in Step7d.
4. After the new immutable companion review is saved, repoint both selectors together, with no other changes in those two files: `REVIEW` in `tests/test_ingredient_bundle.py`, and `--review` in `.github/workflows/qc-reviewed-sssom.yaml`. Old selector: `reports/step7d_mapping_901_20261103/refresh-v2/companion-review.json`. New selector proposed here: `reports/owned_name_deferred_669_20261103/companion-review.json`. Compare against original bytes with exactly that string replacement; every assertion remains unchanged. The separate already authorized #1130 tests/context tests are independent changes, not selector weakening.
5. The current publisher dry-run proposes policy manifest SHA `6b6fe48246bd43dd70499e82f508a7b7ea0fcd121bccafafa0217aae84a17778`. After application, read/hash the actual manifest and require equality with the final independently reviewed publication proof; pass that exact hash below. If publication changes during review, this checklist's forecast hash is not authority to reuse an old proof.
6. Check all new output paths, including ignored files and symlink aliases, before any export. Use new paths and never erase an occupied output. The full graph path must be exactly `output/mim-kgx-710-full`, because the semantic review must reproduce the CI path (#1125). If occupied, preserve it and resolve the conflict explicitly; do not silently pick a differently named full graph path. Native exporters and the companion refresh reserve fresh outputs themselves.

## Runtime and receipt wrapper

Run from the original repository or any directory; the wrapper selects the owned Step8 worktree, Python3.13, the existing read-only native environment, the existing pinned validator, cached checker executables and offline mode. It uses no dependency sync and no paid provider calls. Do not replace the vendored validator pin with the newer generator.

```bash
NEXT23_RUN=/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z
NEXT23_W="$NEXT23_RUN/step8-aliases"
next23run() {
  next23_tag="$1"
  shift
  python3 "$NEXT23_RUN/run_next23_mim_v2.py" step8-aliases "next23-postpublication-${next23_tag}-v1" -- env UV_OFFLINE=1 "$@"
}
```

Each tag is single-use and creates `RUN/logs/<tag>.json` and `.log`. Use a new versioned tag for a justified rerun; do not overwrite prior receipts. Execute sequentially, stop on nonzero, and do not continue by ignoring an error. The function above does not itself enforce shell `errexit`; the controlling root script must check every exit code or use `set -euo pipefail`.

## Native regeneration and verification order

After the exact guarded assembler literal advance:

```bash
next23run 01-assemble python -B reports/sssom_completion_20260921/assemble_review.py
next23run 02-assemble-check python -B reports/sssom_completion_20260921/assemble_review.py --check
next23run 03-export-full just export-kgx output/mim-kgx-710-full
next23run 04-semantic-build python -B reports/semantic_review_20260921/resolution/build_review.py --bundle output/mim-kgx-710-full
next23run 05-semantic-integrity python -B -m mediaingredientmech.validation.semantic_release --root . --report reports/semantic_review_20260921/resolution/current-review.json
next23run 06-assemble-after-semantic-check python -B reports/sssom_completion_20260921/assemble_review.py --check
next23run 07-companion-refresh python -B scripts/refresh_unchanged_cohort.py --root "$NEXT23_W" --baseline 0ee56c11a2894ed50a476b331d56297be0a3ee12 --prior-review reports/step7d_mapping_901_20261103/refresh-v2/companion-review.json --output reports/owned_name_deferred_669_20261103/companion-review.json --receipt reports/owned_name_deferred_669_20261103/companion-refresh-receipt.json --prior-copy reports/owned_name_deferred_669_20261103/prior-companion-review.json --owned-name-suppression-manifest-sha256 6b6fe48246bd43dd70499e82f508a7b7ea0fcd121bccafafa0217aae84a17778
```

The new `--owned-name-suppression-manifest-sha256` argument is required for this transition. It invokes the closed native proof of the exact23 export-only removals, full source inventory, unchanged scientific decisions, native receipt chain and manifest checkpoint bridge. It is mutually exclusive with earlier form/registry/stock projection modes; do not pass those historical flags.

Now perform the exact paired-selector repoint from precondition4. Then use these native commands. The suggested output paths match the CI workflow paths and must all be fresh:

```bash
next23run 08-companion-export python -B -m mediaingredientmech.export.ingredient_bundle export --review reports/owned_name_deferred_669_20261103/companion-review.json --output output/mim-reviewed-ingredient-bundle
next23run 09-reviewed-export just export-reviewed-sssom reports/sssom_completion_20260921/review.json output/mim-reviewed-sssom
next23run 10-reviewed-qc-schema just qc-reviewed-sssom reports/sssom_completion_20260921/review.json output/mim-reviewed-sssom
next23run 11-supported-export just export-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/mim-kgx-710-supported
next23run 12-supported-qc just qc-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/mim-kgx-710-supported
next23run 13-supported-schema python -B -c 'from sssom.parsers import parse_sssom_table; from sssom.validators import SchemaValidationType, validate; validate(parse_sssom_table("output/mim-kgx-710-supported/ingredient_mappings.sssom.tsv"), validation_types=[SchemaValidationType.JsonSchema, SchemaValidationType.PrefixMapCompleteness, SchemaValidationType.StrictCurieFormat]); print("PASS supported SSSOM schema/prefix/CURIE validation")'
```

The reviewed recipe already runs assembler `--check`, the native reviewed exporter `--validate-only`, and `scripts/validate_reviewed_sssom_schema.py`, which checks both supported and withheld SSSOM tables. The supported recipe checks reviewed selection and excluded-claim preservation; the separate schema command matches the supported-graph CI workflow.

Expected maintained derived outputs to inspect: `reports/sssom_completion_20260921/{review.json,mapping-evidence.json}` and the native semantic builder's regenerated files under `reports/semantic_review_20260921/resolution/` (including `current-review.json`, `assertion-dispositions.tsv`, and any recalculated disposition/lineage files). Inspect the exact diff instead of presuming a complete filename list. The new companion/prior-copy/receipt are new artifacts; all historical companion reports remain immutable.

No `sync-curated`, `sync-individual`, ingredient-browser/list/index regeneration, visualization regeneration, or unified rebuild is needed: source bytes are unchanged and the source-dependent outputs must remain byte-identical. `just qc` will verify them. The canonical header and mapping dates also remain unchanged; do not run `bump-sssom-header` for this pure `other` transition.

## Required local checks and CI-specific complements

Run the full data/QC and test gates after derived outputs are final:

```bash
next23run 14-qc just qc
next23run 15-quality just lint format-check typecheck
next23run 16-record-review-contract just test-record-reviews
next23run 17-full-suite just test
next23run 18-published-curies python -B scripts/validate_published_curies.py
next23run 19-sssom-currency python -B scripts/reconcile_sssom.py
next23run 20-unified-freshness python -B scripts/check_unified_freshness.py --check
next23run 21-unified-rejections python -B scripts/check_unified_rejections.py
next23run 22-strict-evidence python -I scripts/run_shared_evidence_validator.py --strict
```

`just qc` includes validate-all, validate-strict, evidence validation, qc-sssom, roundtrip, duplicate IDs, KG node IDs, component partonomy, flat coverage, instruction refs and curation targets. It does not include the reviewed/supported exports, full test suite, static quality checks, or the two unified checks. The SSSOM workflow also runs published-CURIE validation and reconciliation, hence the explicit complements. The evidence workflow's strict mode is stricter than the default `just qc-evidence` recipe and uses the same unchanged vendored pin. Keep all failure receipts.

`just test` runs the full suite and package coverage floor35%, then reports legacy-script coverage. No changed skip/coverage/assertion threshold is permitted. The local environment has live read-only sibling inputs; CI is hermetic. Report actual local and CI counts separately; do not reuse Step7d counts. The CI pytest job also runs `just test-record-reviews`, so retain that separate proof.

Additional existing CI jobs remain authoritative, including instruction refs, curation history, vendored sync and reusable ID-label correspondence. The vendored checker may fetch the public pinned Claw revision, but it performs no paid research; do not repair it by changing the pin. No workflow modification is required except the paired `--review` selector above.

## Assertions for final evidence and review

- Recompute current canonical counts:3014 rows, exactly23 changed `other` cells at the plan positions, no other cell/header/order/date/stamp change, no added/removed row. Old sidecar11 rows retain exact raw bytes;23 prior-only events produce34 total; baseline retains its original header and0 data rows. These counts come from the frozen proposal/current preflight and must be rechecked after publication.
- All23 touched review positions remain `WITHHOLD`; every untouched disposition remains the same. Receipt26 does not authorize identity, form, role, source merge or release approval.
- Prior companion currently has20 owners and51 claims:18 identifier,20 mapping,10 occurrence,3 product. The refresh must preserve exact owner bytes, claims and scientific support, and bind the new current review/manifest by native proof. Verify the prior copy is byte-identical.
- Native semantic integrity PASS and supported-export PASS do not assert universal corpus readiness. The current baseline report says `release_verdict=FAIL`, with1733 blocking findings,2369 blocking assertions and4 evidence-gap groups; those are preserved backlog states, not a reason to fake a global PASS. Record the newly generated actual verdict/counts and any unexpected difference.
- The semantic report must name exactly `output/mim-kgx-710-full` and bind that bundle's actual manifest SHA, matching CI. Compare the successor native receipt chain length26 and receipt26 hash to the publication proof.
- Preserve the source/aggregate/label-index/unified SHA inventories from `unchanged-inventory.json`; historical receipt prefixes and all old report bytes stay immutable. Record the five publication hashes, generated review hashes, companion hash and final branch head.
- Obtain independent adversarial review of the final head, file genuine findings, fix in scope, re-review, and require all16 CI checks SUCCESS at that exact head. Current workflow job names are: `history`, `instruction-refs`, `id-label-gate` (reusable workflow; use its actual reported check name), `qc-component-partonomy`, `qc-duplicate-ids`, `qc-evidence`, `qc-flat-coverage`, `reviewed-sssom`, `roundtrip`, `qc-sssom`, `supported-graph`, `qc-unified-freshness`, `check`, `pytest`, `validate-strict`, `vendored-sync`.
- PR-head results do not substitute for merge-queue candidate results. Root follows the approved queue/squash/content verification/ordinary branch cleanup plan after review, then closes #912 with verified replacement pointers. This checklist performs none of those actions.
