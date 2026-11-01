# Step 3 native dependency chain — prepared, not executed

This package contains an executable, guarded orchestration script for the root
to review and run after the #1004 source and canonical transactions pass their
independent review. Preparation changed only this run-owned directory. It did
not apply sources, run the chain, change production data, advance a review pin,
create a mapping receipt, refresh an export, or run tests. The script has been
parsed as Python syntax only.

`prepared-inputs.json` binds the current native sources, base
`99fe4b44d78126d78041a69eeb366c52bedf0caa`, the separate merged Claw producer,
the pinned validator checkout and environment helper. `step2-command-basis.json`
contains 16 successful Step 2 command receipts with independently checked log
hashes. The code/CLI contracts were read directly; no provider calls were made.
`planned-repository-paths.json` separates the chain's writes from root-owned
source/promotion/receipt/export/selector work and the preserved historical files.

## Required ordering

1. Root completes the reviewed guarded three-owner source transaction. Preserve
   the actual source log and its beforeimages. Run `just sync-curated` after the
   per-record edits. Root runs the merged Claw producer in its isolated copy,
   inspects/validates the candidate, then promotes only the approved canonical
   rows and the two retired Rule K allowances through the bounded writer.
2. Root publishes the native mapping-change receipt with all three owner entries,
   no scientific approval, verified sequence 17 and the actual original canonical
   beforeimage. Root advances only `REVIEWED_SOURCE` in the assembler to the
   promoted canonical hash. The driver checks these conditions and refuses an
   unexpected chain base instead of silently adapting it.
3. Run the driver's `build` stage. It executes canonical QC, mapping assembly,
   reviewed SSSOM export/QC, full KGX export, semantic review assembly, native
   semantic integrity, supported KGX export/QC/schema validation, then the native
   unchanged-cohort refresh and companion export/validation. It obtains the
   companion manifest hash from the newly written bytes; no old hash is reused.
4. Review `verified-output.json`, the native logs and diffs. Root makes the exact
   companion pointer changes below, documents the measured counts and shifts,
   refreshes flat/visualization products, and completes the separately reviewed
   merged-Claw unified generation and provenance stamp. Do not regenerate
   occurrence membership broadly; the source transaction already migrates the
   exact approved historical membership.
5. Run `gates`. It checks the final pointers and output assertions, runs receipt,
   semantic, companion, routing, writer and unified regressions; full `just qc`;
   CURIE/product-label checks; unified rejection/freshness checks; then the full
   test suite. Root retains the independent final-state/head review and PR/merge
   workflow. This script does not commit, mutate GitHub or merge anything.

