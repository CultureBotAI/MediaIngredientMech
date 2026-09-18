# `data/ingredients/mapped/Eugon_agar_BD-Difco.yaml`

## Verdict

Pass with minor issues. The CultureMech residual was grounded to the exact
MICRO Eugon agar medium term and publishes a clean final SSSOM row, but this
newer record is missing the expected `ingredient_type` backfill.

## Identity

- Reviewed record: `data/ingredients/mapped/Eugon_agar_BD-Difco.yaml`.
- Identifier and grounding: `identifier: MICRO:0001358` with matching
  `ontology_mapping.ontology_id`, canonical label `Eugon agar`, source
  `MICRO`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- The record's structured evidence points to
  `culturemech:output/ingredient_occurrences.tsv`, and the creation history
  records one CultureMech occurrence grounded to `MICRO:0001358` on an exact
  synonym match against `eugon agar`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Eugon_agar_BD-Difco.yaml data/ingredients/mapped/Euphol.yaml data/ingredients/mapped/Eurocidin.yaml data/ingredients/mapped/Europium_Iii_Chloride.yaml data/ingredients/mapped/Exfoliatin.yaml --out /tmp/mim_eug_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because `MICRO` is
  outside the CHEBI/OBO subset used for the mixed batch.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  MICRO identifier, CultureMech residual provenance, occurrence count, and
  restored `ontology_mapping.evidence` block as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Eugon_agar_BD-Difco` to `MICRO:0001358` with `skos:exactMatch`, object
  label `Eugon agar`, and an empty `other` column.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Eugon_agar_BD-Difco`,
  `Eugon agar`, and `MICRO:0001358` found the active YAML, aggregate copy,
  final SSSOM row, CultureMech residual provenance, and ignored aggregate
  backups; it did not expose a contradictory active mapping.

## Completeness

- The exact named-medium identity, source occurrence, mapping evidence, and
  final SSSOM row are populated.
- Minor: unlike older named media records, this newer CultureMech residual
  record lacks an `ingredient_type`. The appropriate value appears to be
  `NAMED_MEDIUM`.

## Recommended Edits

- Minor: set `ingredient_type: NAMED_MEDIUM` on
  `data/ingredients/mapped/Eugon_agar_BD-Difco.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation.
