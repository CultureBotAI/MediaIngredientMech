# `data/ingredients/mapped/Cystargin.yaml`

## Verdict

Pass. The placeholder `kgmicrobe.compound:cystargin` record was upgraded to the
exact MeSH primary `mesh:C058276`; a prefix-specific live OLS4 lookup resolves
that CURIE as current `cystargin`, and the record publishes no roles, synonyms,
or structure fields that would overstate the sparse source.

## Identity

- Reviewed record: `data/ingredients/mapped/Cystargin.yaml`.
- Current identifier and grounding: `identifier: mesh:C058276`,
  `ontology_mapping.ontology_id: mesh:C058276`,
  `ontology_label: cystargin`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS4 exact `obo_id` lookup for `mesh:C058276` returns current label
  `cystargin`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records the
  exact prefix-specific EBI OLS resolution of `mesh:C058276` to `cystargin`
  with IRI `http://id.nlm.nih.gov/mesh/C058276`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `mesh:C058276` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cycloviracin_B2.yaml data/ingredients/mapped/Cystargin.yaml data/ingredients/mapped/Cysteine.yaml data/ingredients/mapped/Cystine.yaml data/ingredients/mapped/Cytidine.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cycloviracin_B2.yaml data/ingredients/mapped/Cysteine.yaml data/ingredients/mapped/Cystine.yaml data/ingredients/mapped/Cytidine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  This record was intentionally skipped because `mesh:C058276` is outside the
  CHEBI/OBO prefix scope of the local LinkML term-validator command.
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

- The record carries the original kg-microbe placeholder evidence and the later
  `MESH via OLS search` exact-label upgrade that changed its primary CURIE to
  `mesh:C058276`.
- The older
  `mappings/ingredient_mappings_oak_ols_review.tsv` `UNKNOWN_TERM` row, the
  old batch-review `Ontology term mesh:C058276 does not exist` finding, and the
  old `Invalid CURIE format` finding are stale: the maintained row-review
  manifest classifies the miss as
  `missing_prefix_validator_coverage_issue` and the prefix-specific OLS row
  now resolves the exact CURIE.
- The final SSSOM row publishes `MIM:Cystargin skos:exactMatch mesh:C058276`
  with `registry:mesh`, cites the original kg-microbe import and `MESH via OLS
  search`, and has an empty `other` column.

## Completeness

- No roles, synonyms, CAS RN, parent mappings, or chemical structure fields are
  asserted; leaving those empty is appropriate for a MeSH-only exact mapping
  with 0/0 CultureMech occurrences.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found only the expected stale generic-validator
  misses and the newer prefix-specific OLS acceptance row; no current curated
  record conflicts with the `mesh:C058276` identity.

## Recommended Edits

- None for this record.
