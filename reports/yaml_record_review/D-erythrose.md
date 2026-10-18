# `data/ingredients/mapped/D-erythrose.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The CultureBotHT exact
`CHEBI:27904` identity, CAS/formula/structure fields, 0/0 occurrence count, and
final SSSOM synonym payload pass, but `CARBON_SOURCE` is asserted only from
provisional CHEBI-ancestry evidence and needs direct media-use support or
removal.

## Identity

- Reviewed record: `data/ingredients/mapped/D-erythrose.yaml`.
- Current identifier and grounding: `identifier: CHEBI:27904`,
  `ontology_mapping.ontology_id: CHEBI:27904`,
  `ontology_label: D-erythrose`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:27904` returns active `CHEBI:27904` labelled
  `D-erythrose`, neutral formula `C4H8O4`, CAS xref `583-50-6`, and exact
  synonyms including `(2R,3R)-2,3,4-trihydroxybutanal` and `D-erythro-tetrose`.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:27904`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-arabinose.yaml data/ingredients/mapped/D-arabitol.yaml data/ingredients/mapped/D-aspartate.yaml data/ingredients/mapped/D-erythrose.yaml data/ingredients/mapped/D-fructose.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- Five `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  invocations, one per reviewed CHEBI-primary file in this batch: all exited 0.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with 104 non-blocking plausibility
  warnings across the full corpus.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe transformed ontology files were absent.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1334`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1334`:
  passed; 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.
- `uv run --frozen python scripts/run_shared_evidence_validator.py`: failed
  because the sibling `culturebotai-claw` evidence validator checkout is absent.

## Evidence

- The record's CAS RN, molecular formula, InChI, and SMILES agree with active
  `CHEBI:27904`.
- `mappings/culturemech_recipe_membership.tsv` contains 0 rows for
  `CHEBI:27904`, matching the record's 0/0 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no mapping action required.
- The final SSSOM row publishes `MIM:D-erythrose skos:exactMatch CHEBI:27904`.
  Its `other` tokens are the live ChEBI synonyms
  `(2R,3R)-2,3,4-trihydroxybutanal` and `D-erythro-tetrose` plus
  `CAS:583-50-6`.
- `CARBON_SOURCE` is supported only by `COMPUTATIONAL_PREDICTION` from CHEBI
  carbohydrate ancestry, and the evidence row calls itself provisional.

## Completeness

- No parent mappings, supplied-form assertions, components, environmental
  contexts, or source occurrences are asserted, so there are no unsupported
  secondary claims beyond the provisional nutritional role.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/D-erythrose.yaml`, either replace the
  computational `CARBON_SOURCE` evidence with direct, source-backed media-role
  evidence for D-erythrose, or remove the role facet; then rerun strict
  validation and the final SSSOM gates.
