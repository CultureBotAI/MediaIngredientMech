# `data/ingredients/mapped/Trinitrotoluene.yaml`

## Verdict

Needs curation, major. The CAS RN, `TNT` synonym, occurrence count, aggregate
row, and final SSSOM row are synchronized, but CAS `118-96-7` denotes
`2,4,6-trinitrotoluene` and the record is exact-mapped to broader
`CHEBI:27135` while exact candidate `CHEBI:46053` is available.

## Identity

- Reviewed record: `data/ingredients/mapped/Trinitrotoluene.yaml`.
- Identifier and grounding: `identifier: CHEBI:27135` with matching
  `ontology_mapping.ontology_id`, label `trinitrotoluene`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `118-96-7`.
- Synonyms: one CultureBotHT `TNT` exact synonym.
- Occurrences: 0 recipe occurrences in 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trimethylamine-hcl` through `Tris_Acetate_Stock_Solution`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for current target `CHEBI:27135` returns a
  low-specificity `trinitrotoluene` term that has children and lacks formula,
  InChI, SMILES, or CAS metadata.
- Fresh CHEBI-scoped OLS4 exact search for `2,4,6-trinitrotoluene` returns
  `CHEBI:46053`, whose label is the specific TNT isomer.
- Fresh PubChem lookup for CAS `118-96-7` returns CID 8376 with
  `CHEBI:46053`, `2,4,6-Trinitrotoluene`, `Trinitrotoluene`, and `TNT` among
  its synonyms.
- The final SSSOM row has
  `MIM:Trinitrotoluene skos:exactMatch CHEBI:27135` and exports `TNT` plus
  `CAS:118-96-7` in `other`.

## Issues

### Major: the exact target is broader than the CAS-backed subject

CAS `118-96-7` identifies `2,4,6-trinitrotoluene`; ChEBI also has
`CHEBI:46053` for that exact isomer. Leaving the row exact-mapped to the
broader `trinitrotoluene` class loses isomer specificity.

## Completeness

- The YAML, aggregate copy, and final SSSOM row agree on the current broader
  mapping.
- The consequential gap is remapping the CAS-backed TNT identity to the
  exact ChEBI isomer.

## Recommended Edits

- Remap `Trinitrotoluene` from `CHEBI:27135` to `CHEBI:46053`, backfill the
  ChEBI formula and structure fields for the specific TNT isomer, and
  regenerate the aggregate and final SSSOM row.
