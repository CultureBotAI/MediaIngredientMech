# `data/ingredients/mapped/Butan-1-amine.yaml`

## Verdict

Pass. The exact `CHEBI:43799` butan-1-amine identity, structure fields,
MicrobeDecoder provenance, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Butan-1-amine.yaml`.
- Identifier and grounding: `identifier: CHEBI:43799` with
  `ontology_mapping.ontology_id: CHEBI:43799`,
  `ontology_label: butan-1-amine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS search for `Butan-1-amine` returns `CHEBI:43799` as the exact
  neutral butylamine term and separates it from sibling derivatives such as
  `CHEBI:195458` butan-1-aminium.
- PubChem resolves `Butan-1-amine` to CID 8007 with formula `C4H11N` and the
  same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Butan-1-amine.yaml data/ingredients/mapped/Butane-14-diol.yaml data/ingredients/mapped/Butanol.yaml data/ingredients/mapped/Butyl_Stearate.yaml data/ingredients/mapped/Butyl_Vinyl_Ether.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Butan-1-amine.yaml data/ingredients/mapped/Butane-14-diol.yaml data/ingredients/mapped/Butanol.yaml data/ingredients/mapped/Butyl_Stearate.yaml data/ingredients/mapped/Butyl_Vinyl_Ether.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder candidate and unmapped-label
  provenance for `kgmicrobe.trait:butan_1_amine`, the authoritative exact SSSOM
  row at `mappings/ingredient_mappings.sssom.tsv` row 638, and the aggregate
  copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Butan-1-amine` to `CHEBI:43799` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, MicrobeDecoder occurrence, single-ingredient
  classification, formula, InChI, SMILES, molecular weight, SSSOM row, and
  aggregate copy are populated.
- `occurrence_statistics.total_occurrences: 0` and `media_count: 0` are
  consistent with a MicrobeDecoder-only import that has no CultureMech recipe
  memberships.
- No roles, components, or environmental contexts are required for this
  single-compound utilization label.

## Recommended Edits

- None.
