# `data/ingredients/mapped/Feso4.yaml`

## Verdict

Needs curation, with a major final-SSSOM synonym issue. The exact anhydrous
ferrous sulfate ChEBI identity, CAS-backed structure, supported
CultureMech iron-source role, and occurrence split after #652 pass, but a
malformed heptahydrate-derived token still exports as a synonym of anhydrous
`FeSO4`.

## Identity

- Reviewed record: `data/ingredients/mapped/Feso4.yaml`.
- Identifier and grounding: `identifier: CHEBI:75832` with matching
  `ontology_mapping.ontology_id`, canonical label
  `iron(2+) sulfate (anhydrous)`, source `CHEBI`, `mapping_quality:
  SYNONYM_MATCH`, `mapping_status: MAPPED`, `kg_microbe_node_id:
  CHEBI:75832`, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `7720-78-7` resolved to CID 24393 with formula
  `FeO4S` and the same anhydrous ferrous sulfate InChI recorded under
  `chemical_properties`.
- `nutritional_roles.IRON_SOURCE` is supported by a `DATABASE_ENTRY` reference
  to CultureMech's original `Mineral` role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Feso4.yaml data/ingredients/mapped/Feso4_X_5_H2o.yaml data/ingredients/mapped/Feso4_X_6_H2o.yaml data/ingredients/mapped/Feso4_X_7_H2o.yaml data/ingredients/mapped/Feso4_X_7h2o.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Feso4.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  anhydrous ChEBI identifier, CAS RN, formula, InChI, SMILES, kg-microbe node
  ID, supported iron-source role, and post-#652 occurrence counts as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Feso4` to
  `CHEBI:75832` with `skos:exactMatch`.
- Major: the final SSSOM `other` column exports `FeSO .7H O`, which is a
  malformed heptahydrate-like surface rather than an exact synonym of
  anhydrous ferrous sulfate.
- `mappings/hydrate_review.tsv` and `reports/hydrate_grounding.tsv` confirm
  that exact pentahydrate and hexahydrate labels moved off this anhydrous
  parent onto local hydrate identities, and that the heptahydrate has its own
  `CHEBI:75836` identity.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `MIM:Feso4`,
  `Feso4_X_*`, and `FeSO4` found the active YAML, aggregate copies, final
  SSSOM rows, hydrate review rows, OAK/OLS row-review provenance, the
  hydrate-family tests, component references in Wolfe's mineral mixes, and
  ignored aggregate backups.

## Completeness

- The exact anhydrous identity, CAS RN, structure fields, supported
  iron-source role, kg-microbe cross-reference, ingredient type, occurrence
  counts, and accepted exact synonyms are populated.
- The final SSSOM synonym payload needs filtering for the malformed
  hydrate-derived token.

## Recommended Edits

- Major: remove or retype `FeSO .7H O` in
  `data/ingredients/mapped/Feso4.yaml` so it no longer exports as an exact
  synonym, sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
