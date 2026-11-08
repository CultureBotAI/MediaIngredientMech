# Native owner boundary correction: #1251 and #1252

Author: Codex `/root/next23_context`; this is implementation evidence awaiting distinct independent review. I started from clean integration worktree `eac469f1d94f06bab0714fff891abf64b8ebdbe9` and changed only `src/mediaingredientmech/curate/campaign_owner_apply.py` and appended tests in `tests/test_campaign_owner_apply.py`. No commit, source/corpus application, J change, workflow/pin/threshold change, owner selection or scientific approval was made.

#1251 compares complete before/after **colliding path pairs**, including the identity/name key, instead of selected-only uniqueness. No new pair can appear. Owners in surviving inherited pairs must retain their exact identifiers, preferred names, status and path. A genuinely reviewed owner can leave a family without creating a collision, through the ordinary accepted-proposal/preimage/history path. Two-/three-member identity/name reductions are positive controls. The first equality-based draft incorrectly prevented reductions; it is preserved in `equality-draft-v1`, and the correction followed issue1251 comment6720714388. The remaining nickel scientific hold is unchanged.

#1252 admits substantive same-path REJECTED→REJECTED maintenance only while identifier/preferred term stay unchanged. It explicitly rejects revival, new rejected creations, reidentification, renaming and relocation. This establishes an activation refusal that the original record-stage lacked; it is not claimed to have existed before. All other schema, category, source-original, current Git/head, history/no-op, complete inventory, native owner-chain, captured producer, output reservation, filesystem/alias, completion and recovery guards remain. Angustmycin's required explicit demotion and TSB's genuine new identity collision are excluded.

## Verification on frozen code

- `pytest-v2.log`: **121 passed**,12 existing LinkML/Pydantic deprecation warnings. All42 original test/helper ASTs equal the baseline;33 parametrized new cases cover real accepted fixture Git origins, native prepare/application/completed verification, unchanged family pairs either order or single selection, unique/family tombstones, legitimate reductions and meaningful refusals (new member, replacement at same count, shared-key change, case-only name edit within a surviving pair, status change/revival, stale origin, relocation, new rejected creation and completed-owner drift).
- `publisher-regression-v1.log`: two unchanged native publisher tests passed (116 deselected), including real owner writer application followed by mapping publication and completed owner verification after canonical advancement.
- `actual-replay-v3.json`:14 exact current-record-stage probes against all2956 source records. Both nickel edits alone/joint/reversed pass; three unchanged rejected maintenance cases pass; live+tombstone dithionite and all six maintenance edits pass. Three transparent in-memory revival mutants, genuine TSB promotion and same-path Angustmycin all refuse. All original owner bytes remain unchanged. This is a record-stage proof, not a full accepted actual-campaign application or scientific approval.
- Ruff, Black check, focused Mypy and `git diff --check` pass. Python3.13 and existing read-only tools were used; no environment installation or providers.

Definitive test command (from this directory):

```sh
env PYTHONPATH=../worktree/src ../../../kgm-unmapped-20261107/env/bin/python -B -m pytest ../worktree/tests/test_campaign_owner_apply.py --no-cov -p no:cacheprovider --basetemp=pytest-v2 -q
```

Use a fresh private basetemp/log name for any future rerun. The two publisher tests are selected by `-k 'actual_native_multi_owner or actual_owner_writer_checkpoint'`. All runs use private working directory, explicit no coverage and disabled pytest cache.

## Preserved diagnostics and limitations

`pytest-v1.log` is invalidated as final evidence:45 failed/67 passed because I ran Black while the pytest process was active; captured-producer guards correctly refused changed input bytes. Definitive v2 began after source freeze. The original Ruff shadowed-name finding was fixed before v2. Two private replay script attempts failed before any record-stage execution (syntax error, then nullable deferred action destination); v1/v2 scripts/logs remain. v3 is the valid actual replay. One shell attempt used a root-relative path from this private working directory and failed before reading/writing tests; the intended test additions were applied later with explicit correct paths. No failed artifact was rewritten or falsely reported as passing.

The manifest seals bounded source/diff/log/receipt evidence. Disposable but durable pytest fixture repositories and Mypy caches are retained in this directory but excluded from the packet manifest; their exact execution is covered by source/test hashes and logs, not a claim that every generated fixture object is a campaign input. The actual-corpus/source input packet and all prior independent reviews remain at their original paths. Whole-campaign QC, distinct final review, root commit and native application remain separate. Reviewers must use the new code hash and rebind future accepted producer pins; earlier producer approvals do not transfer.
