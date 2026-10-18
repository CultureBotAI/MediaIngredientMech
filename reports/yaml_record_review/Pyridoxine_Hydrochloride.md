# `data/ingredients/mapped/Pyridoxine_Hydrochloride.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pyridoxine hydrochloride` is mapped exactly to active `CHEBI:30961` / `pyridoxine hydrochloride`. OLS4 CHEBI confirms the same monohydrochloride term and salt-scoped aliases, and PubChem lookup by CAS `58-56-0` confirms the stored formula, SMILES, and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyridoxine_Hydrochloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyridoxine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, PubChem/CultureBotHT CAS lookups, KG-Microbe synonyms, and row-review manifest support the exact CHEBI salt identity. Final SSSOM row 2461 keeps real aliases such as `Pyridoxine-HCl`, `Pyridoxine HCl`, and `CAS:58-56-0`, but it also exports `Pyridoxine-HCl (VitaminB6)` and `Pyridoxine-HCl (Vitamin B6)`, which are parenthetical recipe occurrence strings rather than true names for the salt.

**Completeness**: The `VITAMIN_SOURCE` role is backed by CultureMech `DATABASE_ENTRY` evidence for use as `Vitamin`. The only major issue is the pair of parenthetical final SSSOM tokens.

**Recommended Edits**: Keep the exact CHEBI mapping and salt aliases, but remove the two parenthetical `Pyridoxine-HCl` occurrence strings from final SSSOM by deleting those `RAW_TEXT` aliases or filtering parenthetical annotation aliases during SSSOM construction. Then regenerate SSSOM and rerun `scripts/validate_sssom_invariants.py` plus the final `other` synonym review.
