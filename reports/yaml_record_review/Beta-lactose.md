# `data/ingredients/mapped/Beta-lactose.yaml`

## Verdict

Pass. The exact `CHEBI:36218` beta-lactose identity, CAS-RN lookup, synonyms,
structure fields, occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Beta-lactose.yaml`.
- Identifier and grounding: `identifier: CHEBI:36218` with
  `ontology_mapping.ontology_id: CHEBI:36218`,
  `ontology_label: beta-lactose`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- PubChem resolves CAS `5965-66-2` to beta-lactose formula `C12H22O11` and the
  same standard InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 581, the legacy
  `MIM:Beta_Lactose` alias in `mappings/mim_curie_aliases.tsv`, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirmed the
  `CHEBI:36218` row in the OAK/OLS review.
- `mappings/culturemech_recipe_membership.tsv` contains one row for
  `CHEBI:36218`, matching the record's refreshed 1/1 medium and total
  occurrence counts.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact CHEBI identifier, CAS RN, single-ingredient classification,
  formula, InChI, SMILES, SSSOM row, occurrence statistics, and aggregate copy
  are populated.
- The carbon- and energy-source roles are explicitly marked as computational
  provisional in their claim-level evidence; the record does not overstate them
  as experimentally reviewed roles.

## Recommended Edits

- None.
