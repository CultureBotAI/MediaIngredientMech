# `data/ingredients/mapped/Pyridoxal_Phosphate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pyridoxal phosphate` is mapped exactly to active `CHEBI:18405` / `pyridoxal 5'-phosphate`. OLS4 CHEBI confirms the phosphate term, and PubChem lookup by CAS `54-47-7` confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyridoxal_Phosphate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyridoxal_Phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, KG-Microbe synonyms, and OAK/OLS row review support the exact CHEBI phosphate identity, and final SSSOM row 2456 keeps real aliases such as `PLP`, `PYRIDOXAL-5'-PHOSPHATE`, and `CAS:54-47-7`. The same row also exports `pyridoxal-phosphate (Sigma Aldrich)`, a catalog-qualified recipe occurrence string that should not be an `other` synonym.

**Completeness**: The `VITAMIN_SOURCE` role is backed by `DATABASE_ENTRY` evidence imported from CultureMech with the original `Vitamin Source` role text. The remaining issue is only the vendor-qualified final synonym token.

**Recommended Edits**: Keep the exact CHEBI mapping and real phosphate aliases, but remove `pyridoxal-phosphate (Sigma Aldrich)` from final SSSOM by deleting the catalog variant or filtering `CATALOG_VARIANT` synonyms during SSSOM construction. Then regenerate SSSOM and rerun `scripts/validate_sssom_invariants.py` plus the final `other` synonym review.
