# `data/ingredients/mapped/Pyridoxamine.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pyridoxamine` is mapped exactly to active `CHEBI:16410` / `pyridoxamine`. OLS4 CHEBI confirms the same free-base term, and PubChem lookup by CAS `85-87-0` confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyridoxamine.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyridoxamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, PubChem CAS lookup, KG-Microbe synonym, and OAK/OLS row review support the exact CHEBI identity. Final SSSOM row 2457 preserves the real all-caps IUPAC-style alias plus `CAS:85-87-0`, but it also exports a parenthetical concentration-qualified CultureMech occurrence string for pyridoxamine at 15 micrograms per microliter.

**Completeness**: The `VITAMIN_SOURCE` role is backed by `DATABASE_ENTRY` evidence imported from CultureMech with the original `Vitamin Source` role text. The remaining issue is only the concentration-qualified final synonym token.

**Recommended Edits**: Keep the exact CHEBI mapping and real pyridoxamine aliases, but remove the concentration-qualified `Pyridoxamine` occurrence string from final SSSOM by deleting the raw occurrence alias or teaching SSSOM construction to filter concentration-bearing `RAW_TEXT` synonyms. Then regenerate SSSOM and rerun `scripts/validate_sssom_invariants.py` plus the final `other` synonym review.
