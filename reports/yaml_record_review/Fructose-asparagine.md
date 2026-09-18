# `data/ingredients/mapped/Fructose-asparagine.yaml`

## Verdict

Needs curation, with major unsupported-role assertions. The CAS fallback
identity and PubChem structure fields still resolve through the recorded CID,
but both nutritional roles are only provisional name-pattern predictions.

## Identity

- Reviewed record: `data/ingredients/mapped/Fructose-asparagine.yaml`.
- Identifier and grounding: `identifier: cas:34393-27-6` with matching
  `ontology_mapping.ontology_id`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct PubChem lookup by the stored CID `71316980` resolved to a
  `Fructose-asparagine` record with formula `C10H18N2O8` and the same InChI
  recorded under `chemical_properties`.
- PubChem lookup by CAS RN `34393-27-6` did not return a CID, so the CAS alias
  should be rechecked against the original CultureBotHT source or another
  registry source when this record is next curated.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fructose-asparagine.yaml data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fructose.yaml data/ingredients/mapped/Fucoidan.yaml data/ingredients/mapped/Fucose.yaml data/ingredients/mapped/Fumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  CAS fallback identifier, PubChem CID, structure fields, ingredient type, and
  provisional nutritional roles as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fructose-asparagine` to `cas:34393-27-6` with `skos:exactMatch` and
  exports only `CAS:34393-27-6` in `other`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` correctly triages the
  CAS identity row as an expected registry identifier rather than a missing OBO
  term.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from the curated media-role name pattern
  and the evidence note explicitly says the role is provisional.
- Major: `nutritional_roles.ENERGY_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence added alongside the carbon-source
  prediction and likewise needs claim-level support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, unknown-term triage row, and the current name-list guard that
  excludes conjugates such as `Fructose-asparagine`.

## Completeness

- The exact local CAS fallback identity, PubChem CID, structure fields,
  ingredient type, and final CAS SSSOM identity row are populated.
- CAS `34393-27-6` should be reverified from a registry source because current
  PubChem lookup by the CAS RN itself did not resolve.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` in
  `data/ingredients/mapped/Fructose-asparagine.yaml` with inspected
  source-backed evidence, or remove the unsupported roles; then sync
  `data/curated/mapped_ingredients.yaml`.
- Minor: verify the CAS RN against the original CultureBotHT input or another
  registry source, because CID `71316980` resolves to fructose-asparagine but
  PubChem no longer resolves that CID from the stored CAS text.
