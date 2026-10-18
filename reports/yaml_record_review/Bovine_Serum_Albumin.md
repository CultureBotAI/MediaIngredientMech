# `data/ingredients/mapped/Bovine_Serum_Albumin.yaml`

## Verdict

Pass. The CAS primary identity, `NCIT:C85253` parent mapping, required registry
identity rows, occurrence count, SSSOM rows, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bovine_Serum_Albumin.yaml`.
- Identifier and grounding: `identifier: cas:9048-46-8` with
  `ontology_mapping.ontology_id: NCIT:C85253`,
  `ontology_label: Bovine Serum Albumin`, `ontology_source: NCIT`,
  `mapping_quality: NARROW_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Bovine Serum Albumin` still resolves
  `NCIT:C85253`. PubChem finds no CID for CAS `9048-46-8`, preserving the
  need for a CAS registry identity alongside the NCIT parent.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bottromycin.yaml data/ingredients/mapped/Bovine_Albumin.yaml data/ingredients/mapped/Bovine_Calf_Serum.yaml data/ingredients/mapped/Bovine_Serum_Albumin.yaml data/ingredients/mapped/Brain_Heart_Infusion.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bottromycin.yaml data/ingredients/mapped/Bovine_Serum_Albumin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the MESH/NCIT-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the prefix-specific NCIT resolution, the
  expected-CAS and kgmicrobe registry dispositions, the `skos:narrowMatch`
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 624, the CAS and
  kgmicrobe identity rows at rows 625-626, seven
  `mappings/culturemech_recipe_membership.tsv` rows for `cas:9048-46-8`, and
  the aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM narrow-match and registry rows follow Rule B1 for a local
  CAS primary ID with an external parent ontology term.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The CAS identifier, NCIT parent, CAS chemical-property value, 7/7 occurrence
  count, narrow-match SSSOM row, registry identity rows, and aggregate copy are
  populated.

## Recommended Edits

- None.
