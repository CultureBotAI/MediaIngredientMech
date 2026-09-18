# `data/ingredients/mapped/S-isocorydine.yaml`

**Verdict**: pass with minor issues.

**Identity**: `S-Isocorydine ()` maps by CAS lookup to active, defining
`CHEBI:6000` / `Isocorydine`. Fresh OLS4 lookup resolved the ChEBI term with
the same formula, InChI, SMILES, and `475-67-2` CAS xref as the record, and
PubChem resolved `475-67-2` to the same stereospecific isocorydine InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/S-isocorydine.yaml
data/ingredients/mapped/Saccharin.yaml data/ingredients/mapped/Safrole.yaml
data/ingredients/mapped/Sake.yaml data/ingredients/mapped/Salicin.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct `linkml-term-validator
validate-data` with `--labels` passed for the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2544 maps exactly
to `CHEBI:6000`, uses the expected `skos:exactMatch` own-identifier row despite
the `CAS_RN_LOOKUP` curation method, and exports only `CAS:475-67-2`.

**Completeness**: The exact ChEBI identity, CAS, structure, and final SSSOM row
agree. No roles or components are asserted.

**Recommended Edits**: Optionally clean the malformed imported display label in
`data/ingredients/mapped/S-isocorydine.yaml` from `S-Isocorydine ()` to an exact
isocorydine synonym, preserving `475-67-2` and `CHEBI:6000` as the grounding
evidence.
