# Approved-plan workflow audit

Read-only audit of isolated `step1-mim` and `claw`; this file is the only audit output written. No Git refs, code, data, GitHub objects, paid providers, goals, or cycle state were changed. Searches for workflow/receipt references included ignored and hidden files.

## Observed sources and remote policy

- Approval: `/Users/marcin/xmb-instructions/mim-approved-plan-20261101.txt`; recorded plan digest and `supervisor_binding: null` in `plan-context.json`.
- Native MIM authority: `AGENTS.md`, `justfile`, `docs/MERGE_QUEUE.md`, `docs/INGREDIENT_BUNDLE.md`, `docs/SSSOM_RELEASE.md`, maintained producers and CI workflows.
- Claw authority: `AGENTS.md`, `docs/guides/MERGE_QUEUES.md`, `.claude/skills/cross-mech-sync/SKILL.md` sections E–F, `docs/guides/MECH_SESSION_WORKFLOWS.md` closure contract. The backlog prompt's sections 3–4 describe independent final-head review, filing confirmed findings, green dependency-ordered merges, and verified cleanup; existing user authorization is sufficient.
- Live `gh api repos/CultureBotAI/MediaIngredientMech/commits/main --jq .sha` returned `2add44fbfe37544218d2f4daeb322b35debc5dd4` during this audit. Claw returned `16fd7c9484d98b14a53aec55616d26dae70a0af7`.
- Live effective rules for both repositories require native queues with `merge_method: SQUASH`, `grouping_strategy: ALLGREEN`, and one entry merged at a time. MIM `delete_branch_on_merge` is false; `allow_auto_merge` and `allow_squash_merge` are true. These observations must be refreshed immediately before merging.
- MIM required job contexts observed: `check`, `history`, `id-label-gate / label-correspondence`, `instruction-refs`, `pytest`, `qc-component-partonomy`, `qc-duplicate-ids`, `qc-evidence`, `qc-flat-coverage`, `qc-sssom`, `roundtrip`, `validate-strict`, `vendored-sync`.
- Claw required contexts observed: `fleet-audit`, `history-round-trip`, `id-label-contract`, `pytest`. Do not change queue configuration or reduce requirements.

## Exact queue path and evidence

Run terminal `gh` with explicit `-R`; Git operations use the isolated clone/worktree and explicit HTTPS URL or its verified HTTPS origin. Both remote reads succeeded from this Terminal environment. Do not edit global Git/auth settings or the shared M5 claw checkout.

Before enqueueing, save final-head validation logs, independent adversarial review, confirmed-finding issue URLs and dispositions, PR file/scope review, and these fresh reads:

```sh
gh api "repos/$TARGET_GITHUB/rules/branches/main"
git -C "$WT" fetch origin refs/heads/main:refs/remotes/origin/main
git -C "$WT" rev-parse HEAD
git -C "$WT" ls-remote origin "refs/heads/$BRANCH"
gh pr checks "$PR_NUMBER" -R "$TARGET_GITHUB"
gh pr view "$PR_NUMBER" -R "$TARGET_GITHUB" --json state,isDraft,baseRefName,headRefName,headRefOid,headRepository,mergeable,mergeStateStatus,statusCheckRollup,files
```

Require a non-draft open PR targeting `main`, correct source repository/branch, identical local/remote/PR/reviewed heads, `MERGEABLE`, scoped files, and green checks. User also requires `just qc`, including `qc-sssom`, and independent final-head review even though remote policy's minimum review count is zero. Do not manufacture a GitHub approval from the author or impersonate a reviewer.

```sh
gh pr merge "$PR_NUMBER" -R "$TARGET_GITHUB" --match-head-commit "$REVIEWED_HEAD"
```

The active queue provides **squash**; no merge strategy flag is required. Do not use `--admin`, direct merge REST endpoints, or `--delete-branch`. A queued/auto-merge-enabled response is not a merge. Preserve the worktree through queue failure/ejection. Save merge-group SHA and corresponding `merge_group` Actions evidence; ordinary PR checks alone do not prove the combined candidate passed. Diagnose infrastructure failures before one retry; repeated failure requires fixing the cause.

