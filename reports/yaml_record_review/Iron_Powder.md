# `data/ingredients/mapped/Iron_Powder.yaml`

## Verdict

Pass. The record is an intentional `#631` rejected tombstone whose occurrences
were transferred to `Iron`, whose representative points at `CHEBI:82664`, and
whose duplicate final SSSOM row is absent.

## Identity

- Reviewed record: `data/ingredients/mapped/Iron_Powder.yaml`.
- Identifier and grounding: `identifier: CHEBI:82664` with
  `ontology_mapping.ontology_id: CHEBI:82664`, label `iron(0)`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: REJECTED`, and
  `representative: CHEBI:82664`.
- Chemical properties: CAS RN `7439-89-6`, formula `Fe`, InChI
  `InChI=1S/Fe`, and SMILES `[Fe]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Iron_Powder.yaml data/ingredients/mapped/Iron_Stock.yaml data/ingredients/mapped/Isepamicin.yaml data/ingredients/mapped/Isobutyl_Alcohol.yaml data/ingredients/mapped/Isobutyramide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI records.
  `Iron_Stock` was outside adapter scope because its primary identifier is a
  local `kgmicrobe.ingredient` CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1645`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1645`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:82664` as the active ChEBI class `iron(0)`, with CAS
  xref `7439-89-6`, formula `Fe`, InChI `InChI=1S/Fe`, SMILES `[Fe]`, and
  exact iron(0) aliases covering the retained kg-microbe labels.
- PubChem resolves CAS RN `7439-89-6` to formula `Fe` and the same InChI stored
  on the record.
- The final SSSOM contains no `MIM:Iron_Powder` row, so this rejected duplicate
  no longer publishes an independent mapping after its occurrences were merged
  into `Iron`.
- The stale `IRON_SOURCE` role and raw CultureMech role synonym remain on the
  rejected tombstone only; they do not generate a live SSSOM row or leak raw
  role text into a final `other` field.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate tombstone, docs projections, the final SSSOM survivor row on
  `MIM:Iron`, the element repair regression tests, and stale pre-`#631` review
  rows that no longer match the current final SSSOM.

## Completeness

- The rejected tombstone keeps the representative pointer, active iron(0)
  grounding, historical curation trail, aggregate copy, and zero occurrence
  count expected after the `#631` merge.
- A hidden and ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found no live `MIM:Iron_Powder` export.

## Recommended Edits

- None.
