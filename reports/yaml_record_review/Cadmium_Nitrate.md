# `data/ingredients/mapped/Cadmium_Nitrate.yaml`

## Verdict

Pass. The cadmium nitrate record is exactly grounded to `CHEBI:77732`; its
canonical label, anhydrous formula, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cadmium_Nitrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:77732`,
  `ontology_mapping.ontology_id: CHEBI:77732`,
  `ontology_label: cadmium nitrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:77732` returns the active label
  `cadmium nitrate`.
- The local ChEBI-derived formula `Cd.2NO3`, InChI, and SMILES describe the
  anhydrous cadmium dinitrate salt named by the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cadmium_Nitrate.yaml data/ingredients/mapped/Caffeic_Acid.yaml data/ingredients/mapped/Caffeine.yaml data/ingredients/mapped/Caffeine_Hydrobromide.yaml data/ingredients/mapped/Cahpo4.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cadmium_Nitrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `docs/data`, excluding bulky backups, found the active SSSOM
  row, the exact aggregate copy, and historical references from
  `Ca_No32.yaml` and `Ferric_Citrate_Monohydrate.yaml` where unrelated records
  were remapped away from this cadmium nitrate term.
- The SSSOM row maps `MIM:Cadmium_Nitrate` to `CHEBI:77732` with
  `skos:exactMatch` and publishes only `cadmium dinitrate` as a synonym.
- The active `CHEBI:64205` calcium nitrate and `CHEBI:144434` iron(III)
  citrate monohydrate rows preserve their own identities; the stale cadmium
  labels left on `Ca_No32` were reviewed separately and do not make this
  cadmium nitrate record ambiguous.

## Completeness

- The exact ChEBI identifier, canonical label, anhydrous formula, InChI,
  SMILES, single-ingredient classification, SSSOM row, 1/0 source count, and
  aggregate copy are populated.
- No cadmium nitrate tetrahydrate labels are resolving through this anhydrous
  record; that form has the separate `Cd_No32_X_4_H2o` record.

## Recommended Edits

- None for this record.
