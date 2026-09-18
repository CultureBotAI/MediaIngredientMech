# `data/ingredients/mapped/Flavofungin.yaml`

## Verdict

Pass. The record was promoted from the local antibiotic placeholder to an exact
MeSH `flavofungin` term, and the narrower CHEBI `Flavofungin I/II/III`
component candidates did not reach the active final SSSOM row.

## Identity

- Reviewed record: `data/ingredients/mapped/Flavofungin.yaml`.
- Identifier and grounding: `identifier: mesh:C001897` with matching
  `ontology_mapping.ontology_id`, label `flavofungin`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- EBI OLS for MeSH resolves `mesh:C001897` as `flavofungin`.
- The original kg-microbe placeholder evidence listed CHEBI `Flavofungin I`,
  `Flavofungin II`, and `Flavofungin III` as candidates; the record instead
  uses the exact MeSH class for the unsuffixed label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Flavensomycin.yaml data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml data/ingredients/mapped/Flavofungin.yaml data/ingredients/mapped/Flavomycin.yaml data/ingredients/mapped/Flavone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Flavofungin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  MeSH identifier, empty synonyms, zero occurrence counts, and ingredient type
  as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Flavofungin` to `mesh:C001897` with `skos:exactMatch` and an empty
  `other` column.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `mesh:C001897` exactly through prefix-specific EBI OLS; the older
  `UNKNOWN_TERM` row in `mappings/ingredient_mappings_oak_ols_review.tsv` was
  a validator-prefix coverage gap, not a bad identifier.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, MeSH OLS validation row, row-review provenance,
  component-candidate provenance in the YAML, and ignored historical batch
  reports.

## Completeness

- The exact MeSH identity, empty final SSSOM synonym payload, and ingredient
  type are populated.
- The absence of CultureMech occurrences and roles is coherent for this
  kg-microbe placeholder-derived antibiotic record.
- I found no consequential missing component, environment, or synonym payload.

## Recommended Edits

- None.
