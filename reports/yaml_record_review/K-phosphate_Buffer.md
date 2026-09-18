# `data/ingredients/mapped/K-phosphate_Buffer.yaml`

## Verdict

Pass with minor issues. The #288 stock-solution fallback to
`kgmicrobe.ingredient:k-phosphate_buffer` is represented consistently in YAML,
the aggregate, and the final SSSOM, but the import-era free-text `notes` field
still says curator review is needed even though the record has been manually
promoted.

## Identity

- Reviewed record: `data/ingredients/mapped/K-phosphate_Buffer.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:k-phosphate_buffer` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:k-phosphate_buffer`,
  label `K-phosphate buffer`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- The record intentionally has no CAS RN, ChEBI formula, InChI, or SMILES
  because it models a named phosphate buffer preparation rather than one simple
  chemical.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Jasmonic_Acid.yaml data/ingredients/mapped/Juglone.yaml data/ingredients/mapped/K-acetate.yaml data/ingredients/mapped/K-phosphate_Buffer.yaml data/ingredients/mapped/K2co3.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was skipped for this record because local
  `kgmicrobe.ingredient` CURIEs are non-OBO identifiers covered by downstream
  product validation rather than `sqlite:obo:` term lookup.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2130`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2130`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- The #288 promotion history records the local fallback decision: this is a
  named multi-component stock solution with no exact public ontology term and no
  parent single-compound term.
- Fresh exact OLS4 ChEBI searches for `K-phosphate buffer` and
  `K-phosphate Buffer` returned zero hits, matching the local fallback.
- The final SSSOM publishes one `skos:exactMatch` row from the case-preserved
  subject `MIM:K-phosphate_Buffer` to
  `kgmicrobe.ingredient:k-phosphate_buffer`, with no `other` synonyms.
- `mappings/mim_curie_alias_seeds.tsv` and
  `tests/test_published_mim_subject_case.py` explicitly cover the published
  `MIM:K-phosphate_Buffer` subject spelling, so the capital `B` in the SSSOM
  row is expected rather than an unresolved orphan.
- Minor: `notes` still repeats the April import text, including `no CAS-RN or
  CHEBI/NCIT match. Curator review needed.`, even though the August #288
  curation event promoted the record and explains the fallback target.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, alias seed, case-preserved
  subject test, and the original exact-OLS audit row.

## Completeness

- The local fallback identifier, aggregate copy, occurrence count, alias seed,
  and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.
- Only stale explanatory text remains in `notes`; the actual status, mapping
  object, and curation history are current.

## Recommended Edits

- Minor: refresh or remove the stale `notes` text in
  `data/ingredients/mapped/K-phosphate_Buffer.yaml`, then synchronize the
  aggregate and rerun strict, round-trip, component, and SSSOM validation.
