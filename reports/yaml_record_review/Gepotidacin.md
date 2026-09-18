# `data/ingredients/mapped/Gepotidacin.yaml`

## Verdict

Pass. The high-accession exact `CHEBI:747127` gepotidacin identity resolves,
the CAS/PubChem structure fields match, and the final SSSOM row exports only
the expected CAS xref.

## Identity

- Reviewed record: `data/ingredients/mapped/Gepotidacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:747127` with matching
  `ontology_mapping.ontology_id`, canonical label `gepotidacin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:747127` as active gepotidacin with CAS xref
  `1075236-89-3`, formula `C24H28N6O3`, and InChI matching the PubChem-derived
  YAML value.

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
  the same ChEBI exact mapping, CAS RN, PubChem CID, structure fields, and
  single-ingredient type as the per-record YAML.
- OLS4 confirms that `CHEBI:747127` carries CAS `1075236-89-3`. The curation
  history records that the exact ChEBI primary superseded a narrower NCIT
  parent after the same CAS resolved uniquely through a ChEBI xref.
- The final SSSOM row maps `MIM:Gepotidacin` to `CHEBI:747127` by
  `skos:exactMatch` and exports only `CAS:1075236-89-3` in `other`.
- The row-review manifest records older NCIT, CAS, and local registry rows as
  either missing-prefix-validator or expected-registry rows; those are stale
  relative to the final exact ChEBI primary and do not indicate an active
  mapping problem.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM and row-review rows, the high-ChEBI accession ceiling tests, generated
  indexes, and ignored aggregate backups.

## Completeness

- The exact gepotidacin identity, CAS RN, PubChem structure fields, ingredient
  type, and final SSSOM row are populated.

## Recommended Edits

- None.
