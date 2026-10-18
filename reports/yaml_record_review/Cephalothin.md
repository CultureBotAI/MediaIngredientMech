# `data/ingredients/mapped/Cephalothin.yaml`

## Verdict

Needs curation; minor issue. The MicrobeDecoder cephalothin label is exactly
grounded to active `NCIT:C62021`, and its source occurrence annotation, zero
media occurrence count, SSSOM row, and aggregate copy agree. Active ChEBI now
also has the same neutral cephalothin identity as exact synonym `Cephalothin`
on `CHEBI:124991`, so this record should be considered for a source-preference
regrounding to ChEBI.

## Identity

- Reviewed record: `data/ingredients/mapped/Cephalothin.yaml`.
- Identifier and grounding: `identifier: NCIT:C62021`,
  `ontology_mapping.ontology_id: NCIT:C62021`,
  `ontology_label: Cephalothin`, `ontology_source: NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The focused LinkML label validator resolves `NCIT:C62021` and accepts the
  stored `Cephalothin` ontology label.
- Current exact OLS search across CHEBI and NCIT returns active
  `NCIT:C62021` labelled `Cephalothin`; it also returns active
  `CHEBI:124991` labelled `cefalotin`, whose exact synonyms include
  `Cephalothin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cellulose.yaml data/ingredients/mapped/Cellulose_powder.yaml data/ingredients/mapped/Cephalexin.yaml data/ingredients/mapped/Cephalosporin.yaml data/ingredients/mapped/Cephalothin.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cellulose.yaml data/ingredients/mapped/Cellulose_powder.yaml data/ingredients/mapped/Cephalexin.yaml data/ingredients/mapped/Cephalosporin.yaml data/ingredients/mapped/Cephalothin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact `MIM:Cephalothin` NCIT SSSOM row, the
  approved `mappings/microbedecoder_auto_mapped_review.tsv` row, and matching
  aggregate/docs rows for `NCIT:C62021`.
- `reports/yaml_record_review_batch/validation_report.md` still says
  `NCIT:C62021` is invalid and does not exist, but that advisory batch report
  is stale for NCIT prefix coverage; the focused LinkML validator and current
  OLS exact search both resolve the NCIT term.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `NCIT:C62021` rows,
  which matches the explicit 0/0 media `occurrence_statistics`.
- The MicrobeDecoder `source_occurrences` annotation preserves the 105 BacDive
  antibiotic sensitivity/resistance mentions that caused this ingredient-like
  trait to be imported. Those source mentions are not CultureMech recipe
  occurrences.

## Completeness

- The exact NCIT identifier, source occurrence count, SSSOM row, aggregate copy,
  docs row, and zero media occurrence count are populated and agree.
- No chemical properties are populated. That is appropriate for the current
  NCIT grounding, but a move to active `CHEBI:124991` would allow this record
  to carry the neutral cephalothin formula, InChI, and SMILES.

## Recommended Edits

- Minor: evaluate promoting `Cephalothin` from exact `NCIT:C62021` to synonym
  match `CHEBI:124991` under MIM's source preference, then rerun strict
  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
