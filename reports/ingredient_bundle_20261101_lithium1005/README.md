# Companion dependency refresh after #1005

The maintained [`refresh_unchanged_cohort.py`](../../scripts/refresh_unchanged_cohort.py)
produced this immutable successor from baseline
`838d0c2627552b0094545ebb580b5bb9b1a84d57` and the preserved
[#1004 companion](../ingredient_bundle_20261101_carnitine1004/review.json).
`prior-review.json` is its exact byte copy; `dependency-refresh.json` records
input hashes and complete comparisons.

All 51 claims and decisions, 20 owner hashes, selected mapping payloads and
complete evidence entries remain unchanged: 20 mappings, 18 identifier
annotations, three products and ten occurrences. Removing the false lithium-salt
CAS identity row relocates eight selected base decisions. Each relocated decision
resolves its own unchanged complete evidence; the receipt records both positions
and evidence keys.

Only proven dependency hashes and those locators change. The corrected lithium
owner is outside this cohort. This refresh grants no scientific approval, does
not override its two withheld mappings or provisional role, and preserves the
prior NLDM approval withdrawals. Earlier companion reviews remain unchanged.

Native export and validation passed with manifest SHA256
`69ccc316431534f309c3d545282cd365c3f752b28f1a1da9a273900eb2989b3f`.
The owned CI selector, integration test and public export example select this
successor. Reproduce into new output paths whose parents already exist:

```bash
python scripts/refresh_unchanged_cohort.py \
  --baseline 838d0c2627552b0094545ebb580b5bb9b1a84d57 \
  --prior-review reports/ingredient_bundle_20261101_carnitine1004/review.json \
  --output output/lithium1005-review.json \
  --receipt output/lithium1005-refresh.json \
  --prior-copy output/lithium1005-prior.json
python -m mediaingredientmech.export.ingredient_bundle export \
  --review reports/ingredient_bundle_20261101_lithium1005/review.json \
  --output output/lithium1005-bundle
```
