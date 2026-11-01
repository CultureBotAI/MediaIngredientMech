# Issue #1046 test runtime correction

Only the test module changed. An explicit optional Claw fixture now guards transaction/integration cases; pure proposal, primary-evidence, promotion, provenance comment, validation stamp, exact target-row shape and claim-substitution checks remain active in MIM-only CI. No fake publisher or module-level skip was introduced.

The original test and original checkpoint are preserved here. The original checkpoint remains immutable and its test hash describes the pre-#1046 version; receipt.json supplies the new test hash. All other 21 owned files, including writer, fixtures and scientific source package, retain their original hashes.

MIM-only PYTHONPATH=src:. run: 16 passed, 33 native transaction cases skipped. Explicit native profile: 49 passed. Cached Ruff 0.16.3 passed. Fresh-process pure controls: 14 passed; removing candidate-claim enforcement or comment preservation causes the intended assertion failures. These synthetic counterfactuals use isolated tiny copies and do not mutate production or author files.

The MIM-only failure before this fix is retained at ../step4-independent/lithium-without-claw-runtime.log; it is a test dependency defect, not a scientific mapping finding. See the exact command receipts and hashes in receipt.json. No new scientific approval or supervisor binding is asserted.
