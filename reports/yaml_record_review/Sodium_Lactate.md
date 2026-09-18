# `data/ingredients/mapped/Sodium_Lactate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium lactate` maps exactly to active, defining
`CHEBI:75228` / `sodium lactate`. Fresh OLS4 lookup confirmed the ChEBI label,
CAS RN `72-17-3`, formula `C3H5O3.Na`, InChI, InChIKey, SMILES, and the
same-substance ChEBI synonyms, and PubChem resolves the CAS RN to CID
`23666456` with the same formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_L-lactate.yaml
data/ingredients/mapped/Sodium_Lactate.yaml
data/ingredients/mapped/Sodium_M-arsenite.yaml
data/ingredients/mapped/Sodium_Malate.yaml
data/ingredients/mapped/Sodium_Maleate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, InChI, SMILES, and
stereo-unspecified lactate synonyms pass. The CultureMech `CARBON_SOURCE` role
also passes because it is a `DATABASE_ENTRY` retaining the original
`Carbon Source` role text. The raw `Role:` / `Properties:` strings and the
`(after autoclaving)` occurrence fragment are correctly filtered from final
SSSOM. The per-record YAML agrees with the regenerated aggregate row when keyed
by identifier and preferred term.

Two fields need cleanup. Final SSSOM row 2653 exports `1 M Sodium lactate` and
`1 % Sodium Lactate`, which are concentration-specific recipe labels rather
than synonyms for sodium lactate. The `ENERGY_SOURCE` role is still a
`COMPUTATIONAL_PREDICTION` added alongside `CARBON_SOURCE` with a provisional
`review recommended` curator note.

**Completeness**: The record has refreshed 283-occurrence statistics, but the
final synonym set and the energy role still need review.

**Recommended Edits**: Remove or scope the concentration-qualified lactate
labels before SSSOM export and either source or remove the provisional
`ENERGY_SOURCE` role.
