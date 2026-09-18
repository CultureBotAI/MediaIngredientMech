# `data/ingredients/mapped/Skimmed_Milk.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Skimmed milk` maps exactly to active, defining
`FOODON:03301484` / `skim milk food product`. Fresh OLS4 lookup resolved the
FOODON term and lists both `skimmed milk` and `skim milk` as exact synonyms.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sio2.yaml
data/ingredients/mapped/Sisomicin_Sulfate_Salt.yaml
data/ingredients/mapped/Skim_milk_powder.yaml
data/ingredients/mapped/Skimmed_Milk.yaml
data/ingredients/mapped/Skirrow_Supplement.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for `Sio2`, `Sisomicin_Sulfate_Salt`, and `Skimmed_Milk`; the MICRO and
kgmicrobe.ingredient records were skipped because those prefixes are outside the
Engine A OBO term-validation subset.

**Evidence**: The kgm-metatraits source-preset import, exact FOODON identity,
raw `Skim milk` alias, and undefined-mixture classification pass. The
per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`.

The final SSSOM row needs synonym cleanup. Row 2597 exports
`Skim milk (BD-Difco)` as `other`, but that is a catalog-qualified variant of a
CultureMech surface form rather than an exact synonym of the FOODON skim-milk
food product.

**Completeness**: The exact FOODON identity, undefined-mixture classification,
and exact `Skim milk` alias agree. The vendor/catalog-qualified alias needs to
be filtered from final SSSOM or moved out of the exported synonym set.

**Recommended Edits**: Remove `Skim milk (BD-Difco)` from
`data/ingredients/mapped/Skimmed_Milk.yaml` or update the SSSOM synonym policy
to exclude `CATALOG_VARIANT` synonyms, then rebuild final SSSOM and confirm row
2597 no longer exports that token.
