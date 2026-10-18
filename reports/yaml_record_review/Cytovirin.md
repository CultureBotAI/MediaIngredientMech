# `data/ingredients/mapped/Cytovirin.yaml`

## Verdict

Pass. The reviewed local `kgmicrobe.compound:cytovirin` placeholder is still
the maintained identity for Cytovirin: the prior placeholder review found no
local duplicate or exact OLS candidate, a fresh exact OLS search across the
same external ontologies still finds none, and the record asserts no roles,
synonyms, or structure fields beyond that local identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Cytovirin.yaml`.
- Current identifier and grounding:
  `identifier: kgmicrobe.compound:cytovirin`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:cytovirin`,
  `ontology_label: Cytovirin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, and `mapping_status: MAPPED`.
- A live exact OLS label/synonym search across CHEBI, MeSH, NCIT, MICRO, BTO,
  and FOODON found no exact `Cytovirin` candidate.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using
  `kgmicrobe.compound:cytovirin` as its primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cytidine_5-Monophosphate.yaml data/ingredients/mapped/Cytisine.yaml data/ingredients/mapped/Cytochrome.yaml data/ingredients/mapped/Cytosine.yaml data/ingredients/mapped/Cytovirin.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cytidine_5-Monophosphate.yaml data/ingredients/mapped/Cytisine.yaml data/ingredients/mapped/Cytochrome.yaml data/ingredients/mapped/Cytosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  This record was intentionally skipped because
  `kgmicrobe.compound:cytovirin` is a local placeholder primary identifier.
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

- `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`
  records `NO_EXACT_CANDIDATE` for Cytovirin in the CHEBI, MeSH, NCIT, MICRO,
  BTO, and FOODON placeholder search.
- `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` records
  `NO_LOCAL_DUPLICATE_NO_OLS_CANDIDATE`, matching the YAML note that retains
  the `kgmicrobe.compound` primary until an exact external identity is curated.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the
  residual `UNKNOWN_TERM` as an expected registry identifier and says to keep
  the local placeholder pending curator promotion.
- The final SSSOM row publishes
  `MIM:Cytovirin skos:exactMatch kgmicrobe.compound:cytovirin` with
  `kgm:compound` as the object source and an empty `other` column.

## Completeness

- No roles, parent mappings, CAS RN, chemical structure fields, or synonyms are
  asserted, so there are no unsupported secondary claims to adjudicate.
- The older batch-review `Ontology term ... does not exist` and `Invalid CURIE`
  findings are expected false positives for this local placeholder namespace.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found no local mapped duplicate or promoted
  external-ontology replacement for `kgmicrobe.compound:cytovirin`.

## Recommended Edits

- None for this record.
