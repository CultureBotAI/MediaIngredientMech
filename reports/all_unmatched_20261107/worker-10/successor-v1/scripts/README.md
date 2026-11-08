# Executed worker helpers

These copies preserve the actual local workflow used to build and validate the successor evidence. Scientific author builders and remediation helpers are historical execution inputs, not integration commands. Rerunning an author builder would create new timestamps and draft bytes; it must not overwrite the reviewed successor or its predecessor.

Native validators operated on private scratch copies or in-memory records. `native_prepare.py` performs strict validation, guarded private writes and combined partonomy. `native_inspect.py` and `native_review_build.py` prepare the bounded formal review; only the maintained `scripts/record_review.py save` publishes the authoritative YAML/Markdown pair. Command receipts and actual logs are in `../native/`.

The final ledger resolves artifact captures against `reports/all_unmatched_20261107/worker-10/`, including unchanged predecessor evidence. Frozen queue captures remain external read-only inputs with their original hashes. No helper is authority to apply proposed owner bytes or rebuild downstream products.
