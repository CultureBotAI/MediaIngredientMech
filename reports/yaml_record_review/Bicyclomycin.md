# `data/ingredients/mapped/Bicyclomycin.yaml`

## Verdict

Pass. The exact `CHEBI:60584` bicozamycin identity, Bicyclomycin synonym, CAS
lookup provenance, structure fields, SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bicyclomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:60584` with
  `ontology_mapping.ontology_id: CHEBI:60584`,
  `ontology_label: bicozamycin`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- OLS confirms `Bicyclomycin` as a related synonym of `CHEBI:60584` and lists
  CAS `38129-37-2` as a cross-reference.
- PubChem resolves CAS `38129-37-2` to the same formula and standard InChI
  stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bicine.yaml data/ingredients/mapped/Bicine_Buffer.yaml data/ingredients/mapped/Bicyclomycin.yaml data/ingredients/mapped/Bile_Acid.yaml data/ingredients/mapped/Bile_Salts.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bicine.yaml data/ingredients/mapped/Bicine_Buffer.yaml data/ingredients/mapped/Bicyclomycin.yaml data/ingredients/mapped/Bile_Acid.yaml data/ingredients/mapped/Bile_Salts.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 592, the OAK/OLS confirmation row
  in `mappings/ingredient_mappings_row_review_manifest.tsv`, and the aggregate
  copy in `data/curated/mapped_ingredients.yaml`.
- The 2026-08-24 history entry correctly preserves `CAS_RN_LOOKUP`: the record
  was created by an explicit CAS-to-ChEBI lookup, and the current CAS remains a
  ChEBI xref on the current term.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact CHEBI identifier, CAS RN, single-ingredient classification,
  formula, InChI, SMILES, provisional selective-agent role, SSSOM row, zero
  occurrence count, and aggregate copy are populated.

## Recommended Edits

- None.
