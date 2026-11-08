PR1205 publisher review at `4c8a987da40d48cceeb4390550f1ff7545927a0b` found one bounded recovery-evidence defect.

**IR-PR1205-PUBLISHER-001 — P2: a completed publication can retain corrupted recovery backups.** In `campaign_publication.py:1217`, output rechecks verify reserved handles, links and inodes. Only the native mapping receipt receives an expected-byte comparison. The two backups written at line 1227 have no later content check.

The targeted private probe used the exact committed publisher and native code with the existing synthetic fixture. Immediately before the real `finish_receipt`, it overwrote either `canonical-before.tsv` or `policy-before.json` without changing the inode. Both cases returned `complete`, left a complete publication log and passed separate validation as `verified`. The unchanged positive retained both correct backups. Full results and exact hashes are in `backup-integrity-probe-result.json`.

The accepted plan's immutable beforeimages remained valid, and the actual canonical/policy/native-chain verification passed. This finding concerns the integrity of the additional recovery files. It does not demonstrate a wrong mapping, source identity, scientific approval or release bypass. Source-owner proof and external generation were explicitly mocked by the existing fixture; publication, native receipt replay, reservation, `check_reserved`, `finish_receipt` and validation were real.

Recheck backup bytes against their captured beforeimages after writing and through completion. Add both deterministic in-place mutation controls and retain the positive. Keep standalone validator scope explicit if recovery files are outside its input contract.

The requested #1194, #1195, #1198 and #1200 fixes are supported by current code, targeted tests and archived independent results; adjacent #1197 owner-chain preflight is also covered. The archived final publisher run reports 106 passing tests, and its independent focused rerun reports 11 passing tests. Those suites were not rerun here. The only new execution was the authorized three-case private probe.

The integration worktree remained clean at the requested head. No integration, maintained-data or GitHub mutation occurred. `review.json`, `commands.json` and `source-and-evidence-manifest.json` bind the review scope and evidence.
