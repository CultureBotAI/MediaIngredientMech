# `data/ingredients/mapped/Capsaicin.yaml`

## Verdict

Pass. The CultureBotHT CAS record is exactly grounded to active `CHEBI:3374`
capsaicin, and its CAS, formula, InChI, SMILES, synonym, SSSOM row, and
aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Capsaicin.yaml`.
- Identifier and grounding: `identifier: CHEBI:3374`,
  `ontology_mapping.ontology_id: CHEBI:3374`,
  `ontology_label: capsaicin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3374` returns active label `capsaicin`, CAS
  `404-86-4`, and formula `C18H27NO3`.
- PubChem resolves CAS `404-86-4` to CID `1548943` with formula `C18H27NO3`
  and InChI/SMILES matching the local `chemical_properties`.

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

- The source CAS `404-86-4` resolves to the same structure represented by
  `CHEBI:3374`, and the ChEBI synonym in YAML is exported in the current SSSOM
  `other` field and docs label index.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Capsaicin` SSSOM row,
  matching aggregate/docs rows, and the `CONFIRMED_NO_ACTION` row-review
  manifest entry.
- The capsaicin/Zostrix labels wrongly present on `Calcium_Pantothenate` are
  not present on this capsaicin record; that is a Calcium_Pantothenate export
  defect rather than a defect in this exact mapping.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, synonym,
  single-ingredient classification, SSSOM row, aggregate copy, and docs row are
  populated.
- No roles or media occurrences are asserted, which is coherent for this
  CultureBotHT-only source record.

## Recommended Edits

- None for this record.
