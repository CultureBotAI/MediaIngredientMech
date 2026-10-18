# `data/ingredients/mapped/D-Gluconic_acid.yaml`

## Verdict

Pass. The CultureMech residual record maps exactly to active `CHEBI:33198`,
keeps restored structured SSSOM evidence, has a 4/4 occurrence count from the
residual source table, and exports a clean final SSSOM row with no unsafe
`other` labels.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Gluconic_acid.yaml`.
- Current identifier and grounding: `identifier: CHEBI:33198`,
  `ontology_mapping.ontology_id: CHEBI:33198`,
  `ontology_label: D-gluconic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:33198` returns active `CHEBI:33198` labelled
  `D-gluconic acid` with formula `C6H12O7` and structure fields.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:33198` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Galacturonic_Acid_Monohydrate.yaml data/ingredients/mapped/D-Glucaric_Acid.yaml data/ingredients/mapped/D-Gluconic_acid.yaml data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml data/ingredients/mapped/D-Glucosamine_Hydrochloride.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Glucaric_Acid.yaml data/ingredients/mapped/D-Gluconic_acid.yaml data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
  `D-Galacturonic_Acid_Monohydrate` and `D-Glucosamine_Hydrochloride` were
  intentionally skipped because their primary identifiers are CAS registry
  CURIEs.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Live OLS confirms the exact `CHEBI:33198` label and current structure for
  D-gluconic acid.
- The curation history records four mentions across four CultureMech recipes,
  and the structured `ontology_mapping.evidence` field now carries
  `culturemech:output/ingredient_occurrences.tsv`, the source read by the SSSOM
  builder.
- The final SSSOM row publishes
  `MIM:D-Gluconic_acid skos:exactMatch CHEBI:33198`, cites the restored
  CultureMech occurrence evidence, and has an empty `other` column.

## Completeness

- No roles, synonyms, CAS RN, parent mappings, supplied-form assertions, or
  mixture components are asserted, so there are no unsupported secondary claims
  to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found no conflicting primary record for `CHEBI:33198`.

## Recommended Edits

- None for this record.
