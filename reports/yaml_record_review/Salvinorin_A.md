# `data/ingredients/mapped/Salvinorin_A.yaml`

**Verdict**: pass.

**Identity**: `Salvinorin A` maps exactly to active, defining `CHEBI:67900` /
`salvinorin A`. Fresh OLS4 lookup resolved the ChEBI term with the same CAS RN,
formula, InChI, and SMILES as the record, and PubChem also resolved
`83729-01-5`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Salt_Solution_II.yaml
data/ingredients/mapped/Salt_Water.yaml
data/ingredients/mapped/Salts_Solution.yaml
data/ingredients/mapped/Salvinorin_A.yaml
data/ingredients/mapped/Sandramycin.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the OBO-resolvable subset, `Salt_Water`, `Salvinorin_A`, and
`Sandramycin`; the two `kgmicrobe.ingredient` fallback-registry records in
this batch are outside Engine A coverage.

**Evidence**: The CultureBotHT CAS payload `83729-01-5` agrees with the active
CHEBI xref and PubChem lookup. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(identifier, preferred_term)`. Final SSSOM row
2557 maps exactly to `CHEBI:67900` and exports `CAS:83729-01-5` in `other`.

**Completeness**: The exact CHEBI identity, CAS, structure fields,
single-ingredient type, and final SSSOM row agree. No roles, components, or
curated synonyms are asserted.

**Recommended Edits**: None.
