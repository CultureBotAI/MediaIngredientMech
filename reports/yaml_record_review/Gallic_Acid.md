# `data/ingredients/mapped/Gallic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed gallic acid row maps to the exact active
ChEBI chemical, the stored CAS RN and structure agree with ChEBI, and the final
SSSOM row publishes only valid same-subject aliases.

## Identity

- Reviewed record: `data/ingredients/mapped/Gallic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30778` with matching
  `ontology_mapping.ontology_id`, canonical label `gallic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:30778` as active ChEBI term `gallic acid` with formula
  `C7H6O5`, InChI
  `InChI=1S/C7H6O5/c8-4-1-3(7(11)12)2-5(9)6(4)10/h1-2,8-10H,(H,11,12)`,
  SMILES `O=C(O)c1cc(O)c(O)c(O)c1`, CAS xref `149-91-7`, and exact synonym
  `3,4,5-Trihydroxybenzoic acid`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gallate_Formate.yaml data/ingredients/mapped/Gallic_Acid.yaml data/ingredients/mapped/Gallium_Iiichloride.yaml data/ingredients/mapped/Gambogic_Acid.yaml data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gallic_Acid.yaml data/ingredients/mapped/Gambogic_Acid.yaml data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CultureBotHT source, CAS RN, curated ChEBI synonym,
  structure fields, and ingredient type as the per-record YAML.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirmed the ChEBI
  row and marked it `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Gallic_Acid` to `CHEBI:30778` with `skos:exactMatch` and exports
  `3,4,5-Trihydroxybenzoic acid|CAS:149-91-7` in `other`; both tokens are
  valid for the subject.
- The record has no inferred nutritional, physicochemical, component,
  source-occurrence, or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, row-review confirmation, generated indexes, and ignored aggregate
  backups.

## Completeness

- The exact gallic acid identity, single-ingredient type, structure fields, CAS
  RN, CultureBotHT provenance, curated synonym, and final SSSOM row are
  populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
