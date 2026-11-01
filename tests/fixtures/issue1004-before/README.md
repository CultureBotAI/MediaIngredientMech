# Immutable #1004 migration inputs

These exact files come from MIM base `99fe4b44d78126d78041a69eeb366c52bedf0caa`.
`manifest.json` binds original and archive bytes; the membership and canonical
SSSOM files use deterministic gzip (mtime zero). The writer also hard-codes the
uncompressed input hashes and refuses drift.

The three owners, ledger and membership are the historical source transaction
preimage. Canonical SSSOM and Rule K baseline are the promotion preimage. The
writer replays these original bytes to recognize an exact completed operation
without accepting a marker-only or partial state. The whole original owner
history and removed free-substance chemistry remain recoverable here.

The 14-pair membership assertion applies to this migration only. These fixtures
do not freeze future live recipe counts; separate native occurrence tests cover
new recipes and repeated listings. Primary evidence and its hash-bound manifest
live in `reports/carnitine_hydrochloride_1004_20261101/sources/`.
