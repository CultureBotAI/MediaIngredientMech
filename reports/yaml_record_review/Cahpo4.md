# `data/ingredients/mapped/Cahpo4.yaml`

## Verdict

Pass. The calcium hydrogenphosphate record is exactly grounded to
`CHEBI:32596` with matching CAS, formula, InChI, SMILES, SSSOM, occurrences,
and aggregate data.

## Identity

- Reviewed record: `data/ingredients/mapped/Cahpo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:32596`,
  `ontology_mapping.ontology_id: CHEBI:32596`,
  `ontology_label: calcium hydrogenphosphate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:32596` returns the active label
  `calcium hydrogenphosphate`.
- PubChem resolves CAS `7757-93-9` to formula `CaHO4P`, the same salt
  represented locally as `Ca.HO4P`, with an InChI and SMILES matching the local
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cadmium_Nitrate.yaml data/ingredients/mapped/Caffeic_Acid.yaml data/ingredients/mapped/Caffeine.yaml data/ingredients/mapped/Caffeine_Hydrobromide.yaml data/ingredients/mapped/Cahpo4.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cahpo4.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  directories, found the active SSSOM row, the exact aggregate copy, four
  current `mappings/culturemech_recipe_membership.tsv` rows, and the
  `CONFIRMED_NO_ACTION` row-review manifest entry.
- The SSSOM row maps `MIM:Cahpo4` to `CHEBI:32596` with `skos:exactMatch` and
  includes the ChEBI/curated synonyms plus `CAS:7757-93-9`.
- The 2026-08-27 occurrence refresh records 4 total mentions in 4 recipes,
  matching the current membership rows.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, ChEBI synonyms,
  single-ingredient classification, 4/4 occurrence count, SSSOM row, and
  aggregate copy are populated.
- No raw hydrate, salt, or generic source labels were found on this record.

## Recommended Edits

- None for this record.
