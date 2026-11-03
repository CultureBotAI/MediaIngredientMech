# Issue #1123 — proposed test-only correction

This proposal is external. The maintained
`tests/test_source_mapping_concern_history.py` is unchanged at SHA256
`d5477373374b5aa0b9652310a25f8d4925b61035f304af38f64f63c0882345df`.
Do not apply it while the #1122 operator still pins the old tests. Wait for the
parent's confirmation that #1122 application and review refresh are complete.
No production code, workflow, rule, threshold, pin, data or Git commit is part
of this proposal.

Authoritative proposed file:
`resumption1123-proposed-v2-test_source_mapping_concern_history.py`, SHA256
`61f7edb6ad1dc069b7a45a8c908f15a80f8073a4a41b40ddb22a8aa55d830097`.
Patch: `resumption1123-proposed-v2.patch`, SHA256
`521b3ff79c524bb8999d13df97df2508daef3b7bf6b2e0c2d8efdb0112f3c39b`.

The existing test's error is coordinate use: receipt 24's `after_position`
belongs to its own checkpoint, while current decisions belong to the current
canonical file. Native production replay already composes those maps. The test
now starts with each exact receipt-24 after-payload, checks the corresponding
verified checkpoint state, and follows every subsequent receipt map in order.
At every later checkpoint it requires the same full row payload. A later
correction/removal of one of those endpoints fails explicitly; removing and
readding an identical-looking row cannot be substituted for preserving its
lineage. Distinct final positions and exact current payloads are required.

The eight-row count and WITHHOLD assertion move into the shared assertion
helper used by the original assembly test and new negative controls. All 32
original assertion ASTs remain present unchanged, including exact historical
quotes, all negative-review bases, policy text, owner/source/mapping proof,
current evidence equality, and the no-scientific/role-approval assertions.
`resumption1123-proposed-v2-preservation.json` records that comparison; the new
file has 45 assertion statements. No assertion is skipped or loosened.

Fourteen added regression cases:

- Three positive cases append native-validated synthetic receipts for insertion,
  removal, and three successive insertion/removal/insertion shifts. They compose
  through the full existing chain plus every suffix link, preserve the eight
  exact payloads, and compare against independently specified position offsets.
- Three negative cases reject a wrong map target, a wrong current payload, and
  a native-valid removal followed by readdition of the identical held payload.
- Eight negative cases, one for each actual current touched row, replace its
  decision with SUPPORTED and require the same WITHHOLD assertion to fail. They
  use correctly composed current coordinates, not unrelated stale positions.

The synthetic suffixes are validated by the existing public
`walk_mapping_changes` contract before the test helper consumes them. Synthetic
receipts stay in memory and are expressly approval-free. They do not append any
real receipt or write a fixture over repository state.

Initial external execution ran all 36 test cases: 35 passed; the assembly case
failed because the current canonical hash no longer matched the completed
review while the parent's #1122 refresh was in progress. Its guard remains
intact. The failure is saved in
`RUN/logs/step7d-resumption1123-external-proposal-v1.json`, log SHA256
`698a824314cf327b15a63ef352a8ebbfc6a7d7111f4f051fb95eff33664c7aa7`.
This is not reported as a passing full-file run. Version 2 additionally fixes an
uninformative self-comparison in the new positive fixture test by comparing to
a deep pre-run copy; original evidence remains preserved.

After the parent confirms refresh completion, rerun the exact external proposal
with only its ROOT bound to W by the saved execution fixture:

```bash
python3 RUN/run_step7d_mim.py step7d step7d-resumption1123-external-proposal-v2 -- python -B -m pytest ../step7d-execution-20261103/resumption1123-validation-v2/test_source_mapping_concern_history.py -q -o addopts= -p no:cacheprovider --basetemp ../step7d-execution-20261103/resumption1123-validation-v2/tmp
```

The `execution-binding.json` file proves the environmental ROOT literal is the
only difference from the proposed test file. All assertions and fixture code
are identical. An actual maintained-file run remains required after application:

```bash
uv run --frozen --extra dev pytest tests/test_source_mapping_concern_history.py
```

The parent reviews the bounded patch before any commit. Proposed ordinary
commit message: `test: compose source-history receipt positions (#1123)`.
Full QC, full suite and independent final-head review remain the parent's
release steps; this test author does not provide that independent review.
