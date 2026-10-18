# `data/ingredients/mapped/Saccharin.yaml`

**Verdict**: pass.

**Identity**: `Saccharin` maps exactly to active, defining `CHEBI:32111` /
`saccharin`. Fresh OLS4 lookup resolved the ChEBI term with the same formula,
InChI, SMILES, and `81-07-2` CAS xref as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/S-isocorydine.yaml
data/ingredients/mapped/Saccharin.yaml data/ingredients/mapped/Safrole.yaml
data/ingredients/mapped/Sake.yaml data/ingredients/mapped/Salicin.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct `linkml-term-validator
validate-data` with `--labels` passed for the same 5 files.

**Evidence**: CHEBI:32111 lists the curated IUPAC label as an exact synonym, so
the first final SSSOM `other` token is a true synonym. PubChem resolved
`81-07-2` to the same formula and InChI as the record, matching the CAS xref on
the ChEBI term. The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2545 maps exactly
to `CHEBI:32111` and exports only the exact ChEBI IUPAC synonym plus
`CAS:81-07-2`.

**Completeness**: The exact ChEBI identity, structure, CAS, CultureBotHT
provenance, and final SSSOM row agree. No roles or components are asserted.

**Recommended Edits**: None.
