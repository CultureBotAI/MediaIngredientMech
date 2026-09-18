# `data/ingredients/mapped/Farm_soil.yaml`

## Verdict

Pass with minor issues. The CultureMech residual was grounded to the exact ENVO
farm soil term and publishes a clean final SSSOM row, but this newer record is
missing the expected `ingredient_type` backfill.

## Identity

- Reviewed record: `data/ingredients/mapped/Farm_soil.yaml`.
- Identifier and grounding: `identifier: ENVO:00005749` with matching
  `ontology_mapping.ontology_id`, canonical label `farm soil`, source `ENVO`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and `mapping_status:
  MAPPED`.
- The record's structured evidence points to
  `culturemech:output/ingredient_occurrences.tsv`, and the creation history
  records one CultureMech occurrence grounded to `ENVO:00005749` on an exact
  canonical-label match.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Exopolysaccharide.yaml data/ingredients/mapped/FCCP.yaml data/ingredients/mapped/FSL.yaml data/ingredients/mapped/Fad.yaml data/ingredients/mapped/Farm_soil.yaml --out /tmp/mim_f_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because `ENVO` is
  outside the CHEBI-focused term-validation subset used for the mixed batch.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ENVO identifier, CultureMech residual provenance, occurrence count, and
  restored `ontology_mapping.evidence` block as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Farm_soil` to `ENVO:00005749` with `skos:exactMatch`, object label
  `farm soil`, and an empty `other` column.
- `mappings/culturemech_residual_groundings.tsv` records that this was a new
  MIM record for the one CultureMech residual, and
  `mappings/culturemech_residual_triage.tsv` records the same label as an
  alias of `ENVO:00005749` in the pinned index.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Farm_soil`,
  `ENVO:00005749`, and `farm soil` found the active YAML, aggregate copy,
  final SSSOM row, CultureMech residual provenance, and ignored aggregate
  backups; it did not expose a contradictory active mapping.

## Completeness

- The exact soil identity, source occurrence, mapping evidence, and final SSSOM
  row are populated.
- Minor: unlike existing soil and environmental-material records such as
  `Soil`, `Garden_Soil`, and `Sea_Water`, this newer CultureMech residual
  record lacks `ingredient_type: UNDEFINED_MIXTURE`.

## Recommended Edits

- Minor: set `ingredient_type: UNDEFINED_MIXTURE` on
  `data/ingredients/mapped/Farm_soil.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation.
