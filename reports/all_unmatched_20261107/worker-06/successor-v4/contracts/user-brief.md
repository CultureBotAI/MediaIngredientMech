# MIM complete unmatched-name review with ten M5 codex-work workers

## Explicit user authorization and objective

The user requests a goal on the existing MIM session to review **all 1,330 CultureMech names unmatched to MIM**, together with **all remaining KG-Microbe unmapped chemical cases**, using **10 parallel codex-work sessions**, subagents, and other effective division-of-work strategies, all on M5. This explicitly authorizes the ten-worker launch and use of the work account. Do not ask again merely because there are more than three tasks or one repository has multiple isolated worktrees. Ordinary later sign-in, trust, approval and update prompts retain their own rules.

Carry this goal through the complete corpus: evidence-backed review, justified MIM curation, native mapping/SSSOM regeneration, validation, independent review, and review-ready PRs. Every source case must have a documented outcome, including unresolved cases with precise missing evidence. Do not equate completion of review with forced mapping or release approval. No merge or new KG-Microbe production rebuild is authorized.

## Preserve the current work

Finish and retain the final validation/review evidence for PR #1158 without merging it. Preparatory read-only queue construction can proceed while its final CI finishes. Freeze a reviewed baseline that includes the accepted current candidate changes; record the exact commit and PR dependency if it is still unmerged. Do not rebase/reset or overwrite that running work. Existing scientific holds remain in force until the correct evidence-backed review resolves them.

Relevant current M5 roots:

- MIM coordinator: `/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech`.
- Current task: MIM `.temp/kgm-unmapped-20261107/`, with its isolated `worktree`, source audit, reconciliation ledgers and candidate exports.
- CultureMech: `/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech`.
- Current KG candidate: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe-mim-1788-20261107`.
- Claw orchestration: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw`.

Reverify all identities and source generations before using them. Keep existing CultureMech and KG-Microbe source checkouts/outputs read-only during review; take content-bound snapshots. Do not replace mappings used by running KG validation. No changes to unrelated fleet sessions.

## Freeze and reconcile the full queue

The current unified rebuild scanned 15,915 CultureMech recipe files at clean revision `199cd9191881e8e929cd95ea0ed13aabe388e58c`, yielding 4,170 names: 2,840 matched to MIM and 1,330 unmatched. Verify this against current upstream and the exact baseline. Use the native generator's actual unmatched criterion; preserve every original row, recipe occurrence and source identifier. The generated `output/ingredients_list.tsv` has different aggregation semantics from the 4,170-name unified table; do not substitute its row count or assume modification time establishes currency.

Use current KG chemical queues and the existing 549-candidate source audit as the starting point for KG residuals; recalculate which remain unresolved after #1158. Include complete low-frequency MicrobeDecoder compound cases, MediaDive supplied-form/material cases and metatraits compound placeholders. Trait/taxon failures and the 632 unknown MediaDive endpoints are not automatically chemical candidates.

Create an immutable union ledger, preserving source-specific cases and linking duplicates safely. A shared spelling does not establish shared chemical identity. Keep stock concentrations, hydrates, salt stoichiometry, stereochemistry, mixtures, biological products and generic classes distinct. Record source commits, generator/mapping versions, hashes and current counts. Account for changes from the quoted 1,330 explicitly; do not drop cases because they are already withheld, ambiguous, duplicated, rare, or inconvenient.

## Ten external workers, with subagents

You are the MIM coordinating session. Use the M5-local claw boss workflow and existing GUI-login tmux server for worker ownership, metadata locking and persistence. Read the current claw `.claude/skills/boss/SKILL.md` and fleet control contract. The user's `codex-work` requirement supersedes the skill's illustrative `claude` command. Use ten actual external Codex sessions, not ten in-process subagents presented as sessions. Use the existing codex-work wrapper with `--no-daemon`, verify the work account with supported login-status output, retain normal permissions, and record each effective model/effort. Do not switch to a personal account or copy credentials. Do not use disabled experimental openclaw agent/pipeline live launch paths.

