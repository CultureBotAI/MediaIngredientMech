# `data/ingredients/mapped/Bis-tris.yaml`

## Verdict

Pass. The exact `CHEBI:41250` Bis-Tris identity, CAS, ChEBI synonyms, buffer
role, structure fields, SSSOM row, occurrence count, and aggregate copy all
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bis-tris.yaml`.
- Identifier and grounding: `identifier: CHEBI:41250` with
  `ontology_mapping.ontology_id: CHEBI:41250`,
  `ontology_label: bis-tris`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Bis-Tris` returns a `CHEBI:41250` document for
  the exact bis-tris label; the same term has the stored canonical label, CAS
  `6976-37-0`, formula `C8H19NO5`, InChI, SMILES, and ChEBI synonyms.
- PubChem resolves CAS `6976-37-0` to CID 81462 with formula `C8H19NO5` and
  the same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py 'data/ingredients/mapped/Bis(2-ethylhexyl)phthalate.yaml' data/ingredients/mapped/Bis-4-nitrophenyl-phenyl_Phosphonate.yaml data/ingredients/mapped/Bis-4-nitrophenyl-phosphorylcholine.yaml data/ingredients/mapped/Bis-4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/Bis-tris.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data 'data/ingredients/mapped/Bis(2-ethylhexyl)phthalate.yaml' data/ingredients/mapped/Bis-4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/Bis-tris.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 605, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/culturemech_recipe_membership.tsv` contains 4 rows for
  `CHEBI:41250`, matching the record's refreshed 4/4 medium and total
  occurrence counts.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, ChEBI synonyms, single-ingredient
  classification, formula, InChI, SMILES, provisional buffer role, SSSOM row,
  occurrence statistics, and aggregate copy are populated.

## Recommended Edits

- None.
