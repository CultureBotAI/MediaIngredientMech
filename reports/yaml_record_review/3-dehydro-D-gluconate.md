# `data/ingredients/mapped/3-dehydro-D-gluconate.yaml`

## Verdict

Pass with minor issues, minor. The exact `CHEBI:85256`
`3-dehydro-D-gluconate` identity, microbedecoder occurrence count,
ChEBI/PubChem chemistry, SSSOM row, and aggregate row pass; only stale advisory
rows and a historical timestamp-ordering nit remain.

## Identity

- Reviewed record: `data/ingredients/mapped/3-dehydro-D-gluconate.yaml`.
- Identifier and grounding: `identifier: CHEBI:85256` with
  `ontology_mapping.ontology_id: CHEBI:85256`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:85256`
  resolves to `3-dehydro-D-gluconate`, lists formula `C6H9O7`, and matches the
  record InChI and SMILES.
- The direct microbedecoder
  `BacDive_Metabolite_utilization` count of 1 is preserved under
  `source_occurrences`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-aminobutyric_Acid.yaml data/ingredients/mapped/3-beta-d-glucan.yaml data/ingredients/mapped/3-dehydro-D-gluconate.yaml data/ingredients/mapped/3-fucosyllactose.yaml data/ingredients/mapped/3-hydroxybenzoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-dehydro-D-gluconate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-dehydro-D-gluconate` to `CHEBI:85256` row.

## Evidence

- The active ChEBI page confirms the exact D-configured anion identity, formula,
  and structure.
- The older `microbedecoder_auto_mapped_review.tsv` row explicitly warned that
  its approval did not check for homonyms or wrong-sense matches. The direct
  ChEBI verification performed here closes that gap for this record.
- Stale: `mappings/record_research_validation.tsv` still notes that the ChEBI
  release status should be checked and that `ingredient_type` was missing; the
  active ChEBI page now resolves and the record has
  `ingredient_type: SINGLE_INGREDIENT`.
- Minor: the `REVIEWED_AND_PROMOTED` curation event has a midnight timestamp on
  `2026-08-04`, so it sorts before the earlier same-day import and
  `PENDING_REVIEW` events despite documenting a later transition.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, microbedecoder review, generated docs, and stale advisory
  rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Formula, molecular weight, InChI, and SMILES are populated from ChEBI/PubChem.
- The direct microbedecoder source occurrence is represented.
- No material record-local curation defect remains.

## Recommended Edits

No YAML edit is required for this record. The stale advisory rows can be
ignored or refreshed when `mappings/record_research_validation.tsv` is rebuilt;
the timestamp-ordering nit can be left alone unless the curation history is
normalized later.
