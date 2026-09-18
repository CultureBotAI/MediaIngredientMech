# `data/ingredients/mapped/Caffeine.yaml`

## Verdict

Pass. The CultureBotHT caffeine record is exactly grounded to `CHEBI:27732`
with matching CAS, formula, InChI, SMILES, SSSOM, and aggregate data.

## Identity

- Reviewed record: `data/ingredients/mapped/Caffeine.yaml`.
- Identifier and grounding: `identifier: CHEBI:27732`,
  `ontology_mapping.ontology_id: CHEBI:27732`,
  `ontology_label: caffeine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:27732` returns the active label `caffeine`.
- PubChem resolves CAS `58-08-2` to caffeine with formula `C8H10N4O2`, the same
  InChI as the local record, and an equivalent SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cadmium_Nitrate.yaml data/ingredients/mapped/Caffeic_Acid.yaml data/ingredients/mapped/Caffeine.yaml data/ingredients/mapped/Caffeine_Hydrobromide.yaml data/ingredients/mapped/Cahpo4.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caffeine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  and `reports`, excluding bulky backups and generated review-report
  directories, found the active SSSOM row, the exact aggregate copy, and the
  `CONFIRMED_NO_ACTION` row-review manifest entry.
- The SSSOM row maps `MIM:Caffeine` to `CHEBI:27732` with `skos:exactMatch` and
  includes the ChEBI synonym plus `CAS:58-08-2`.
- The record was created from CultureBotHT rather than CultureMech media
  occurrences, so 0/0 occurrence statistics are expected.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, ChEBI synonym,
  single-ingredient classification, SSSOM row, and aggregate copy are
  populated.
- No roles or occurrence memberships are asserted, and none are required for
  this CultureBotHT-only compound.

## Recommended Edits

- None for this record.
