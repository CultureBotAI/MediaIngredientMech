# `data/ingredients/mapped/Agave.yaml`

## Verdict

Pass with minor issues. The exact `FOODON:00005198` grounding and aggregate
copy pass; only the top-level import `notes` still say curator review is needed
after the FoodOn promotion.

## Identity

- Reviewed record: `data/ingredients/mapped/Agave.yaml`.
- Identifier and grounding: `identifier: FOODON:00005198` with
  `ontology_mapping.ontology_id: FOODON:00005198`, source `FOODON`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `FOODON:00005198` to canonical label `agave`.
- `ingredient_type: UNDEFINED_MIXTURE` is present and is appropriate for a
  FoodOn biological material rather than a defined small molecule.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Agave.yaml data/ingredients/mapped/Air-dried_Garden_Soil.yaml data/ingredients/mapped/Air.yaml data/ingredients/mapped/Al2_So43_X_18_H2o.yaml data/ingredients/mapped/Alanosine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Agave.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:foodon aliases FOODON:00005198`:
  returned canonical `agave`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The FoodOn label supports the exact Agave grounding that
  `resolve_unmapped` created from `UNMAPPED_0140`.
- `mappings/ingredient_mappings.sssom.tsv` row 355 maps `MIM:Agave` to
  `FOODON:00005198` with `skos:exactMatch` and the expected FoodOn trailer.
- The top-level `notes` still say the CultureBotHT import had no CAS or CHEBI
  mapping available and needed curator review even though the record now has an
  exact FoodOn mapping.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, generated indexes, and ignored
  aggregate backups.

## Completeness

- Curation history, FoodOn evidence, and `ingredient_type` are populated.
- No CAS, formula, component, role, environmental context, discussion, source
  occurrence, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Refresh the stale top-level `notes` in
  `data/ingredients/mapped/Agave.yaml`; no identity or SSSOM repair is needed.
