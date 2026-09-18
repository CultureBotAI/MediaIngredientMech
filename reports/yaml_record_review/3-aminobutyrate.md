# `data/ingredients/mapped/3-aminobutyrate.yaml`

## Verdict

Pass with minor issues, minor. The exact `CHEBI:87997`
`3-aminobutyrate` identity, microbedecoder occurrence count, ChEBI/PubChem
chemistry, SSSOM row, and aggregate row pass; only stale advisory rows and a
historical timestamp-ordering nit remain.

## Identity

- Reviewed record: `data/ingredients/mapped/3-aminobutyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:87997` with
  `ontology_mapping.ontology_id: CHEBI:87997`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:87997`
  resolves to `3-aminobutyrate`, lists formula `C4H8NO2`, and matches the
  record InChI and SMILES.
- The direct microbedecoder
  `BacDive_Metabolite_utilization` count of 4 is preserved under
  `source_occurrences`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Pyridinesulfonic_Acid.yaml data/ingredients/mapped/3-_N-morpholinopropanesulfonic_Acid.yaml data/ingredients/mapped/3-acetylpyridine.yaml data/ingredients/mapped/3-aminobenzoate.yaml data/ingredients/mapped/3-aminobutyrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-aminobutyrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-aminobutyrate` to `CHEBI:87997` row.

## Evidence

- The active ChEBI page confirms the exact anion identity, formula, and
  structure.
- The older `microbedecoder_auto_mapped_review.tsv` row explicitly warned that
  its approval did not check for homonyms or wrong-sense matches. The direct
  ChEBI verification performed here closes that gap for this record.
- Stale: `mappings/record_research_validation.tsv` still recommends an
  unresolved status and still reports `ingredient_type` as missing; the record
  is currently `MAPPED`, passes the direct ChEBI check, and has
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
