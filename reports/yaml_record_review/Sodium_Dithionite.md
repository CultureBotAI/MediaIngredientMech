# `data/ingredients/mapped/Sodium_Dithionite.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium dithionite` maps exactly to active, defining
`CHEBI:66870` / `sodium dithionite`. Fresh OLS4 lookup confirmed the ChEBI
label, CAS RN `7775-14-6`, formula `2Na.O4S2`, InChI, InChIKey, SMILES, and
exact IUPAC synonym, and PubChem resolves the CAS RN to CID `24489` with the
same InChI and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Cyanide.yaml
data/ingredients/mapped/Sodium_D-Lactate.yaml
data/ingredients/mapped/Sodium_Deoxycholate.yaml
data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Dithionite.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CAS, formula, structure fields, and
same-substance dithionite aliases pass. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(preferred_term, mapping_status)`.

Two claims need cleanup. The `REDUCING_AGENT` role is still a provisional
`COMPUTATIONAL_PREDICTION` claim from a name-pattern rule. Final SSSOM row 2636
also exports the old scutellarin labels inherited from the wrongly grounded
`Na2S2O4` duplicate; those labels describe the previous `CHEBI:61278`
candidate, not sodium dithionite.

**Completeness**: The raw `Properties:` strings are correctly filtered from
final SSSOM. The record is otherwise complete for exact sodium dithionite
identity after the `Na2S2O4` merge.

**Recommended Edits**: Remove the scutellarin inherited synonyms from
`data/ingredients/mapped/Sodium_Dithionite.yaml` and either source or remove
the provisional `REDUCING_AGENT` role, then rebuild final SSSOM and confirm row
2636 exports only same-substance dithionite aliases plus `CAS:7775-14-6`.
