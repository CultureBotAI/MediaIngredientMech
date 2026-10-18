# `data/ingredients/mapped/Sodium_Maleate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium maleate` maps exactly to active, defining `CHEBI:91263` /
`disodium maleate`. Fresh OLS4 lookup confirmed the ChEBI label, CAS RN
`371-47-1`, formula `C4H2O4.2Na`, InChI, InChIKey, SMILES, and exact IUPAC
synonym, and PubChem resolves the CAS RN to CID `6364608` with the same
formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_L-lactate.yaml
data/ingredients/mapped/Sodium_Lactate.yaml
data/ingredients/mapped/Sodium_M-arsenite.yaml
data/ingredients/mapped/Sodium_Malate.yaml
data/ingredients/mapped/Sodium_Maleate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, InChI, SMILES, and
same-substance maleate synonyms pass. The raw `Properties:` string is
correctly filtered from final SSSOM row 2656, whose `other` column contains
only `Maleic acid, disodium salt`, `disodium (2Z)-but-2-enedioate`, and
`CAS:371-47-1`. The per-record YAML agrees with the regenerated aggregate row
when keyed by identifier and preferred term.

The `BUFFER` role is still a provisional in-session LLM role assignment with
`COMPUTATIONAL_PREDICTION` evidence, confidence `0.6`, and a `review
recommended` curator note.

**Completeness**: The record is otherwise complete for exact disodium maleate
identity and has refreshed 3-occurrence statistics.

**Recommended Edits**: Either replace the provisional `BUFFER` role with a
sourced database or literature claim, or remove it.