The default invocation prints commands and scope without writing. These are the
actual execution forms after root has reviewed this package and selected the
real receipt paths (the variables must be set to the root's existing receipts):

```bash
python3 output/approved-plan-20261101T031134Z/step3-native-chain-plan/native_chain.py \
  build --execute --tag step3-chain-v1 \
  --source-log "$step3_actual_source_log" \
  --mapping-receipt "$step3_published_mapping_receipt"

# After root's pointer/docs/export/unified work:
python3 output/approved-plan-20261101T031134Z/step3-native-chain-plan/native_chain.py \
  gates --execute --tag step3-chain-final-v1
```

The script locates the isolated worktree and run helper relative to itself, so
the example command is launched from the original repository root. A published
mapping-receipt argument is relative to `step3-mim`; the actual source log is an
absolute path. Every native command is run by `RUN/run_step3_mim.py step3-mim`
under its owned environment. Native command receipts and logs use unique tags
under `RUN/logs`; driver execution proofs and beforeimages use a new directory
under this package's `executions/`. A failure stops immediately and retains all
partial products/logs. Nothing is deleted or silently reused. If an output
already exists, root must inspect it and choose a reviewed continuation; reruns
must not erase evidence to satisfy the absence check.

## Exact output paths and selectors

The full KGX path must remain `output/mim-kgx-710-full`: the existing
`qc-supported-kgx.yaml` rebuilds exactly that bundle before validating the
content-bound report. The driver requires that path to be absent at the start.
It creates `output/mim-reviewed-sssom`, `output/step3-supported-kgx` and
`output/step3-ingredient-bundle`; all are immutable/new native output directories.

The new companion is
`reports/ingredient_bundle_20261101_carnitine1004/`. The native refresh flags are:

```bash
uv run --frozen python scripts/refresh_unchanged_cohort.py \
  --baseline 99fe4b44d78126d78041a69eeb366c52bedf0caa \
  --prior-review reports/ingredient_bundle_20261101_ncit875/review.json \
  --output reports/ingredient_bundle_20261101_carnitine1004/review.json \
  --receipt reports/ingredient_bundle_20261101_carnitine1004/dependency-refresh.json \
  --prior-copy reports/ingredient_bundle_20261101_carnitine1004/prior-review.json
```

The output parent must exist and all three destinations must be new; the driver
creates the new parent just before invoking the native guarded refresher.
It preserves the previous cohort, its claims and its historical review bytes.

After that refresh/export validates, root advances these current selectors from
`reports/ingredient_bundle_20261101_ncit875/review.json` to
`reports/ingredient_bundle_20261101_carnitine1004/review.json`:

- `tests/test_ingredient_bundle.py:26`, only the `REVIEW` constant.
- `.github/workflows/qc-reviewed-sssom.yaml:38`, only the `--review` argument.
- `docs/INGREDIENT_BUNDLE.md`, current successor link, export example and
  next-refresh `--prior-review` example; add the new successor README using the
  actual refresh audit, including its measured locator changes.

The manifest binds exact beforehashes. The gate stage proves the test and CI
changes are exactly one replacement against baseline bytes. Root explicitly
confirmed that this owned Step 2 CI selector advance is authorized and necessary;
the earlier blanket workflow protection was an overly broad preflight assumption.
`qc-evidence.yaml`, the other workflows, `.vendored_canon_ref`, and the Intel
workflow-review files remain hash-protected. No historical cohort test fixture,
old companion, explicit scientific approval plan or release hold is restamped.

Root also updates `docs/SSSOM_RELEASE.md` and
`reports/sssom_completion_20260921/README.md` from the actual new canonical/review
hashes and counts, preserving their historical sections. The latter's complete
graph finding count must be recomputed, not copied from this preparation.

The successful Step 2 flat-publication commands, applicable after this bounded
source change, were:

```bash
just export-indexes export-lists export-browser
uv run --frozen python scripts/refresh_visualization_metadata.py
just check-visualizations
```

The native visualization refresher changes stable node metadata while preserving
coordinates; its actual diff still needs review. These root-owned commands are
not silently run by this dependency driver. Root owns the unified build, bounded
publication, provenance stamp and their exact producer/input evidence separately.

## Expected changes and release boundaries

The captured current baseline has 2,986 mappings: 1,740 SUPPORTED and 1,246
WITHHOLD. Five carnitine salt rows are already withheld. Their approved
replacement is one withheld exact NCIT:C216679 row. The one previously supported
NLDM mapping is withdrawn because its owner changed. The intended final partition
is therefore **2,982 mappings: 1,739 supported and 1,243 withheld**. The driver
requires this exact partition and verifies that the rejected duplicate has no
canonical ownership. It never treats the new source identity as release approval.

`nldm-before.json` captures the actual pre-change decisions, row, owner hash and
payload hashes. It proves 64 approved component assertions, four approved
nutritional-role assertions and one supported mapping. After this change:

- All **69 approvals withdraw**: 68 nonmapping assertions become OPEN and the
  mapping becomes WITHHOLD / graph OPEN.
- Component position 59 is the only changed nonmapping payload; the other
  **67 payload hashes remain identical**, with changed owner hashes.
- The supported graph excludes all 69 claims, and its separate unsupported
  backlog preserves all 69. The full graph's scientific release remains FAIL.
- Native semantic integrity must pass. The command intentionally omits
  `--require-pass`: it verifies integrity of the honest full scientific FAIL,
  rather than clearing or weakening unresolved science. Counts are recorded
  from the newly generated review. With this bounded assertion scope, the
  anticipated full graph has 4,487 assertions, 2,151 APPROVED and 2,336 OPEN;
  the script reports actual counts for review rather than restamping them.

The companion's 20 owners do not intersect the three changed owners. It keeps
all **51 claims** (20 mappings, 18 identifier annotations, three products and ten
occurrences), all decisions, complete selected mapping proofs and owner bytes.
Only proven global dependency hashes and any source-position/evidence-key
relocations change. The number of relocated selections is calculated from the
new audit, not copied from #875's 14 shifts. No Step 6 approval port or bypass is
part of this chain.

This package is an execution preparation, not a completed scientific review,
an application receipt, a supervisor binding or evidence that future gates pass.
