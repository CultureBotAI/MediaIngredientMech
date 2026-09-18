# `data/ingredients/mapped/Fucose.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The exact generic fucose
identity, corrected CAS RN, ChEBI synonyms, and final SSSOM payload pass, but
`CARBON_SOURCE` is still only a provisional ChEBI-ancestry prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Fucose.yaml`.
- Identifier and grounding: `identifier: CHEBI:33984` with matching
  `ontology_mapping.ontology_id`, canonical label `fucose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The CAS RN `7724-73-4` is the dbxref on `CHEBI:33984`; the 2026-08-06
  correction replaced an EC/EINECS registry number that had previously been
  misfiled in the CAS slot.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fructose-asparagine.yaml data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-primary records in the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28757 CHEBI:5181 CHEBI:33984 CHEBI:29806`:
  returned the active ChEBI label, synonyms, xrefs, and definition for
  `CHEBI:33984`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, exact mapping, corrected CAS RN, ingredient type, synonyms,
  occurrence counts, and provisional carbon-source role as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fucose` to
  `CHEBI:33984` with `skos:exactMatch`, exports the valid exact synonyms
  `6-Deoxygalactose` and `Fuc`, and exports the corrected `CAS:7724-73-4`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from the ChEBI carbohydrate closure and
  the evidence note explicitly says the role is provisional.
- The hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, row-review provenance, the expected registry triage row, and the
  distinct exact `L-fucose` record.

## Completeness

- The exact fucose identity, single-ingredient type, corrected CAS RN,
  occurrence counts, and final SSSOM identity row are populated.
- No component, environment, unsafe final synonym, or missing structure gap
  remains for the current ChEBI identity.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Fucose.yaml` with inspected source-backed evidence
  for fucose in media, or remove the unsupported role; then sync
  `data/curated/mapped_ingredients.yaml` and rerun strict validation.
