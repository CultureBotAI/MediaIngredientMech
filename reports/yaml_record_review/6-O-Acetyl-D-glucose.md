# `data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:17901` identity, exact synonym,
chemistry, SSSOM row, and aggregate copy pass, but the carbon-source and
energy-source roles are only provisional computational assertions.

## Identity

- Reviewed record: `data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml`.
- Identifier and grounding: `identifier: CHEBI:17901` with
  `ontology_mapping.ontology_id: CHEBI:17901`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:17901` to
  `6-O-acetyl-D-glucose` with formula `C8H14O7`, the stored SMILES, and the
  stored InChI.
- Local OAK metadata carries the same formula, structure strings, mass, and
  exact synonym `6-O-acetyl-D-glucopyranose`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml data/ingredients/mapped/6-Pentyl-2H-pyran-2-one.yaml data/ingredients/mapped/6-deoxy-d-galactose.yaml data/ingredients/mapped/6-hydroxypyridine-3-carboxylic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  returned the official exact and related synonym set for `CHEBI:17901`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  returned the expected ChEBI formula, structure strings, and mass for
  `CHEBI:17901`.

## Evidence

- The active ChEBI term, formula, SMILES, InChI, and exact ChEBI synonym
  support the 6-O-acetyl-D-glucose identity.
- The SSSOM row maps `MIM:6-O-Acetyl-D-glucose` to `CHEBI:17901` with
  `skos:exactMatch`, `6-O-acetyl-D-glucopyranose|CAS:7286-45-5` in `other`,
  and confirmed OAK/OLS review provenance.
- The `CARBON_SOURCE` and `ENERGY_SOURCE` roles are asserted only from
  `COMPUTATIONAL_PREDICTION` entries that both say review is recommended. No
  inspected occurrence or source entry in the record supports either role for
  6-O-acetyl-D-glucose.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, source review confirmation, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No components, source occurrences, environmental context, or discussion
  entries need review.

## Recommended Edits

- In `data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml`, either remove the
  provisional `CARBON_SOURCE` and `ENERGY_SOURCE` roles or replace the
  computational placeholders with source-backed evidence scoped to
  6-O-acetyl-D-glucose.
- Rebuild `data/curated/mapped_ingredients.yaml` and rerun strict validation,
  SSSOM invariants, and the id/label correspondence gate after the role edit.
