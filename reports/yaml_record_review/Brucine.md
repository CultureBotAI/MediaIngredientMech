# `data/ingredients/mapped/Brucine.yaml`

## Verdict

Pass. The exact `CHEBI:3193` brucine identity, CAS, stereospecific structure
fields, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Brucine.yaml`.
- Identifier and grounding: `identifier: CHEBI:3193` with
  `ontology_mapping.ontology_id: CHEBI:3193`,
  `ontology_label: brucine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS search for `Brucine` returns `CHEBI:3193` as the exact base
  molecule and also shows salt or derivative siblings; the populated record is
  grounded to the base molecule, not to brucine sulfate or a charged derivative.
- PubChem resolves `Brucine` to CID 442021 with formula `C23H26N2O4` and the
  same standard InChI stored in `chemical_properties`.

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
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 636, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Brucine` to `CHEBI:3193` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`; its `other` field contains `CAS:357-57-3`, the same CAS
  stored in `chemical_properties`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, single-ingredient classification, formula,
  InChI, SMILES, SSSOM row, and aggregate copy are populated.
- `occurrence_statistics.total_occurrences: 0` and `media_count: 0` are
  consistent with a CultureBotHT compound import that has no CultureMech recipe
  memberships.
- No roles, components, or environmental contexts are required for this
  single-compound record.

## Recommended Edits

- None.
