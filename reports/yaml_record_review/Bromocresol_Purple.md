# `data/ingredients/mapped/Bromocresol_Purple.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:86154` bromocresol purple identity,
CAS, pH-indicator role, structure fields, occurrence count, SSSOM row, and
aggregate copy agree, but one kg-microbe synonym still has a stray trailing
quote.

## Identity

- Reviewed record: `data/ingredients/mapped/Bromocresol_Purple.yaml`.
- Identifier and grounding: `identifier: CHEBI:86154` with
  `ontology_mapping.ontology_id: CHEBI:86154`,
  `ontology_label: bromocresol purple`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Bromocresol purple` returns the single ChEBI hit
  `CHEBI:86154`, whose CAS, formula, InChI, SMILES, and pH-indicator
  description match the populated local claims.
- PubChem resolves CAS `115-40-2` to CID 8273 with formula `C21H16Br2O5S` and
  the same standard InChI stored in `chemical_properties`.

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
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 631, nine
  `mappings/culturemech_recipe_membership.tsv` rows for `CHEBI:86154`, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bromocresol_Purple` to `CHEBI:86154` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, ChEBI/kg-microbe synonyms,
  single-ingredient classification, formula, InChI, SMILES, pH-indicator role,
  9/9 occurrence count, SSSOM row, and aggregate copy are populated.
- Minor gap: synonym `bromocresol purple"` is a malformed duplicate of the
  preferred label, and the same extra quote is published in the SSSOM
  `other` field.

## Recommended Edits

- Minor: remove the malformed `bromocresol purple"` synonym from
  `data/ingredients/mapped/Bromocresol_Purple.yaml`, regenerate the SSSOM row,
  then run `just sync-curated` and focused strict/term/SSSOM validation.
