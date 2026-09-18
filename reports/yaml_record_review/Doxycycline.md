# `data/ingredients/mapped/Doxycycline.yaml`

## Verdict

Pass. The MicrobeDecoder antibiotic identity exact-matches active
`CHEBI:50845` doxycycline, its formula and structure agree with the ChEBI term,
and the final SSSOM row is a clean exact match with no noisy synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Doxycycline.yaml`.
- Identifier and grounding: `identifier: CHEBI:50845` with
  `ontology_mapping.ontology_id: CHEBI:50845`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 68 MicrobeDecoder source
  occurrences.
- Local OAK resolves `CHEBI:50845` to active `doxycycline`, formula
  `C22H24N2O8`, the expected InChI and SMILES, CAS xref `564-25-0`, and
  doxycycline synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Doxorubicin.yaml data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml data/ingredients/mapped/Doxycycline.yaml data/ingredients/mapped/Doxycycline_Hyclate.yaml data/ingredients/mapped/Dried_Bovine_Hemoglobin_BD_212392.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Doxorubicin.yaml data/ingredients/mapped/Doxorubicin_Hydrochloride.yaml data/ingredients/mapped/Doxycycline.yaml data/ingredients/mapped/Doxycycline_Hyclate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4 CHEBI files; `Dried_Bovine_Hemoglobin_BD_212392.yaml` was
  skipped because `MICRO:` identifiers are outside this CHEBI/OBO-focused
  batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28748 CHEBI:31522 CHEBI:50845 CHEBI:34730`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref, formula,
  InChI, SMILES, charge, and mass for `CHEBI:50845`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:50845` found only the active Doxycycline YAML, its
  MicrobeDecoder approval row, and its final SSSOM row.
- `mappings/microbedecoder_auto_mapped_review.tsv` records this ChEBI lexical
  match as `APPROVED`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Doxycycline` to `CHEBI:50845` with `skos:exactMatch`, canonical object
  label `doxycycline`, CHEBI object source, and no `other` tokens.

## Completeness

- Formula, InChI, SMILES, molecular weight, ChEBI/PubChem structure provenance,
  and MicrobeDecoder source occurrences are populated.
- CAS RN, supplied forms, mixture components, nutritional roles,
  physicochemical roles, biological roles, and environmental contexts are
  correctly empty.

## Recommended Edits

- None.
