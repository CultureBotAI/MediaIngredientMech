# `data/ingredients/mapped/Ribitol.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Ribitol` maps exactly to active, defining `CHEBI:15963` /
`ribitol`. Fresh OLS4 lookup resolved the ChEBI term and matched the record's
formula, InChI, and SMILES. The `D-adonitol (D-ribitol)` backfill token is
chemically consistent with the target because OLS also returns `D-Adonitol` and
`D-Ribitol` as ChEBI synonyms for `CHEBI:15963`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhodomycin_A.yaml
data/ingredients/mapped/Rhodomycin_B.yaml data/ingredients/mapped/Ribitol.yaml
data/ingredients/mapped/Riboflavin.yaml
data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the same 5
files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2506 maps exactly
to `CHEBI:15963`.

The final SSSOM `other` payload still exports `(+)-D-arabitol`, which is not a
synonym for ribitol. A fresh ChEBI OLS exact search for that surface resolves
to `CHEBI:18333` / `D-arabinitol`, a different stereoisomer, while
`CHEBI:15963` lists ribitol/adonitol synonyms but not arabitol.

**Completeness**: The exact ChEBI identity, chemical properties, and occurrence
provenance are complete enough. The only unsafe payload is the backfilled
arabitol synonym.

**Recommended Edits**: Remove the `(+)-D-arabitol` `sssom_other_backfill`
synonym from `data/ingredients/mapped/Ribitol.yaml` and regenerate final SSSOM;
row 2506 should keep `D-adonitol (D-ribitol)` but stop exporting the arabitol
token.
