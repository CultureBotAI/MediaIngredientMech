# Step 4 native dependency chain — implementation preparation

This run-owned driver adapts the already executed Step 3 native chain to the approved lithium-salt correction. Its author is an implementation author for Step 4, not its independent reviewer. The separate `step4_design_review` agent must review the driver and actual execution. No source application, canonical promotion, receipt publication, export, dependency rebuild, Git operation or scientific approval was performed while preparing this directory.

The actual durable base is `838d0c2627552b0094545ebb580b5bb9b1a84d57`, worktree `../step4-mim`, branch `fix/lithium-glycerophosphate-1005-20261101`. `prepared-inputs.json` binds the run helper, context, approved plan and live [decision comment 6556888392](https://github.com/CultureBotAI/MediaIngredientMech/issues/1005#issuecomment-6556888392), the existing 17 mapping receipts, native implementation inputs and protected files. Original baseline content is read from this durable Git commit; no corpus, full graph, backlog or duplicate evidence archive is copied into fixtures.

`native_chain.py plan` prints the supported commands without executing them. `preflight` checks the unchanged initial base and reports three held target mapping rows, one OPEN provisional role and two OPEN historical findings. It is an initial-state check: after the root applies the owner correction, its original-source check is expected to fail. `verify` is a read-only final-state check that requires the completed source receipt and the next published mapping receipt. None of these three modes writes execution artifacts or invokes a mutating producer.

The `build`, `exports` and `gates` stages require explicit `--execute` and a unique `--tag`. Without `--execute`, they only print the plan. Only the root should trigger actual execution after the relevant author and independent review have cleared the source, candidate promotion and receipts.

## Supervisor-owned prerequisites

The driver never applies the owner writer, promotes canonical rows, creates receipt 18, advances `REVIEWED_SOURCE`, edits selectors or documentation, or rebuilds/stamps the unified mapping. Those remain separate reviewed root operations.

Before `build`, the root must provide:

1. A regular complete applied source receipt with exactly one owner transition for `data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml`, no approval, the exact baseline owner/canonical/Rule K hashes, and the current owner output hash.
2. Completed reviewed bounded promotion: three lithium subject rows become two, with only the free-CAS exact identity removed. All unrelated canonical row bytes stay identical, and metadata date fields equal the actual newest row date. Both old target stamps, historical source tokens and the broad-row #390 explanation remain. The local row has the native primary-registry explanation and procurement `CAS:17989-41-2` display token; the broad row has no parent alias or CAS token.
3. Exactly the one approved Rule K pair removed, with every other baseline byte preserved.
4. A native mapping receipt published exclusively by the root. The driver derives the next sequence from the verified contiguous old chain, requires its tail to match the merged canonical preimage, then requires sequence 18, exact one-owner context, issue #1005, two changed/one removed/zero added rows and target-relative alignment `[first, null, second]`. The actual receipt path set must be exactly the old 17 plus this one new direct member; ignored/nested additions are not hidden.
5. An assembler source pin changed only by the exact old-to-new canonical SHA replacement. No unrelated assembler code edits are accepted.

The source writer uses the existing validated publication and its own receipt/backup/no-op defenses. This driver checks completed receipt and current output bindings, but does not replace that writer's transactional guarantees. It checks the maintained individual-record membership including ignored/nested YAML and preserves every other owner's baseline bytes. There is no new Li stoichiometry, role evidence or scientific approval in this layer.

## Commands and execution order

Use the maintained Python 3.13 environment and `run_step4_mim.py` profile `step4-mim`. The examples below are templates; replace the absolute run path and actual receipt paths. They have **not** been executed as a production chain during preparation.

```text
RUN/envs/mim/bin/python RUN/run_step4_mim.py step4-mim UNIQUE-plan -- python RUN/step4-native-chain-plan/native_chain.py plan
RUN/envs/mim/bin/python RUN/run_step4_mim.py step4-mim UNIQUE-preflight -- python RUN/step4-native-chain-plan/native_chain.py preflight

# Only after the independently reviewed source/promotion/native receipt are complete:
RUN/envs/mim/bin/python RUN/run_step4_mim.py step4-mim UNIQUE-dispatch-build -- python RUN/step4-native-chain-plan/native_chain.py build --execute --tag UNIQUE-build --source-log ABS_COMPLETE_SOURCE_LOG --mapping-receipt reports/sssom_completion_20260921/mapping_changes/ACTUAL_RECEIPT.json
RUN/envs/mim/bin/python RUN/run_step4_mim.py step4-mim UNIQUE-verify -- python RUN/step4-native-chain-plan/native_chain.py verify --source-log ABS_COMPLETE_SOURCE_LOG --mapping-receipt reports/sssom_completion_20260921/mapping_changes/ACTUAL_RECEIPT.json
RUN/envs/mim/bin/python RUN/run_step4_mim.py step4-mim UNIQUE-dispatch-exports -- python RUN/step4-native-chain-plan/native_chain.py exports --execute --tag UNIQUE-exports --source-log ABS_COMPLETE_SOURCE_LOG --mapping-receipt reports/sssom_completion_20260921/mapping_changes/ACTUAL_RECEIPT.json

# Root separately proves/refines the companion selectors/docs and executes the
# native unified replay with zero row changes before any freshness stamp.
RUN/envs/mim/bin/python RUN/run_step4_mim.py step4-mim UNIQUE-dispatch-gates -- python RUN/step4-native-chain-plan/native_chain.py gates --execute --tag UNIQUE-gates --source-log ABS_COMPLETE_SOURCE_LOG --mapping-receipt reports/sssom_completion_20260921/mapping_changes/ACTUAL_RECEIPT.json
```

`build` runs native canonical QC, mapping-review assembly, reviewed SSSOM export/QC, full KGX export and semantic build/integrity, supported KGX export/QC and supported SSSOM schema validation. It refreshes the unchanged companion from `reports/ingredient_bundle_20261101_carnitine1004/review.json` into `reports/ingredient_bundle_20261101_lithium1005/`, exports it and validates the actual generated manifest hash. Existing output directories cause refusal; failed or partial outputs are preserved for root review, not silently overwritten or rolled back.

`exports` runs maintained indexes/lists/browser producers, then `scripts/refresh_visualization_metadata.py` and strict visualization currency checking. The maintained metadata refresher is intended for targeted curation and preserves coordinates; this does not require a full embedding/layout rebuild. Any unexpected removal/update still needs independent final product-delta review.

Before `gates`, the root must advance only the exact companion selector occurrence in `.github/workflows/qc-reviewed-sssom.yaml` and `tests/test_ingredient_bundle.py`, and document the actual unchanged-cohort proof. The driver itself changes neither selector. It requires `UNIFIED_INGREDIENT_MAPPING.tsv` to remain byte-identical to the merged baseline; the root's native zero-row rebuild and guarded provenance stamp are separate prerequisites proven by the native freshness gate.

`gates` runs the focused writer/receipt/mapping/semantic/companion/unified tests, `just qc`, CURIE/product labels, unified rejection/freshness, native writer audit and the full test suite. The actual logs determine counts, warnings and coverage; this plan does not predict successful outcomes or infer execution from collection. No coverage percentage is invented.

## Before/after guarantees

- Both surviving lithium mappings remain WITHHOLD. All unrelated mapping decisions are compared as complete dictionaries after excluding **only** their native `source_position` and `evidence_key`; each side resolves its own canonical triple. A row hash, owner, disposition, reason or evidence change is refused.
- The provisional CARBON_SOURCE payload, reasons and evidence remain unchanged and OPEN under the new full-owner hash. Both historical mixed-identity/role and role-evidence findings remain OPEN, with only their current-owner hash allowed to change. No blanket finding retirement is allowed.
- Every unrelated nonmapping assertion and finding remains exact. Unrelated mapping assertions are aligned by full canonical triple; only native assertion ID, current canonical source hash and row position may move, while payload hash, disposition, reason and evidence stay exact. The current source hash must be the actual canonical hash.
- Existing NLDM withdrawals are preserved through these whole-cohort comparisons. This step does not carry back approvals from unchanged payloads or alter the approval model. The full scientific-release verdict remains FAIL; actual counts are measured rather than copied from Step 3.
- The supported graph contains none of the target's held claims. Its unsupported backlog retains exactly the two mappings and the provisional role.
- The companion's existing 20 owner hashes and 51 claim decisions remain exact. The target owner is excluded; locator movements are counted from the native dependency-refresh receipt. No new approval is added.
- The preceding 17 mapping receipts, native source modules, explicit review plans, protected workflow/pin files and Intel reviews remain hash-bound. Source/code/schema/profile membership, current owner/canonical/Rule K, receipt membership and source log are rechecked before and after every native command. This detects drift across the sequential chain; it is not a claim of atomic isolation against arbitrary external writes. Each native writer retains its own locking behavior.

Execution is intentionally restricted to the prepared branch at the durable base, before a feature commit. Post-commit and merge-group verification belong to the separate independent reviewer. Each executed stage retains `start.json`, actual command logs and a success receipt only after final verification. A failed command leaves its evidence and partial outputs for explicit recovery.

## Preparation checks and limitations

The first read-only preflight and printed plan passed before root source application. The initial offline suite passed 34 tests, covering valid three-to-two transformation and date handling, preservation of hash-prefixed plain-TSV names, legitimate mapping/assertion locator movement, and refusal of wrong identity, restored CAS row, alias re-entry, stamp/comment/source loss, changed unrelated payload/owner/reason/evidence/approval, provisional-role approval and blanket finding retirement. Final source-bound reruns are indexed in `preparation-receipt.json`.

These are bounded implementation checks, not execution of a production dependency chain or independent scientific review. Complete native replay and final generated-state checks remain to be run by the root and reviewed independently. No full fixture corpus, graph or backlog was copied. No paid provider, source recapture, GitHub mutation or shared-checkout edit occurred.
