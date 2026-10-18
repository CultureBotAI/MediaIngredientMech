# `data/ingredients/mapped/D-trehalose_Dihydrate.yaml`

## Verdict

Needs curation. The hydrate-specific `CHEBI:232797` identity, CAS, formula,
structure, 15/15 CultureMech count, and final SSSOM synonym payload pass, but
both `CARBON_SOURCE` and `ENERGY_SOURCE` are provisional computational roles.

## Identity

- Reviewed record: `data/ingredients/mapped/D-trehalose_Dihydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:232797` with
  `ontology_mapping.ontology_id: CHEBI:232797`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:232797` to `trehalose dihydrate` with formula
  `C12H22O11.2H2O`, charge `0`, InChI, SMILES, CAS `6138-23-4`, and the same
  hydrate-specific IUPAC synonym published in SSSOM `other`.
- The mapping is to the hydrate term itself, not to an anhydrous trehalose
  parent.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-tagatose.yaml data/ingredients/mapped/D-threonine.yaml data/ingredients/mapped/D-trehalose_Dihydrate.yaml data/ingredients/mapped/D-tryptophan.yaml data/ingredients/mapped/D-valine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-tagatose.yaml data/ingredients/mapped/D-threonine.yaml data/ingredients/mapped/D-trehalose_Dihydrate.yaml data/ingredients/mapped/D-tryptophan.yaml data/ingredients/mapped/D-valine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16443 CHEBI:16398 CHEBI:232797 CHEBI:16296 CHEBI:27477`:
  returned formula, charge, CAS, InChI, SMILES, mass, and exact synonym data
  for `CHEBI:232797`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 15 rows for
  `CHEBI:232797`, matching `occurrence_statistics.media_count: 15` and
  `total_occurrences: 15`.
- `mappings/hydrate_review.tsv` marks D-Trehalose dihydrate as a high-confidence
  hydrate match with matching hydrate-specific CAS `6138-23-4`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-trehalose_Dihydrate` to `CHEBI:232797` with `skos:exactMatch`,
  object label `trehalose dihydrate`, CHEBI object source, the
  hydrate-specific IUPAC synonym, and `CAS:6138-23-4` in `other`.
- Both the `CARBON_SOURCE` and `ENERGY_SOURCE` roles are supported only by
  `COMPUTATIONAL_PREDICTION` evidence objects whose curator notes call them
  provisional and recommend review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record for `CHEBI:232797`; the only other
  active data hit is `NLDM_metabolites`, where trehalose dihydrate is a mixture
  component.
- CAS, formula, InChI, SMILES, occurrence statistics, and hydrate-specific
  synonyms are populated.
- No mixture decomposition is required for the free trehalose dihydrate record.

## Recommended Edits

- In `data/ingredients/mapped/D-trehalose_Dihydrate.yaml`, remove the
  provisional `CARBON_SOURCE` and `ENERGY_SOURCE` roles or replace their
  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level evidence.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-trehalose_Dihydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
