# `data/ingredients/mapped/Na2HPO4-NaH2PO4_Buffer.yaml`

## Verdict

Pass. The record is a curated local stock-solution registry entry for
`Na2HPO4-NaH2PO4 buffer`; it correctly avoids a false single-compound parent,
records the #288 no-external-term search, and publishes a local final exact row
with no extra synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2HPO4-NaH2PO4_Buffer.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:na2hpo4-nah2po4_buffer` with matching
  `ontology_mapping.ontology_id`, label `Na2HPO4-NaH2PO4 buffer`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- Occurrences: 7 CultureMech recipe occurrences across 7 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2-edta_X_2_H2o` through `Na2HPO4-NaH2PO4_Buffer`: exited 0 and wrote zero
  ERROR rows.
- Engine A term validation was skipped for this record because
  `kgmicrobe.ingredient` is not in the narrow OBO-safe prefix set.

## Evidence

- The #288 curation history records a direct CHEBI, NCIT, MeSH, FOODON, and ENVO
  label/synonym search that found no external term denoting the named
  multi-component preparation.
- The #288 convention is applied correctly: the record uses a local
  `kgmicrobe.ingredient` identity and leaves off a parent because this stock
  solution is not a narrower form of any single compound.
- The final SSSOM row for `MIM:Na2HPO4-NaH2PO4_Buffer` maps exactly to the local
  target and emits no unsupported `other` synonyms.

## Completeness

- The local identity, fallback-registry provenance, 7/7 occurrence count,
  stock-solution type, and final registry row agree.
- A component decomposition is not required for this record because it is a
  named buffer with no maintained concentration breakdown in the curated YAML.

## Recommended Edits

- None.
