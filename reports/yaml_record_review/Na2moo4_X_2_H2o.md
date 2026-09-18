# `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:75213` sodium molybdate dihydrate
identity, CAS-backed structure, source-backed `TRACE_ELEMENT` role, duplicate
merge, occurrence count, and final exact row pass, but final SSSOM still
publishes malformed formula strings as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2moo4_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:75213` with
  `ontology_mapping.ontology_id: CHEBI:75213`, label
  `sodium molybdate dihydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4008 CultureMech recipe occurrences across 3998 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2moo42h2o` through `Na2s2o3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:75213` as active
  `sodium molybdate dihydrate`. A fresh PubChem lookup for CAS RN `10102-40-6`
  resolves to the same dihydrate formula and InChI stored in
  `chemical_properties`.
- `reports/hydrate_grounding.tsv` classifies `CHEBI:75213` as
  `OK_HYDRATE_TERM`, and the `Na2moo42h2o` tombstone correctly defers to this
  active record.
- `nutritional_roles.TRACE_ELEMENT` is supported by the migrated CultureMech
  role evidence: the raw CultureMech role text was `Mineral source`, and
  molybdenum is the trace element supplied by this molybdate salt.
- Major: final SSSOM `other` still publishes sulfur-containing and one-sodium
  molybdate formulas as exact synonyms, including `Na2MoSO4 x 2 H2O`,
  `Na2MoSO4`, `NaMoO4 x 2 H2O`, and `NaMoO4`. Those are not clean labels for
  disodium molybdate dihydrate.

## Completeness

- The active ChEBI target, canonical CAS RN, formula, structure, source-backed
  trace-element role, 4008/3998 occurrence count, duplicate merge, tombstone
  merge, and final exact row agree.
- The remaining consequential gap is filtering malformed formula tokens from
  final SSSOM.

## Recommended Edits

- Major: demote or reject the sulfur-containing and one-sodium formula tokens
  so they no longer publish as exact `CHEBI:75213` synonyms. Rebuild final SSSOM
  and rerun final SSSOM validation plus product label validation.
