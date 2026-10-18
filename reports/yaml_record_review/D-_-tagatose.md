# `data/ingredients/mapped/D-_-tagatose.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The active `CHEBI:4249`
synonym match, CAS xref, structure fields, 0/0 occurrence count, and final
SSSOM CAS payload pass, but `CARBON_SOURCE` is asserted only from provisional
CHEBI-ancestry evidence and needs direct media-use support or removal.

## Identity

- Reviewed record: `data/ingredients/mapped/D-_-tagatose.yaml`.
- Current identifier and grounding: `identifier: CHEBI:4249`,
  `ontology_mapping.ontology_id: CHEBI:4249`,
  `ontology_label: D-tagatopyranose`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:4249` returns active `CHEBI:4249` labelled
  `D-tagatopyranose`, formula `C6H12O6`, CAS xref `87-81-0`, matching
  InChI/SMILES strings, and the related synonym `D-Tagatose`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:4249` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml data/ingredients/mapped/D-_-pantolactone.yaml data/ingredients/mapped/D-_-tagatose.yaml data/ingredients/mapped/D-_-turanose.yaml data/ingredients/mapped/D-apiose.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-_-pantolactone.yaml data/ingredients/mapped/D-_-tagatose.yaml data/ingredients/mapped/D-_-turanose.yaml data/ingredients/mapped/D-apiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 with no failures for the four CHEBI-primary records in this batch.
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

- The record's formula, InChI, SMILES, and CAS RN agree with active
  `CHEBI:4249`.
- The hidden/ignored-inclusive membership search found no `CHEBI:4249` rows in
  `mappings/culturemech_recipe_membership.tsv`, matching the record's 0/0
  `occurrence_statistics`.
- The final SSSOM row publishes
  `MIM:D-_-tagatose skos:exactMatch CHEBI:4249` and carries only
  `CAS:87-81-0` in `other`.
- The `CARBON_SOURCE` facet is supported only by
  `COMPUTATIONAL_PREDICTION` from CHEBI ancestry and its own `curator_note`
  calls it provisional.

## Completeness

- No parent mappings, supplied-form assertions, components, source occurrences,
  or additional synonyms are asserted, so there are no unsupported secondary
  claims beyond the provisional nutritional role.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- In `data/ingredients/mapped/D-_-tagatose.yaml`, either replace the
  computational `CARBON_SOURCE` evidence with direct CultureBotHT or
  source-backed media-role evidence for this ingredient, or remove the role
  facet; then rerun strict validation and the final SSSOM build.
