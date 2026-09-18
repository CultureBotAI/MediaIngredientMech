# `data/ingredients/mapped/Voso4_X_2_H2o.yaml`

## Verdict

Pass. The exact `CHEBI:87009` vanadyl sulfate dihydrate identity, structure
fields, source-backed trace-element role, aggregate row, and final SSSOM row
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Voso4_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:87009` with matching
  `ontology_mapping.ontology_id`, label `vanadyl sulfate dihydrate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical fields: formula `2H2O.O4S.OV` with populated InChI and SMILES
  strings.
- Synonyms: two raw CultureMech role/property strings, five hydrate spellings,
  six clean vanadyl sulfate dihydrate labels, and the reviewed IUPAC synonym
  `oxovanadium(2+) sulfate--water (1/2)`.
- Occurrences: 81 CultureMech recipe occurrences across 81 media.
- Role: `TRACE_ELEMENT` imported from CultureMech original role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vitamins` through `Voso4_X_5_H2o`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the three
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:87009` returns active label
  `vanadyl sulfate dihydrate`, defines it as the dihydrate form of vanadyl
  sulfate, and exposes matching formula and structure strings.
- The OLS4 synonym set includes the reviewed `VOSO4.2H2O` and
  `oxovanadium(2+) sulfate--water (1/2)` strings plus the clean dihydrate
  labels `vanadic sulfate dihydrate`,
  `vanadium oxide sulfate dihydrate`, `vanadium oxysulfate dihydrate`, and
  `vanadium(IV) oxide sulfate dihydrate`.
- The `TRACE_ELEMENT` role is backed by `DATABASE_ENTRY` evidence carrying the
  original CultureMech role text `Mineral`.
- The final SSSOM row correctly has
  `MIM:Voso4_X_2_H2o skos:exactMatch CHEBI:87009` with no concentration- or
  process-qualified `other` labels.

## Issues

None.

## Completeness

- The exact CHEBI mapping, structure fields, occurrence count, source-backed
  trace-element role, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
