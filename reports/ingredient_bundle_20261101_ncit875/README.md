# Companion dependency refresh after #875

This immutable successor was produced by the maintained
[`refresh_unchanged_cohort.py`](../../scripts/refresh_unchanged_cohort.py), using
baseline `40b787d37d33d544551389ff019f2d64ad63d7cc` and the preserved
[`prior review`](../ingredient_bundle_20261101_followup/review.json).
`prior-review.json` is its exact byte copy. The command and all comparisons are
recorded in `dependency-refresh.json`.

All 51 companion claims and decisions, 20 owners, selected mapping payloads,
scientific decisions, and complete evidence entries remain unchanged. The
cohort contains 20 mappings, 18 identifier annotations, three products, and ten
occurrences. Removing #875's obsolete registry row relocates 14 selected base
decisions. The #1028 fix resolves each decision through its own position and
evidence key, then compares the complete proof; it does not waive evidence or
scientific checks. Both old and new locations are recorded in the receipt.

Only verified global dependency hashes and those locators change. No scientific
approval or release hold changes. Na2HPO4·7H2O is outside this companion cohort;
its new NCIT:C61946 row remains withheld by the complete mapping review.
CI, the public instructions, and the native integration test explicitly select
this successor after successful native export and validation.

Reproduce into three new paths whose parents already exist:

```bash
python scripts/refresh_unchanged_cohort.py \
  --baseline 40b787d37d33d544551389ff019f2d64ad63d7cc \
  --prior-review reports/ingredient_bundle_20261101_followup/review.json \
  --output output/ncit875-review.json \
  --receipt output/ncit875-refresh.json \
  --prior-copy output/ncit875-prior.json
python -m mediaingredientmech.export.ingredient_bundle export \
  --review reports/ingredient_bundle_20261101_ncit875/review.json \
  --output output/ncit875-bundle
```

The broader #875 evidence report records the generation, receipt replay,
validation and independent review. Historical reports remain immutable.
