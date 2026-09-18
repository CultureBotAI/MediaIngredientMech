# `data/ingredients/mapped/Lignin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:6457 identity, empty role and synonym
payloads, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lignin.yaml`.
- Identifier and grounding: `identifier: CHEBI:6457` with
  `ontology_mapping.ontology_id: CHEBI:6457`, label `lignin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The record has no curated formula, structure, CAS RN, or role facets.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Levorin` through `Lignin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for
  `Levulinic_Acid.yaml`, `Lichenan_Icelandic_Moss.yaml`, `Licl.yaml`, and
  `Lignin.yaml`.

## Evidence

- EBI OLS4 resolves `CHEBI:6457` as active `lignin`.
- The MicrobeDecoder occurrence is retained in `source_occurrences` as one
  `BacDive_Metabolite_utilization` import, while `total_occurrences` and
  `media_count` correctly remain zero for the media-recipe corpus.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:6457` and has
  an empty `other` field.
- The aggregate `data/curated/mapped_ingredients.yaml` copy matches the
  per-record identity, status, and mapping.

## Completeness

- The active CHEBI identity, aggregate copy, and final SSSOM row are present and
  consistent.
- No nutritional, physicochemical, cellular, environmental, structure, or CAS
  assertion is present.

## Recommended Edits

- None.
