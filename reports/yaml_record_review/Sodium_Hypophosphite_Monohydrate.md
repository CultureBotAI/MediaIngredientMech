# `data/ingredients/mapped/Sodium_Hypophosphite_Monohydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium hypophosphite monohydrate` keeps its own hydrate CAS
identifier `cas:10039-56-2` and maps by `CLOSE_MATCH` to active, defining
`CHEBI:234148` / `sodium hypophosphite`, the broader anhydrous parent. Fresh
OLS4 lookup confirmed the parent ChEBI label, formula, InChI, InChIKey, and
SMILES, and PubChem resolves the record's CAS RN to the monohydrate formula
`H2NaO3P`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Fluorophosphate.yaml
data/ingredients/mapped/Sodium_Gluconate.yaml
data/ingredients/mapped/Sodium_Glutamate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Hypochlorite.yaml
data/ingredients/mapped/Sodium_Hypophosphite_Monohydrate.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed for the ChEBI parent.

**Evidence**: The CAS monohydrate identity, close anhydrous-parent mapping,
and exact CAS registry companion row in final SSSOM pass. The per-record YAML
agrees with the regenerated aggregate row when keyed by identifier and
preferred term.

Two hydrate defects remain. First, `chemical_properties.molecular_formula` was
updated to the monohydrate, but `chemical_properties.inchi` and
`chemical_properties.smiles` still describe anhydrous `CHEBI:234148` and omit
the water layer present in PubChem CID `23708894` for CAS RN `10039-56-2`.
Second, `reports/hydrate_grounding.tsv` classifies this record as
`CAS_MISSING_ANCHOR_ROWS`: final SSSOM rows 2646-2647 preserve the close ChEBI
parent and exact CAS registry row, but the `kgmicrobe.compound` hydrate anchor
row is still missing.

**Completeness**: The final row avoids exporting the broader anhydrous label as
a synonym, but the record still needs hydrate-specific structure fields and the
local hydrate anchor in final SSSOM.

**Recommended Edits**: Replace the inherited anhydrous InChI/SMILES with
hydrate-specific structure values and add the missing
`kgmicrobe.compound:sodium_hypophosphite_monohydrate` exact registry row next
to the parent-CHEBI and CAS rows.
