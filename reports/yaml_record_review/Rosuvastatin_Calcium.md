# `data/ingredients/mapped/Rosuvastatin_Calcium.yaml`

**Verdict**: pass.

**Identity**: `Rosuvastatin calcium` maps exactly to active, defining
`CHEBI:77249` / `rosuvastatin calcium`. Fresh OLS4 lookup resolved the ChEBI
term with the same `2C22H27FN3O6S.Ca` empirical formula, InChI, SMILES, and
`147098-20-2` CAS xref as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rosaramicin.yaml
data/ingredients/mapped/Roseoflavin.yaml
data/ingredients/mapped/Rosmarinic_Acid.yaml
data/ingredients/mapped/Rosuvastatin_Calcium.yaml
data/ingredients/mapped/Rotenone.yaml` passed for the 5-file batch with 0 ERROR
rows. Direct `linkml-term-validator validate-data` with `--labels` passed for
the same 5 files.

**Evidence**: CHEBI:77249 lists the curated calcium-bis IUPAC label as an exact
synonym, so the first final SSSOM `other` token is a true synonym. PubChem
resolved `147098-20-2` to the same calcium salt, formula, and InChI as the
record, matching the CAS xref on the ChEBI term. The per-record YAML agrees
with the regenerated aggregate row when keyed by `(identifier,
preferred_term)`. Final SSSOM row 2532 maps exactly to `CHEBI:77249` and
exports only the exact ChEBI IUPAC synonym plus `CAS:147098-20-2`.

**Completeness**: Hidden and ignored inclusive search across `data`, `src`,
`tests`, `mappings`, `scripts`, and `reports` found only expected references to
the Rosuvastatin calcium label, `CHEBI:77249`, and `147098-20-2`: the live
per-record and aggregate copies, generated indexes, row-review provenance,
final SSSOM rows, and historical backups. No roles or components are asserted.

**Recommended Edits**: None.