Main advancing after review is **not** itself a reason to rebase a queued PR: the queue validates current main plus queued changes. Repair actual conflicts and repeat validation/review for any changed branch. The approved plan separately requires the **next** PR to start from the previous merged main; create that fresh branch only after the preceding merge completes. Never rewrite an old PR branch.

After queue completion:

```sh
gh pr view "$PR_NUMBER" -R "$TARGET_GITHUB" --json state,baseRefName,headRefName,headRefOid,headRepository,mergeCommit,mergedAt
```

Require `MERGED`, exact reviewed identity/head and a nonempty merge commit. Record these responses and post-merge integrity evidence before declaring success. Recheck remote head and delete only the reviewed branch. The documented safe deletion is:

```sh
git -C "$WT" push origin --force-with-lease="refs/heads/$BRANCH:$REVIEWED_HEAD" ":refs/heads/$BRANCH"
git -C "$WT" ls-remote --exit-code --heads origin "$BRANCH"
```

The first command is an exact-old-head **deletion**, not a history rewrite; the lease protects another writer's new commit. It is justified by the user's explicit delete-branch instruction. Never use it to publish/rewrite branch commits. Require the second command's status **2** (no matching ref); an API/network error is not absence. If the branch moved, preserve it. After clean-worktree and exact-head checks, repository-native cleanup uses `git worktree remove "$WT"` without force and `git update-ref -d "refs/heads/$BRANCH" "$REVIEWED_HEAD"` from its controlling repository. Preserve runtime review/log artifacts outside the removed worktree.

## Step 1 native regeneration and receipt ordering

Do not copy the old generated artifacts as authoritative. The five approved cherry-picks include stale exports/review material and the first contains the explicitly excluded claw pin hunks. Preserve current `.github/workflows/qc-evidence.yaml` and `scripts/.vendored_canon_ref`. Use final intended per-record edits as source, then:

```sh
just sync-curated
just export-indexes
just export-lists
just export-browser
just generate-visualizations
just rebuild-unified "$ISOLATED_CLAW" "$VERIFIED_CULTUREMECH"
```

`rebuild-unified` runs the claw builder with both root environment variables, then `check-unified-rejections`, then stamps provenance. It needs claw's own environment at `$ISOLATED_CLAW/.venv/bin/python`; MIM's environment is not a substitute. Inspect diffs after synchronization and each output group. Verify all three user invariants directly against the final products: no REJECTED row with empty `mim_id`; no `kgmicrobe.compound` row carrying CHEBI; all nine named merge tombstones have `representative:`.

Review receipts must be append-only and content-bound. The assembler's fixed `REVIEWED_SOURCE` is the current end of the verified SSSOM receipt chain, not permission to restamp scientific approvals. Determine whether final SSSOM bytes or existing owner bytes actually changed before adding a link. Changes outside existing review owners can leave the standalone mapping review unchanged. Changed owners are not approved by receipt generation, even for formatting, history, graphs, or occurrence counts.

For an actual mapping/owner transition, preserve exact prechange SSSOM bytes and a truthful apply log; use a new receipt name and the next verified sequence:

```sh
uv run --frozen python reports/sssom_completion_20260921/mapping_changes/make_receipt.py \
  --batch "$BATCH" --sequence "$NEXT_SEQUENCE" --issue "$ISSUE_URL" \
  --scope "$SCOPE" --before-sssom "$BEFORE_SSSOM" --apply-log "$APPLY_LOG"
```

The apply log's `records` entries require `source_record`, `shape`, exact `before_yaml_sha256`/`after_yaml_sha256`, `change`, and `verification`. The writer refuses mismatching postimage hashes but does **not** reserve its receipt output exclusively; verify the target does not exist before invoking it. Never overwrite historical receipt bytes. Its result has `approval: NONE`; touched rows remain WITHHOLD until fresh mapping-specific approval. Keep the assembler's end hash consistent with the verified new chain; changing only that constant cannot fix a broken chain.

Then regenerate and independently check the current complete mapping disposition review:

```sh
uv run --frozen python reports/sssom_completion_20260921/assemble_review.py
uv run --frozen python reports/sssom_completion_20260921/assemble_review.py --check
just export-reviewed-sssom reports/sssom_completion_20260921/review.json output/step1-reviewed-sssom
just qc-reviewed-sssom reports/sssom_completion_20260921/review.json output/step1-reviewed-sssom
```

