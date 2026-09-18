# `data/ingredients/mapped/Cetrimonium_Bromide.yaml`

## Verdict

Pass. The CAS-derived cetrimonium bromide record is correctly grounded to
active `CHEBI:3567`, and its CAS, formula, InChI, SMILES, exact synonym,
surfactant role, zero occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cetrimonium_Bromide.yaml`.
- Identifier and grounding: `identifier: CHEBI:3567`,
  `ontology_mapping.ontology_id: CHEBI:3567`,
  `ontology_label: cetyltrimethylammonium bromide`,
  `ontology_source: CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3567` returns one active ChEBI term labelled
  `cetyltrimethylammonium bromide` with CAS `57-09-0`, formula `Br.C19H42N`,
  and the same InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cetocycline.yaml data/ingredients/mapped/Cetomacrogol_1000.yaml data/ingredients/mapped/Cetrimonium_Bromide.yaml data/ingredients/mapped/Chalcopyrite.yaml data/ingredients/mapped/Champamycin_B.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cetrimonium_Bromide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed. The same focused validator also passed for `Cetocycline`,
  `Cetomacrogol_1000`, and `Chalcopyrite`; `Champamycin_B` was skipped because
  its `kgmicrobe.compound` placeholder CURIE is a local registry ID outside
  Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Cetrimonium_Bromide` SSSOM row, the
  `CONFIRMED` row-review disposition, and matching aggregate and docs rows for
  `CHEBI:3567`.
- The active SSSOM row includes CAS `57-09-0` and the ChEBI-reviewed exact
  synonym already present in YAML.
- Direct OLS traversal of the `CHEBI:3567` `has_role` relation returns the
  active `CHEBI:35195` `surfactant` role, matching
  `physicochemical_roles.SURFACTANT`.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:3567` rows,
  matching the explicit 0/0 `occurrence_statistics`.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, exact synonym, ChEBI
  role, SSSOM row, aggregate copy, docs row, and zero occurrence count are
  populated and agree.
- The record has no component or environment assertions that need additional
  evidence.

## Recommended Edits

- None for this record.
