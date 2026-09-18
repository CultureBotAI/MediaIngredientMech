# `data/ingredients/mapped/Cytochrome.yaml`

## Verdict

Pass. The MicrobeDecoder label maps exactly to active `CHEBI:4056`, keeps the
reviewed one-count BacDive production provenance, intentionally omits
small-molecule structure fields for this broad cytochrome class, and exports a
clean final SSSOM row with no unsafe `other` labels.

## Identity

- Reviewed record: `data/ingredients/mapped/Cytochrome.yaml`.
- Current identifier and grounding: `identifier: CHEBI:4056`,
  `ontology_mapping.ontology_id: CHEBI:4056`,
  `ontology_label: cytochrome`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:4056` returns active `CHEBI:4056` labelled
  `cytochrome`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:4056` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cytidine_5-Monophosphate.yaml data/ingredients/mapped/Cytisine.yaml data/ingredients/mapped/Cytochrome.yaml data/ingredients/mapped/Cytosine.yaml data/ingredients/mapped/Cytovirin.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cytidine_5-Monophosphate.yaml data/ingredients/mapped/Cytisine.yaml data/ingredients/mapped/Cytochrome.yaml data/ingredients/mapped/Cytosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  `Cytovirin` was intentionally skipped because its primary identifier is a
  local `kgmicrobe.compound` placeholder.
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

- Live OLS confirms the exact `CHEBI:4056` cytochrome label; no formula, InChI,
  or SMILES block is available for that broad class, so the empty
  `chemical_properties` slot is not stale chemical data.
- `data/custom/microbedecoder/ingredient_candidates.tsv` records `cytochrome`
  with count 1 from `BacDive_Metabolite_production`, matching the record's
  `source_occurrences` entry.
- `mappings/culturemech_recipe_membership.tsv` contains no `CHEBI:4056` rows,
  matching the record's 0/0 `occurrence_statistics`.
- `mappings/microbedecoder_auto_mapped_review.tsv` marks `Cytochrome.yaml`
  approved, and the final SSSOM row publishes
  `MIM:Cytochrome skos:exactMatch CHEBI:4056` with an empty `other` column.

## Completeness

- No roles, parent mappings, CAS RN, or synonyms are asserted, so there are no
  unsupported secondary claims to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`,
  `data/custom/microbedecoder`, `scripts`, `tests`, and `reports` found no
  conflicting primary mapping for `CHEBI:4056`.

## Recommended Edits

- None for this record.
