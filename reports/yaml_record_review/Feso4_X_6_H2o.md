# `data/ingredients/mapped/Feso4_X_6_H2o.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The hexahydrate now has a
local kg-microbe identity, curated `Fe.O4S.6H2O` formula, an asymmetric
anhydrous parent row, and clean same-hydrate `other` labels, but `IRON_SOURCE`
is still only a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Feso4_X_6_H2o.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:feso4_x_6_h2o`; `mapping_quality:
  NARROW_MATCH`; anhydrous parent `ontology_mapping.ontology_id:
  CHEBI:75832`; `mapping_status: MAPPED`; and `ingredient_type:
  SINGLE_INGREDIENT`.
- The #652 curator judgment preserves `FeSO4 x 6 H2O` as a formula-supported
  hydrate with no verified exact external ontology term, while keeping
  `CHEBI:75832` only as the anhydrous parent.
- `mappings/hydrate_review.tsv` marks the post-#652 hexahydrate identity as
  `LOCAL_IDENTITY_RETAINED` with medium confidence, and
  `reports/hydrate_grounding.tsv` reports `OK_LOCAL_REGISTRY_ID`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Feso4.yaml data/ingredients/mapped/Feso4_X_5_H2o.yaml data/ingredients/mapped/Feso4_X_6_H2o.yaml data/ingredients/mapped/Feso4_X_7_H2o.yaml data/ingredients/mapped/Feso4_X_7h2o.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Feso4_X_6_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the anhydrous ChEBI parent label.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, `NARROW_MATCH` anhydrous parent mapping, curated formula,
  rejected sibling-hydrate labels, and 23 occurrence counts as the per-record
  YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` rows publish
  `MIM:Feso4_X_6_H2o skos:narrowMatch CHEBI:75832` plus the required
  `skos:exactMatch kgmicrobe.compound:feso4_x_6_h2o` registry row.
- The final SSSOM `other` tokens are all alternate spellings of the
  hexahydrate; pentahydrate, heptahydrate, anhydrous, and malformed labels are
  rejected in YAML and no longer exported.
- Major: `nutritional_roles.IRON_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule. The role may be
  true, but it needs a source-backed CultureMech or literature assertion
  before being curated at 0.8 confidence.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for the FeSO4 hydrate
  labels found the active YAML, aggregate copy, final SSSOM registry and
  parent rows, hydrate review rows, hidden-synonym rejection tests, occurrence
  routing helpers, and ignored aggregate backups.

## Completeness

- The local hydrate identity, curated formula, rejected false synonyms,
  ingredient type, occurrence count, final SSSOM row pair, and true
  hexahydrate aliases are populated.
- The iron-source role needs non-provisional evidence.

## Recommended Edits

- Major: replace or remove the provisional `IRON_SOURCE` assignment in
  `data/ingredients/mapped/Feso4_X_6_H2o.yaml`; if a source supports it, attach
  `DATABASE_ENTRY` or literature evidence at the role. Then sync
  `data/curated/mapped_ingredients.yaml` and rerun strict validation plus the
  final SSSOM invariant gates.
