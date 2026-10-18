# `data/ingredients/mapped/Borate.yaml`

## Verdict

Pass. The exact `CHEBI:22908` borate identity, restored CultureMech residual
evidence, occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Borate.yaml`.
- Identifier and grounding: `identifier: CHEBI:22908` with
  `ontology_mapping.ontology_id: CHEBI:22908`,
  `ontology_label: borate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Live OLS search for `Borate` returns `CHEBI:22908`, and the ChEBI term's
  stored formula, InChI, and SMILES describe the borate ion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Boldine.yaml data/ingredients/mapped/Borate.yaml data/ingredients/mapped/Borneol.yaml data/ingredients/mapped/Boron_Stock.yaml data/ingredients/mapped/Borrelidin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Boldine.yaml data/ingredients/mapped/Borate.yaml data/ingredients/mapped/Borneol.yaml data/ingredients/mapped/Borrelidin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the CultureMech residual triage and grounding rows,
  the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 617, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Borate` to `CHEBI:22908` with
  `skos:exactMatch` and carries the restored
  `MIM:culturemech:output/ingredient_occurrences.tsv` source token required by
  the structured `ontology_mapping.evidence` field.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CultureMech residual source evidence, occurrence
  count, SSSOM row, and aggregate copy are populated.

## Recommended Edits

- None.
