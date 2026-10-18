# `data/ingredients/mapped/Rhodinyl_Acetate.yaml`

**Verdict**: pass.

**Identity**: `Rhodinyl Acetate` is preserved as the CAS-primary
`cas:141-11-7` fallback. PubChem lookup by the CAS resolved CID 8833 and
matched the formula, SMILES, InChI, and stored `pubchem_cid`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhamnogalacturonan_I_From_Potato_Pectic_Fiber.yaml
data/ingredients/mapped/Rhamnolipid.yaml data/ingredients/mapped/Rhamnose.yaml
data/ingredients/mapped/Rhodinyl_Acetate.yaml
data/ingredients/mapped/Rhodocladonic_Acid.yaml` passed for the 5-file batch
with 0 ERROR rows. Engine A OBO label validation was skipped because this is a
CAS-only registry record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM row 2501 maps exactly to
`cas:141-11-7`, and the only `other` token is the matching `CAS:141-11-7`.
`mappings/ingredient_mappings_unknown_term_triage.tsv` already classifies the
old `UNKNOWN_TERM` review row as an expected registry identifier.

**Completeness**: The fallback CAS, PubChem structure, ingredient type, and
final SSSOM registry row are populated. No roles or components are asserted.

**Recommended Edits**: None.
