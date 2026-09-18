# `data/ingredients/mapped/Calcium.yaml`

## Verdict

Pass. `Calcium.yaml` is a rejected duplicate tombstone that now points at the
surviving calcium(2+) record and no longer publishes an atom-grounded SSSOM row.

## Identity

- Reviewed record: `data/ingredients/mapped/Calcium.yaml`.
- Identifier and representative: both `identifier` and `representative` are
  `CHEBI:29108`.
- The record is `mapping_status: REJECTED` with 0 total occurrences and 0 media
  occurrences after the 2026-09-11 `fix_element_atom_overclaims` merge into
  `Calcium(2+)`.
- The retained ontology mapping points to the active `CHEBI:29108`
  `calcium(2+)` target and records the curator judgement that the CultureMech
  source rows carried KEGG `ca2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py 'data/ingredients/mapped/Calcium(2).yaml' data/ingredients/mapped/Calcium.yaml data/ingredients/mapped/Calcium_Chloride.yaml data/ingredients/mapped/Calcium_D-Pantothenate.yaml data/ingredients/mapped/Calcium_Pantothenate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data 'data/ingredients/mapped/Calcium(2).yaml' data/ingredients/mapped/Calcium.yaml data/ingredients/mapped/Calcium_Chloride.yaml data/ingredients/mapped/Calcium_D-Pantothenate.yaml data/ingredients/mapped/Calcium_Pantothenate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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

- Direct OLS lookup confirms `CHEBI:29108` is the active calcium(2+) ChEBI term.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found no active `MIM:Calcium` row in
  `mappings/ingredient_mappings.sssom.tsv`; the only live SSSOM row for this
  repaired identity is `MIM:Calcium~282~29`.
- The aggregate and docs rows keep `Calcium` as a rejected duplicate with 0/0
  occurrences, matching the per-record tombstone.

## Completeness

- The tombstone has no synonyms, chemistry, roles, or stale occurrence counts
  left after the merge.
- The append-only history keeps the original `CHEBI:22984` calcium-atom import
  and records the exact 2026-09-11 merge reason, so the status transition is
  traceable.

## Recommended Edits

- None for this record.
