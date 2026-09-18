# `data/ingredients/mapped/Caprolactam.yaml`

## Verdict

Pass. The CultureBotHT CAS record is exactly grounded to active
`CHEBI:28579` epsilon-caprolactam, and its CAS, formula, InChI, SMILES,
synonym, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Caprolactam.yaml`.
- Identifier and grounding: `identifier: CHEBI:28579`,
  `ontology_mapping.ontology_id: CHEBI:28579`,
  `ontology_label: epsilon-caprolactam`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:28579` returns active label
  `epsilon-caprolactam`, CAS `105-60-2`, and formula `C6H11NO`.
- PubChem resolves CAS `105-60-2` to CID `7768` with formula `C6H11NO` and
  InChI/SMILES matching the local `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Caprolactam.yaml data/ingredients/mapped/Caps_Buffer.yaml data/ingredients/mapped/Capsaicin.yaml data/ingredients/mapped/Capso.yaml data/ingredients/mapped/Carbenicillin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caprolactam.yaml data/ingredients/mapped/Caps_Buffer.yaml data/ingredients/mapped/Capsaicin.yaml data/ingredients/mapped/Capso.yaml data/ingredients/mapped/Carbenicillin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The source CAS `105-60-2` resolves to ChEBI and PubChem entries for
  epsilon-caprolactam, matching the local structure fields.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Caprolactam` SSSOM row with
  `azepan-2-one` and `CAS:105-60-2` in `other`, matching aggregate/docs rows,
  and the `CONFIRMED_NO_ACTION` row-review manifest entry.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, synonym,
  single-ingredient classification, SSSOM row, aggregate copy, and docs row are
  populated.
- No roles or media occurrences are asserted, which is coherent for this
  CultureBotHT-only source record.

## Recommended Edits

- None for this record.
