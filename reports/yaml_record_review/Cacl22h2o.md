# `data/ingredients/mapped/Cacl22h2o.yaml`

## Verdict

Needs curation, minor. The duplicate calcium chloride dihydrate record is
correctly rejected and no longer emits a `MIM:Cacl22h2o` SSSOM row, but the
tombstone still carries live-record chemical and mineral-role fields after its
occurrences were transferred to `Cacl2_X_2_H2o`.

## Identity

- Reviewed record: `data/ingredients/mapped/Cacl22h2o.yaml`.
- Tombstone state: `identifier: CHEBI:86158`,
  `preferred_term: CaCl22H2O`, `mapping_status: REJECTED`, and
  `ontology_mapping.ontology_id: CHEBI:86158`.
- Direct OLS lookup for `CHEBI:86158` returns the active label
  `calcium chloride dihydrate`.
- PubChem resolves CAS `10035-04-8` to calcium chloride dihydrate, matching the
  local `Ca.2Cl.2H2O` formula, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ca_No32_X_4_H2o.yaml data/ingredients/mapped/Cacl2.yaml data/ingredients/mapped/Cacl22h2o.yaml data/ingredients/mapped/Cacl2_X_2_H2o.yaml data/ingredients/mapped/Cacl2_X_6_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cacl22h2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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

- Hidden/ignored-inclusive search over `data/curated`, `mappings`, `docs/data`,
  `reports`, `scripts`, `history`, and `.claude`, excluding bulky backups and
  generated review-report directories, found the rejected aggregate copy in
  `data/curated/mapped_ingredients.yaml`, the `MIM:Cacl22h2o_2` alias row in
  `mappings/mim_curie_aliases.tsv`, and no live `MIM:Cacl22h2o` row in
  `mappings/ingredient_mappings.sssom.tsv`.
- The 2026-08-20 `MERGED_INTO` curation event records that `CaCl22H2O` merged
  into `CaCl2 x 2 H2O` on the same `CHEBI:86158` identity and transferred its
  occurrences there.
- Minor gap: despite that tombstone transition, this rejected record still has
  calcium chloride dihydrate `chemical_properties` and a `MINERAL_SOURCE`
  nutritional role whose evidence text cites 2 old CultureMech occurrences.

## Completeness

- The duplicate no longer publishes its own SSSOM row and has 0/0 occurrence
  statistics.
- The active `data/ingredients/mapped/Cacl2_X_2_H2o.yaml` record owns the
  `CaCl22H2O` raw-text synonym and the current 6013/5959 occurrence count.

## Recommended Edits

- Minor: compact `data/ingredients/mapped/Cacl22h2o.yaml` to a pure rejected
  duplicate tombstone by removing the stale role and, if tombstones are not
  meant to carry duplicate structures, the copied `chemical_properties`; keep
  the merge history pointing to `data/ingredients/mapped/Cacl2_X_2_H2o.yaml`,
  then run `just sync-curated` and focused strict/SSSOM validation.
