# `data/ingredients/mapped/Air.yaml`

## Verdict

Needs curation. The exact `ENVO:00002005` grounding for air is valid, but the
CultureMech residual occurrence accounting is only partially reconciled: the
record captures the 12 uppercase `Air` mentions while a second lowercase `air`
row with five mentions remains in the residual grounding table.

## Identity

- Reviewed record: `data/ingredients/mapped/Air.yaml`.
- Identifier and grounding: `identifier: ENVO:00002005` with
  `ontology_mapping.ontology_id: ENVO:00002005`, source `ENVO`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Local OAK resolves `ENVO:00002005` to canonical label `air`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Agave.yaml data/ingredients/mapped/Air-dried_Garden_Soil.yaml data/ingredients/mapped/Air.yaml data/ingredients/mapped/Al2_So43_X_18_H2o.yaml data/ingredients/mapped/Alanosine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Air.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:envo aliases ENVO:00002263 ENVO:00002005`:
  returned canonical `garden soil` and `air`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` row 358 maps `MIM:Air` to
  `ENVO:00002005` with `skos:exactMatch` and preserves the CultureMech
  occurrence source after the September 2026 evidence restoration.
- `mappings/culturemech_residual_groundings.tsv` has two `ENVO:00002005`
  worklist rows: `Air` with 12 mentions across 12 recipes and `air` with 5
  mentions across 5 recipes. The record creation history and
  `occurrence_statistics` only account for the 12 uppercase `Air` mentions.
- A hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  found no `ENVO:00002005` rows, so the 12 current occurrences are not yet
  traceable through the same membership table used by the occurrence refresher.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, residual grounding/triage rows,
  generated indexes, and ignored aggregate backups.

## Completeness

- Mapping evidence, occurrence statistics, and curation history are populated.
- The lowercase `air` residual should be folded into this record or explicitly
  rejected before the occurrence count is complete.
- No CAS, formula, component, role, environmental context, discussion, or
  dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Fold the lowercase `air` CultureMech residual row into
  `data/ingredients/mapped/Air.yaml` and refresh membership/occurrence products
  so all 17 mentions are represented, or document why those 5 mentions are
  intentionally excluded.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Air.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
