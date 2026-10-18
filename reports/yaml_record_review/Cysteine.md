# `data/ingredients/mapped/Cysteine.yaml`

## Verdict

Pass. The CultureMech record maps the generic cysteine identity to active
`CHEBI:15356`, keeps matching structure fields and a database-backed nitrogen
role, has a current 51/51 CultureMech occurrence count, and exports only real
synonyms plus its own CAS alias in the final SSSOM `other` column.

## Identity

- Reviewed record: `data/ingredients/mapped/Cysteine.yaml`.
- Current identifier and grounding: `identifier: CHEBI:15356`,
  `ontology_mapping.ontology_id: CHEBI:15356`,
  `ontology_label: cysteine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:15356` returns active `CHEBI:15356` labelled
  `cysteine` with formula `C3H7NO2S` and matching InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:15356` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cycloviracin_B2.yaml data/ingredients/mapped/Cystargin.yaml data/ingredients/mapped/Cysteine.yaml data/ingredients/mapped/Cystine.yaml data/ingredients/mapped/Cytidine.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cycloviracin_B2.yaml data/ingredients/mapped/Cysteine.yaml data/ingredients/mapped/Cystine.yaml data/ingredients/mapped/Cytidine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  `Cystargin` was intentionally skipped because its primary identifier is
  `mesh:C058276`, outside this CHEBI/OBO validation scope.
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

- The record's formula, InChI, SMILES, and CAS RN match the generic active
  `CHEBI:15356` identity selected after the earlier CAS conflict was resolved.
- `mappings/culturemech_recipe_membership.tsv` contains 51 rows for
  `CHEBI:15356`, matching the record's 51/51 `occurrence_statistics`.
- The `NITROGEN_SOURCE` role is attached as a role facet with CultureMech
  database-entry evidence; it is not merely inferred from the CHEBI class.
- The final SSSOM row publishes `MIM:Cysteine skos:exactMatch CHEBI:15356`,
  cites the CultureMech import and reviewed KG-Microbe surfaces, and exports
  only same-substance synonyms plus `CAS:3374-22-9` in `other`.

## Completeness

- The YAML still retains raw CultureMech `Role:`/`Properties:` strings as
  `RAW_TEXT` synonym provenance, but the final SSSOM synonym policy filters
  them out of `other`; they do not pollute the published synonym payload.
- The separate `L-cysteine` and `L-cystine` sibling records remain distinct
  from this generic cysteine record.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected older kg-microbe companion rows and
  no current primary-record conflict for `CHEBI:15356`.

## Recommended Edits

- None for this record.
