# `data/ingredients/mapped/Rhodomycin_B.yaml`

**Verdict**: pass.

**Identity**: `Rhodomycin B` maps to active, defining `CHEBI:81879` /
`beta-Rhodomycin`. Fresh OLS4 lookup resolved `CHEBI:81879` with Rhodomycin B
as a registered ChEBI synonym, and PubChem lookup by Rhodomycin B resolved CID
3037123 with the same formula and InChI as the YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhodomycin_A.yaml
data/ingredients/mapped/Rhodomycin_B.yaml data/ingredients/mapped/Ribitol.yaml
data/ingredients/mapped/Riboflavin.yaml
data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the same 5
files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2505 maps exactly
to `CHEBI:81879`, exports no unsafe `other` payload, and carries the
curator-reviewed `MIM curation (#213)` evidence that the B and beta
designations refer to the same ChEBI term.

**Completeness**: The MicrobeDecoder occurrence provenance, promoted ChEBI
identity, ingredient type, ChEBI/PubChem structure fields, and final SSSOM row
agree.

**Recommended Edits**: None.
