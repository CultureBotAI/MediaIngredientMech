# `data/ingredients/mapped/Glutathione_Oxidized.yaml`

## Verdict

Needs curation. The kgm-metatraits exact match to active `CHEBI:17858`
glutathione disulfide and the structure fields pass, but the final SSSOM row
exports `reduction: glutathione oxidized` as an `other` synonym even though it
is process text, not a same-subject label.

## Identity

- Reviewed record: `data/ingredients/mapped/Glutathione_Oxidized.yaml`.
- Identifier and grounding: `identifier: CHEBI:17858` with matching
  `ontology_mapping.ontology_id`, canonical label `glutathione disulfide`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C20H32N6O12S2`, ChEBI-derived InChI, and
  ChEBI-derived SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glutaric_Acid.yaml data/ingredients/mapped/Glutathione.yaml data/ingredients/mapped/Glutathione_Oxidized.yaml data/ingredients/mapped/Gly-DL-Asp.yaml data/ingredients/mapped/Gly-Gln_Monohydrate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glutaric_Acid.yaml data/ingredients/mapped/Glutathione.yaml data/ingredients/mapped/Glutathione_Oxidized.yaml data/ingredients/mapped/Gly-DL-Asp.yaml data/ingredients/mapped/Gly-Gln_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, exact IUPAC synonym, raw process string, formula,
  InChI, SMILES, and singleton type as the per-record YAML.
- OLS4 resolves `CHEBI:17858` as `glutathione disulfide`, matching the YAML
  `ontology_mapping`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glutathione_Oxidized` to `CHEBI:17858` by `skos:exactMatch`.
- Major: the final SSSOM `other` payload includes
  `reduction: glutathione oxidized`. That string is process-qualified source
  text restored by `claude_sssom_surface_form_backfill`, not a synonym for
  glutathione disulfide.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, the synonym-enrichment row that found the real surface already
  represented, generated indexes, old batch validation reports, and ignored
  aggregate backups.

## Completeness

- The exact ChEBI identity, formula, InChI, SMILES, kgm-metatraits source, and
  final SSSOM row are populated.
- The process-text synonym needs removal or a final-SSSOM filter.

## Recommended Edits

- Major: change the `reduction: glutathione oxidized` synonym in
  `data/ingredients/mapped/Glutathione_Oxidized.yaml` to provenance-only text
  or make `src/mediaingredientmech/synonym_policy.py` filter `reduction:`
  process strings before rebuilding final SSSOM.
