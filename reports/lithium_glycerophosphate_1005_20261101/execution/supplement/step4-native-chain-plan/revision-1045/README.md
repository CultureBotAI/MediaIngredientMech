# Step 4 chain inventory repair — issue #1045

This is implementation-author evidence, not an independent Step 4 approval.
Only the run-owned dependency-chain driver and its tests changed. The production
chain was not executed by this author.

The original driver read Git's default quoted text output with `splitlines()` and
then selected strings ending in `.yaml`. A quoted Unicode filename ends in a
quote instead, so the unchanged real corpus failed before any native command.
The root's original dispatch failure is retained in `checks/`.

The repaired `individual_record_scope()` retains the same exact membership and
unrelated-file byte checks. It requests `git ls-tree --name-only -z` and decodes
each NUL-separated path using the filesystem encoding. The worktree side still
uses an ignored-inclusive, nested `Path.rglob` scan. Only the authorized lithium
owner is exempt from the unchanged-content comparison.

Seven new cases use actual temporary Git repositories with `core.quotePath=true`,
tracked Greek/accented/newline names and a real ignored directory. They verify
unchanged membership and target-only content changes succeed; ignored additions,
ASCII/Unicode removal, same-count renames and unrelated byte changes fail.
The extracted original enumeration produced three assertion failures and four
passes. The repaired complete suite passes all 41 tests with zero skips.

`before/` preserves all six original files byte-for-byte, including the historical
preparation receipt and evidence index. `red/` records the behavior-preserving
helper extraction used for the red tests; `after/` freezes the repair. The old
root-level preparation receipt/index remain unchanged; this append-only repair
has its own receipt and version index. The current-tree probe checks only paths,
bytes and Git status; it does not execute a native chain command.
