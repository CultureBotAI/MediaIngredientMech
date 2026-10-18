# `data/ingredients/mapped/Galactose.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The exact galactose
identity, CultureMech carbon-source role, corrected CAS xref, curated
synonyms, and final SSSOM payload pass, but `ENERGY_SOURCE` is still only a
provisional computational prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Galactose.yaml`.
- Identifier and grounding: `identifier: CHEBI:28260` with matching
  `ontology_mapping.ontology_id`, canonical label `galactose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:28260` as active ChEBI term `galactose` with formula
  `C6H12O6`, CAS xref `26566-61-0`, and same-subject synonyms `Gal`,
  `Galaktose`, and `galacto-hexose`.
- PubChem lookup by CAS RN `26566-61-0` resolved to CID 3037556 with formula
  `C6H12O6`, matching the ChEBI xref retained by the #114 CAS audit.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Galactomannan_From_Guar.yaml data/ingredients/mapped/Galactonate.yaml data/ingredients/mapped/Galactose.yaml data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml data/ingredients/mapped/Galacturonate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Galactonate.yaml data/ingredients/mapped/Galactose.yaml data/ingredients/mapped/Galacturonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CultureMech source, 14 CultureMech occurrences, corrected
  CAS RN, kg-microbe synonyms, nutritional-role facets, and ingredient type as
  the per-record YAML.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirmed the ChEBI
  row and marked it `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Galactose` to `CHEBI:28260` with `skos:exactMatch` and exports only
  `Gal`, `Galaktose`, `galacto-hexose`, and `CAS:26566-61-0` in `other`.
- The `CARBON_SOURCE` facet is source-backed by a `DATABASE_ENTRY` with original
  CultureMech role text.
- Major: `nutritional_roles.ENERGY_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_energy_source` with a provisional
  curator note; no inspected source in the record supports the role.
- The raw CultureMech `Role: ... Properties: ...` synonym text is retained in
  YAML but is correctly filtered out of the final SSSOM `other` column.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, row-review confirmation, generated indexes, and ignored aggregate
  backups.

## Completeness

- The exact galactose identity, CAS RN, CultureMech occurrence count,
  source-backed carbon role, kg-microbe synonyms, and final SSSOM row are
  populated.
- The energy-source role still needs source-backed evidence or removal.

## Recommended Edits

- Major: replace the provisional `ENERGY_SOURCE` facet in
  `data/ingredients/mapped/Galactose.yaml` with source-backed evidence or
  remove it; sync `data/curated/mapped_ingredients.yaml` and rerun strict
  validation.
