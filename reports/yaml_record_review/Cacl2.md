# `data/ingredients/mapped/Cacl2.yaml`

## Verdict

Needs curation, major. The exact anhydrous calcium dichloride mapping to
`CHEBI:3312`, CAS, formula, SSSOM row, and aggregate copy agree, but
`CaCl .6H O` remains an exact synonym and is exported as a resolving alias of
anhydrous calcium chloride.

## Identity

- Reviewed record: `data/ingredients/mapped/Cacl2.yaml`.
- Identifier and grounding: `identifier: CHEBI:3312`,
  `ontology_mapping.ontology_id: CHEBI:3312`,
  `ontology_label: calcium dichloride`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3312` returns the active label
  `calcium dichloride`.
- PubChem resolves CAS `10043-52-4` to anhydrous `CaCl2`, matching the local
  `Ca.2Cl` formula, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ca_No32_X_4_H2o.yaml data/ingredients/mapped/Cacl2.yaml data/ingredients/mapped/Cacl22h2o.yaml data/ingredients/mapped/Cacl2_X_2_H2o.yaml data/ingredients/mapped/Cacl2_X_6_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cacl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  `data/curated/mapped_ingredients.yaml`, and the exported
  `docs/data/label_index.csv` alias for `CaCl .6H O`.
- The SSSOM row maps `MIM:Cacl2` to `CHEBI:3312` with `skos:exactMatch` and
  carries `CAS:10043-52-4`, so the primary identity is consistent with the YAML.
- Major gap: `CaCl .6H O` is still `EXACT_SYNONYM` in the YAML, is still in
  the SSSOM `other` field, and still appears in `docs/data/label_index.csv` as
  a unique synonym for `CHEBI:3312`. The string is malformed, but the `.6H O`
  surface is hydrate-like and must not resolve as an exact alias of anhydrous
  calcium chloride.
- The same record correctly downgraded the other hidden hydrate labels to
  `REJECTED_LABEL` on 2026-09-12, so this is a one-label residual of that
  repair, not a broader anhydrous/hydrate conflation.

## Completeness

- The anhydrous ChEBI identifier, canonical label, CAS, formula, InChI, SMILES,
  mineral-source role, 1052/1052 occurrence count, SSSOM row, and aggregate
  copy are populated.
- The record is incomplete until all hydrate-like malformed aliases are
  non-resolving. The current resolver still sends `CaCl .6H O` to `CHEBI:3312`.

## Recommended Edits

- Major: change `CaCl .6H O` from `EXACT_SYNONYM` to `REJECTED_LABEL` in
  `data/ingredients/mapped/Cacl2.yaml`, or move it to a distinct local hydrate
  identity if source inspection proves it denotes a recoverable hydrate; then
  run `just sync-curated` and regenerate SSSOM/docs so
  `mappings/ingredient_mappings.sssom.tsv` and `docs/data/label_index.csv` stop
  publishing it as an anhydrous calcium chloride alias.
