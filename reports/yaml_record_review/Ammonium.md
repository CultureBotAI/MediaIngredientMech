# `data/ingredients/mapped/Ammonium.yaml`

## Verdict

Needs curation. The exact `CHEBI:28938` ammonium identity, MicrobeDecoder
occurrence, `NH4+` synonym, chemistry, review-ingredients approval, SSSOM row,
and aggregate copy pass, but the three CultureMech `NH4+` residual mentions are
still absent from `mappings/culturemech_recipe_membership.tsv` and from the
record's `0/0` CultureMech counters.

## Identity

- Reviewed record: `data/ingredients/mapped/Ammonium.yaml`.
- Identifier and grounding: `identifier: CHEBI:28938` with
  `ontology_mapping.ontology_id: CHEBI:28938`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:28938` to `ammonium` with formula `H4N`, charge
  `+1`, SMILES `[H][N+]([H])([H])[H]`, InChIKey
  `QGZKDVFQNNGYKY-UHFFFAOYSA-O`, and `NH4+` as a related synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium.yaml data/ingredients/mapped/Ammonium_Acetate.yaml data/ingredients/mapped/Ammonium_Chloride_Nitrogen_Source.yaml data/ingredients/mapped/Ammonium_Molybdate_Tetrahydrate.yaml data/ingredients/mapped/Ammonium_Persulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned canonical `ammonium`, `NH4+`, and other ammonium aliases for
  `CHEBI:28938`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28938 CHEBI:62947 CHEBI:31206 CHEBI:91249 CHEBI:156543`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:28938`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:ammonium` in BacDive metabolite production and utilization
  columns with count `81`, matching `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved `Ammonium.yaml`
  after `CHEBI:28938` resolved locally with canonical label `ammonium`.
- `mappings/culturemech_residual_groundings.tsv` records three residual `NH4+`
  mentions across three recipes and grounds them to `CHEBI:28938`.
- `mappings/ingredient_mappings.sssom.tsv` row 398 maps `MIM:Ammonium` to
  `CHEBI:28938` with `skos:exactMatch`, the review-ingredients trailer, and
  `NH4+` as an exported source label.
- A hidden/ignored-inclusive search over
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:28938` row, so
  the three restored CultureMech residuals are not represented in refreshed
  recipe membership and the active YAML still reports `total_occurrences: 0`.

## Completeness

- Formula, SMILES, InChI, molecular weight, MicrobeDecoder occurrence, curation
  history, `NH4+` synonym, and `ingredient_type` are populated.
- The only consequential gap is synchronization of the three CultureMech
  residual `NH4+` mentions into `occurrence_statistics` and
  `mappings/culturemech_recipe_membership.tsv`.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the stale `0/0` CultureMech counters.

## Recommended Edits

- Refresh CultureMech membership and `occurrence_statistics` so the three
  residual `NH4+` recipes are represented on
  `data/ingredients/mapped/Ammonium.yaml` and
  `mappings/culturemech_recipe_membership.tsv`.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
