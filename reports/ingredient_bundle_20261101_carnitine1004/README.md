# Companion dependency refresh after #1004

The maintained [`refresh_unchanged_cohort.py`](../../scripts/refresh_unchanged_cohort.py)
produced this immutable successor from baseline
`99fe4b44d78126d78041a69eeb366c52bedf0caa` and the preserved
[#875 companion](../ingredient_bundle_20261101_ncit875/review.json).
`prior-review.json` is its exact byte copy; `dependency-refresh.json` records the
command, input hashes and complete comparisons.

All 51 claims and decisions, 20 owning records, selected mapping payloads and
complete evidence entries remain unchanged: 20 mappings, 18 identifier
annotations, three products and ten occurrences. Removing four obsolete
carnitine rows relocates 17 selected base decisions. Each relocated decision
resolves its own unchanged complete evidence entry; both positions and evidence
keys are recorded in the receipt.

Only proven global dependency hashes and those locators change. The three
changed carnitine/NLDM owners are outside this cohort. This refresh adds no
scientific approval and does not override their withheld mappings or NLDM's
withdrawn component and role approvals. The prior companion remains unchanged.

Native export and validation passed with manifest SHA256
`1534bc1cef2f995deabb6e7c725bc02c62fb5e6ee4edc762def85b509c0ccd49`.
CI, the native integration test and the public export example explicitly select
this successor. Reproduce into new output paths whose parents already exist:

```bash
python scripts/refresh_unchanged_cohort.py \
  --baseline 99fe4b44d78126d78041a69eeb366c52bedf0caa \
  --prior-review reports/ingredient_bundle_20261101_ncit875/review.json \
  --output output/carnitine1004-review.json \
  --receipt output/carnitine1004-refresh.json \
  --prior-copy output/carnitine1004-prior.json
python -m mediaingredientmech.export.ingredient_bundle export \
  --review reports/ingredient_bundle_20261101_carnitine1004/review.json \
  --output output/carnitine1004-bundle
```
