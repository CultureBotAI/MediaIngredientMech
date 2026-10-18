# `data/ingredients/mapped/Exopolysaccharide.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder metabolite-production label was
grounded to the exact active ChEBI exopolysaccharide term and publishes a clean
final SSSOM row, but this newer MicrobeDecoder record is missing the expected
`ingredient_type` backfill.

## Identity

- Reviewed record: `data/ingredients/mapped/Exopolysaccharide.yaml`.
- Identifier and grounding: `identifier: CHEBI:72813` with matching
  `ontology_mapping.ontology_id`, canonical label `exopolysaccharide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The source occurrence block records 8 MicrobeDecoder
  `BacDive_Metabolite_production` mentions.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Exopolysaccharide.yaml data/ingredients/mapped/FCCP.yaml data/ingredients/mapped/FSL.yaml data/ingredients/mapped/Fad.yaml data/ingredients/mapped/Farm_soil.yaml --out /tmp/mim_f_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Exopolysaccharide.yaml data/ingredients/mapped/FCCP.yaml data/ingredients/mapped/Fad.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the CHEBI subset in this mixed batch.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, MicrobeDecoder provenance, reviewed promotion history, and
  BacDive source-occurrence count as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Exopolysaccharide` to `CHEBI:72813` with `skos:exactMatch` and an empty
  `other` column.
- `mappings/microbedecoder_auto_mapped_review.tsv` records this label as
  approved and promoted after local OAK confirmed that `CHEBI:72813` resolves
  and its canonical label case-insensitively matches `exopolysaccharide`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Exopolysaccharide`,
  `CHEBI:72813`, and `Exopolysaccharide` found the active YAML, aggregate
  copy, final SSSOM row, MicrobeDecoder review provenance, and ignored
  aggregate backups; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, MicrobeDecoder source occurrence, review provenance, and
  final SSSOM row are populated.
- Minor: unlike older CHEBI-primary single-ingredient records such as
  `Cellulose`, `Dextran`, and `Lipopolysaccharide`, this newer MicrobeDecoder
  record lacks `ingredient_type: SINGLE_INGREDIENT`.

## Recommended Edits

- Minor: set `ingredient_type: SINGLE_INGREDIENT` on
  `data/ingredients/mapped/Exopolysaccharide.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation.
