# `data/ingredients/mapped/Trypsin_Sigma-Aldrich.yaml`

## Verdict

Needs curation, major. The CultureMech occurrence and final SSSOM row are
synchronized, but a vendor-qualified trypsin ingredient is exact-mapped to the
MICRO `trypsin assay` class.

## Identity

- Reviewed record: `data/ingredients/mapped/Trypsin_Sigma-Aldrich.yaml`.
- Identifier and grounding: `identifier: MICRO:0000673` with matching
  `ontology_mapping.ontology_id`, label `trypsin assay`, source `MICRO`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Synonyms: none.
- Occurrences: 1 CultureMech recipe occurrence in 1 medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triton_X-100` through `Tryptamine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh MICRO-scoped OLS4 search for `trypsin assay` returns `MICRO:0000673`
  with label `trypsin assay`.
- Fresh MICRO-scoped OLS4 search for `trypsin` also shows why the residual
  matcher hit this term: `MICRO:0000673` carries `trypsin` as a synonym.
- The final SSSOM row has
  `MIM:Trypsin_Sigma-Aldrich skos:exactMatch MICRO:0000673`, publishing an
  exact match from the Sigma-Aldrich enzyme ingredient to the assay class.

## Issues

### Major: a trypsin product is exact-mapped to a trypsin assay

The CultureMech source surface is a vendor-qualified trypsin ingredient. An
assay class is not an ingredient identity, even if the assay class carries
`trypsin` as a synonym. This should not publish as an exact SSSOM mapping.

## Completeness

- The YAML, aggregate copy, and final SSSOM row agree on the current assay
  mapping.
- The consequential gap is replacing the assay target with the trypsin
  ingredient identity or merging this vendor-qualified occurrence into
  `data/ingredients/mapped/Trypsin.yaml` if the source supports that collapse.

## Recommended Edits

- Remap this row from `MICRO:0000673` to an ingredient identity such as
  `CHEBI:9765`, or merge the Sigma-Aldrich surface into `Trypsin` as a
  non-exported raw/vendor occurrence if it should not remain a separate MIM
  subject.
