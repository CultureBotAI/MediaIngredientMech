# `data/ingredients/mapped/Roccellic_Acid.yaml`

**Verdict**: pass.

**Identity**: `Roccellic Acid` maps exactly to active, defining
`CHEBI:144218` / `Roccellic acid`. Fresh OLS4 lookup resolved the ChEBI term and
matched the YAML formula, SMILES, and InChI. Fresh PubChem lookup by the stored
CAS `22139-54-4` resolved a roccellic-acid CID with the same formula and the
same CAS in its synonym list.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ristocetin_B.yaml data/ingredients/mapped/Rna.yaml
data/ingredients/mapped/Robustic_Acid.yaml
data/ingredients/mapped/Roccellic_Acid.yaml
data/ingredients/mapped/Rolled_Oats.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2527 maps exactly
to `CHEBI:144218` and exports only `CAS:22139-54-4` in `other`.

**Completeness**: The CultureBotHT provenance, exact ChEBI identity, CAS,
chemical properties, ingredient type, and final SSSOM row agree.

**Recommended Edits**: None.
