# `data/ingredients/mapped/Dimethyl_Sulfide.yaml`

## Verdict

Pass. The CultureBotHT record exact-matches active `CHEBI:17437` dimethyl
sulfide, the merged `Dimethylsulfide` raw label is a same-compound synonym,
and the final SSSOM row exports only true aliases plus `CAS:75-18-3`.

## Identity

- Reviewed record: `data/ingredients/mapped/Dimethyl_Sulfide.yaml`.
- Identifier and grounding: `identifier: CHEBI:17437` with
  `ontology_mapping.ontology_id: CHEBI:17437`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:17437` to active `dimethyl sulfide`, CAS xref
  `75-18-3`, formula `C2H6S`, InChI, SMILES, exact synonym
  `(METHYLSULFANYL)METHANE`, and related synonyms for the same compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dihydrostreptomycin.yaml data/ingredients/mapped/Dihydroxyacetone.yaml data/ingredients/mapped/Dimethyl_Disulfide.yaml data/ingredients/mapped/Dimethyl_Sulfide.yaml data/ingredients/mapped/Dimethyl_Sulfone.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dihydrostreptomycin.yaml data/ingredients/mapped/Dihydroxyacetone.yaml data/ingredients/mapped/Dimethyl_Disulfide.yaml data/ingredients/mapped/Dimethyl_Sulfide.yaml data/ingredients/mapped/Dimethyl_Sulfone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:38291 CHEBI:16016 CHEBI:4608 CHEBI:17437 CHEBI:9349`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:17437`.
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
  found the expected active record, generated/indexed copies, row-review rows,
  and two mixture records that use `CHEBI:17437` only as a component.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:17437` found `data/ingredients/mapped/Dimethyl_Sulfide.yaml` and the
  component-only `Formatedimethylsulfide.yaml` and `H2dimethylsulfide.yaml`
  records, with no duplicate exact dimethyl sulfide record.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:17437` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dimethyl_Sulfide` to `CHEBI:17437` with `skos:exactMatch`, canonical
  object label `dimethyl sulfide`, CHEBI object source, the exact ChEBI
  synonym, the merged `Dimethylsulfide` label, and `CAS:75-18-3`.

## Completeness

- CAS RN, formula, InChI, SMILES, curated synonym review, duplicate merge
  history, and row-review provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT record with no
  tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
