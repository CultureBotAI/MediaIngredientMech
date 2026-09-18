# `data/ingredients/mapped/Na-phosphate_Buffer.yaml`

## Verdict

Pass. The record is a curated local stock-solution registry entry for
`Na-phosphate buffer`; it correctly avoids a false single-compound parent,
records the #288 no-external-term search, folds the punctuation-only duplicate,
and publishes a local final exact row.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-phosphate_Buffer.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:na-phosphate_buffer` with matching
  `ontology_mapping.ontology_id`, label `Na-phosphate buffer`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- Occurrences: 6 CultureMech recipe occurrences across 6 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-orotate` through `Na-silicate`: exited 0 and wrote zero ERROR rows.
- Engine A term validation was skipped for this record:
  `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Na-phosphate_Buffer.yaml
  "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"` exited 1 because
  `kgmicrobe.ingredient` is not in the narrow OBO-safe prefix set.

## Evidence

- The #288 curation history records a direct CHEBI, NCIT, MeSH, FOODON, and ENVO
  label/synonym search that found no external term denoting the named
  multi-component preparation.
- The #288 convention is applied correctly: the record uses a local
  `kgmicrobe.ingredient` identity and leaves off a parent because this stock
  solution is not a narrower form of any single compound.
- The final SSSOM row for `MIM:Na-phosphate_Buffer` maps exactly to the local
  `kgmicrobe.ingredient:na-phosphate_buffer` target and carries
  `Na-Phosphate-Buffer` only as a spelling/punctuation surface.

## Completeness

- The local identity, fallback-registry provenance, 6/6 occurrence count,
  duplicate merge, stock-solution type, and final registry row agree.
- A component decomposition is not required for this record because it is a
  named buffer with no maintained concentration breakdown in the curated YAML.

## Recommended Edits

- None.
