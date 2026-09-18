# `data/ingredients/mapped/Dopamine_Hydrochloride.yaml`

## Verdict

Pass. The CultureBotHT identity exact-matches active `CHEBI:4698` Dopamine
hydrochloride, its CAS RN and structure match ChEBI and PubChem, and the final
SSSOM row is a clean exact match with `CAS:62-31-7` in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Dopamine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:4698` with
  `ontology_mapping.ontology_id: CHEBI:4698`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:4698` to active `Dopamine hydrochloride`, formula
  `C8H11NO2.HCl`, the expected InChI and SMILES, and CAS xref `62-31-7`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dodecanol.yaml data/ingredients/mapped/Dopamine_Hydrochloride.yaml data/ingredients/mapped/Dopsisamine.yaml data/ingredients/mapped/Doripenem.yaml data/ingredients/mapped/Dotriacontane.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dodecanol.yaml data/ingredients/mapped/Dopamine_Hydrochloride.yaml data/ingredients/mapped/Doripenem.yaml data/ingredients/mapped/Dotriacontane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4 CHEBI files; `Dopsisamine.yaml` was skipped because `mesh:`
  identifiers are outside this CHEBI/OBO-focused batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:23866 CHEBI:4698 CHEBI:135928 CHEBI:36020`:
  returned the canonical ChEBI label, synonyms, CAS xref, formula, InChI,
  SMILES, charge, and mass for `CHEBI:4698`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `62-31-7` to CID 65340 with formula `C8H12ClNO2` and the
  same InChIKey as the salt formula on `CHEBI:4698`.
- The hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:4698` and `62-31-7` found only the active per-record
  YAML, row-review rows, and final SSSOM row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `CHEBI:4698` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dopamine_Hydrochloride` to `CHEBI:4698` with `skos:exactMatch`,
  canonical object label `Dopamine hydrochloride`, CHEBI object source, and
  `CAS:62-31-7`.

## Completeness

- CAS RN, formula, InChI, SMILES, and CultureBotHT provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT compound with no
  tracked CultureMech recipe memberships.
- Supplied forms, mixture components, nutritional roles, physicochemical roles,
  biological roles, and environmental contexts are correctly empty.

## Recommended Edits

- None.
