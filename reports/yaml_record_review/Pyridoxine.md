# `data/ingredients/mapped/Pyridoxine.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pyridoxine` is mapped exactly to active `CHEBI:16709` / `pyridoxine`. OLS4 CHEBI resolves the same free-base term, and PubChem lookup by CAS `65-23-6` confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyridoxine.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyridoxine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, PubChem CAS lookup, KG-Microbe structure synonyms, and OAK/OLS row review support the exact CHEBI free-base identity. Final SSSOM row 2460 keeps those true pyridoxine aliases and `CAS:65-23-6`, but it also exports `vitamin B6`; OLS4 exposes `vitamin B6` as the broader `CHEBI:27306` vitamer class, not an exact label for only the pyridoxine free base.

**Completeness**: The `VITAMIN_SOURCE` role is backed by `DATABASE_ENTRY` evidence imported from CultureMech with the original `Vitamin Source` role text. The remaining unsupported assertion is the over-broad final synonym.

**Recommended Edits**: Remove `vitamin B6` from the `Pyridoxine` exact-synonym list or teach SSSOM construction to filter KG-Microbe related/broader vitamin class labels. Then regenerate SSSOM and rerun `scripts/validate_sssom_invariants.py` plus the final `other` synonym review.
