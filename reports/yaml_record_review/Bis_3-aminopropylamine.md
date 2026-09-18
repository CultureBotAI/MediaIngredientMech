# `data/ingredients/mapped/Bis_3-aminopropylamine.yaml`

## Verdict

Pass. The exact `CHEBI:16841` bis(3-aminopropyl)amine identity, CAS, ChEBI
synonym, structure fields, SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bis_3-aminopropylamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16841` with
  `ontology_mapping.ontology_id: CHEBI:16841`,
  `ontology_label: bis(3-aminopropyl)amine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS search returns `CHEBI:16841` for the exact preferred label, with CAS
  `56-18-8`, formula `C6H17N3`, the stored InChI/SMILES, and the stored
  `3,3'-azanediyldi(propanamine)` synonym.
- PubChem resolves CAS `56-18-8` to CID 5942 with formula `C6H17N3` and the
  same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bis_3-aminopropylamine.yaml data/ingredients/mapped/Bisabolene.yaml data/ingredients/mapped/Bismuth_Iii_Chloride.yaml data/ingredients/mapped/Blasticidin_A.yaml data/ingredients/mapped/Blasticidin_S.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bis_3-aminopropylamine.yaml data/ingredients/mapped/Bisabolene.yaml data/ingredients/mapped/Blasticidin_A.yaml data/ingredients/mapped/Blasticidin_S.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 606, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bis_3-aminopropylamine` to `CHEBI:16841` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, ChEBI synonym, single-ingredient
  classification, formula, InChI, SMILES, SSSOM row, and aggregate copy are
  populated.

## Recommended Edits

- None.
