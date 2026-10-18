# `data/ingredients/mapped/Feso4_X_7_H2o.yaml`

## Verdict

Pass. The canonical `FeSO4 x 7 H2O` record denotes iron(II) sulfate
heptahydrate exactly, has the hydrate-specific ChEBI and CAS identities, and
publishes only heptahydrate synonyms in final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Feso4_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:75836` with matching
  `ontology_mapping.ontology_id`, canonical label
  `iron(2+) sulfate heptahydrate`, source `CHEBI`, `mapping_quality:
  SYNONYM_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- `mappings/hydrate_review.tsv` marks the named heptahydrate and
  `CHEBI:75836` mapping as correct and high-confidence.
- PubChem lookup by CAS RN `7782-63-0` resolved to CID 62662 with formula
  `FeH14O11S` and the same heptahydrate InChI recorded under
  `chemical_properties`.
- `nutritional_roles.IRON_SOURCE` is supported by a `DATABASE_ENTRY` reference
  to CultureMech's original `Mineral source` role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Feso4.yaml data/ingredients/mapped/Feso4_X_5_H2o.yaml data/ingredients/mapped/Feso4_X_6_H2o.yaml data/ingredients/mapped/Feso4_X_7_H2o.yaml data/ingredients/mapped/Feso4_X_7h2o.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Feso4_X_7_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, supported iron-source role,
  duplicate-merge history, and 2,779 occurrence count as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Feso4_X_7_H2o` to `CHEBI:75836` with `skos:exactMatch`.
- The final SSSOM `other` tokens are spelling variants of `FeSO4.7H2O`,
  exact heptahydrate names, `iron(2+) sulfate--water (1/7)`, the merged
  `FeSO4 x 7H2O` label, and `CAS:7782-63-0`; all denote the same
  heptahydrate or its CAS RN.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for the FeSO4 hydrate
  labels found the active YAML, aggregate copy, final SSSOM row, hydrate review
  row, duplicate-merge provenance, label-index precedence tests, occurrence
  routing helpers, and ignored aggregate backups.

## Completeness

- The exact heptahydrate identity, hydrate-specific CAS RN, structure fields,
  supported iron-source role, ingredient type, occurrence counts, duplicate
  merge provenance, and accepted hydrate synonyms are populated.
- I found no consequential missing component, environment, discussion, or final
  SSSOM payload for this single hydrate.

## Recommended Edits

- None.
