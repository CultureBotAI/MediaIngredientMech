# `data/ingredients/mapped/Rubidium_Chloride.yaml`

**Verdict**: pass.

**Identity**: `rubidium chloride` maps exactly to active, defining
`CHEBI:78672` / `rubidium chloride`. Fresh OLS4 lookup resolved the ChEBI term
with the same formula, InChI, SMILES, and `7791-11-9` CAS xref as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Roxithromycin.yaml
data/ingredients/mapped/Rubidium_Chloride.yaml
data/ingredients/mapped/Rubradirin.yaml
data/ingredients/mapped/Rubrolone.yaml
data/ingredients/mapped/Rumen_Fluid.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: `RbCl` is the molecular-formula surface for rubidium chloride and
is supported by the manual CultureMech gap-label decision in the record.
PubChem resolved `7791-11-9` to the same formula and InChI as the record,
matching the CAS xref on the ChEBI term. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(identifier, preferred_term)`. Final
SSSOM row 2535 maps exactly to `CHEBI:78672` and exports only `RbCl` plus
`CAS:7791-11-9`.

**Completeness**: The exact ChEBI identity, chemistry, CultureMech occurrence
count, formula abbreviation, and final SSSOM row agree. No roles or components
are asserted.

**Recommended Edits**: None.
