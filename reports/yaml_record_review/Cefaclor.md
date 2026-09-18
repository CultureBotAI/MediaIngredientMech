# `data/ingredients/mapped/Cefaclor.yaml`

## Verdict

Needs curation; major issue. The cefaclor identity is grounded exactly to
active `CHEBI:3478`, and its CAS, formula, InChI, SMILES, synonyms, SSSOM row,
aggregate copy, and 0/0 occurrence count agree. The remaining
`SELECTIVE_AGENT` role is supported only by a provisional name-pattern
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Cefaclor.yaml`.
- Identifier and grounding: `identifier: CHEBI:3478`,
  `ontology_mapping.ontology_id: CHEBI:3478`, `ontology_label: cefaclor`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3478` returns one active ChEBI term labelled
  `cefaclor` with CAS `53994-73-3`, formula `C15H14ClN3O4S`, and the same
  InChI, SMILES, and exact IUPAC synonyms stored in the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cefaclor.yaml data/ingredients/mapped/Cefadroxil.yaml data/ingredients/mapped/Cefaloridine.yaml data/ingredients/mapped/Cefalotin.yaml data/ingredients/mapped/Cefamandole.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cefaclor.yaml data/ingredients/mapped/Cefadroxil.yaml data/ingredients/mapped/Cefaloridine.yaml data/ingredients/mapped/Cefalotin.yaml data/ingredients/mapped/Cefamandole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  backups, found the active exact `MIM:Cefaclor` SSSOM row, the
  `CONFIRMED_NO_ACTION` row-review disposition, and matching aggregate/docs
  rows for `CHEBI:3478`.
- Hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  found no `CHEBI:3478` rows, which matches the explicit 0/0
  `occurrence_statistics`.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, IUPAC synonyms,
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.
- The record has no component, environment, or mechanistic assertions that need
  additional evidence.

## Recommended Edits

- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` with inspected
  evidence for cefaclor as a selective agent in this media scope, or remove the
  role, then rerun strict validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
