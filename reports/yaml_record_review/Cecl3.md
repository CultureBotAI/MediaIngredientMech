# `data/ingredients/mapped/Cecl3.yaml`

## Verdict

Needs curation; major issue. The anhydrous cerium trichloride identity is
grounded exactly to active `CHEBI:35458`, and its CAS, formula, InChI, SMILES,
synonyms, SSSOM row, aggregate copy, and 4/4 occurrence count agree. The
remaining TRACE_ELEMENT role is supported only by a provisional in-session LLM
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Cecl3.yaml`.
- Identifier and grounding: `identifier: CHEBI:35458`,
  `ontology_mapping.ontology_id: CHEBI:35458`,
  `ontology_label: cerium trichloride`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:35458` returns one active ChEBI term labelled
  `cerium trichloride` with CAS `11098-86-5` and `7790-86-5`, formula
  `CeCl3`, and the same InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cecl3.yaml data/ingredients/mapped/Cecl3_X_7_H2o.yaml data/ingredients/mapped/Cecropin_A.yaml data/ingredients/mapped/Cecropin_B.yaml data/ingredients/mapped/Cedrelone.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cecl3.yaml data/ingredients/mapped/Cecl3_X_7_H2o.yaml data/ingredients/mapped/Cecropin_A.yaml data/ingredients/mapped/Cecropin_B.yaml data/ingredients/mapped/Cedrelone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  backups, found the active exact `MIM:Cecl3` SSSOM row, the aggregate/docs
  rows for `CHEBI:35458`, and the
  `mappings/other_cross_record_baseline.tsv` row that keeps the anhydrous
  record distinct from `CeCl3 x 7 H2O`.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain four
  distinct recipes and four total occurrences for `CHEBI:35458`, matching
  `occurrence_statistics`.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `claude_in_session_curation` and is explicitly marked "Provisional
  in-session LLM role assignment; review recommended."

## Completeness

- The exact ChEBI identifier, active label, CAS, formula, InChI, SMILES,
  synonyms, 4/4 occurrence count, SSSOM row, aggregate copy, and docs row are
  populated.
- The record has no component, environment, or mechanistic assertions that need
  additional evidence.

## Recommended Edits

- Major: either replace `nutritional_roles.TRACE_ELEMENT` with inspected
  evidence for cerium trichloride as a trace element in media, or remove the
  role, then rerun strict validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
