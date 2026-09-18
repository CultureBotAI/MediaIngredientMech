# `data/ingredients/mapped/Gelatine.yaml`

## Verdict

Pass. The record intentionally maps the British spelling `Gelatine` to active
`CHEBI:5291` by synonym match, its CultureMech solidifying-agent role is
source-backed, and the final SSSOM row exports only the valid CAS xref in
`other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Gelatine.yaml`.
- Identifier and grounding: `identifier: CHEBI:5291` with matching
  `ontology_mapping.ontology_id`, canonical label `gelatin`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:5291` as active gelatin with the related synonym
  `Gelatine` and CAS xref `9000-70-8`. The term carries no structural formula,
  which is consistent with the YAML carrying only the CAS RN and no molecular
  formula, SMILES, or InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gamma-cyclodextrin.yaml data/ingredients/mapped/Garden_Soil.yaml data/ingredients/mapped/Gardimycin.yaml data/ingredients/mapped/Gelatine.yaml data/ingredients/mapped/Gelrite.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gamma-cyclodextrin.yaml data/ingredients/mapped/Gelatine.yaml data/ingredients/mapped/Gelrite.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI synonym match, 15 CultureMech occurrences, CAS RN, kg-microbe
  node id, single-ingredient type, and solidifying-agent role as the per-record
  YAML.
- The record was deliberately regraded from `EXACT_MATCH` to `SYNONYM_MATCH`
  in issue `#322` because the spelling is a synonym of the ChEBI label rather
  than a canonical-label exact match.
- `physicochemical_roles.SOLIDIFYING_AGENT` is supported by a
  `DATABASE_ENTRY` imported from the CultureMech pipeline with original role
  text `Solidifying Agent`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the current
  `Gelatine` to `CHEBI:5291` row as `CONFIRMED_NO_ACTION`.
- The final SSSOM row maps `MIM:Gelatine` to `CHEBI:5291` by
  `skos:exactMatch`, with object label `gelatin`, CAS `9000-70-8` in `other`,
  and an `OAK+OLS` confirmed review marker. The raw `Role:`/`Properties:`
  synonym is filtered from final SSSOM as expected.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM and row-review rows, generated indexes, old batch validation reports,
  and ignored aggregate backups.

## Completeness

- The gelatine identity, CAS xref, role evidence, occurrence count, and final
  SSSOM row are populated.

## Recommended Edits

- None.
