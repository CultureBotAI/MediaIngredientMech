# `data/ingredients/mapped/Navo3_X_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:132095` sodium metavanadate
monohydrate identity, hydrate structure, occurrence count, and CAS support
pass, but the record over-exports a variable hydrate label and over-specifies a
generic imported `Mineral` role as `TRACE_ELEMENT`.

## Identity

- Reviewed record: `data/ingredients/mapped/Navo3_X_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:132095` with
  `ontology_mapping.ontology_id: CHEBI:132095`, label
  `sodium metavanadate hydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 21 CultureMech recipe occurrences across 21 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Natural_Sea_Water` through `Neomycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:132095` as active
  `sodium metavanadate hydrate` with formula `H2O.Na.O3V` and the same InChI
  and SMILES as the record.
- OLS does not list CAS `20740-98-1` on `CHEBI:132095`, but a fresh PubChem
  CAS lookup for `20740-98-1` resolves to sodium metavanadate hydrate with the
  same InChI; `reports/hydrate_grounding.tsv` also grades the record
  `OK_HYDRATE_TERM`.
- Major: the final SSSOM `other` field still includes `NaVO3 x n H2O` from the
  merged `Navo3_X_N_H2o` duplicate. A variable-hydrate label is broader than
  exact monohydrate `CHEBI:132095`.
- Major: `nutritional_roles.TRACE_ELEMENT` has only a `DATABASE_ENTRY` note
  preserving `Original role text: Mineral`; the record does not cite a source
  establishing that sodium metavanadate hydrate specifically supplies a trace
  element in these media rather than only an unspecified mineral.

## Completeness

- The active hydrate ChEBI term, formula, structure, hydrate-grounding row,
  21/21 occurrence count, and core exact SSSOM row agree.
- The remaining consequential gaps are the broader variable-hydrate synonym in
  final `other` and the over-specific role facet migrated from generic
  CultureMech `Mineral` source text.

## Recommended Edits

- Major: in `data/ingredients/mapped/Navo3_X_H2o.yaml`, reject or delete the
  `NaVO3 x n H2O` synonym, then rebuild final SSSOM so `other` exports only
  monohydrate-compatible sodium metavanadate hydrate aliases plus
  `CAS:20740-98-1`.
- Major: in the same maintained YAML file, either replace `TRACE_ELEMENT` with
  a source-backed role that preserves the original `Mineral` scope or add
  source evidence showing that sodium metavanadate hydrate is a trace-element
  ingredient in the source recipes.
