# `data/ingredients/mapped/Geraniol.yaml`

## Verdict

Pass. The exact `CHEBI:17447` geraniol identity, CAS RN, structure fields,
curated IUPAC synonym, and final SSSOM row are all consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Geraniol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17447` with matching
  `ontology_mapping.ontology_id`, canonical label `geraniol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:17447` as active geraniol with CAS xref `106-24-1`,
  formula `C10H18O`, the curated `(2E)-3,7-dimethylocta-2,6-dien-1-ol`
  synonym, and InChI/SMILES matching the YAML.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gentisic_Acid.yaml data/ingredients/mapped/Geomycin.yaml data/ingredients/mapped/Gepotidacin.yaml data/ingredients/mapped/Geraniol.yaml data/ingredients/mapped/Ginger.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gentisic_Acid.yaml data/ingredients/mapped/Gepotidacin.yaml data/ingredients/mapped/Geraniol.yaml data/ingredients/mapped/Ginger.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI/NCIT-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact mapping, CAS RN, structure fields, single-ingredient
  type, and IUPAC synonym as the per-record YAML.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the current
  `Geraniol` to `CHEBI:17447` row as `CONFIRMED_NO_ACTION`.
- The final SSSOM row maps `MIM:Geraniol` to `CHEBI:17447` by
  `skos:exactMatch` and exports only the OLS4 IUPAC synonym plus
  `CAS:106-24-1` in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM and row-review rows, generated indexes, old batch validation reports,
  and ignored aggregate backups.

## Completeness

- The exact geraniol identity, CAS RN, structure fields, curated synonym,
  ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
