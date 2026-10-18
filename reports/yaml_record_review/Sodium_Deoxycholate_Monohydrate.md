# `data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium deoxycholate monohydrate` is correctly kept distinct from
anhydrous `CHEBI:9177` / `sodium deoxycholate` with primary identifier
`cas:145224-92-6`. Fresh PubChem lookup resolved CAS RN `145224-92-6` to CID
`23679071` with the monohydrate formula, SMILES, and InChI in the record, and
fresh ChEBI OLS search found no specific monohydrate term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Cyanide.yaml
data/ingredients/mapped/Sodium_D-Lactate.yaml
data/ingredients/mapped/Sodium_Deoxycholate.yaml
data/ingredients/mapped/Sodium_Deoxycholate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Dithionite.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The monohydrate CAS identity, PubChem structure, and
`skos:closeMatch` to the anhydrous ChEBI term pass, and the per-record YAML
agrees with the regenerated aggregate row when keyed by `(preferred_term,
mapping_status)`.

The final SSSOM needs repair. `reports/hydrate_grounding.tsv` classifies this
record as `CAS_MISSING_ANCHOR_ROWS`: rows 2634-2635 preserve the exact CAS
identity but omit an exact
`kgmicrobe.compound:sodium_deoxycholate_monohydrate` anchor. Row 2634 also
exports an exact anhydrous `CHEBI:9177` IUPAC synonym and a misspelled raw
`Sodim deoxycholate monohydrate` label in `other`.

**Completeness**: No roles or components are asserted. The hydrate has enough
CAS and PubChem support for a distinct CAS-primary identity; the material gap
is the missing kg-microbe anchor and unsafe final synonyms.

**Recommended Edits**: Add the missing exact
`kgmicrobe.compound:sodium_deoxycholate_monohydrate` anchor, remove anhydrous
and typo labels from the hydrate's final `other`, rebuild final SSSOM, and
confirm the hydrate-grounding row no longer reports `CAS_MISSING_ANCHOR_ROWS`.
