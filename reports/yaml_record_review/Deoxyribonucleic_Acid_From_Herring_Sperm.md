# `data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml`

## Verdict

Pass with minor issues. This record is intentionally a rejected duplicate
tombstone after being merged into the live `Fish-sperm_Dna` record; the
herring-sperm raw label is preserved on the survivor and no final SSSOM row is
exported for the tombstone, but stale pre-merge ontology fields remain in the
rejected YAML and generated docs still surface it in mapped-record tables.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml`.
- Current tombstone identity: `identifier: kgmicrobe.ingredient:fish-sperm_dna`
  and `mapping_status: REJECTED`.
- Merge history says this record was merged into `Fish-Sperm DNA`, had its
  occurrences transferred, was tombstoned with SSSOM rows dropped, and then
  had its identifier repointed from `CHEBI:16991` to
  `kgmicrobe.ingredient:fish-sperm_dna` so downstream label lookup reaches the
  surviving local identity.
- The live survivor is `data/ingredients/mapped/Fish-sperm_Dna.yaml`, also
  `identifier: kgmicrobe.ingredient:fish-sperm_dna`, with the herring-sperm
  label preserved as a `RAW_TEXT` synonym.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Delta-Undecalactone.yaml data/ingredients/mapped/Deoxycholic_Acid.yaml data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml data/ingredients/mapped/Dermcidin.yaml data/ingredients/mapped/Desferrioxamine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Delta-Undecalactone.yaml data/ingredients/mapped/Deoxycholic_Acid.yaml data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml data/ingredients/mapped/Dermcidin.yaml data/ingredients/mapped/Desferrioxamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records, including the stale `CHEBI:16991` tombstone
  `ontology_mapping` label check.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found this rejected tombstone, the live `Fish-sperm_Dna.yaml` record, the
  live final SSSOM rows for `MIM:Fish-sperm_Dna`, the row-review records
  classifying both synonym-enrichment proposals as already represented, and
  the `mappings/other_cross_record_baseline.tsv` row for the preserved
  herring-sperm synonym.
- The final `mappings/ingredient_mappings.sssom.tsv` has no
  `MIM:Deoxyribonucleic_Acid_From_Herring_Sperm` row, matching the merge
  history that says this tombstone's SSSOM rows were dropped.
- The live `MIM:Fish-sperm_Dna` SSSOM narrow row exports
  `Deoxyribonucleic acid from herring sperm` in `other`; that is the raw label
  carried forward from this duplicate record, not a live synonym emitted by the
  rejected tombstone.
- `mappings/culturemech_recipe_membership.tsv` has seven
  `kgmicrobe.ingredient:fish-sperm_dna` rows that match the live survivor's 7/7
  occurrence statistics; this tombstone correctly has 0/0 after the merge.

## Completeness

- The tombstone is complete enough for duplicate lookup: it records the merge
  target, the repointed identifier, 0/0 occurrences, and no standalone final
  SSSOM row.
- Minor: `ontology_mapping` and `kg_microbe_node_id` still carry pre-merge
  `CHEBI:16991` values on this rejected record, and generated
  `docs/data/mapped_ingredients.*` tables still include the rejected
  mapped-directory tombstone.

## Recommended Edits

- Minor: if rejected tombstones are meant to retain only merge pointers and
  raw labels, prune the stale `ontology_mapping` and `kg_microbe_node_id`
  fields from `data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml`.
- Review or retire the stale
  `mappings/other_cross_record_baseline.tsv` `UNREVIEWED` row now that the
  herring-sperm synonym is intentionally represented on the live
  `Fish-sperm_Dna` record.
