# `data/ingredients/mapped/Folinic_Acid.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The folinic acid identity
is mapped to the exact ChEBI synonym target, the calcium-salt raw label is
filtered out of final SSSOM, and the CAS-backed structure fields agree with
PubChem, but `VITAMIN_SOURCE` is still only a provisional computational
prediction from ChEBI ancestry.

## Identity

- Reviewed record: `data/ingredients/mapped/Folinic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:15640` with matching
  `ontology_mapping.ontology_id`, canonical label `5-formyltetrahydrofolic
  acid`, source `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `58-05-9` resolved to CID 135403648 titled
  `Leucovorin` with formula `C20H23N7O7` and the same InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Folic_Acid.yaml data/ingredients/mapped/Folinic_Acid.yaml data/ingredients/mapped/Formaldehyde.yaml data/ingredients/mapped/Formamicin.yaml data/ingredients/mapped/Formamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Folic_Acid.yaml data/ingredients/mapped/Folinic_Acid.yaml data/ingredients/mapped/Formaldehyde.yaml data/ingredients/mapped/Formamicin.yaml data/ingredients/mapped/Formamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed with no diagnostics for the 5-file batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, synonym-grade exact mapping, structure fields, CAS RN,
  ingredient type, raw calcium-salt synonym, and provisional nutritional role as
  the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Folinic_Acid` to `CHEBI:15640` with `skos:exactMatch`, exports only the
  ChEBI exact synonym and `CAS:58-05-9` in `other`, and correctly omits the raw
  `(calcium salt)` token.
- Major: `nutritional_roles.VITAMIN_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from the ChEBI vitamin-role closure and
  the evidence note explicitly says the role is provisional.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` only records that
  the raw calcium-salt candidate text was already present in the YAML; the
  synonym policy filters that parenthetical form out of the final SSSOM row.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports, found
  the active YAML, aggregate copy, final SSSOM row, row-review entries, and
  ignored historical aggregate backups.

## Completeness

- The exact folinic acid identity, single-ingredient type, PubChem structure,
  CAS RN, occurrence counts, and final SSSOM identity row are populated.
- No component, environment, unsafe final synonym, or missing structure gap
  remains for the current ChEBI identity.

## Recommended Edits

- Major: either replace the provisional
  `nutritional_roles.VITAMIN_SOURCE` inference in
  `data/ingredients/mapped/Folinic_Acid.yaml` with source-backed evidence for
  folinic acid as a vitamin source in media, or remove the role; then sync
  `data/curated/mapped_ingredients.yaml` and rerun strict validation.
