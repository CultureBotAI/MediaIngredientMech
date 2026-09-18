# `data/ingredients/mapped/Dihydroxyacetone.yaml`

## Verdict

Needs curation. The CultureBotHT identity exact-matches active `CHEBI:16016`
dihydroxyacetone, its CAS RN and structure match ChEBI, and the final SSSOM
row exports only true ChEBI synonymy. The `CARBON_SOURCE` role is still only a
provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Dihydroxyacetone.yaml`.
- Identifier and grounding: `identifier: CHEBI:16016` with
  `ontology_mapping.ontology_id: CHEBI:16016`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:16016` to active `dihydroxyacetone`, CAS xref
  `96-26-4`, formula `C3H6O3`, InChI, SMILES, exact synonym
  `1,3-Dihydroxypropan-2-one`, and related synonyms including
  `Dihydroxyacetone` and `Glycerone`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dihydrostreptomycin.yaml data/ingredients/mapped/Dihydroxyacetone.yaml data/ingredients/mapped/Dimethyl_Disulfide.yaml data/ingredients/mapped/Dimethyl_Sulfide.yaml data/ingredients/mapped/Dimethyl_Sulfone.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dihydrostreptomycin.yaml data/ingredients/mapped/Dihydroxyacetone.yaml data/ingredients/mapped/Dimethyl_Disulfide.yaml data/ingredients/mapped/Dimethyl_Sulfide.yaml data/ingredients/mapped/Dimethyl_Sulfone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:38291 CHEBI:16016 CHEBI:4608 CHEBI:17437 CHEBI:9349`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:16016`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus
  plausibility warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record, generated/indexed copies, and row-review
  rows.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:16016` found only
  `data/ingredients/mapped/Dihydroxyacetone.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:16016` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dihydroxyacetone` to `CHEBI:16016` with `skos:exactMatch`, canonical
  object label `dihydroxyacetone`, CHEBI object source, the exact ChEBI
  synonym, and `CAS:96-26-4`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from the ChEBI
  `CHEBI:16646` carbohydrate ancestry closure. It is not source-backed.

## Completeness

- CAS RN, formula, InChI, SMILES, ChEBI synonym, CultureBotHT provenance, and
  row-review provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT record with no
  tracked CultureMech recipe memberships; supplied forms, mixture components,
  and environmental contexts are correctly empty.

## Recommended Edits

- Major: replace the `CARBON_SOURCE` computational role in
  `data/ingredients/mapped/Dihydroxyacetone.yaml` with source-backed role
  evidence scoped to dihydroxyacetone, or remove the role if no support is
  available; then synchronize `data/curated/mapped_ingredients.yaml`.
