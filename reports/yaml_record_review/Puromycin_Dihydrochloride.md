# `data/ingredients/mapped/Puromycin_Dihydrochloride.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Puromycin dihydrochloride` is mapped exactly to active `CHEBI:8642` / `puromycin dihydrochloride`. OLS4 CHEBI confirms CAS `58-58-2`, formula `C22H29N7O5.2HCl`, and the two-hydrochloride SMILES/InChI for the salt.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Puromycin_Dihydrochloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Puromycin_Dihydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS import and OAK/OLS row review support the exact CHEBI salt identity. Final SSSOM row 2443 keeps the real CHEBI synonym `3'-deoxy-N,N-dimethyl-3'-[(O-methyl-L-tyrosyl)amino]adenosine dihydrochloride` and `CAS:58-58-2`; both are scoped to the dihydrochloride salt.

**Completeness**: The only unsupported active claim is `physicochemical_roles.SELECTIVE_AGENT`. It was added by `infer_roles_from_name_lists` and is backed only by `COMPUTATIONAL_PREDICTION` evidence with the curator note `Provisional role from a curated name-pattern rule; review recommended.`

**Recommended Edits**: In `data/ingredients/mapped/Puromycin_Dihydrochloride.yaml`, replace `physicochemical_roles.SELECTIVE_AGENT` with source-backed evidence from a recipe or source table that actually uses puromycin dihydrochloride as a selective agent, or remove the role. Then synchronize `data/curated/mapped_ingredients.yaml` and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
