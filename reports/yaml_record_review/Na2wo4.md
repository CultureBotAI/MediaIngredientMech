# `data/ingredients/mapped/Na2wo4.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63940` anhydrous sodium tungstate
identity, CAS-backed structure, duplicate merge, occurrence count,
`TRACE_ELEMENT` role, and hidden-dihydrate rejection pass, but final SSSOM still
publishes a concentration-qualified label as a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2wo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:63940` with
  `ontology_mapping.ontology_id: CHEBI:63940`, label `sodium tungstate`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 132 CultureMech recipe occurrences across 132 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2so3_X_5_H2o` through `Na2wo4_X_2_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63940` as active anhydrous
  `sodium tungstate` with formula `2Na.O4W`, CAS `13472-45-2`, and an InChI
  matching the record.
- A fresh PubChem CAS lookup for `13472-45-2` resolves to anhydrous sodium
  tungstate with the same formula and InChI, confirming the chemical block.
- The `TRACE_ELEMENT` role is supported by imported CultureMech `Mineral` role
  text for this tungsten salt.
- The #251 repair correctly marked the sibling dihydrate label as
  `REJECTED_LABEL`, and that rejected label is filtered from final SSSOM.
- Major: final SSSOM `other` publishes `Na2WO4 (10 mM)`, a concentration-stated
  recipe label rather than a clean same-substance synonym.

## Completeness

- The active ChEBI term, canonical CAS RN, formula, structure, 132/132
  occurrence count, trace-element role, rejected hidden-dihydrate label, and
  exact final SSSOM row otherwise agree.
- The remaining consequential gap is the concentration-qualified label in the
  final synonym surface.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2wo4.yaml`, demote or reject
  `Na2WO4 (10 mM)` so it no longer publishes as an exact `CHEBI:63940`
  synonym. Rebuild final SSSOM and rerun final SSSOM validation plus product
  label validation.
