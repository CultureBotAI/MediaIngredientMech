# `data/ingredients/mapped/Rutin.yaml`

**Verdict**: pass.

**Identity**: `Rutin` maps exactly to active, defining `CHEBI:28527` / `rutin`.
Fresh OLS4 lookup resolved the ChEBI term with the same formula, InChI, SMILES,
and `153-18-4` CAS xref as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rutilantinone.yaml
data/ingredients/mapped/Rutin.yaml data/ingredients/mapped/Rye-bran.yaml
data/ingredients/mapped/S-3-hydroxybutyrate.yaml
data/ingredients/mapped/S-adenosyl_Homocysteine.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` crashed on CAS-primary rows in the mixed batch; rerunning it on this
batch's CHEBI/FOODON subset passed.

**Evidence**: CHEBI:28527 lists the curated IUPAC label as an exact synonym, so
the first final SSSOM `other` token is a true synonym. PubChem resolved
`153-18-4` to the same formula and InChI as the record, matching the CAS xref
on the ChEBI term. The per-record YAML agrees with the regenerated aggregate
row when keyed by `(identifier, preferred_term)`. Final SSSOM row 2540 maps
exactly to `CHEBI:28527` and exports only the exact ChEBI IUPAC synonym plus
`CAS:153-18-4`.

**Completeness**: The exact ChEBI identity, structure, CAS, CultureBotHT
provenance, and final SSSOM row agree. No roles or components are asserted.

**Recommended Edits**: None.
