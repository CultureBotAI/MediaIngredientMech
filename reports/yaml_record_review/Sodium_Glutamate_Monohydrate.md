# `data/ingredients/mapped/Sodium_Glutamate_Monohydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium glutamate monohydrate` is now correctly grounded to
active, defining `CHEBI:232425` / `monosodium L-glutamate hydrate`. Fresh OLS4
lookup confirmed the ChEBI hydrate formula `C5H8NO4.H2O.Na` and hydrate
InChI, and PubChem resolves CAS RN `6106-04-3` to a hydrated sodium-glutamate
record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Fluorophosphate.yaml
data/ingredients/mapped/Sodium_Gluconate.yaml
data/ingredients/mapped/Sodium_Glutamate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Hypochlorite.yaml
data/ingredients/mapped/Sodium_Hypophosphite_Monohydrate.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed.

**Evidence**: The exact CHEBI hydrate identity, corrected formula, CAS RN, and
CultureMech-imported `NITROGEN_SOURCE` role pass. The raw `Role:` /
`Properties:` strings are correctly filtered from final SSSOM, and the
per-record YAML agrees with the regenerated aggregate row when keyed by
identifier and preferred term.

Two hydrate-boundary defects remain. First, `chemical_properties.inchi` and
`chemical_properties.smiles` still describe the anhydrous salt and omit the
water layer present in `CHEBI:232425` and PubChem CID `87090819`. Second, final
SSSOM row 2644 exports anhydrous `CHEBI:64243` surface forms, including
`Glutamate Sodium`, `Glutamate monosodium salt`, `Glutamic acid, monosodium
salt`, `L(+) Sodium glutamate`, `MSG`, `Sodium hydrogen glutamate`, and
`sodium (2S)-2-ammoniopentanedioate`, on the monohydrate record. A hidden and
ignored-inclusive search found a separate `Sodium_L-glutamate.yaml` record for
the anhydrous `CHEBI:64243` sibling.

**Completeness**: The record has refreshed 16-occurrence statistics. It needs
hydrate-specific structure fields and should keep only hydrate-specific labels
in final SSSOM.

**Recommended Edits**: Replace the anhydrous InChI/SMILES with the
hydrate-specific ChEBI or PubChem structure, move the anhydrous
monosodium-glutamate synonyms to `Sodium_L-glutamate.yaml` where absent, and
rebuild final SSSOM so row 2644 exports only hydrate-specific aliases plus
`CAS:6106-04-3`.
