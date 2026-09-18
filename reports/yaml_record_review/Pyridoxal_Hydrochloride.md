# `data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pyridoxal hydrochloride` is mapped exactly to active `CHEBI:131529` / `pyridoxal hydrochloride`. OLS4 CHEBI confirms the same hydrochloride term and its salt-scoped aliases, and PubChem lookup by CAS `65-22-5` confirms the stored hydrochloride formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyridoxal_Hydrochloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyridoxal_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, KG-Microbe synonyms, and row-review manifest support the exact CHEBI salt identity, and the final SSSOM row includes real aliases such as `Pyridoxal HCl` plus `CAS:65-22-5`. However, final SSSOM row 2455 also exports `pyridoxal-HCl (Sigma Aldrich)`, a catalog-qualified occurrence string that is not a real synonym.

**Completeness**: The `VITAMIN_SOURCE` role is backed by `DATABASE_ENTRY` evidence imported from CultureMech with the original `Vitamin Source` role text. The remaining issue is only the vendor-qualified final synonym token.

**Recommended Edits**: Keep the exact CHEBI mapping and salt aliases, but remove `pyridoxal-HCl (Sigma Aldrich)` from final SSSOM by deleting the catalog variant or filtering `CATALOG_VARIANT` synonyms during SSSOM construction. Then regenerate SSSOM and rerun `scripts/validate_sssom_invariants.py` plus the final `other` synonym review.
