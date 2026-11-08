# Actual postpublication SSSOM checks

All requested native commands passed against the actual A canonical `d50988d2…` and plan `0ebe0d92…` at unchanged HEAD `7b7a4fb1…`:

- `just qc-sssom`: exit 0, zero rejected rows. Rules A, B1, B2, B3, B5, C, D, E, F, G, H, I, J, K and L passed. B4 explicitly skipped BTO, CHEBI, ENVO, FOODON, MICRO and UBERON because the validator's literal sibling transform path is absent; no bypass or fresh label-validation claim.
- `just curie-validate`: exit 0; 3,014 rows and 6,028 CURIEs passed artifact syntax/prefix checks; normalizer tests: 20 passed, one skipped in 0.05 seconds. The actual data predicate confirms the skip reason: every subject has an exactMatch.
- `python -B scripts/check_sssom_subject_files.py`: exit 0; 2,611 subjects, 2,956 file stems, 18 unresolved subject stems. The native script reports these under #236 as advisory, not a new release gate or new scientific finding.

The wrapper exited 1 solely because it also demanded completely unchanged tracked status. `qc-sssom` legitimately rewrote its documented `mappings/needs_curator_review.tsv` diagnostic: only two date-header quote normalizations changed; zero rejected rows before and after. `RESULT.json` and `FAILURE.json` remain unchanged. The append-only qualification proves that exact diagnostic-only difference without rerunning commands, changing source or pretending the original wrapper passed.

Actual completed-source proof, all 2,956 owner hashes, 34 current protected files, canonical/policy, sidecar/baseline, original 27 receipts plus new native receipt 28, HEAD and index remained exact. The ignored-inclusive monitored A file surface changed only at the native diagnostic path. Concurrent report outputs and unused A/.venv were excluded from the broad scan, with protected report/history bytes checked explicitly. Private UV/pytest/temp caches are excluded from this evidence manifest.

This packet records deterministic command execution, not a new scientific review or release approval. The earlier source validator/tests were not repeated; full QC, companion and derived-export work remain separate. No helper, native guard, source or test was repaired by this task.
