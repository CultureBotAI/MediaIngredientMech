# `data/ingredients/mapped/K2so4.yaml`

## Verdict

Needs curation. The exact potassium sulfate identity, CAS RN, structure fields,
rejected hydrate alias, occurrence count, and final SSSOM row pass, but both
active nutritional roles need claim-level evidence repair.

## Identity

- Reviewed record: `data/ingredients/mapped/K2so4.yaml`.
- Identifier and grounding: `identifier: CHEBI:32036` with
  `ontology_mapping.ontology_id: CHEBI:32036`, label `potassium sulfate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7778-80-5`, formula `2K.O4S`, InChI
  `InChI=1S/2K.H2O4S/c;;1-5(2,3)4/h;;(H2,1,2,3,4)/q2*+1;/p-2`, and SMILES
  `O=S(=O)([O-])[O-].[K+].[K+]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/K2cro4.yaml data/ingredients/mapped/K2hpo4.yaml data/ingredients/mapped/K2hpo4_X_3_H2o.yaml data/ingredients/mapped/K2s4o6.yaml data/ingredients/mapped/K2so4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2140`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2140`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:32036` as the active ChEBI class `potassium sulfate`,
  with CAS xref `7778-80-5`, formula `2K.O4S`, the same InChI and SMILES stored
  on the record, and the exported kg-microbe labels as synonyms.
- PubChem resolves CAS RN `7778-80-5` to the same potassium sulfate InChI stored
  on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:K2so4` to
  `CHEBI:32036`, exports only true potassium sulfate labels plus
  `CAS:7778-80-5`, omits the raw `Role:` and `Properties:` strings, and
  correctly filters the rejected heptahydrate label.
- Major: `nutritional_roles.SULFUR_SOURCE` is backed by a `DATABASE_ENTRY`
  whose curator note says `Original role text: Mineral`; that source supports a
  mineral annotation, not a sulfur-source role.
- Major: `nutritional_roles.MINERAL_SOURCE` has an empty `evidence` list after
  the #128 residual-role repair.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, heptahydrate sibling rows,
  and row-review disposition for this record.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, specific
  potassium sulfate synonyms, rejected sibling-hydrate label, aggregate copy,
  occurrence count, and final SSSOM row are present and consistent.
- The record is incomplete until both active nutritional roles carry inspected,
  role-specific evidence or are removed.

## Recommended Edits

- Major: remove `nutritional_roles.SULFUR_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support potassium sulfate
  as a sulfur source.
- Major: attach inspected database or literature evidence to
  `nutritional_roles.MINERAL_SOURCE`, or remove it if the imported mineral role
  is not supportable for this exact record, then rerun strict, term,
  round-trip, id-label, component, and SSSOM validation.
