# `data/ingredients/mapped/Bromophenol_blue.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:59424` bromophenol blue identity,
restored CultureMech residual evidence, KOH-solution alias, SSSOM row, and
aggregate copy agree, but the occurrence statistics were not refreshed after a
second CultureMech raw label was folded into the record.

## Identity

- Reviewed record: `data/ingredients/mapped/Bromophenol_blue.yaml`.
- Identifier and grounding: `identifier: CHEBI:59424` with
  `ontology_mapping.ontology_id: CHEBI:59424`,
  `ontology_label: bromophenol blue`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Bromophenol blue` returns the single ChEBI hit
  `CHEBI:59424`, whose formula, InChI, and SMILES match the current compound.
- PubChem resolves `Bromophenol blue` to CID 8272 with formula `C19H10Br4O5S`
  and the same standard InChI as ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Brain_Heart_Infusion_Broth.yaml data/ingredients/mapped/Brainheart_infusion_agar.yaml data/ingredients/mapped/Brazilein.yaml data/ingredients/mapped/Bromocresol_Purple.yaml data/ingredients/mapped/Bromophenol_blue.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Brazilein.yaml data/ingredients/mapped/Bromocresol_Purple.yaml data/ingredients/mapped/Bromophenol_blue.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found two CultureMech residual grounding rows for
  `CHEBI:59424`, the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 632, the KOH-solution label in
  the SSSOM `other` field, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bromophenol_blue` to `CHEBI:59424` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- Hidden/ignored-inclusive search found no `CHEBI:59424` row in
  `mappings/culturemech_recipe_membership.tsv`, so the exact refreshed count
  should come from the maintained CultureMech occurrence table.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, restored CultureMech evidence, KOH-solution raw
  label, SSSOM row, and aggregate copy are populated.
- Minor gap: `occurrence_statistics` still says 1/1 even though
  `Bromophenol blue` and `Bromophenol blue (0.5% in 0.2N KOH)` were each
  recorded as one CultureMech residual mention.

## Recommended Edits

- Minor: refresh `data/ingredients/mapped/Bromophenol_blue.yaml` occurrence
  statistics from the maintained CultureMech occurrence table and add a
  `supplied_form` or note for the 0.5% bromophenol blue in 0.2 N KOH source
  surface if that concentration/solvent should remain attached to the compound
  record; then run `just sync-curated` and focused strict/term validation.
