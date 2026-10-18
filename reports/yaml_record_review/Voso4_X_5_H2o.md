# `data/ingredients/mapped/Voso4_X_5_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:132758` vanadyl sulfate pentahydrate identity,
structure fields, CAS RN, source-backed trace-element role, aggregate row, and
final exact SSSOM predicate pass, but final SSSOM exports one
concentration-qualified label and one hydrate-erasing `VOSO4` label as exact
`other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Voso4_X_5_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:132758` with matching
  `ontology_mapping.ontology_id`, label `vanadyl sulfate pentahydrate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `14708-82-8`.
- Chemical fields: formula `5H2O.O4S.OV` with populated InChI and SMILES
  strings.
- Synonyms: one raw CultureMech role/property string, three hydrate spellings,
  five clean vanadyl sulfate pentahydrate labels, the reviewed IUPAC synonym
  `oxovanadium(2+) sulfate--water (1/5)`, and the raw recovered surface form
  `VOSO4`.
- Occurrences: 16 CultureMech recipe occurrences across 16 media.
- Role: `TRACE_ELEMENT` imported from CultureMech original role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vitamins` through `Voso4_X_5_H2o`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the three
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:132758` returns active label
  `vanadyl sulfate pentahydrate`, defines it as vanadyl sulfate with five water
  molecules, and exposes matching formula, structure strings, and CAS
  `14708-82-8`.
- Fresh OLS4 exact search for `VOSO4` did not return `CHEBI:132758`; it
  returned only the unspecified vanadyl sulfate hydrate class through hydrate
  formula strings containing `VOSO4`.
- The `TRACE_ELEMENT` role is backed by `DATABASE_ENTRY` evidence carrying the
  original CultureMech role text `Mineral`.
- The final SSSOM row correctly has
  `MIM:Voso4_X_5_H2o skos:exactMatch CHEBI:132758`.

## Issues

- Major: the final exact `CHEBI:132758` row exports
  `VOSO4 x 5 H2O (0.01% w/v)` as an `other` synonym. That string describes a
  recipe concentration, not a synonymous label for vanadyl sulfate
  pentahydrate.
- Major: the final exact `CHEBI:132758` row also exports bare `VOSO4` as an
  `other` synonym. That label erases the pentahydrate water count and is not
  present on the active ChEBI pentahydrate term.

## Completeness

- The exact CHEBI mapping, structure fields, CAS RN, occurrence count,
  source-backed trace-element role, aggregate copy, and SSSOM predicate agree.
- The final synonym set needs to be restricted to pentahydrate-specific labels
  that do not encode recipe-specific concentration context.

## Recommended Edits

- Remove `VOSO4 x 5 H2O (0.01% w/v)` and `VOSO4` from the record's exported
  synonym set, or update final SSSOM export to suppress those stale
  surface-form and concentration-qualified tokens.
- Rebuild SSSOM and rerun strict validation, LinkML term validation, SSSOM
  invariant validation, and the cross-record `other` synonym audit.
