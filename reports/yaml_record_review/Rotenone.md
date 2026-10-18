# `data/ingredients/mapped/Rotenone.yaml`

**Verdict**: pass.

**Identity**: `Rotenone` maps exactly to active, defining `CHEBI:28201` /
`rotenone`. Fresh OLS4 lookup resolved the ChEBI term with the same formula,
InChI, SMILES, and `83-79-4` CAS xref as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rosaramicin.yaml
data/ingredients/mapped/Roseoflavin.yaml
data/ingredients/mapped/Rosmarinic_Acid.yaml
data/ingredients/mapped/Rosuvastatin_Calcium.yaml
data/ingredients/mapped/Rotenone.yaml` passed for the 5-file batch with 0 ERROR
rows. Direct `linkml-term-validator validate-data` with `--labels` passed for
the same 5 files.

**Evidence**: CHEBI:28201 lists the curated stereospecific IUPAC label as an
exact synonym, so the first final SSSOM `other` token is a true synonym.
PubChem resolved `83-79-4` to the same formula and InChI as the record,
matching the CAS xref on the ChEBI term. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(identifier, preferred_term)`. Final
SSSOM row 2533 maps exactly to `CHEBI:28201` and exports only the exact ChEBI
IUPAC synonym plus `CAS:83-79-4`.

**Completeness**: Hidden and ignored inclusive search across `data`, `src`,
`tests`, `mappings`, `scripts`, and `reports` found only expected references to
the Rotenone label, `CHEBI:28201`, and `83-79-4`: the live per-record and
aggregate copies, generated indexes, row-review provenance, final SSSOM rows,
and historical backups. No roles or components are asserted.

**Recommended Edits**: None.
