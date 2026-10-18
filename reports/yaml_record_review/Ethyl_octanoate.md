# `data/ingredients/mapped/Ethyl_octanoate.yaml`

## Verdict

Pass with minor issues. The CultureMech residual was grounded to the exact
ChEBI ethyl octanoate term and publishes a clean SSSOM row, but this newer
record is missing the expected `ingredient_type` backfill.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethyl_octanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:87426` with matching
  `ontology_mapping.ontology_id`, canonical label `ethyl octanoate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and one
  CultureMech occurrence.
- The record's structured evidence points to
  `culturemech:output/ingredient_occurrences.tsv`, and the creation history
  records an exact canonical-label match to the query `ethyl octanoate`.
- PubChem lookup by name `ethyl octanoate` resolved to CID 7799 with formula
  `C10H20O2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethyl_Decanoate.yaml data/ingredients/mapped/Ethyl_Methyl_Sulfide.yaml data/ingredients/mapped/Ethyl_octanoate.yaml data/ingredients/mapped/Ethylene_Glycol.yaml data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml --out /tmp/mim_ethyl_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethyl_octanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CultureMech residual provenance, occurrence count, and
  restored `ontology_mapping.evidence` block as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethyl_octanoate` to `CHEBI:87426` with `skos:exactMatch`, the canonical
  ChEBI object label, and an empty `other` column.
- `mappings/culturemech_residual_groundings.tsv` records that this was a new
  MIM record for the one CultureMech residual, and
  `mappings/culturemech_residual_triage.tsv` records the same label as an
  alias of `CHEBI:87426` in the pinned index.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Ethyl_octanoate`,
  `Ethyl octanoate`, and `CHEBI:87426` found the active YAML, aggregate copy,
  final SSSOM row, and expected CultureMech residual provenance; it did not
  expose a contradictory active mapping.

## Completeness

- The exact identity, source occurrence, mapping evidence, and final SSSOM row
  are populated.
- Minor: unlike the older CHEBI-primary single-ingredient records, this newer
  CultureMech residual record lacks `ingredient_type: SINGLE_INGREDIENT`.

## Recommended Edits

- Minor: set `ingredient_type: SINGLE_INGREDIENT` on
  `data/ingredients/mapped/Ethyl_octanoate.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation.
