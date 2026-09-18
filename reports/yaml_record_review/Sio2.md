# `data/ingredients/mapped/Sio2.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `SiO2` maps exactly to active, defining `CHEBI:30563` /
`silicon dioxide`. Fresh OLS4 lookup resolved the ChEBI term, and PubChem
resolves CAS RN `7631-86-9` to CID 24261 with a formula, InChI, and SMILES
matching the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sio2.yaml
data/ingredients/mapped/Sisomicin_Sulfate_Salt.yaml
data/ingredients/mapped/Skim_milk_powder.yaml
data/ingredients/mapped/Skimmed_Milk.yaml
data/ingredients/mapped/Skirrow_Supplement.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for `Sio2`, `Sisomicin_Sulfate_Salt`, and `Skimmed_Milk`; the MICRO and
kgmicrobe.ingredient records were skipped because those prefixes are outside the
Engine A OBO term-validation subset.

**Evidence**: The CultureMech direct match, exact CHEBI identity, CAS field, and
structure fields pass. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(identifier, preferred_term)`.

The final SSSOM row needs synonym cleanup. Row 2592 correctly filters the raw
`Role: Mineral source` token, but it still exports unreviewed kg-microbe related
synonyms as `other`. Fresh OLS4 lookup lists `Silica, amorphous`, `(SiO2)n`,
`[SiO2]`, and several alternate strings only in ChEBI `related_synonyms`; only
`silicon(IV) oxide` is listed as an exact synonym among the exported non-CAS
tokens.

**Completeness**: The exact CHEBI identity, CAS field, structure fields,
single-ingredient classification, occurrence counts, and row-review
confirmation agree. The final SSSOM synonym payload needs exact-scope review.

**Recommended Edits**: Remove or demote any non-exact kg-microbe synonyms from
`data/ingredients/mapped/Sio2.yaml`, then rebuild final SSSOM and confirm row
2592 exports only exact synonyms plus `CAS:7631-86-9`.
