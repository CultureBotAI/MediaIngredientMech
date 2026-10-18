# `data/ingredients/mapped/Navo3.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:75221` sodium metavanadate identity,
CAS-backed structure, occurrence count, and final exact SSSOM row pass, but
`TRACE_ELEMENT` is only derived from generic imported `Mineral` role text.

## Identity

- Reviewed record: `data/ingredients/mapped/Navo3.yaml`.
- Identifier and grounding: `identifier: CHEBI:75221` with
  `ontology_mapping.ontology_id: CHEBI:75221`, label `sodium metavanadate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 7 CultureMech recipe occurrences across 7 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Natural_Sea_Water` through `Neomycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:75221` as active
  `sodium metavanadate` with formula `Na.O3V`, CAS `13718-26-8`, and the same
  InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `13718-26-8` resolves to sodium metavanadate
  with the same InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Navo3` exactly to `CHEBI:75221`, keeps only
  true sodium metavanadate aliases plus `CAS:13718-26-8` in `other`, and
  filters the raw CultureMech `Role:`/`Properties:` labels.
- Major: `nutritional_roles.TRACE_ELEMENT` has only a `DATABASE_ENTRY` note
  preserving `Original role text: Mineral`; the record does not cite a source
  establishing that sodium metavanadate specifically supplies a trace element
  in these media rather than only an unspecified mineral.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 7/7 occurrence count, and
  final exact row agree.
- The remaining consequential gap is the over-specific role facet migrated
  from generic CultureMech `Mineral` source text.

## Recommended Edits

- Major: in `data/ingredients/mapped/Navo3.yaml`, either replace
  `TRACE_ELEMENT` with a source-backed role that preserves the original
  `Mineral` scope or add source evidence showing that sodium metavanadate is a
  trace-element ingredient in the source recipes.
