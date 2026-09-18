# `data/ingredients/mapped/Cyanuric_acid.yaml`

## Verdict

Pass. The CultureMech residual record maps the source label `Cyanuric acid`
exactly to active `CHEBI:38028`, restores structured evidence used by the SSSOM
builder, carries the expected 1/1 residual occurrence count, and exports a
clean final SSSOM row with no unsafe `other` labels.

## Identity

- Reviewed record: `data/ingredients/mapped/Cyanuric_acid.yaml`.
- Current identifier and grounding: `identifier: CHEBI:38028`,
  `ontology_mapping.ontology_id: CHEBI:38028`,
  `ontology_label: cyanuric acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:38028` returns active `CHEBI:38028` labelled
  `cyanuric acid` with formula `C3H3N3O3`, CAS xrefs, InChI, SMILES, and
  cyanuric acid synonyms.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:38028` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cuso4_X_5_H2o.yaml data/ingredients/mapped/Cuso4_X_6_H2o.yaml data/ingredients/mapped/Cyanocobalamin.yaml data/ingredients/mapped/Cyanuric_acid.yaml data/ingredients/mapped/Cyclodextrin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cuso4_X_5_H2o.yaml data/ingredients/mapped/Cuso4_X_6_H2o.yaml data/ingredients/mapped/Cyanocobalamin.yaml data/ingredients/mapped/Cyanuric_acid.yaml data/ingredients/mapped/Cyclodextrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI exact records in this batch.
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

- `mappings/culturemech_residual_groundings.tsv` records the residual
  `Cyanuric acid` label with 1 mention in 1 recipe and creates
  `CHEBI:38028` on an exact match to the canonical label.
- The curation history records the 1/1 occurrence refresh and the later
  structured `ontology_mapping.evidence` restoration for the SSSOM builder.
- The final SSSOM row publishes `MIM:Cyanuric_acid skos:exactMatch
  CHEBI:38028`, cites `MIM:culturemech:output/ingredient_occurrences.tsv`,
  uses `manual:claude_culturemech_residual_grounding|CREATED|2026-08-30`, and
  has an empty `other` column.

## Completeness

- No roles, chemical structure, source synonyms, CAS RN, or parent mappings are
  asserted, so there are no unsupported secondary claims to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the expected residual grounding and
  generated index rows; none contradict the exact CHEBI identity.

## Recommended Edits

- None for this record.
