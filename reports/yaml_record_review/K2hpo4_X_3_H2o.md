# `data/ingredients/mapped/K2hpo4_X_3_H2o.yaml`

## Verdict

Needs curation. The record now has a distinct local registry identifier, a
`skos:closeMatch` row to the anhydrous ChEBI parent, an exact registry row, and
hydrate-specific synonyms, but the structure pair and `kg_microbe_node_id`
still point at anhydrous `CHEBI:131527`.

## Identity

- Reviewed record: `data/ingredients/mapped/K2hpo4_X_3_H2o.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:k2hpo4_x_3_h2o` with
  `ontology_mapping.ontology_id: CHEBI:131527`, label
  `dipotassium hydrogen phosphate`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: no CAS RN after the #334 removal, formula
  `HO4P.2K.3H2O`, but the active InChI and SMILES still describe only the
  anhydrous `CHEBI:131527` parent.

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

- Fresh exact OLS4 ChEBI searches for `K2HPO4 x 3 H2O` and `K2HPO4.3H2O`
  returned zero standalone ChEBI hits, matching the #321 local-registry mint.
- The final SSSOM publishes the intended pair of rows: a `skos:closeMatch` from
  `MIM:K2hpo4_X_3_H2o` to anhydrous `CHEBI:131527` and a
  `skos:exactMatch` to `kgmicrobe.compound:k2hpo4_x_3_h2o`. The close-match
  row keeps only hydrate-specific surface forms in `other`.
- The #334 curation event correctly removed CAS RN `7758-11-4` because it
  belongs to anhydrous K2HPO4, not this trihydrate.
- Major: `chemical_properties.inchi` and `chemical_properties.smiles` still
  match the anhydrous parent even though the formula was corrected to include
  three waters of hydration.
- Major: `kg_microbe_node_id: CHEBI:131527` is a stale cross-prefix
  compatibility value after the #321 mint to
  `kgmicrobe.compound:k2hpo4_x_3_h2o`; the hidden and ignored-inclusive search
  found the same mismatch in `reports/kg_microbe_node_id_mismatches.tsv`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM rows, docs projections, hydrate review rows, and
  row-review dispositions for this record.

## Completeness

- The local hydrate identifier, close parent mapping, exact registry row,
  hydrate-specific formula, CAS removal, aggregate copy, occurrence count, and
  buffer role are present.
- The structure strings and downstream node compatibility ID remain incomplete
  because they still reference the anhydrous parent.

## Recommended Edits

- Major: replace or remove the anhydrous `chemical_properties.inchi` and
  `chemical_properties.smiles` values in
  `data/ingredients/mapped/K2hpo4_X_3_H2o.yaml`.
- Major: replace or delete `kg_microbe_node_id: CHEBI:131527` so downstream
  node exports do not collapse the trihydrate onto the anhydrous ChEBI parent,
  then rerun strict, term, round-trip, SSSOM, and
  `scripts/audit_kg_microbe_node_ids.py --check`.
