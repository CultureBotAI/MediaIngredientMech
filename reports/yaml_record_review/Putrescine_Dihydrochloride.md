# `data/ingredients/mapped/Putrescine_Dihydrochloride.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Putrescine Dihydrochloride` is a CAS-primary record for `cas:333-93-7` with a `skos:narrowMatch` parent at active `CHEBI:201718` / `1,4-Diaminobutane dihydrochloride`. OLS4 CHEBI now resolves that CHEBI term as an exact putrescine dihydrochloride salt term, with `butane-1,4-diamine;dihydrochloride` as an exact synonym, and PubChem lookup by CAS `333-93-7` confirms the stored formula, SMILES, InChI, and CID `9532`.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Putrescine_Dihydrochloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Putrescine_Dihydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CAS and kgmicrobe exact registry rows in final SSSOM rows 2449-2450 preserve the salt identity, and the `Putrescine 2 HCl` plus `butane-1,4-diamine;dihydrochloride` synonyms are salt-scoped. Final SSSOM row 2448 still emits `skos:narrowMatch` to the exact CHEBI salt term, though, and its `other` field exports `Putrescine`; `mappings/other_cross_record_baseline.tsv` already flags that token as colliding with the separate `MIM:Putrescine` free-base subject.

**Completeness**: The record has no role assertions to fix, but the active parent grade and synonym set are stale now that the salt itself resolves in CHEBI. Leaving `Putrescine` in final SSSOM as an exact-like `other` token erases the salt/free-base boundary.

**Recommended Edits**: Promote `CHEBI:201718` to the exact primary identity for `data/ingredients/mapped/Putrescine_Dihydrochloride.yaml`, or otherwise change the CHEBI row to emit `skos:exactMatch` for that term. Remove the broad `Putrescine` synonym while retaining salt-scoped aliases such as `Putrescine 2 HCl`, synchronize `data/curated/mapped_ingredients.yaml`, regenerate SSSOM, and rerun the SSSOM cross-record and invariant checks.
