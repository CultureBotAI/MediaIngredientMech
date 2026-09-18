# `data/ingredients/mapped/2-dehydro-D-gluconate.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:16808` anion identity passes, but
`source_occurrences` omits the absorbed `2-oxogluconate` microbedecoder count.

## Identity

- Reviewed record: `data/ingredients/mapped/2-dehydro-D-gluconate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16808` with
  `ontology_mapping.ontology_id: CHEBI:16808`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:16808`
  resolves to `2-dehydro-D-gluconate` and lists formula `C6H9O7`.
- The absorbed `2-oxogluconate` label is represented as a raw synonym, and the
  SSSOM `other` field preserves both `2-oxogluconate` and
  `2-Ketogluconate (2-dehydro-D-gluconate)`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-bromo-2-nitro-13-propanediol.yaml data/ingredients/mapped/2-butanolCO2.yaml data/ingredients/mapped/2-chloro-4ethylamino-6-isopropylamino-135-triazine.yaml data/ingredients/mapped/2-dehydro-D-gluconate.yaml data/ingredients/mapped/2-deoxyadenosine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-dehydro-D-gluconate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-dehydro-D-gluconate` to `CHEBI:16808` row.

## Evidence

- The active ChEBI target confirms the same D-configured anion denoted by the
  record label.
- `data/custom/microbedecoder/unmapped_labels.tsv` has 152 occurrences for
  `kgmicrobe.trait:2_dehydro_d_gluconate` and 15 occurrences for the absorbed
  `kgmicrobe.trait:2_oxogluconate`. The active record only reports the 152
  direct-label occurrences.
- Stale: `mappings/record_research_validation.tsv` still contains old rows that
  asked for direct ChEBI verification or `ingredient_type` enrichment; ChEBI now
  resolves the term, and `ingredient_type` is populated.
- Non-blocking audit nit: `curation_history` is not timestamp-monotonic; the
  2026-08-04T00:00 review promotion follows later 2026-08-04 import and
  flag-for-review events.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the original and absorbed microbedecoder source rows, the active
  YAML/aggregate/SSSOM rows, sibling potassium-salt records that correctly use
  `CHEBI:16808` as a parent, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Formula, InChI, SMILES, and molecular weight are populated for the active
  anion form.
- The missing absorbed-label occurrence count is consequential because the
  `2-oxogluconate` synonym came from a real source row, not from optional
  ChEBI vocabulary enrichment.

## Recommended Edits

1. In `data/ingredients/mapped/2-dehydro-D-gluconate.yaml`, update
   `occurrence_statistics.source_occurrences` so the microbedecoder count
   includes the absorbed `2-oxogluconate` 15-count row in addition to the direct
   152-count `2_dehydro_d_gluconate` row.
2. Run `just sync-curated`, `just validate-strict
   data/ingredients/mapped/2-dehydro-D-gluconate.yaml`, `just validate-terms
   data/ingredients/mapped/2-dehydro-D-gluconate.yaml`, `just qc-sssom`, and
   `just qc-flat-coverage` after that curation edit.
