# `data/ingredients/mapped/Radicicol.yaml`

**Verdict**: pass.

**Identity**: `Radicicol` maps exactly to defining `CHEBI:556075` / `radicicol`.
Fresh OLS4 lookup resolved the ChEBI CURIE, and PubChem lookup by the stored CAS
`12772-57-5` resolved CID 6323491 with the same formula and InChI as the YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rac-3-Hydroxypentanoic_Acid.yaml
data/ingredients/mapped/Racemomycin_E.yaml data/ingredients/mapped/Radicicol.yaml
data/ingredients/mapped/Raffinose.yaml data/ingredients/mapped/Ramoplanin.yaml`
passed for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for this CHEBI
record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. Final SSSOM row 2490 maps exactly to
`CHEBI:556075` and exports only the long ChEBI exact synonym plus
`CAS:12772-57-5`, which belongs to the stored chemical-properties CAS.

**Completeness**: The exact ChEBI identity, structure, CAS, ingredient type, and
final SSSOM row agree. No roles or components are asserted.

**Recommended Edits**: None.
