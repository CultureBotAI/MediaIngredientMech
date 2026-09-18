# `data/ingredients/mapped/Bromosuccinate.yaml`

## Verdict

Pass. The exact `CHEBI:73706` bromosuccinate identity, dianion structure
fields, MicrobeDecoder provenance, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bromosuccinate.yaml`.
- Identifier and grounding: `identifier: CHEBI:73706` with
  `ontology_mapping.ontology_id: CHEBI:73706`,
  `ontology_label: bromosuccinate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS search for `Bromosuccinate` returns `CHEBI:73706`; that term denotes
  the dianion from deprotonated bromosuccinic acid and carries the same
  formula, InChI, SMILES, charge, and mass used in `chemical_properties`.
- PubChem resolves `Bromosuccinate` to CID 21650627 with the same standard
  InChI as the local ChEBI-backed structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bromosuccinate.yaml data/ingredients/mapped/Bromothymol_Blue.yaml data/ingredients/mapped/Brucella_Agar.yaml data/ingredients/mapped/Brucine.yaml data/ingredients/mapped/Butamine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bromosuccinate.yaml data/ingredients/mapped/Bromothymol_Blue.yaml data/ingredients/mapped/Brucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder candidate and unmapped-label
  provenance for `kgmicrobe.trait:bromosuccinate`, the authoritative exact
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 633, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bromosuccinate` to `CHEBI:73706` with
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
