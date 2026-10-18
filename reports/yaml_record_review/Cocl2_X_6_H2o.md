# `data/ingredients/mapped/Cocl2_X_6_H2o.yaml`

## Verdict

Needs curation; minor. This record is a rejected duplicate tombstone merged into
`Cobalt_chloride_hexahydrate`, its identifier, `ontology_mapping.ontology_id`,
and `kg_microbe_node_id` now all point at `CHEBI:53503`, and it has no active
final SSSOM row. The stale anhydrous CoCl2 structure fields,
hydrate-mismatched synonyms, `ingredient_type`, and provisional
`TRACE_ELEMENT` role should be cleaned from the rejected record.

## Identity

- Reviewed record: `data/ingredients/mapped/Cocl2_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:53503`,
  `ontology_mapping.ontology_id: CHEBI:53503`,
  `ontology_label: cobalt chloride hexahydrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: REJECTED`, and
  `kg_microbe_node_id: CHEBI:53503`.
- The August 2026 and September 2026 curation history records show this row was
  merged into `Cobalt_chloride_hexahydrate`, had its tombstone ontology pointer
  refreshed from `CHEBI:35696` to `CHEBI:53503`, had its CAS RN corrected from
  the anhydrous `7646-79-9` value to the hydrate-specific `7791-13-1` value, and
  had its compatibility node id corrected to `CHEBI:53503`.
- The record still stores `molecular_formula: 2Cl.Co`, the anhydrous CoCl2
  InChI, and the anhydrous `[Cl-].[Cl-].[Co+2]` SMILES even though
  `CHEBI:53503` is cobalt chloride hexahydrate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cocl2_X_6_H2o.yaml data/ingredients/mapped/Coenzyme_A.yaml data/ingredients/mapped/Colchiceine.yaml data/ingredients/mapped/Colistin_Sulfate.yaml data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cocl2_X_6_H2o.yaml data/ingredients/mapped/Coenzyme_A.yaml data/ingredients/mapped/Colchiceine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-identified records in this batch.
  `Colistin_Sulfate` and `Colistin_Sulfate_Salt` were intentionally skipped
  because they are grounded to NCIT, while this LinkML term-validation pass was
  limited to CHEBI records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found this rejected `CHEBI:53503` tombstone, the active
  `MIM:Cobalt_chloride_hexahydrate` SSSOM row, the stale pre-merge row-review
  artifacts for this record, and expected generated docs rows.
- Hidden/ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found the active `MIM:Cobalt_chloride_hexahydrate` row and no
  `MIM:Cocl2_X_6_H2o` row, matching the tombstone curation note that SSSOM rows
  were dropped.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 2636 rows for the active
  `CHEBI:53503` target whose occurrence weights sum to 2638, and the rejected
  duplicate keeps `0/0` occurrences.
- Live OLS lookup for `CHEBI:53503` was checked with the adjacent active
  `Cobalt_chloride_hexahydrate` review and matched cobalt chloride hexahydrate,
  its `7791-13-1` CAS RN, and its hydrate-specific formula, InChI, and SMILES.
- The final SSSOM export drops rejected records, so this record's anhydrous
  synonyms and different-hydrate synonyms are not present in the active SSSOM
  `other` column.
- `TRACE_ELEMENT` still cites the old CultureMech role text with
  `COMPUTATIONAL_PREDICTION`-style evidence despite this row now being a
  zero-occurrence rejected duplicate.

## Completeness

- The tombstone pointer, corrected CAS RN, compatibility id, lack of active
  SSSOM export, and `0/0` occurrence count are internally consistent.
- The cleanup gap is limited to stale fields left behind on the rejected
  duplicate and does not affect final SSSOM identity rows.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Cocl2_X_6_H2o.yaml`, clear the stale
  anhydrous `chemical_properties` structure fields, remove the anhydrous and
  different-hydrate synonyms that should not be labels for the `CHEBI:53503`
  tombstone, and remove the residual `ingredient_type` and `nutritional_roles`.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
