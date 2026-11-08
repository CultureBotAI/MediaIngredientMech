# #1256: mutation-time Git revision versus historical verification

This independent bounded review confirms the source-application finding and a related canonical-publication boundary gap at exact commit `16c39b63bc95d3e7978ddccc6280b0d57954f4a5`. No fix or corpus application was performed. The recommended correction is a mutation-time baseline check, **not** a perpetual HEAD restriction in historical verification.

## Exact executed scope

`probe-v2.py` executed seven real source prepare/apply/verify lifecycles and five maintained owner→publisher interface cases. All loaded operator, receipt guard, and fixture files were checked against Git objects at 16c before execution and rehashed afterward. Source cases use no native function mocks. Publisher cases use the maintained interface fixture's explicit replacement for external generation; source application, canonical projection, policy reconstruction, native receipt maker/replay, guarded publication, and completed verification are real. This is not a fresh full Claw reconstruction.

The original `probe.py` invocation refused before creating any fixture because K had advanced to the separately authorized #1255 commit `7a990e36b0e08d1deff943fe58bdc40d24d3834f`. Its failure is retained in `run.log`. The successful successor imports W08's frozen exact-16c tree and checks its files against those committed objects. It does not claim to test #1255 or future #1256 repairs.

## Observed results

| Boundary | Actual result at 16c | Required interpretation |
|---|---|---|
| Unchanged source lifecycle | complete; verified | Positive control |
| HEAD moved before source prepare | refused before receipt | Existing initial baseline guard works |
| Empty commit after source prepare | apply complete; verified | Confirmed #1256 mutation-time failure |
| Unrelated tracked commit after source prepare | apply complete; verified; baseline diff includes unrelated file but HEAD diff does not | Confirmed #1256 mutable-diff-anchor failure |
| Valid source completion, then later empty commit | exact same historical proof verifies | Required historical positive |
| Valid source completion, then commit owner changes and an unrelated file | exact same historical proof verifies | Required historical positive; current HEAD differs legitimately |
| Valid source completion, later commit, then current owner byte tamper | historical verification refuses | Existing exact-content guard remains effective |
| Unchanged real owner→publisher interface | complete; all maintained interface assertions pass | Positive control, external generation fixture limitation |
| Empty or unrelated commit before publisher invocation | publish complete; all interface assertions pass | Publisher mutation-time counterpart; captured manifest baseline alone is insufficient |
| Empty commit after publisher prepare returns | publish complete; all interface assertions pass | Publisher needs repeated boundary checks, not an entry-only test |
| Valid publication, then later commit | source and publication historical verification pass | Preserve completed-verification semantics |

All fixture commits are local private fixture commits. No I/J/K files, workers, accepted plan, maintained records, or GitHub state were modified by this review.

## Why the source correction belongs in `_recheck`

At 16c `campaign_owner_apply.prepare` lines 885–891 checks actual HEAD and tracked cleanliness once. `_recheck` at line 956 checks loaded code, complete source/receipt/context membership and immutable bytes, but omits HEAD. It already runs for dry-run, before receipt directory creation, at owner write/retirement transitions, and through `finish_receipt`. Add exact current HEAD equality with `prepared.plan['baseline_commit']` there. Keep the accepted baseline immutable; do not repin it to a newer commit.

The final tracked-file comparison at lines 1259–1263 must compare the accepted baseline, not mutable `HEAD`. Use the literal NUL path handling from the separately reviewed #1255 repair. This is one baseline freshness correction, not an unrelated path-policy relaxation. Detecting drift after some writes must preserve the existing failed receipt/recovery evidence and prevent a complete receipt; do not delete evidence or silently roll back another actor's commit.

`verify_completed` (1286 onward) is a historical/content verifier. It binds the saved receipt baseline to the accepted plan, replays immutable beforeimages/checkpoints and checks current exact after-owner content. It does not need actual current HEAD to equal that old baseline. A valid old application followed by the intended canonical publication and a normal commit must remain verifiable. Putting the transaction check in `_recheck`, rather than `_load` or `verify_completed`, preserves this distinction.

## Publisher counterpart and bounded recommendation

The publisher's `_owner_proof` (427) intentionally calls historical `verify_completed`. That should not be changed to a transaction verifier. `_generation` checks actual Claw and KG revisions and matches the captured MIM generation revision to the owner proof baseline (1033–1035), but does not compare current MIM HEAD to that baseline. The scoped full-file `rev-parse` read confirms all existing publisher HEAD calls concern Claw or KG. Thus a commit after generation can escape both checks; the five publisher interface cases exercise that boundary without claiming full generation replay.

After issue publication, add a publisher mutation-only closure checking actual MIM HEAD equals `owner_proof['baseline_commit']`. Invoke it during `prepare(..., completed=False)` after the real source proof is available, before expensive reconstruction/reservation, and register it with that preparation's existing capture rechecks. This covers dry-run, final prepare readback, pre-write and post-write checks, native receipt publication, and both `finish_receipt` boundaries. The prepared mutation closure must remain active even when `publish` internally calls historical `validate`.

Do not register that live-HEAD requirement for `prepare(..., completed=True)` / standalone `validate`, and do not impose it in the shared `_owner_proof` or historical source verifier. Preserve all existing generation pins, alias guards, owner inventories, receipt suffix logic and content checks. No intervening commit is permitted during the actual source→sync→generation→publisher sequence; later verification remains historical.

## Bounded regression scope

1. Source: real empty and unrelated tracked commits after prepare and before enabled apply or dry-run must refuse with no output/owner mutation. Retain the initial-moved-HEAD negative and unchanged positive.
2. Source: inject real commits at pre-write, post-write, retirement, and final receipt pre-/post-flush boundaries across edit/create/promote/demote. Every detected drift must prevent success; partial writes retain honest failed/recovery evidence. Do not simulate refusal by replacing the native checker itself.
3. Final tracked comparison: verify accepted-baseline anchoring plus existing literal Unicode/NUL path controls from #1255; no clean result from comparing a newly moved HEAD.
4. Historical source positives: valid completion then later empty commit, committed owner publication, and unrelated commit all still verify if all required content/proofs remain exact. Keep current-owner, receipt, checkpoint and path-alias tamper negatives.
5. Publisher: actual source receipt plus generation input at its accepted baseline; empty/unrelated commit before publish and after prepare must refuse. Exercise late commits at guarded canonical/policy/native-receipt/final receipt boundaries. A failed late check must not leave a complete receipt.
6. Historical publisher positive: valid publication followed by an ordinary commit still validates under existing exact content/history constraints. Keep wrong generation revision, producer drift and owner/checkpoint negatives. A focused interface fixture may isolate generation, but retain a separately bound real pinned-generator control for final integration claims.

No schema, identity, scientific acceptance, owner selection, scope budget, threshold, review cohort or approval requirement changes are proposed.
