# `data/ingredients/mapped/Salsoline.yaml`

**Verdict**: pass.

**Identity**: `Salsoline` maps by CAS RN to active, defining `CHEBI:112` /
`(-)-Salsoline`. Fresh OLS4 lookup resolved the ChEBI term with the same CAS RN,
formula, InChI, and SMILES as the record, and PubChem also resolved `89-31-6`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Salicylate.yaml
data/ingredients/mapped/Salicylic_Acid.yaml
data/ingredients/mapped/Salidroside.yaml
data/ingredients/mapped/Salinomycin.yaml
data/ingredients/mapped/Salsoline.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The CultureBotHT CAS payload `89-31-6` agrees with the active
ChEBI xref and PubChem lookup. The `CAS_RN_LOOKUP` mapping quality correctly
keeps the lookup provenance while the own-identifier SSSOM row remains exact
under Rule D. The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2553 maps exactly
to `CHEBI:112` and exports `CAS:89-31-6` in `other`.

**Completeness**: The CAS-backed CHEBI identity, structure fields,
single-ingredient type, and final SSSOM row agree. No roles, components, or
curated synonyms are asserted.

**Recommended Edits**: None.
