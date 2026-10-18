# `data/ingredients/mapped/Bromothymol_Blue.yaml`

## Verdict

Pass. The exact `CHEBI:86155` bromothymol blue identity, CAS, synonyms,
pH-indicator role, occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bromothymol_Blue.yaml`.
- Identifier and grounding: `identifier: CHEBI:86155` with
  `ontology_mapping.ontology_id: CHEBI:86155`,
  `ontology_label: bromothymol blue`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Bromothymol blue` returns the single ChEBI hit
  `CHEBI:86155`; the term is active and its ChEBI CAS xref, formula, InChI,
  and SMILES match the populated local claims.
- PubChem resolves `Bromothymol blue` to CID 6450 with formula
  `C27H28Br2O5S` and the same standard InChI stored in
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bromosuccinate.yaml data/ingredients/mapped/Bromothymol_Blue.yaml data/ingredients/mapped/Brucella_Agar.yaml data/ingredients/mapped/Brucine.yaml data/ingredients/mapped/Butamine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bromosuccinate.yaml data/ingredients/mapped/Bromothymol_Blue.yaml data/ingredients/mapped/Brucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 634, all 174
  current `mappings/culturemech_recipe_membership.tsv` rows for
  `CHEBI:86155`, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bromothymol_Blue` to `CHEBI:86155` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`; its `other` field contains the four ChEBI-backed
  synonyms plus `CAS:76-59-5`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, imported CultureMech role surface, ChEBI
  synonyms, single-ingredient classification, formula, InChI, SMILES, 174/174
  occurrence count, SSSOM row, and aggregate copy are populated.
- No components or environmental contexts are required for this
  single-compound indicator.

## Recommended Edits

- None.
