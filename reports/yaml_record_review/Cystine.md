# `data/ingredients/mapped/Cystine.yaml`

## Verdict

Pass. The MicrobeDecoder label maps exactly to active generic `CHEBI:17376`,
keeps matching cystine structure fields, has the expected 1/1 CultureMech count
plus one BacDive utilization source occurrence, and exports a clean final SSSOM
row with no unsafe `other` labels.

## Identity

- Reviewed record: `data/ingredients/mapped/Cystine.yaml`.
- Current identifier and grounding: `identifier: CHEBI:17376`,
  `ontology_mapping.ontology_id: CHEBI:17376`,
  `ontology_label: cystine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:17376` returns active `CHEBI:17376` labelled
  `cystine` with formula `C6H12N2O4S2` and matching InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:17376` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cycloviracin_B2.yaml data/ingredients/mapped/Cystargin.yaml data/ingredients/mapped/Cysteine.yaml data/ingredients/mapped/Cystine.yaml data/ingredients/mapped/Cytidine.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cycloviracin_B2.yaml data/ingredients/mapped/Cysteine.yaml data/ingredients/mapped/Cystine.yaml data/ingredients/mapped/Cytidine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  `Cystargin` was intentionally skipped because its primary identifier is
  `mesh:C058276`, outside this CHEBI/OBO validation scope.
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

- The record's formula, InChI, SMILES, and molecular weight match live
  `CHEBI:17376`.
- `mappings/culturemech_recipe_membership.tsv` contains one row for
  `CHEBI:17376`, matching the refreshed 1/1 `occurrence_statistics`.
- `data/custom/microbedecoder/ingredient_candidates.tsv` records `cystine` with
  count 1 from `BacDive_Metabolite_utilization`, matching the record's
  `source_occurrences` entry, and
  `mappings/microbedecoder_auto_mapped_review.tsv` marks `Cystine.yaml`
  approved.
- The final SSSOM row publishes `MIM:Cystine skos:exactMatch CHEBI:17376` and
  has an empty `other` column.

## Completeness

- No roles, parent mappings, CAS RN, or synonyms are asserted, so there are no
  unsupported secondary claims to adjudicate.
- The exact generic `CHEBI:17376` identity is distinct from the separate
  `L-cystine` sibling on `CHEBI:16283`; this record does not collapse the two.
- Hidden/ignored-inclusive searches over `data`, `mappings`,
  `data/custom/microbedecoder`, `scripts`, `tests`, and `reports` found no
  stale conflicting primary mapping for generic cystine.

## Recommended Edits

- None for this record.
