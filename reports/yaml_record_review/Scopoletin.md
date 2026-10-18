# `data/ingredients/mapped/Scopoletin.yaml`

**Verdict**: pass.

**Identity**: `Scopoletin` maps exactly to active, defining `CHEBI:17488` /
`scopoletin`. Fresh OLS4 lookup resolved the ChEBI term with the same CAS RN,
formula, InChI, and SMILES as the record, and PubChem also resolved `92-61-5`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sarcidin.yaml data/ingredients/mapped/Sarcosine.yaml
data/ingredients/mapped/Sclareolide.yaml
data/ingredients/mapped/Scopoletin.yaml
data/ingredients/mapped/Sea_Salts.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the OBO-resolvable subset, `Sarcosine`, `Sclareolide`,
`Scopoletin`, and `Sea_Salts`; the `kgmicrobe.compound` placeholder is outside
Engine A coverage.

**Evidence**: The CultureBotHT CAS payload `92-61-5` agrees with the active
CHEBI xref and PubChem lookup. The retained `7-hydroxy-6-methoxy-2H-chromen-2-one`
synonym is an exact OLS4 synonym of `CHEBI:17488`. The per-record YAML agrees
with the regenerated aggregate row when keyed by `(identifier, preferred_term)`.
Final SSSOM row 2564 maps exactly to `CHEBI:17488` and exports
`7-hydroxy-6-methoxy-2H-chromen-2-one|CAS:92-61-5` in `other`.

**Completeness**: The exact CHEBI identity, CAS, structure fields,
single-ingredient type, curated synonym, and final SSSOM row agree. No roles or
components are asserted.

**Recommended Edits**: None.
