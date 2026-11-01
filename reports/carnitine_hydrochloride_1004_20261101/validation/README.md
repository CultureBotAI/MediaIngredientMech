# Final native validation checkpoint

The completed native gates passed: 484 focused regression tests, `just qc`, CURIE/product-label checks, unified rejection/freshness gates, and the full Python 3.13 suite (3,693 passed, one skipped, 27 warnings). The receipts bind commands, environment, execution times and log hashes. Local full-suite execution used `-o addopts=`; no local coverage percentage is claimed. CI remains a separate required check.

The full graph retains its scientific FAIL verdict; native integrity and the supported subset pass. Product validation retains 101 non-blocking label warnings. Actual KG transform coverage and its BTO/MICRO gaps are recorded in the separate generation package.

`evidence/` preserves independent actual-product and package reviews, their original/fixed diagnostic probes, completed gate driver receipts and native logs. Paths retain the original run-relative identities. Historical reviewer harness failures and the superseded parser diagnostic are classified in their review notes; they are not represented as production failures.

`summary.json` and `manifest.json` bind this checkpoint. These reviews precede native structured review persistence and the exact committed-head attestation; the PR identifies those later records. No scientific approval, cycle advancement or supervisor binding is created here.
