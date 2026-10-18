# `data/ingredients/mapped/Cacl2_X_6_H2o.yaml`

## Verdict

Pass. The calcium chloride hexahydrate identity, `CHEBI:91243` exact mapping,
CAS, hydrate synonyms, corrected formula, SSSOM row, occurrence count, and
aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cacl2_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:91243`,
  `ontology_mapping.ontology_id: CHEBI:91243`,
  `ontology_label: calcium chloride hexahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:91243` returns the active label
  `calcium chloride hexahydrate`.
- PubChem resolves CAS `7774-34-7` to calcium chloride hexahydrate, matching
  the local `Ca.2Cl.6H2O` formula, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ca_No32_X_4_H2o.yaml data/ingredients/mapped/Cacl2.yaml data/ingredients/mapped/Cacl22h2o.yaml data/ingredients/mapped/Cacl2_X_2_H2o.yaml data/ingredients/mapped/Cacl2_X_6_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cacl2_X_6_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  generated review-report directories, found the active SSSOM row in
  `mappings/ingredient_mappings.sssom.tsv`, the exact aggregate copy in
  `data/curated/mapped_ingredients.yaml`, an `OK_HYDRATE_TERM` row in
  `reports/hydrate_grounding.tsv`, and the
  `CONFIRMED_NO_ACTION` row-review manifest entry for this mapping.
- The SSSOM row maps `MIM:Cacl2_X_6_H2o` to `CHEBI:91243` with
  `skos:exactMatch`, carries `CAS:7774-34-7`, and publishes only hexahydrate
  source forms.
- The 2026-08-13 `fix_scrambled_hydrate_cas` event replaced the inherited
  anhydrous CAS with the hexahydrate-specific ChEBI xref, and the 2026-08-27
  occurrence refresh records 70/70 occurrences.

## Completeness

- The exact ChEBI identifier, canonical label, hydrate-specific CAS, formula,
  InChI, SMILES, raw CultureMech role surface, mineral-source role, occurrence
  statistics, SSSOM row, and aggregate copy are populated.
- No exact label or SSSOM alias inspected in this pass points at anhydrous
  calcium chloride, calcium chloride dihydrate, or the unresolved heptahydrate
  identity.

## Recommended Edits

- None for this record.
