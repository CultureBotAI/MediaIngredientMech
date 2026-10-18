# `data/ingredients/mapped/Calcium(2).yaml`

## Verdict

Pass. The surviving calcium record is exactly grounded to `CHEBI:29108`
`calcium(2+)`, carries the absorbed CultureMech `Calcium` surface form as raw
text, and publishes a single active SSSOM row for the calcium(2+) ion.

## Identity

- Reviewed record: `data/ingredients/mapped/Calcium(2).yaml`.
- Identifier and grounding: `identifier: CHEBI:29108`,
  `ontology_mapping.ontology_id: CHEBI:29108`,
  `ontology_label: calcium(2+)`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:29108` returns the active ChEBI label
  `calcium(2+)`, formula `Ca`, charge 2, InChI `InChI=1S/Ca/q+2`, and SMILES
  `[Ca+2]`, matching the local structure fields.

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

- The 2026-09-11 `fix_element_atom_overclaims` event explains the semantic
  repair: the source `Calcium` rows carried KEGG `ca2`, so those 2
  CultureMech occurrences were moved from the ChEBI calcium-atom term to
  `CHEBI:29108`.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active
  `MIM:Calcium~282~29 -> CHEBI:29108` SSSOM row with `Calcium` in `other`.
- The same search found the older `CHEBI:22984` calcium-atom target only in the
  historical residual audit trail for `Calcium`/`Ca`, not as a live SSSOM row
  for this record.

## Completeness

- Formula, charge-specific InChI, SMILES, exact ChEBI grounding, occurrence
  count 2/2, MicrobeDecoder provenance, aggregate copy, docs row, and SSSOM row
  are populated and agree.
- No hydrate, salt, or neutral-atom alias remains on this active calcium(2+)
  record.

## Recommended Edits

- None for this record.
