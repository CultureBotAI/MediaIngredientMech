# #1039 — hash-prefixed TSV rows in the run-owned analyzer

This is dependency-author implementation evidence for
[#1039](https://github.com/CultureBotAI/MediaIngredientMech/issues/1039), not an
independent adversarial review. The defect was in the unpublished diagnostic
analyzer. The native producer and the published unified candidate were correct.
No repository source, tests, production data, frozen implementation package or
mapping artifact was edited by this fix.

The original analyzer removed every `#`-prefixed line from every TSV format. Its
first result, preserved under `original/`, therefore reported 4,166 rows and
209,323 occurrences for the artifact whose SHA256 is
`ca62e2f031ebe0f9e6185efc7816207912095beef9799a04634c889cc27196b5`.
Those diagnostic population/count fields are **superseded and incorrect**.
The correct plain TSV reader reports **4,170 rows and 209,330 occurrences**.
The omitted names were `#N2` (3 occurrences), `#N2O` (2), `#argon` (1) and `#Ar`
(1). The old analyzer's separate raw-byte comparison still protected those rows;
this finding does not mean altered hash rows had passed publication guards.

The corrected `RUN/analyze_step3_final.py` requires an explicit format at every
table call. Unified mappings and the rejection ledger use `plain`; canonical
SSSOM uses `sssom`; recipe membership uses `commented-membership`. Only the latter
two consume a leading comment prelude. Once the header is reached, hash-prefixed
lines remain data in every mode. An absent or unknown format cannot silently
trigger comment stripping. `source.diff` records the complete narrow change.

The original source is preserved byte-for-byte in
`original/analyze_step3_final.py`, SHA256
`38790edcb9f5a8fb6439827ed74905a7b1aaaa0fda1c3c32ed5749bb5b66958a`.
The fixed source is frozen in `fixed/analyze_step3_final.py`, SHA256
`fb887535cc5f4e244d1830aa5576e74dc672535fe802fa786f18792e7e29926e`.
The original finding and original run receipt/log are also retained unchanged.
They remain historical evidence and are not relabeled as successful corrected
results. Root owns the new complete analyzer run and its publication receipt.

`fixture-manifest.json` records the exact source locations, durable baseline
`99fe4b44d78126d78041a69eeb366c52bedf0caa`, compressed-byte hashes and uncompressed
hashes of the snapshots used in the regression suite. These are historical
fixture counts, not a rule that future live corpus sizes remain fixed.

Validation recorded here:

- **23 tests passed.** The tests retain all four hash names and seven occurrences,
  match the complete native plain TSV population/counts, call the actual
  `unified_check` boundary on the frozen before/after pair, and reject edits,
  removals and duplication of hash-prefixed rows at the parsed scope checks.
  They also preserve SSSOM metadata and membership preludes, retain hash data
  after a header, preserve hash-prefixed plain headers, and reject malformed rows
  and unknown format selection.
- A fresh-process probe imports the exact original analyzer and reproduces
  4,166 / 209,323, failing the explicit correct-count assertion. The failure is
  the real row-count defect, not an import or argument error.
- A second fresh process restores the original line-stripping assignment in an
  isolated copy of the fixed script while retaining the new keyword API. It
  produces **21 failed / 2 passed** regressions. The two passing tests verify that
  the original algorithm already handled the ordinary SSSOM and membership
  preludes. Failures are behavioral; collection/import/API errors were excluded.
- The negative-control harness verifies the active fixed analyzer, frozen fixed
  copy and production unified artifact remain unchanged. No full live analyzer,
  source generator, publication operation or repository test suite was launched
  by this fix. Root reruns the complete analyzer after source stability.

Native-run receipts and logs are copied under `logs/`. The test source and
negative-control harness are run-owned and do not modify `step3-mim/tests`.
Reproduce the fixed regressions from the isolated MIM worktree with its maintained
environment:

```bash
uv run --frozen python -m pytest -q -o addopts= -p no:cacheprovider \
  ../step3-analyzer-1039/test_analyzer_parser.py
```

The negative-control runner writes new evidence exclusively under
`negative-controls/`; the retained run must not be overwritten or rerun in place.
For a later reproduction use a new copy/destination and preserve these receipts.

The portable package is separate from the frozen implementation package. Its
`evidence-index.json` binds the exact files for root's generation-evidence copy.
No paid service, network lookup, GitHub mutation, or shared-checkout write was
performed by this bounded diagnostic correction.
