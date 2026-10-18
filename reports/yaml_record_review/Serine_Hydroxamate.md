# `data/ingredients/mapped/Serine_Hydroxamate.yaml`

**Verdict**: pass.

**Identity**: `Serine hydroxamate` maps exactly to active, defining
`CHEBI:75494` / `serine hydroxamate`. Fresh OLS4 lookup resolved the ChEBI term
with the same formula, InChI, and SMILES as the record, and PubChem resolves
both the YAML CAS `55779-32-3` and ChEBI's `4370-83-6` to CID `101173` with the
same formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Serine.yaml
data/ingredients/mapped/Serine_Hydroxamate.yaml
data/ingredients/mapped/Serotonin.yaml data/ingredients/mapped/Serum.yaml
data/ingredients/mapped/Setamycin.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The `N-hydroxyserinamide` synonym is an exact OLS4 synonym of
`CHEBI:75494`. The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2571 maps exactly
to `CHEBI:75494` and exports `N-hydroxyserinamide|CAS:55779-32-3` in `other`.

**Completeness**: The exact CHEBI identity, CAS, structure fields,
single-ingredient type, curated synonym, and final SSSOM row agree. No roles or
components are asserted.

**Recommended Edits**: None.
