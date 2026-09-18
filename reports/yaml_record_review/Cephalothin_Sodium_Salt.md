# `data/ingredients/mapped/Cephalothin_Sodium_Salt.yaml`

## Verdict

Needs curation; major issue. The CAS-derived cephalothin sodium identity is
correctly grounded to active `CHEBI:3542`, and its CAS, formula, InChI,
SMILES, zero occurrence count, SSSOM row, aggregate copy, and exact ChEBI
synonym agree. The remaining `SELECTIVE_AGENT` role is supported only by a
provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Cephalothin_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:3542`,
  `ontology_mapping.ontology_id: CHEBI:3542`,
  `ontology_label: cephalothin sodium`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3542` returns one active ChEBI term labelled
  `cephalothin sodium` with formula `C16H15N2O6S2.Na`, molecular mass
  `418.428`, and the same InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cephalothin_Sodium_Salt.yaml data/ingredients/mapped/Cephamycin_A.yaml data/ingredients/mapped/Cephradine.yaml data/ingredients/mapped/Cerulenin.yaml data/ingredients/mapped/Cesium_Chloride.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cephalothin_Sodium_Salt.yaml data/ingredients/mapped/Cephamycin_A.yaml data/ingredients/mapped/Cephradine.yaml data/ingredients/mapped/Cerulenin.yaml data/ingredients/mapped/Cesium_Chloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
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
  backups, found the active exact `MIM:Cephalothin_Sodium_Salt` SSSOM row, the
  `SYNONYM_ENRICH` row-review disposition, the synonym-enrichment
  `ALREADY_REPRESENTED` row, and matching aggregate/docs rows for
  `CHEBI:3542`.
- The active SSSOM row includes `CAS:58-71-9` and the ChEBI-reviewed exact
  synonym already present in YAML.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:3542` rows,
  which matches the explicit 0/0 `occurrence_statistics`.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The CAS-derived exact ChEBI identifier, CAS, formula, InChI, SMILES, exact
  synonym, SSSOM row, aggregate copy, docs row, and zero occurrence count are
  populated and agree.
- The record has no component, environment, or mechanistic assertions that need
  additional evidence.

## Recommended Edits

- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` with inspected
  evidence for cephalothin sodium as a selective agent in this media scope, or
  remove the role, then rerun strict validation, SSSOM QC, aggregate roundtrip,
  and `git diff --check`.
