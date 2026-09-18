# `data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml`

## Verdict

Needs curation. The exact `CHEBI:30915` identity, CAS, ChEBI/PubChem
chemistry, CultureMech count, SSSOM row, and aggregate copy pass, but
`CARBON_SOURCE` and `ENERGY_SOURCE` are still provisional computational
predictions with no source-context evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30915` with
  `ontology_mapping.ontology_id: CHEBI:30915`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:30915` to
  `2-oxoglutaric acid` with formula `C5H6O5`, CAS `328-50-7`, SMILES
  `O=C(O)CCC(=O)C(=O)O`, and InChIKey `KPGXRSRHYNQIFN-UHFFFAOYSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml data/ingredients/mapped/Alpha-toxicarol_Dl.yaml data/ingredients/mapped/Alphaalpha-Trehalose.yaml data/ingredients/mapped/Althiomycin.yaml data/ingredients/mapped/Aluminium_Sulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned the canonical `2-oxoglutaric acid` label and expected
  2-ketoglutaric/oxoglutaric aliases for `CHEBI:30915`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:30915`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with the same 104 non-blocking
  plausibility warnings seen at corpus scope.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Alpha-ketoglutaric_Acid` to `CHEBI:30915` mapping.
- `mappings/culturemech_recipe_membership.tsv` contains seven `CHEBI:30915`
  rows, matching `occurrence_statistics.total_occurrences: 7`.
- `mappings/ingredient_mappings.sssom.tsv` row 381 maps
  `MIM:Alpha-ketoglutaric_Acid` to `CHEBI:30915` with `skos:exactMatch`, the
  `2026-08-30` CultureMech-alias provenance date, CAS `328-50-7`, and the
  expected exact/RAW source labels.
- The `a-Ketoglutaric acid` merge, `alpha-ketoglutamate` RAW_TEXT merge, and
  `alpha-ketoglutaric acid (100 mM).` CultureMech alias are explicitly
  described in history as absorbed surface forms of this acid record.
- The `CARBON_SOURCE` and `ENERGY_SOURCE` role facets cite computational
  predictions only; neither records evidence that alpha-ketoglutaric acid was a
  nutritional or energy substrate in a source recipe.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, row-review confirmation, residual alias row,
  seven CultureMech membership rows, stale/generated reports, and adjacent
  alpha-ketoglutarate salt records.

## Completeness

- CAS, formula, SMILES, InChI, occurrence statistics, mapping evidence, and
  `ingredient_type` are populated for the exact ChEBI identity.
- No role, component, environmental context, discussion, or dataset entry is
  otherwise required.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the unsupported provisional roles.

## Recommended Edits

- In `data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml`, either replace the
  `CARBON_SOURCE` and `ENERGY_SOURCE` computational predictions with
  source-specific evidence, or remove the unsupported role facets.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
