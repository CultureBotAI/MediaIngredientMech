# `data/ingredients/mapped/Bile_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:3098` bile acid class identity, reviewed MicrobeDecoder
provenance, complex-class ingredient type, SSSOM row, and aggregate copy all
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bile_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:3098` with
  `ontology_mapping.ontology_id: CHEBI:3098`,
  `ontology_label: bile acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: UNDEFINED_MIXTURE`, and
  `mapping_status: MAPPED`.
- OLS confirms current `CHEBI:3098` `bile acid`, with `Bile acid` as a related
  synonym on that chemical class.

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
  `mappings/ingredient_mappings.sssom.tsv` row 593, the approved
  `mappings/microbedecoder_auto_mapped_review.tsv` row, and the aggregate copy
  in `data/curated/mapped_ingredients.yaml`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI class identifier, undefined-mixture classification, zero
  medium count with two preserved MicrobeDecoder source occurrences, SSSOM row,
  and aggregate copy are populated.
- No formula, CAS, InChI, SMILES, or component list is required for this class
  record.

## Recommended Edits

- None.
