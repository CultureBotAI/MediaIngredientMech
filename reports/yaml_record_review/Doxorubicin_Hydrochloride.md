# `data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml`

## Verdict

Pass. The CultureBotHT identity exact-matches active `CHEBI:31522`
Doxorubicin hydrochloride, its CAS RN and structure match ChEBI and PubChem,
and the final SSSOM row is a clean exact match with `CAS:25316-40-9` in
`other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:31522` with
  `ontology_mapping.ontology_id: CHEBI:31522`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:31522` to active `Doxorubicin hydrochloride`,
  formula `C27H29NO11.HCl`, the expected InChI and SMILES, and CAS xref
  `25316-40-9`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Doxorubicin.yaml data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml data/ingredients/mapped/Doxycycline.yaml data/ingredients/mapped/Doxycycline_Hyclate.yaml data/ingredients/mapped/Dried_Bovine_Hemoglobin_BD_212392.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Doxorubicin.yaml data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml data/ingredients/mapped/Doxycycline.yaml data/ingredients/mapped/Doxycycline_Hyclate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4 CHEBI files; `Dried_Bovine_Hemoglobin_BD_212392.yaml` was
  skipped because `MICRO:` identifiers are outside this CHEBI/OBO-focused
  batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28748 CHEBI:31522 CHEBI:50845 CHEBI:34730`:
  returned the canonical ChEBI label, synonyms, CAS xref, formula, InChI,
  SMILES, charge, and mass for `CHEBI:31522`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `25316-40-9` to CID 443939 with formula `C27H30ClNO11`
  and the same InChIKey as the salt formula on `CHEBI:31522`.
- The hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:31522` and `25316-40-9` found only the active
  per-record YAML, row-review rows, and final SSSOM row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `CHEBI:31522` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Doxorubicin_Hydrochloride` to `CHEBI:31522` with `skos:exactMatch`,
  canonical object label `Doxorubicin hydrochloride`, CHEBI object source, and
  `CAS:25316-40-9`.

## Completeness

- CAS RN, formula, InChI, SMILES, and CultureBotHT provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT compound with no
  tracked CultureMech recipe memberships.
- Supplied forms, mixture components, nutritional roles, physicochemical roles,
  biological roles, and environmental contexts are correctly empty.

## Recommended Edits

- None.
