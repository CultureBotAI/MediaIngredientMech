# `data/ingredients/mapped/Indochrome.yaml`

## Verdict

Pass. The local `kgmicrobe.compound` placeholder is intentionally retained as
the exact registry identity for `Indochrome`, the prior no-hit triage and a
fresh OLS/PubChem check found no exact external candidate, and the final SSSOM
row does not export any unreviewed synonym text.

## Identity

- Reviewed record: `data/ingredients/mapped/Indochrome.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:indochrome` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:indochrome`, label
  `Indochrome`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The record has no synonyms, chemical structure block, occurrence count, or
  asserted roles.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Impenum_Monohydrate.yaml data/ingredients/mapped/Indigocarmine.yaml data/ingredients/mapped/Indochrome.yaml data/ingredients/mapped/Indole-3-acetate.yaml data/ingredients/mapped/Indole-3-butyric_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was skipped for this record because its
  `kgmicrobe.compound` identifier is outside the CHEBI/OBO adapter scope; the
  same check passed for the 4 CHEBI files in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1545`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1545`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- The current row-review manifest records `expected_registry_identifier`, and
  the unknown-term triage keeps `kgmicrobe.compound:indochrome` pending future
  curator promotion because no exact external ontology identity was curated.
- A fresh exact OLS4 search for `Indochrome` across CHEBI and NCIT returned no
  documents, and a fresh PubChem name lookup returned no CID.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Indochrome`
  to `kgmicrobe.compound:indochrome`, with empty `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, original no-hit review, and
  current unknown-term triage for this local identifier.

## Completeness

- The local registry identifier, placeholder evidence, aggregate copy, and
  final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None until an exact external ontology candidate appears for `Indochrome`.
