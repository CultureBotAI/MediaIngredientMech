# `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`

## Verdict

Needs curation, major. The mapped calcium nitrate tetrahydrate identity,
`CHEBI:86159` grounding, CAS, chemical properties, SSSOM row, and aggregate copy
agree, but an exact CAS-qualified calcium nitrate tetrahydrate source form still
lives on the unmapped `Ca` placeholder instead of this active record.

## Identity

- Reviewed record: `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86159`,
  `ontology_mapping.ontology_id: CHEBI:86159`,
  `ontology_label: calcium nitrate tetrahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:86159` returns the active label
  `calcium nitrate tetrahydrate`.
- PubChem resolves CAS `13477-34-4` to formula `CaH8N2O10`, the same hydrate
  expressed locally as `Ca.4H2O.2NO3`, with an InChI and SMILES matching the
  local `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ca_No32_X_4_H2o.yaml data/ingredients/mapped/Cacl2.yaml data/ingredients/mapped/Cacl22h2o.yaml data/ingredients/mapped/Cacl2_X_2_H2o.yaml data/ingredients/mapped/Cacl2_X_6_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ca_No32_X_4_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  `mappings`, and `docs/data`, excluding only `data/curated/backups`, found the
  active SSSOM row in `mappings/ingredient_mappings.sssom.tsv`, the matching
  aggregate copy in `data/curated/mapped_ingredients.yaml`, an
  `OK_HYDRATE_TERM` row in `reports/hydrate_grounding.tsv`, and several stale
  `NOT_IN_MIM` rows for calcium nitrate tetrahydrate variants in
  `mappings/hydrate_review.tsv`.
- The SSSOM row maps `MIM:Ca_No32_X_4_H2o` to `CHEBI:86159` with
  `skos:exactMatch`; its `other` field includes all curated resolving synonyms
  and `CAS:13477-34-4`.
- Major gap: `data/ingredients/unmapped/Ca.yaml` still has 3/3 occurrences and
  one raw CultureMech synonym for the same CAS-qualified calcium nitrate
  tetrahydrate form. Its 2026-05-11 history even records that the source label
  is calcium nitrate tetrahydrate and should not be collapsed to elemental
  calcium, so this is a resolved live hydrate that has not been merged into
  `Ca_No32_X_4_H2o`.
- The latest active-record occurrence refresh predates the 2026-08-30
  CultureMech alias backfill, so the 199/199 count is also likely missing at
  least the one non-CAS-qualified tetrahydrate occurrence added by that pass.

## Completeness

- The ChEBI identifier, canonical label, CAS, hydrate synonyms,
  mineral-source role, single-ingredient classification, formula, InChI,
  SMILES, primary SSSOM row, and aggregate copy are populated.
- The CAS-qualified exact source label on `UNMAPPED_0049` should resolve to
  this record, not to a separate unmapped calcium placeholder.

## Recommended Edits

- Major: merge the calcium nitrate tetrahydrate raw label and three occurrences
  from `data/ingredients/unmapped/Ca.yaml` into
  `data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`, retire or update the stale
  `UNMAPPED_0049` placeholder, refresh occurrence statistics, and regenerate
  `mappings/ingredient_mappings.sssom.tsv` and `docs/data/label_index.csv`.
- Minor: refresh the hydrate-review report so the calcium nitrate tetrahydrate
  spellings now carried by this record no longer appear as `NOT_IN_MIM`.
