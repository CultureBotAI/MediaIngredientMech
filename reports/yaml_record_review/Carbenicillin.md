# `data/ingredients/mapped/Carbenicillin.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:3393` carbenicillin identity,
structure fields, CultureBotHT occurrence, SSSOM row, and aggregate copy pass,
but the active `SELECTIVE_AGENT` role is still only a provisional name-pattern
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Carbenicillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:3393`,
  `ontology_mapping.ontology_id: CHEBI:3393`,
  `ontology_label: carbenicillin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3393` returns active label `carbenicillin`, CAS
  `4697-36-3`, and formula `C17H18N2O6S`, matching the local ChEBI-derived
  structure bundle.

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

- The source CultureBotHT row records one CultureBot medium, `Abx Rhodanos`,
  and the record correctly reports 1/1 occurrences.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Carbenicillin` SSSOM row,
  matching aggregate/docs rows, and the `CONFIRMED_NO_ACTION` row-review
  manifest entry.
- The `SELECTIVE_AGENT` role has only `reference_type:
  COMPUTATIONAL_PREDICTION` from a curated name-pattern rule and explicitly
  says review is recommended.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, ChEBI synonym,
  single-ingredient classification, occurrence count, SSSOM row, aggregate
  copy, and docs row are populated.
- Local ChEBI exposes CAS `4697-36-3`, but the source CultureBotHT CAS value
  was blank; leaving `cas_rn` unset is therefore a non-blocking optional gap.

## Recommended Edits

- In `data/ingredients/mapped/Carbenicillin.yaml`, replace the provisional
  `SELECTIVE_AGENT` role evidence with claim-level source evidence or remove
  the role until support is available.
- Regenerate `data/curated/mapped_ingredients.yaml`, docs data, and any role
  exports that consume the aggregate; prove the cleanup with strict validation
  and round-trip verification.