Each worker gets a fresh conversation, a unique topic branch and isolated worktree, exact input shard, durable prompt file and output directory. Use durable state under claw workspace, repository `.temp/`, or `/Users/marcin/agent-work/`; never use /tmp for sessions or unpushed work. Save helper scripts in their owning repository with purpose/input/output/date provenance. Release short metadata locks before workers execute. Do not use `resume --last` or reuse occupied sessions.

Partition the full union into **ten disjoint, reasonably balanced shards**, clustering related names/material families so one worker can resolve shared evidence efficiently. Retain one accountable owner per source case and record cross-shard dependencies. Give each worker subagent-assisted primary-source research and separate skeptical review where useful. Cache reusable ontology/supplier evidence and share immutable evidence references; prevent uncontrolled spawning of additional external sessions beyond these ten.

Run exactly one worker through an initial bounded case end to end using the same launcher/account/environment/output path the batch will use. Verify its assigned input, actual Codex acceptance, nonempty durable evidence/decision artifact, validation and review. Complete the applicable branch/PR canary workflow. Then continue that worker's shard and launch the other nine. This is one ten-worker review campaign; do not stop after the canary or after writing a plan. Verify all ten accepted their tasks and expose their session/PID/worktree/output identities in the worker ledger.

Before every input, inspect the actual worker TUI and stop at sign-in/trust/approval/update prompts; do not answer those implicitly. Do not launch a second server from SSH. The owning M5 orchestrator controls its worker sessions; XMechBay observes their state and dispatches only to you. Preserve observability through named tmux sessions and existing supported viewer/log mechanisms.

## Scientific review and integration

Every case needs a disposition supported by evidence: existing identity/alias; new distinct ingredient; specific-form correction; broad parent relation only; mixture/product/stock context; malformed/nonchemical source token; or unresolved with a precise next requirement. Follow MAPPING_SEMANTICS.md, the LinkML schema, current native curation skills and record-review contracts. Verify candidates against authoritative ontology records and primary source/supplier evidence. Search/LLM suggestions alone are not approval.

Workers may prepare isolated curation proposals and evidence, but do not concurrently regenerate or overwrite shared canonical artifacts. The coordinator integrates reviewed non-conflicting changes in an isolated integration branch, resolving cross-shard identity conflicts first. Preserve raw labels, source-specific scope and curation_history; synchronize aggregate and per-record YAML correctly. New or changed owners require the content-bound mapping review workflow; do not transfer inherited support to changed bytes or treat successful QC as scientific release approval.

Regenerate the unified mapping and SSSOM with supported native commands. Preserve coherent supported/withheld/disposition/manifest artifacts and local registry semantics, plus the unified TSV/provenance pair. Run appropriate focused tests, required repository gates and final full validation. Review the final diff independently, file review findings, and open review-ready PRs. Preserve branch dependencies on #1158 as needed. No merges, person mentions, external messages, or downstream graph rebuild.

## Progress and completion evidence

Persist a coordinator ledger with all ten worker IDs, source/shard hashes, account/model, branch/worktree, session/PID, reviewed/remaining counts, output paths and actual blockers. Save it early, with a short README or status JSON in a discoverable task root, and report that path in your next progress update.

Final accounting must prove every input case was reviewed exactly once or reconciled through an explicit duplicate-group disposition. Report source-case totals separately from distinct names, ingredient identities and SSSOM rows; distinguish scientific review from structural validation. Deliver before/after CultureMech and KG residual counts, new identities/aliases, supported/withheld changes, unresolved reasons and linked issues, immutable candidate export hashes, validation and independent-review evidence, and PR links. Report partial progress honestly if account limits or external evidence block work; do not claim completeness from sampled reviews.

Begin now by acknowledging the broader goal, preserving #1158's checkpoint, constructing the frozen queue and preparing the first worker. Continue through fan-out and the whole review campaign without waiting for another task approval.
