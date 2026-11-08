# Publisher live transaction HEAD correction (#1256)

Author-only patch, not independent approval. The issue addendum was published before this correction.

Only live prepare(completed=False) requires actual repository HEAD to equal the source application's accepted baseline. The same check is registered in existing captured-input verification callbacks, covering reservation, mutations, native receipt, completion and final return. Historical validate remains valid after later commits. No tracked-dirty allowlist was added to the publisher; legitimate uncommitted synchronization products remain allowed.

The three implementation/test files are the complete publisher patch. The source operator and its tests are separately authored by next23_context; exact executed private dependency hashes are in RESULTS.json. No I/J/K files changed.

157 focused cases passed, zero skipped:142 publisher cases and15 genuine source-to-pinned-generator-to-publisher cases. Seventeen added cases cover4 preflight unit refusals,1 late preparation refusal,4 late mutation/completion refusals,2 unit positives,2 actual-generator preflight refusals,3 actual-generator late refusals and1 actual-generator historical positive. Every old assertion is preserved. Existing fixture changes replace the synthetic baseline with a genuine private Git commit and explicitly isolate OPENCLAW_WORKSPACE.

Real-generator cases bind immutable Claw76c and actual J/eac receipt prefix1–27. Prior native demotion, position-map and held-row assertions remain intact. All15 native command/log, post-control manifest and source-receipt packets are included. Negative controls deliberately mutate some manifests after real generation; those snapshots are identified as such. Private fixture trees are excluded. Publication failures retain recovery evidence and clear success-shaped receipts; no rollback claim is made.

Black, Ruff and Mypy passed. Initial focused-v1 failed at collection because the private copy lacked uv.lock; the failure and copy correction remain preserved. focused-v2 is the successful complete run. One packaging pass refused pytest's current-directory symlink; the final inventory excludes such aliases and includes all15 genuine regular case directories. No thresholds, schemas, gates, pins, old receipts or scientific approvals changed.
