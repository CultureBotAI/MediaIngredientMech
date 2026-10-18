# `data/ingredients/mapped/Rhamnogalacturonan_I_From_Potato_Pectic_Fiber.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Rhamnogalacturonan I from potato pectic fiber` is a CAS-primary
fallback to `cas:39280-21-2`; PubChem lookup by that CAS returned no CID. The
fallback CAS is also used exactly by
`Rhamnogalacturonan from soy bean pectic fibre`, so it does not preserve the
source-specific potato identity asserted in this record's preferred term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhamnogalacturonan_I_From_Potato_Pectic_Fiber.yaml
data/ingredients/mapped/Rhamnolipid.yaml data/ingredients/mapped/Rhamnose.yaml
data/ingredients/mapped/Rhodinyl_Acetate.yaml
data/ingredients/mapped/Rhodocladonic_Acid.yaml` passed for the 5-file batch
with 0 ERROR rows. Engine A OBO label validation was skipped because this is a
CAS-only registry record.

**Evidence**: The per-record YAML agrees with its
`data/curated/mapped_ingredients.yaml` row when the aggregate entry is matched by
both `identifier` and `preferred_term`. Final SSSOM row 2498 publishes
`MIM:Rhamnogalacturonan_I_From_Potato_Pectic_Fiber skos:exactMatch
cas:39280-21-2`, which is the same exact object already published for the
source-qualified soybean record at row 2497.

**Completeness**: No roles, components, or supplied forms are asserted.
`ingredient_type: SINGLE_INGREDIENT` is also weaker than the neighboring soybean
record's `UNDEFINED_MIXTURE` classification for a pectic-fiber material.

**Recommended Edits**: Review both rhamnogalacturonan CAS-fallback records
together. If the source labels are the same substance, merge them; if soy bean
and potato pectic-fibre sources are intentionally distinct, mint source-specific
`kgmicrobe.ingredient:` identifiers, keep `39280-21-2` only as shared CAS
provenance rather than as the exact primary identity, and reclassify this record
away from `SINGLE_INGREDIENT`.
