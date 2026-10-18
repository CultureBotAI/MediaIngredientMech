# `data/ingredients/mapped/Nh42ni_So42_X_6_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:86149` ammonium nickel sulfate
hexahydrate identity, hydrate structure, ChEBI CAS, and occurrence count pass,
but final SSSOM exports concentration-qualified and cross-record labels, and
`TRACE_ELEMENT` is only derived from generic imported `Mineral` role text.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh42ni_So42_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86149` with
  `ontology_mapping.ontology_id: CHEBI:86149`, label
  `ammonium nickel sulfate hexahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 150 CultureMech recipe occurrences across 150 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh42hpo4` through `Nh43_Citrate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:86149` as active
  `ammonium nickel sulfate hexahydrate` with formula
  `6H2O.2H4N.Ni.2O4S`, CAS `7785-20-8`, the same InChI and SMILES as the
  record, and the retained hexahydrate aliases.
- The #334 CAS correction moved this explicit hexahydrate row away from the
  older family CAS and onto the ChEBI dbxref CAS `7785-20-8`.
- Major: final SSSOM `other` includes
  `(NH4)2Ni(SO4)2 x 6 H2O (0.1% w/v)`, which is concentration-qualified, and
  also includes bare `(NH4)2Ni(SO4)2`, which now crosses into the separate
  active `Nh42ni_So42` row. The two-row relationship is still flagged as
  unresolved in `mappings/other_cross_record_baseline.tsv`.
- Major: `nutritional_roles.TRACE_ELEMENT` has only a `DATABASE_ENTRY` note
  preserving `Original role text: Mineral`; the record does not cite a source
  establishing that ammonium nickel sulfate hexahydrate specifically supplies a
  trace element in these media rather than only an unspecified mineral.

## Completeness

- The active hydrate ChEBI term, formula, structure, ChEBI CAS, and 150/150
  occurrence count agree.
- The remaining consequential gaps are the concentration-qualified final
  synonym, the unresolved duplicate/cross-record ammonium-nickel-sulfate row,
  and the over-specific role facet migrated from generic CultureMech
  `Mineral` source text.

## Recommended Edits

- Major: reject or demote `(NH4)2Ni(SO4)2 x 6 H2O (0.1% w/v)` and resolve
  whether bare `(NH4)2Ni(SO4)2` belongs only on this hydrate row, only on
  `data/ingredients/mapped/Nh42ni_So42.yaml`, or on a merged representative;
  then rebuild final SSSOM.
- Major: either replace `TRACE_ELEMENT` with a source-backed role that
  preserves the original `Mineral` scope or add source evidence showing that
  ammonium nickel sulfate hexahydrate is a trace-element ingredient in the
  source recipes.
