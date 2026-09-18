# `data/ingredients/mapped/Formic_Acid.yaml`

## Verdict

Needs curation, with major unsupported-role assertions. The exact formic acid
identity, CAS-backed structure fields, ChEBI synonyms, and final SSSOM payload
pass, but both nutritional roles are still provisional computational
predictions.

## Identity

- Reviewed record: `data/ingredients/mapped/Formic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30751` with matching
  `ontology_mapping.ontology_id`, canonical label `formic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `64-18-6` resolved to CID 284 titled `Formic Acid`
  with formula `CH2O2` and the same InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Formatetrimethylamine.yaml data/ingredients/mapped/Formic_Acid.yaml data/ingredients/mapped/Fortimicin_B.yaml data/ingredients/mapped/Fosfomycin.yaml data/ingredients/mapped/Fosmidomycin_Sodium_Salt_Hydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Formic_Acid.yaml data/ingredients/mapped/Fortimicin_B.yaml data/ingredients/mapped/Fosfomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, exact mapping, structure fields, CAS RN, ingredient type,
  synonyms, occurrence counts, and computational nutritional roles as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Formic_Acid` to `CHEBI:30751` with `skos:exactMatch`, exports ChEBI
  exact synonyms and `CAS:64-18-6`, and correctly omits the raw `(sodium salt)`
  token.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from the curated media-role name pattern
  and the evidence note explicitly says the role is provisional.
- Major: `nutritional_roles.ENERGY_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence added alongside the carbon-source
  prediction and likewise needs claim-level support.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` only records that
  the raw sodium-salt candidate text was already present in the YAML; the
  synonym policy filters that parenthetical form out of the final SSSOM row.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, CultureMech recipe memberships, row-review entries, and the
  distinct `Na-formate` sodium-salt record.

## Completeness

- The exact formic acid identity, single-ingredient type, PubChem structure, CAS
  RN, occurrence counts, and final SSSOM identity row are populated.
- No component, environment, unsafe final synonym, or missing structure gap
  remains for the current ChEBI identity.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` in
  `data/ingredients/mapped/Formic_Acid.yaml` with inspected source-backed
  evidence for formic acid in media, or remove the unsupported roles; then sync
  `data/curated/mapped_ingredients.yaml` and rerun strict validation.
