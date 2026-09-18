# `data/ingredients/mapped/Camptothecin.yaml`

## Verdict

Pass. The CultureBotHT CAS record is exactly grounded to active `CHEBI:27656`
camptothecin, and its CAS, formula, InChI, SMILES, synonym, SSSOM row, and
aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Camptothecin.yaml`.
- Identifier and grounding: `identifier: CHEBI:27656`,
  `ontology_mapping.ontology_id: CHEBI:27656`,
  `ontology_label: camptothecin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:27656` returns active label `camptothecin`,
  CAS `7689-03-4`, and formula `C20H16N2O4`.
- PubChem resolves CAS `7689-03-4` to formula `C20H16N2O4`, with InChI and
  isomeric SMILES equivalent to the local `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Camphomycin.yaml data/ingredients/mapped/Camptothecin.yaml data/ingredients/mapped/Canarius.yaml data/ingredients/mapped/Canavanine.yaml data/ingredients/mapped/Candimycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Camptothecin.yaml data/ingredients/mapped/Canavanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed both ChEBI records. Placeholder rows in the batch were skipped by the
  OBO-safe term wrapper.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The source CAS `7689-03-4` resolves to the same structure represented by
  `CHEBI:27656`, and the long ChEBI systematic synonym in YAML is exported in
  the current SSSOM `other` field and docs label index.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Camptothecin` SSSOM row,
  matching aggregate/docs rows, and the `CONFIRMED_NO_ACTION` row-review
  manifest entry.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, synonym,
  single-ingredient classification, SSSOM row, aggregate copy, and docs row are
  populated.
- No roles or media occurrences are asserted, which is coherent for this
  CultureBotHT-only source record.

## Recommended Edits

- None for this record.
