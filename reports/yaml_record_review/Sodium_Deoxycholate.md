# `data/ingredients/mapped/Sodium_Deoxycholate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `sodium Deoxycholate` maps exactly to active, defining
`CHEBI:9177` / `sodium deoxycholate`. Fresh OLS4 lookup confirmed the anhydrous
ChEBI identity, CAS RN `302-95-4`, formula `C24H39O4.Na`, and the curated
IUPAC synonym; PubChem resolves the CAS RN to CID `23668196` with the same
InChI and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Cyanide.yaml
data/ingredients/mapped/Sodium_D-Lactate.yaml
data/ingredients/mapped/Sodium_Deoxycholate.yaml
data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Dithionite.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CultureBotHT CAS, formula, and
structure fields all agree, and the per-record YAML agrees with the
regenerated aggregate row when keyed by `(preferred_term, mapping_status)`.

The final SSSOM row needs synonym cleanup. Row 2633 exports `100`, a raw
numeric CultureBotHT token, and `Sodium deoxycholate monohydrate`, which
belongs to the CAS-primary hydrate sibling, as `other` synonyms of anhydrous
`CHEBI:9177`.

**Completeness**: No roles or components are asserted. The record is complete
for exact anhydrous identity, but it should not publish numeric or hydrate
labels as same-substance anhydrous synonyms.

**Recommended Edits**: Remove `100` and `Sodium deoxycholate monohydrate` from
`data/ingredients/mapped/Sodium_Deoxycholate.yaml` or filter them out of final
SSSOM, rebuild final SSSOM, and confirm row 2633 exports only true anhydrous
aliases plus `CAS:302-95-4`.