If this fails due to old explicit approvals on changed owner bytes, stop that invalid transition and report the exact owner/approval conflict. Do not retrofit section-refresh receipts or copy new hashes into historical approval evidence. Step 6 owns the approval supersession work.

Build the semantic current review from the **canonical relative full bundle path**, because CI reconstructs that exact path:

```sh
just export-kgx output/mim-kgx-710-full
uv run --frozen python reports/semantic_review_20260921/resolution/build_review.py --bundle output/mim-kgx-710-full
uv run --frozen python -m mediaingredientmech.validation.semantic_release --root . --report reports/semantic_review_20260921/resolution/current-review.json
just export-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/step1-supported-kgx
just qc-supported-kgx reports/semantic_review_20260921/resolution/current-review.json output/step1-supported-kgx
```

All exporter output directories must be new; preserve any prior run under a distinct path before rebuilding. `build_review.py` also regenerates assertion/finding dispositions and lineage. Semantic integrity success is distinct from the complete graph's scientific `FAIL`; do not use `--require-pass` to demand resolution of the whole historical scientific backlog.

If the standalone mapping review's dependency hashes changed, create a new immutable companion successor using the maintained command:

The baseline companion's `record_inputs` plus `inputs` have **zero** path intersection with the file changes in approved tombstone commit `e30b6d0` (measured using `git show` and `git diff-tree` during this audit). Thus those intended tombstone edits alone do not require changing a selected companion owner. If the standalone review also stays byte-identical, validate the existing companion instead of manufacturing a successor. This does not exempt regeneration of semantic `current-review.json`, whose owner inventory covers all ingredient records.

```sh
uv run --frozen python scripts/refresh_unchanged_cohort.py \
  --baseline 2add44fbfe37544218d2f4daeb322b35debc5dd4 \
  --prior-review reports/ingredient_bundle_20261101_followup/review.json \
  --output "$NEW_REPORT_DIR/review.json" \
  --receipt "$NEW_REPORT_DIR/dependency-refresh.json" \
  --prior-copy "$NEW_REPORT_DIR/prior-review.json"
uv run --frozen python -m mediaingredientmech.export.ingredient_bundle export \
  --review "$NEW_REPORT_DIR/review.json" --output output/step1-ingredient-bundle
uv run --frozen python -m mediaingredientmech.export.ingredient_bundle validate \
  output/step1-ingredient-bundle --manifest-sha256 "$EXPORTED_MANIFEST_SHA256"
```

The parent directory must already exist; all three destinations must be distinct, new paths. The explicit baseline must contain the prior review and pinned inputs. The helper proves selected owners, rows, claims, decisions, evidence, schema/profile and semantic metadata are unchanged before allowing global dependency/date/version changes. A changed selected cohort needs fresh scientific review. Preserve both historical companion directories. After reviewing the new receipt/export, explicitly update the selector in `.github/workflows/qc-reviewed-sssom.yaml` and current `docs/INGREDIENT_BUNDLE.md`; do not touch the excluded qc-evidence workflow. If no companion dependency changed, prove current companion export still validates and avoid unnecessary successor creation.

Run focused regression tests, `git diff --check`, `just qc`, plus `check-unified-rejections`, `check-unified-freshness`, reviewed-SSSOM, supported-KGX and selected companion export/validation. `just qc` includes core data gates but not these separate release-review jobs. The mapping assembler/current-review/companion sequence must finish before final-head review and CI; subsequent byte changes invalidate that final-head evidence.

## Identity and closure records

This approved ordered plan is not a supervisor goal/cycle. `plan-context.json` explicitly records no binding. Retain plan source/digest, step number, repository, base/head/merge SHAs, PR/issue URLs, command/log hashes, independent review identity/artifact, queue candidate/runs, and deletion verification in this run's ordinary audit records. Do not invent `run_id`, `cycle`, `stage`, `workflow_sha256`, native goal identity, or supervisor `completion.json`.

The supervisor closure format applies only when an authentic current `status.json` supplies its exact binding/template. No such binding was supplied to this audit. Do not start goals/cycles or register these PRs to a guessed monitoring session. The user's per-merge one-line report and final summary remain the completion reporting contract.
