# `data/ingredients/mapped/Fradicin.yaml`

## Verdict

Pass. The kg-microbe placeholder has been upgraded to an exact MeSH fradicin
identity, external-prefix validation resolves the MeSH CURIE, and the final
SSSOM row publishes no unsafe synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fradicin.yaml`.
- Identifier and grounding: `identifier: mesh:C033989` with matching
  `ontology_mapping.ontology_id`, label `fradicin`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  `mesh:C033989` as `RESOLVED_EXACT_CURIE` with exact MeSH label `fradicin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fradicin.yaml data/ingredients/mapped/Framycetin.yaml data/ingredients/mapped/Fraxetin.yaml data/ingredients/mapped/Fructooligosaccharides_Fos.yaml data/ingredients/mapped/Fructose-6-phosphate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fradicin.yaml data/ingredients/mapped/Framycetin.yaml data/ingredients/mapped/Fraxetin.yaml data/ingredients/mapped/Fructose-6-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four OBO/external-prefix records in the batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  MeSH identifier, exact mapping, empty synonym list, 0/0 occurrence counts, and
  ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fradicin`
  to `mesh:C033989` with `skos:exactMatch` and an empty `other` column.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` explains that the
  earlier `UNKNOWN_TERM` review row came from missing prefix dispatch in the
  synonym-review validator, not from a broken MeSH CURIE.
- The record has no inferred nutritional, physicochemical, component, chemical
  structure, or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, external-prefix validation, unknown-term triage row, and generated
  batch findings for the same MeSH CURIE.

## Completeness

- The exact fradicin identifier, MeSH mapping, and final SSSOM row are
  populated.
- ChEBI/PubChem structure fields and CAS are correctly absent because this
  reviewed record is grounded through MeSH.

## Recommended Edits

- None.
