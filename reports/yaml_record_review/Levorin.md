# `data/ingredients/mapped/Levorin.yaml`

## Verdict

Pass. The promoted MeSH `D002174` identity is active and preserves the original
`Levorin` label through the Candicidin descriptor, and the final SSSOM row has no
unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Levorin.yaml`.
- Identifier and grounding: `identifier: mesh:D002174` with
  `ontology_mapping.ontology_id: mesh:D002174`, label `Candicidin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The record has no curated formula, structure, CAS RN, or role facets.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Levorin` through `Lignin`: exited 0 and wrote zero ERROR rows.
- Engine A term-label validation was run for the four CHEBI-grounded records in
  the batch and exited 0; the `mesh:` record was skipped from that CHEBI/OBO
  subset and checked against OLS/NLM manually.

## Evidence

- EBI OLS4 search for `Levorin` in MeSH resolves `mesh:D002174` with label
  `Candicidin`.
- NLM MeSH resolves descriptor `D002174` as active `Candicidin` and records
  historic `LEVORIN` indexing under that descriptor.
- The final SSSOM publishes one `skos:exactMatch` row to `mesh:D002174` and has
  an empty `other` field.
- The aggregate `data/curated/mapped_ingredients.yaml` copy matches the
  per-record identity, status, and mapping.

## Completeness

- The active MeSH identity, aggregate copy, and final SSSOM row are present and
  consistent.
- No nutritional, physicochemical, cellular, environmental, structure, or CAS
  assertion is present.

## Recommended Edits

- None.
