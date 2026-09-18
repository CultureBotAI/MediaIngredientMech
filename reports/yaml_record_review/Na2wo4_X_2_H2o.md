# `data/ingredients/mapped/Na2wo4_X_2_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63939` sodium tungstate dihydrate
identity, CAS-backed structure, duplicate merges, occurrence count, and
`TRACE_ELEMENT` role pass, but final SSSOM still publishes concentration,
malformed, and anhydrous-parent labels as dihydrate synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2wo4_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:63939` with
  `ontology_mapping.ontology_id: CHEBI:63939`, label
  `sodium tungstate dihydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1642 CultureMech recipe occurrences across 1640 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2so3_X_5_H2o` through `Na2wo4_X_2_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63939` as active
  `sodium tungstate dihydrate`, with formula `2H2O.2Na.O4W`, CAS `10213-10-2`,
  and an InChI matching the record.
- A fresh PubChem CAS lookup for `10213-10-2` resolves to sodium tungstate
  dihydrate with the same formula and InChI, confirming the hydrate-specific
  chemical block.
- The `TRACE_ELEMENT` role is supported by imported CultureMech `Mineral` role
  text for this tungsten salt.
- Major: final SSSOM `other` publishes concentration-qualified
  `Na2WO4 x 2 H2O (0.1% w/v)`, malformed `NaWO4` and `Na2WO2` hydrate labels,
  and a bullet-dot CultureMech raw label.
- Major: final SSSOM also publishes aliases that OLS lists on anhydrous
  `CHEBI:63940`, including `Disodium tetraoxotungstate`,
  `Sodium tungstate(VI)`, `Sodium tungsten oxide`, `Sodium wolframate`,
  `Tungstic acid, disodium salt`, and `sodium tetraoxotungstate(VI)`.

## Completeness

- The active ChEBI term, hydrate-specific CAS RN, formula, structure, 1640/1642
  occurrence statistics, duplicate merges, trace-element role, and exact final
  SSSOM row otherwise agree.
- The remaining consequential gap is cleanup of non-synonym final `other`
  tokens.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2wo4_X_2_H2o.yaml`, demote the
  concentration-qualified, malformed, and bullet-dot raw labels that should not
  publish as exact `CHEBI:63939` synonyms.
- Major: remove the anhydrous `CHEBI:63940` aliases from the dihydrate record
  or retype them as rejected parent-term provenance. Rebuild final SSSOM and
  rerun final SSSOM validation plus product label validation.
