# `data/ingredients/mapped/Sodium_Malate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium malate` maps exactly to active, defining `CHEBI:91261` /
`disodium (S)-malate`. Fresh OLS4 lookup confirmed the ChEBI label, CAS RN
`138-09-0`, formula `C4H4O5.2Na`, InChI, InChIKey, SMILES, and
same-substance L-malate synonyms, and PubChem resolves the CAS RN to CID
`6097189` with the same formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_L-lactate.yaml
data/ingredients/mapped/Sodium_Lactate.yaml
data/ingredients/mapped/Sodium_M-arsenite.yaml
data/ingredients/mapped/Sodium_Malate.yaml
data/ingredients/mapped/Sodium_Maleate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, canonical CAS RN, formula, InChI,
SMILES, and same-substance L-malate aliases pass. The raw `Properties:` strings
are correctly filtered from final SSSOM, and the per-record YAML agrees with
the regenerated aggregate row when keyed by identifier and preferred term.

The final row and roles still need curation. Final SSSOM row 2655 exports
`DL-Na-malate`, `Na-DL-malate`, `Na2-DL-malate`, `Sodium DL-malate`,
`DL-Sodium malate`, and the malformed `Sodium Malate And` token on an
L-specific disodium malate term. The `CARBON_SOURCE` and `ENERGY_SOURCE` roles
are both provisional `COMPUTATIONAL_PREDICTION` claims with `review
recommended` curator notes.

**Completeness**: The record has refreshed 82-occurrence statistics. Its exact
identity is sound, but the final synonym set must preserve the L-malate
stereochemical boundary.

**Recommended Edits**: Remove malformed and D,L-malate aliases from this
L-specific record, and either source or remove the provisional carbon and
energy roles before rebuilding final SSSOM.
