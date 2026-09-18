# `data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pustulan (b-1-6 glucan)` has a CAS-primary exact identity row for `cas:37331-28-5` and a `kgmicrobe.compound:pustulan_b-1-6_glucan` exact registry row alongside the `skos:narrowMatch` parent `mesh:C002076` / `pustulan`. OLS4 MeSH resolves `mesh:C002076` exactly, and PubChem lookup by CAS `37331-28-5` returns the same CID `163304499` and stored formula, SMILES, and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pustulan_B-1-6_Glucan.yaml` passed for the 5-file batch with 0 ERROR rows. Direct Engine A term validation was skipped for this MeSH/CAS/local-registry record because the validator pass is CHEBI/OBO-focused; prefix-specific OLS4 MeSH lookup confirmed the parent term instead.

**Evidence**: Final SSSOM rows 2444-2446 preserve the intended three-row shape: a narrow MeSH parent row, an exact CAS registry row, and an exact kgmicrobe registry row. The `UNKNOWN_TERM` result for `mesh:C002076` was already triaged as missing validator prefix coverage, and the CAS and kgmicrobe rows were already triaged as expected registry identifiers.

**Completeness**: The identity rows are complete enough for a CAS-only pustulan record with a broader MeSH parent. The active `nutritional_roles.CARBON_SOURCE` assertion is still only a `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists` with the curator note `Provisional role from a curated name-pattern rule; review recommended.`

**Recommended Edits**: In `data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml`, replace `nutritional_roles.CARBON_SOURCE` with source-backed CultureMech evidence scoped to recipes that use pustulan as a carbon source, or remove the role. Then synchronize `data/curated/mapped_ingredients.yaml` and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
