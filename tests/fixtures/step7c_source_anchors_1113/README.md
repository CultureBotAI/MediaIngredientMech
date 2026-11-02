# Historical source-operation test anchors (#1113)

`anchors.json.gz` contains the exact six protected publication inputs from merged
commit `54eadef802d2ff159bf4ba9bec51492fe3bb99d4`. Each byte sequence was read with
`git cat-file blob` and checked against the existing #1111 source evidence
manifest before this fixture was created. `manifest.json` records the archive
and member SHA-256 hashes. Runtime tests require neither Git objects nor a
private source checkpoint to load this archive.

These are historical test inputs, not current publication outputs. The labels
source operation uses the four `mappings/` anchors; the later corrective source
operation uses all six. The original source tests and writers remain unchanged
because they are preserved execution evidence. The scoped autouse adapter
reconstructs only their original `case` fixtures in their exact pytest temporary
roots before each test runs. Its checks reject changed original test bytes,
wrong fixture roots, aliases, and changed archive/member hashes. It updates only
the matching protected-anchor entries in the labels fixture's expected-before
map; source-owner bytes remain untouched.

The original writer validations, transaction and collision tests still run.
The adapter grants no scientific approval and changes no skip or assertion.
The companion controls show that later deliberate anchor corruption remains
rejected by the real writers. Updating this historical fixture to follow the
current canonical mapping would invalidate its purpose.
