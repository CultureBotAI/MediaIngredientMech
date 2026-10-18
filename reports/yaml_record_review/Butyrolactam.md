# `data/ingredients/mapped/Butyrolactam.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:36592` pyrrolidin-2-one identity, butyrolactam
synonym match, CAS, structure fields, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Butyrolactam.yaml`.
- Identifier and grounding: `identifier: CHEBI:36592` with
  `ontology_mapping.ontology_id: CHEBI:36592`,
  `ontology_label: pyrrolidin-2-one`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Butyrolactam` returns `CHEBI:36592`; ChEBI holds
  `Butyrolactam` as a synonym for primary label `pyrrolidin-2-one` and carries
  the same CAS, formula, InChI, and SMILES as the local record.
- PubChem resolves CAS `616-45-5` to CID 12025 with formula `C4H7NO` and the
  same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Butyrate.yaml data/ingredients/mapped/Butyric_Acid.yaml data/ingredients/mapped/Butyricin_7423.yaml data/ingredients/mapped/Butyrolactam.yaml data/ingredients/mapped/CCCP.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Butyrate.yaml data/ingredients/mapped/Butyric_Acid.yaml data/ingredients/mapped/Butyricin_7423.yaml data/ingredients/mapped/Butyrolactam.yaml data/ingredients/mapped/CCCP.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 645, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Butyrolactam` to `CHEBI:36592` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`; its `other` field contains `CAS:616-45-5`, the same CAS
  stored in `chemical_properties`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, CAS-lookup provenance, single-ingredient
  classification, formula, InChI, SMILES, SSSOM row, and aggregate copy are
  populated.
- `occurrence_statistics.total_occurrences: 0` and `media_count: 0` are
  consistent with a CultureBotHT compound import that has no CultureMech recipe
  memberships.
- No roles, components, or environmental contexts are required for this
  single-compound record.

## Recommended Edits

- None.
