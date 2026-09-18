# `data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup resolves to active `CHEBI:89741` methyl
dihydrojasmonate, the stored CAS RN, formula, InChI, and SMILES match ChEBI,
and the final SSSOM row exports only `CAS:24851-98-7`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml`.
- Identifier and grounding: `identifier: CHEBI:89741` with
  `ontology_mapping.ontology_id: CHEBI:89741`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:89741` to active `Methyl dihydrojasmonate`, CAS
  xref `24851-98-7`, formula `C13H22O3`, InChI, SMILES, and related synonym
  `Dihydrojasmonic acid methyl ester`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydro_Azathymidine.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 4-record CHEBI subset; the local
  `kgmicrobe.compound:` placeholder record is outside Engine A's OBO prefix
  scope.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:89741`:
  returned the canonical ChEBI label, synonyms, CAS xref, formula, InChI,
  SMILES, charge, and mass for `CHEBI:89741`.
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
  `CHEBI:89741` found only
  `data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv`,
  `mappings/ingredient_mappings_synonym_enrich_review.tsv`, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` agree that the
  `CHEBI:89741` mapping needs no row-review action; the proposed
  `dihydrojasmonic acid, methyl ester` synonym is already represented by
  `preferred_term`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dihydrojasmonic_Acid_Methyl_Ester` to `CHEBI:89741` with
  `skos:exactMatch`, canonical object label `Methyl dihydrojasmonate`,
  CHEBI object source, and `CAS:24851-98-7`.

## Completeness

- CAS RN, formula, InChI, SMILES, CultureBotHT provenance, CAS lookup regrade
  history, and row-review provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT record with no
  tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
