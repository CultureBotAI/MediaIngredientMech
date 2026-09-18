# `data/ingredients/mapped/Cellostatin.yaml`

## Verdict

Pass. `Cellostatin` is intentionally retained as the local
`kgmicrobe.compound:cellostatin` placeholder while no exact CHEBI or NCIT
identity is available, and the placeholder record, SSSOM row, zero occurrence
count, aggregate copy, and no-hit review artifacts agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cellostatin.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:cellostatin`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:cellostatin`,
  `ontology_label: Cellostatin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- A current OLS search for `Cellostatin` across CHEBI and NCIT returned zero
  results, matching the earlier no-hit placeholder review.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cellohexaose.yaml data/ingredients/mapped/Cellopentaose.yaml data/ingredients/mapped/Cellostatin.yaml data/ingredients/mapped/Cellotetraose.yaml data/ingredients/mapped/Cellotriose.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cellohexaose.yaml data/ingredients/mapped/Cellopentaose.yaml data/ingredients/mapped/Cellotetraose.yaml data/ingredients/mapped/Cellotriose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external ChEBI records in this batch. The local
  `kgmicrobe.compound:cellostatin` placeholder was intentionally skipped because
  it is a local registry CURIE outside the validator's OAK/OLS prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact `MIM:Cellostatin` SSSOM row, the
  `expected_registry_identifier` row-review disposition, the
  `NO_LOCAL_DUPLICATE_NO_OLS_CANDIDATE` placeholder review, the
  `NO_EXACT_CANDIDATE` OLS-candidate review, and matching aggregate/docs rows
  for `kgmicrobe.compound:cellostatin`.
- `reports/yaml_record_review_batch/validation_report.md` still says
  `kgmicrobe.compound:cellostatin` is invalid and does not exist, but that
  advisory batch report is stale: the active row review explicitly keeps this
  local registry identifier pending promotion to an external ontology term.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:cellostatin` rows, which matches the explicit 0/0
  `occurrence_statistics`.
- The record carries no chemical property, role, component, or environment
  claims.

## Completeness

- The local kg-microbe placeholder identifier, no-hit review note, exact local
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.
- `synonyms` is empty, but no local alternate label, rejected label, or
  additional lookup key is currently required for this local identity.

## Recommended Edits

- None for this record.
