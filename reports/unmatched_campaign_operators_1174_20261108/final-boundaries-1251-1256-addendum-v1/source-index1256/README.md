# Source index-scope correction for issue 1256

This is an author-produced private correction to exact commit `21061aa532401398db70c59a596debf330f70744`. The confirmed residual W08-21061-SRC-001 was filed and read back before changes at [issue 1256](https://github.com/CultureBotAI/MediaIngredientMech/issues/1256#issuecomment-6721304487). No maintained owner, workflow, gate, acceptance, receipt prefix, I/J/K checkout, or GitHub state is changed by this packet. Independent review is still required.

Only `_check_mutation_git_state` changes. The full original test file remains an exact byte prefix. The existing live HEAD, working-path, payload, history, output, and recovery checks remain in place. Historical `verify_completed` is unchanged; it can still verify a valid past application after later commits.

## Index semantics

The live guard now independently compares the cached/index delta against the same accepted baseline using literal NUL-delimited paths, with rename folding disabled and intent-to-add entries visible. Every changed cached path must be an explicitly allowed operation source or destination. Index paths are queried with literal pathspecs, so Unicode, control whitespace and glob characters do not change their meaning.

An unchanged baseline index remains allowed while the operator writes unstaged owner changes. For an index entry that actually differs from the baseline:

- A present entry must be a unique regular stage-zero blob. Its bytes must equal the current regular working file and an accepted authentic-before or final-after digest. Its executable/non-executable mode must match the current working file. Arbitrary staged bytes are refused even when their path is an allowed owner path. An approved future payload is also refused if it has not been installed.
- A staged deletion is allowed only for a genuine source retirement: the path is absent from the final inventory and actually absent on disk. A premature staged deletion is refused.
- The operator does not stage, unstage, commit, replace or repair index contents. Staging in the positive tests is an explicit external test action.

These checks run at the existing initial/prepare, pre-reservation, prewrite, transition and final receipt boundaries. A refusal before mutation creates no application receipt. A failure after mutation preserves the real partial outcome and writes the existing failed/recovery receipt; no false atomicity is claimed.

## Verification and preserved failures

`checks/` contains exact commands, runtime, code/test hashes, full output and exit status. `original-probe-replay-v1/` reruns the unmodified original independent four-case script against the corrected private source, with no mocked native functions: clean completion and historical verification pass; initial hidden-index, post-prepare hidden-index and ordinary drift controls refuse before source mutation. The original script's hardcoded `reviewed_head` still names its historical 21061 context; the replay receipt explicitly identifies the corrected source hashes. Its fixture helper predates only the final rename-test expectation correction, not any production change.

The 53 new parameterized cases cover all four operations (edit/create/promote/demote), initial and late hidden contract changes, midflight/final failures, wrong owner index blobs, approved-but-uninstalled payloads, premature deletions, Unicode/newline/tab/quote/glob paths, intent-to-add, index modes, rename endpoint accounting, malformed NUL output, actual staged accepted endpoints, and historical verification after a later commit. The existing 301 source cases, including all 23 issue-1255 path cases, remain unchanged.

Preserved authoring failures are not hidden: the first focused invocation lacked the private basetemp parent and ran no tests; the extended run had one new test expecting the cached error when the existing working guard correctly refused the rename earlier. Only that new test's precise expectation was corrected, with its decomposition assertions retained. The unrun first draft's misplaced test insertion is preserved; the complete original test prefix was restored before any test execution. The first archive command named an absent script and failed before extraction; its receipt and zero-byte output remain.

`source-index1256.patch` is a two-file portable diff. `verify_and_patch.py` proves its exact replay against original 21061 files, unchanged original test AST and bytes, unchanged historical verifier, and unchanged other archive members. `preservation-proof-v2.json` also records actual clean I/J/K heads and source/test hashes observed during this work.

Runtime fixtures, private Git repositories, complete dependency extraction, and caches are retained locally but omitted from the concise packet manifest. The original exact source archive and baseline receipt allow reconstruction. This manifest describes its selected evidence, not a claim that it includes every runtime file. The separate publisher residual is authored and reviewed separately; this packet grants no source-application, science or release approval.

## Final observed results

All 354 source cases passed, including the original 301 unchanged cases and 53 new cases. The combined command exited nonzero because its 157 publisher/integration cases had missing private fixture prerequisites: the minimal archive omitted the tracked native receipt maker, and one history-root control was pointed at the original 26-receipt checkout rather than frozen K with 27. The complete failure log remains. No production or test change was made to hide it, and that redundant publisher run was not repeated.

The separately authored final publisher packet passed all 164 publisher/integration cases with this exact frozen source/test pair, including 20 actual native-generator cases and zero skips. Its full portable manifest and executed source pins were rehashed; see `publisher-dependency/collection-receipt.json`. These are separate runs, not a single clean 511- or 518-test command. Ruff, Black, Mypy, the 53-case focused run, and the original four-case independent-probe replay passed. Neither author test run substitutes for distinct final code review.
