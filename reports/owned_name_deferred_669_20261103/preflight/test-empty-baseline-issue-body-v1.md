The final #669 alias-policy rollout will retire the remaining 23 baseline obligations. A valid baseline then contains its unchanged TSV header and zero data rows. The current live-format test rejects that state before checking the header:

```python
assert rows, "baseline must not be empty while violations are known"
assert {"subject_id", "token", "owned_by", "disposition"} <= set(rows[0])
```

Confirmed on merged main `0ee56c11a2894ed50a476b331d56297be0a3ee12` in [test_the_baseline_file_is_well_formed](https://github.com/CultureBotAI/MediaIngredientMech/blob/0ee56c11a2894ed50a476b331d56297be0a3ee12/tests/test_sssom_other_cross_record.py#L87). Test file SHA256: `406e04a46f904ecf35681b8ebf5b892d9f4a141f891d13a536e76494b7dacb2c`. Executing that exact function AST against a private fixture with the original four-column header and zero entries raises `AssertionError: baseline must not be empty while violations are known`. No maintained file was changed. Reproduction receipt SHA256: `c883abe112d2b945840dd9cf4e5418f20f1f5df7d3585c06ca29e8d65c40bff8`, saved under `output/approved-plan-20261101T031134Z/next23-execution-20261103/test-empty-baseline-repro-v1/receipt.json`.

Correct the format test to validate `DictReader.fieldnames` independently of row count, retaining the per-row subject and nonempty-disposition assertions. Add empty/populated valid fixtures and missing-column, invalid-subject and empty-disposition negatives. Preserve and run every native ownership/collision negative, the published Rule K check and the unused-baseline check. No production parser, ownership rule, gate threshold, or baseline exemption changes are needed. Historical fixed-fixture `== 23` tests remain unchanged.

This is a test defect for the approved empty-baseline state, not a failure of the merged Step 7d content. Live deduplication inspected all 12 pages of repository issues/PRs (all states), including matches for the function, test module, assertion text and empty/nonempty-baseline wording; no issue for this defect was found. The fix belongs in the separate deferred-23 #669 PR, with regression tests, full QC and independent review.
