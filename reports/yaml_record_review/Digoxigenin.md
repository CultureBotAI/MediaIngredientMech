# `data/ingredients/mapped/Digoxigenin.yaml`

## Verdict

Pass. The CultureBotHT record exact-matches active `CHEBI:42098` digoxigenin,
its CAS RN, formula, InChI, and SMILES agree with ChEBI, and the final SSSOM
row exports only the exact ChEBI synonym plus `CAS:1672-46-4`.

## Identity

- Reviewed record: `data/ingredients/mapped/Digoxigenin.yaml`.
- Identifier and grounding: `identifier: CHEBI:42098` with
  `ontology_mapping.ontology_id: CHEBI:42098`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:42098` to active `digoxigenin`, CAS xref
  `1672-46-4`, formula `C23H34O5`, InChI, SMILES, and exact synonym
  `3beta,12beta,14-trihydroxy-5beta-card-20(22)-enolide`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydro_Azathymidine.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 4-record CHEBI subset; the local
  `kgmicrobe.compound:` placeholder record is outside Engine A's OBO prefix
  scope.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27729 CHEBI:42098 CHEBI:132340 CHEBI:89741`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:42098`.
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
  `CHEBI:42098` found only `data/ingredients/mapped/Digoxigenin.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:42098` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Digoxigenin` to `CHEBI:42098` with `skos:exactMatch`, canonical object
  label `digoxigenin`, CHEBI object source, the exact ChEBI synonym, and
  `CAS:1672-46-4`.

## Completeness

- CAS RN, formula, InChI, SMILES, the ChEBI synonym, CultureBotHT provenance,
  and no-action row-review provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT record with no
  tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
