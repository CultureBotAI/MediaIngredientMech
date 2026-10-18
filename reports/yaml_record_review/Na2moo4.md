# `data/ingredients/mapped/Na2moo4.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:75215` anhydrous sodium molybdate
identity, corrected CAS RN, source-backed `TRACE_ELEMENT` role, occurrence
count, rejected hydrate labels, and final exact row pass, but final SSSOM still
publishes a concentration-qualified source label as a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2moo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:75215` with
  `ontology_mapping.ontology_id: CHEBI:75215`, label
  `sodium molybdate (anhydrous)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 227 CultureMech recipe occurrences across 227 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2hpo4_X_2_H2o` through `Na2moo4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:75215` as active
  `sodium molybdate (anhydrous)`, with anhydrous sodium molybdate related
  synonyms. A fresh PubChem lookup for CAS RN `7631-95-0` resolves to the same
  anhydrous formula and InChI stored in `chemical_properties`.
- The 2026-09-12 hidden-hydrate cleanup correctly marks monohydrate and
  dihydrate labels as rejected so this anhydrous record no longer resolves its
  hydrate siblings.
- `nutritional_roles.TRACE_ELEMENT` is supported by the migrated CultureMech
  role evidence: the raw CultureMech role text was `Mineral source`, and
  molybdenum is the trace element supplied by this molybdate salt.
- Major: final SSSOM still publishes `Na2MoO4 (0.01 M)` in `other`. That token
  is a concentration-qualified recipe label, not a synonym for anhydrous
  `CHEBI:75215`.

## Completeness

- The active ChEBI target, corrected CAS RN, formula, structure, source-backed
  trace-element role, 227/227 occurrence count, rejected sibling hydrate labels,
  and final exact row agree.
- The remaining consequential gap is filtering the concentration-qualified
  final `other` token.

## Recommended Edits

- Major: keep `Na2MoO4 (0.01 M)` as occurrence provenance only so it no longer
  publishes as an exact `Na2MoO4` synonym; rebuild final SSSOM and rerun final
  SSSOM validation plus product label validation.
