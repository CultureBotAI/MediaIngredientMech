# `data/ingredients/mapped/Cellohexaose.yaml`

## Verdict

Needs curation; major issue. The CAS-derived cellohexaose identity is correctly
grounded to active `CHEBI:49533`, and its formula, InChI, SMILES, zero
occurrence count, SSSOM row, aggregate copy, and exact ChEBI synonyms agree.
The remaining `CARBON_SOURCE` role is supported only by a provisional ChEBI
ancestry prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Cellohexaose.yaml`.
- Identifier and grounding: `identifier: CHEBI:49533`,
  `ontology_mapping.ontology_id: CHEBI:49533`,
  `ontology_label: beta-D-cellohexaose`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:49533` returns one active ChEBI term labelled
  `beta-D-cellohexaose` with formula `C36H62O31`, molecular mass `990.861`,
  and the same InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cellohexaose.yaml data/ingredients/mapped/Cellopentaose.yaml data/ingredients/mapped/Cellostatin.yaml data/ingredients/mapped/Cellotetraose.yaml data/ingredients/mapped/Cellotriose.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cellohexaose.yaml data/ingredients/mapped/Cellopentaose.yaml data/ingredients/mapped/Cellotetraose.yaml data/ingredients/mapped/Cellotriose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external ChEBI records in this batch. The local
  `kgmicrobe.compound:cellostatin` placeholder was intentionally skipped because
  it is a local registry CURIE outside the validator's OAK/OLS prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact `MIM:Cellohexaose` SSSOM row, the
  `CONFIRMED` row-review disposition, and matching aggregate/docs rows for
  `CHEBI:49533`.
- The active SSSOM row includes `CAS:2478-35-5` and the two ChEBI-reviewed
  exact synonyms already present in YAML, including the compact
  `Glc(b1-4)...b-Glc` label.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:49533` rows,
  which matches the explicit 0/0 `occurrence_statistics`.
- `CARBON_SOURCE` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_chebi_ancestry` and is explicitly marked "Provisional role
  inferred from CHEBI is_a/has_role closure; review recommended."

## Completeness

- The CAS-derived exact ChEBI identifier, CAS, formula, InChI, SMILES, ChEBI
  exact synonyms, SSSOM row, aggregate copy, docs row, and zero occurrence count
  are populated and agree.
- The record has no component, environment, or mechanistic assertions that need
  additional evidence.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected
  evidence for cellohexaose as a carbon source in media, or remove the role,
  then rerun strict validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
