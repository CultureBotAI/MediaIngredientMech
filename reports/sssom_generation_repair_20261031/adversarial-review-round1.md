Independent adversarial review of CLAW `0d45b0c1d40bec528913e5ff39707174af0b6221` against `18774380e032acb6da0d195214c59368cd47594f`: **one confirmed minor finding; repair and re-review required**.

The reviewer did not author or alter the branch. All four changed source/test files were inspected, together with MIM's identity, synonym and native invariant contracts. This is a mechanical code review, not scientific approval.

- **F1 / P3 — Unicode year bypasses the new header guard** (`scripts/build_mim_ingredient_sssom.py:1022`). `\d` and `datetime.strptime` accept `２０２６-10-15`. Native generation puts it in the header and replaces an existing destination; actual SSSOM validation exits 1 because the header value is not a date. Unicode row extraction predates this patch, but promotion into the new header and bypassing rejection before writing are new. Restrict the date shape to ASCII or use strict ISO parsing, and test that Unicode dates leave existing output untouched. No current-corpus occurrence is alleged.

Independent checks confirmed 2,994 → 2,980 rows, with exactly 14 extra compound registry rows removed, no added rows, and only `other` changed in 17 retained non-exact rows. All curated primary identities remain exact. Native B1/B5/G/K report zero findings on the repaired candidate. Forty-five additional namespace, parent-prefix and predicate cases passed. Seven committed date tests and further leap-day, ordering and malformed-type probes passed; the Unicode-year counterexample failed as described.

Existing scientific obligations remain in MIM issues 669, 875 and 901. The canonical mapping and native review holds were not changed, and this review does not authorize promotion of the diagnostic candidate. The broader CLAW test-suite result belongs to the parent execution and is not claimed here.

Reproduction and exact hashes are in `adversarial-review-round1.json`; executable probes and validator logs are under `adversarial-probes/`. No source, commit or remote changes were made by this reviewer.
