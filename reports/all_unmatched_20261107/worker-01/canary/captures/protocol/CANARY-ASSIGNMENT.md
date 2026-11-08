# Worker 01: bounded source-case canary

Read WORKER-CONTRACT.md in this directory and the full authorized brief it links.
This assignment is the first, single-case phase of the ten-worker campaign. The
other 187 cases in your shard remain assigned to you but are not this phase.

Read `frozen-baseline.json` and verify your actual worktree HEAD equals its
`worker_base_commit`. If it is missing or different, report the mismatch before
work. Preserve the explicit dependency on MIM PR #1158. The immutable queue was
derived against the implementation content identified in that baseline receipt.

Your worker slot is `w01`; your branch is
`review/all-unmatched-w01-source-review-20261107`. Your unique tmux session is
recorded by the coordinator, and must not be used to control any other session.

Your full shard is `queue/preliminary-v5/shards/shard-01.json`, SHA256
`abba82441b807cc6bf476a69de1c19a794dd213991fc2c5f18b4c6797b73c597`.
Review only this case in the canary:

- `KG_CASE:e431bbfe8e78c226a9a06d038b7944f91e4580b44fe5b9e2c83d0e236c6d23cf`
- Source ID: `mediadive.ingredient:1944`.
- Exact extracted case: `queue/canary-1944-case-v1.json`, SHA256
  `2968f96971a4597464a2938f93c9ca83b509edfa536fd5d0f5d8a00318edfb51`.
- The case retains a blank compound label and preparation text in the raw
  attribute. The source ID and complete original fields must survive your review.
  The source-path/hash/selector are in `queue/canary-recommendation-v1.json`.

Determine the source context using the exact frozen raw record, relevant original
recipe/source evidence and current MIM. Look up primary MediaDive context and
supplier/ontology evidence where relevant. A stock/product/malformed-source hold
may be the correct result, but the coordinator has not decided its identity or
outcome for you. Do not guess a yeast-extract owner or alias from the attribute.
Explain what evidence would settle any unresolved identity and where a correction
would belong. Check live related GitHub issues and their comments before filing
any deduplicated finding; the read-only starting index is in
`preflight/github-context-v1/`.

Publishable output belongs under your own worktree's
`reports/all_unmatched_20261107/worker-01/canary/`. Private output belongs under
your own worktree's `.temp/all-unmatched-worker-01/`. Save the acceptance, exact
case decision, evidence, proposal or no-change receipt, progress and independent
review required by WORKER-CONTRACT.md. Use the coordinator's structural output
contract/auditor if available, and report if it conflicts with actual source
shape. Never manufacture a native MIM owner for this source-only case.

Use Python 3.13. If an environment is needed, create your own isolated environment
in your worktree using the existing frozen dependency lock. Do not modify the
coordinator's environment or any shared source checkout. The isolated, read-only
generator copy is
`/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw`
at `76c1ebeea3fc7f80bf1abe044688f298f390cfac`; shared Claw is orchestration only.
No canonical or candidate generation is needed for a source-only no-change
decision. Run native validation applicable to the artifacts you actually create;
retain exact commands/results and prove all maintained data/export bytes remain
unchanged. Do not count a skipped or inapplicable check as a pass.

Obtain a separate skeptical review of this case, its evidence and the complete
branch diff. File real deduplicated findings, address in-scope findings and obtain
re-review. Use ordinary commits and push without force. Open a clearly titled
canary evidence PR targeting `curate/kgm-unmapped-chemicals-20261107`, with the
#1158 dependency and all limitations explicit; no mentions or merge. Verify the
actual PR head and checks. If checks are still running, report that precise state
and leave the coordinator a durable completion/checkpoint receipt.

After the complete bounded case, leave the session idle. Do not continue the
other 187 cases, launch sessions, merge, or clean up. The coordinator verifies the
canary and then sends the continuation for the remainder of your shard.
