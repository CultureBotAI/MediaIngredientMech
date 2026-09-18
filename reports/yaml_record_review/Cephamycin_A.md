# `data/ingredients/mapped/Cephamycin_A.yaml`

## Verdict

Needs curation; major issue. The record correctly preserves the local
`kgmicrobe.compound:cephamycin_a` identity alongside a parent `CHEBI:55429`
cephamycin row, but it still carries generic parent class chemistry, exports
`produces: cephamycin A` as a synonym, and has only a provisional
`SELECTIVE_AGENT` role.

## Identity

- Reviewed record: `data/ingredients/mapped/Cephamycin_A.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:cephamycin_a`,
  `ontology_mapping.ontology_id: CHEBI:55429`,
  `ontology_label: cephamycin`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:55429` returns one active ChEBI parent class
  labelled `cephamycin` with generic formula `C8H7NO4SR2`, the same generic
  SMILES stored in `chemical_properties`, and no exact InChI.

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
  backups, found both active `MIM:Cephamycin_A` SSSOM rows, the
  `SYNONYM_ENRICH` row-review disposition, the expected kg-microbe registry
  disposition, the synonym-enrichment `ALREADY_REPRESENTED` row, and matching
  aggregate/docs rows for `kgmicrobe.compound:cephamycin_a`.
- The active SSSOM surface publishes a `skos:narrowMatch` to the active ChEBI
  parent class `CHEBI:55429` and a `skos:exactMatch` registry row to
  `kgmicrobe.compound:cephamycin_a`.
- The stored formula and SMILES describe the parent cephamycin R-group class,
  not an exact Cephamycin A structure.
- `produces: cephamycin A` is stored and exported as a `RAW_TEXT` synonym even
  though it is a KGX/source statement recovered from SSSOM `other`, not an
  ingredient label.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:cephamycin_a` rows, which matches the explicit 0/0
  `occurrence_statistics`.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The local kg-microbe identifier, ChEBI parent row, registry identity row,
  SSSOM rows, aggregate copy, docs row, and zero occurrence count are
  populated.
- Exact Cephamycin A structure fields are incomplete; the current
  `chemical_properties` block was inherited from `CHEBI:55429`.

## Recommended Edits

- Major: either replace `chemical_properties` with inspected exact Cephamycin A
  structure evidence, or remove the inherited parent formula, SMILES, and
  `data_source`.
- Major: remove or reject `produces: cephamycin A` so a KGX/source statement is
  not exported as a synonym.
- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` with inspected
  evidence for Cephamycin A as a selective agent in this media scope, or remove
  the role, then rerun strict validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
