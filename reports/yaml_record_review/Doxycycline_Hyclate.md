# `data/ingredients/mapped/Doxycycline_Hyclate.yaml`

## Verdict

Needs curation. The CultureBotHT identity exact-matches active `CHEBI:34730`
doxycycline hyclate, its CAS RN and aggregate structure match ChEBI and
PubChem, and the final SSSOM row is clean; the `SELECTIVE_AGENT` role is still
only a provisional name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Doxycycline_Hyclate.yaml`.
- Identifier and grounding: `identifier: CHEBI:34730` with
  `ontology_mapping.ontology_id: CHEBI:34730`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:34730` to active `doxycycline hyclate`, the
  hemiethanolate hemihydrate of doxycycline hydrochloride, with CAS xref
  `24390-14-5`, formula `2C22H25N2O8.C2H6O.2Cl.H2O`, the expected InChI and
  SMILES, and doxycycline hyclate synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Doxorubicin.yaml data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml data/ingredients/mapped/Doxycycline.yaml data/ingredients/mapped/Doxycycline_Hyclate.yaml data/ingredients/mapped/Dried_Bovine_Hemoglobin_BD_212392.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Doxorubicin.yaml data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml data/ingredients/mapped/Doxycycline.yaml data/ingredients/mapped/Doxycycline_Hyclate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4 CHEBI files; `Dried_Bovine_Hemoglobin_BD_212392.yaml` was
  skipped because `MICRO:` identifiers are outside this CHEBI/OBO-focused
  batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28748 CHEBI:31522 CHEBI:50845 CHEBI:34730`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref, formula,
  InChI, SMILES, charge, and mass for `CHEBI:34730`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `24390-14-5` to CID 54686183 with formula
  `C46H58Cl2N4O18` and the same aggregate InChIKey as `CHEBI:34730`.
- The hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:34730` and `24390-14-5` found only the active
  Doxycycline hyclate YAML, row-review rows, and final SSSOM row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `CHEBI:34730` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Doxycycline_Hyclate` to `CHEBI:34730` with `skos:exactMatch`,
  canonical object label `doxycycline hyclate`, CHEBI object source, and
  `CAS:24390-14-5`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists` and a
  provisional curator note. It is not source-backed.

## Completeness

- CAS RN, formula, InChI, SMILES, and CultureBotHT provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT compound with no
  tracked CultureMech recipe memberships.
- Supplied forms, mixture components, nutritional roles, biological roles, and
  environmental contexts are correctly empty.

## Recommended Edits

- Major: replace the `SELECTIVE_AGENT` computational role in
  `data/ingredients/mapped/Doxycycline_Hyclate.yaml` with source-backed role
  evidence scoped to doxycycline hyclate, or remove the role if no support is
  available; then synchronize `data/curated/mapped_ingredients.yaml`.
