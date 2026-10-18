# `data/ingredients/mapped/Boldine.yaml`

## Verdict

Pass. The exact `CHEBI:3148` Boldine identity, CAS, structure fields, SSSOM
row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Boldine.yaml`.
- Identifier and grounding: `identifier: CHEBI:3148` with
  `ontology_mapping.ontology_id: CHEBI:3148`,
  `ontology_label: Boldine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS search returns `CHEBI:3148` for the exact label, with CAS
  `476-70-0`, formula `C19H21NO4`, and the same standard InChI and SMILES
  stored in `chemical_properties`.
- PubChem resolves CAS `476-70-0` to CID 10154 with formula `C19H21NO4` and
  the same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Boldine.yaml data/ingredients/mapped/Borate.yaml data/ingredients/mapped/Borneol.yaml data/ingredients/mapped/Boron_Stock.yaml data/ingredients/mapped/Borrelidin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Boldine.yaml data/ingredients/mapped/Borate.yaml data/ingredients/mapped/Borneol.yaml data/ingredients/mapped/Borrelidin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 616, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Boldine` to `CHEBI:3148` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, single-ingredient classification, formula,
  InChI, SMILES, SSSOM row, and aggregate copy are populated.

## Recommended Edits

- None.
