# `data/ingredients/mapped/Hexadecane.yaml`

## Verdict

Needs curation. The exact `hexadecane` ChEBI identity, CAS RN, structure fields,
ChEBI synonyms, occurrence count, and final SSSOM row pass, but
`nutritional_roles.CARBON_SOURCE` is still only a provisional in-session
computational assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Hexadecane.yaml`.
- Identifier and grounding: `identifier: CHEBI:45296` with
  `ontology_mapping.ontology_id: CHEBI:45296`, label `hexadecane`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:45296`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `544-76-3`, formula `C16H34`, InChI
  `InChI=1S/C16H34/c1-3-5-7-9-11-13-15-16-14-12-10-8-6-4-2/h3-16H2,1-2H3`,
  and SMILES `CCCCCCCCCCCCCCCC`.
- Occurrence statistics: `total_occurrences: 21` and `media_count: 21`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hesperidin.yaml data/ingredients/mapped/Hexachlorocyclo-hexane.yaml data/ingredients/mapped/Hexadecane.yaml data/ingredients/mapped/Hexadecanoate.yaml data/ingredients/mapped/Hexane.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:45296`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1424`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1424`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:45296` as active `hexadecane`, with the stored synonyms
  `CH3-[CH2]14-CH3`, `Cetan`, `Hexadekan`, `Zetan`, `cetane`, `n-cetane`, and
  `n-hexadecane`.
- PubChem resolves CAS RN `544-76-3` to `Hexadecane`, formula `C16H34`, the
  same SMILES, and the same InChI.
- The raw `Role: Carbon source` synonym is correctly filtered from the final
  SSSOM, while the ChEBI synonyms and `CAS:544-76-3` are exported in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from in-session Claude reasoning and no
  inspected CultureMech role row or literature citation that supports
  hexadecane as a carbon source in the asserted scope.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hexadecane` to
  `CHEBI:45296`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  count, KG-Microbe node ID, final SSSOM row, and synchronized aggregate entry
  are present and consistent.
- The record is incomplete until the carbon-source role is either backed by
  claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` unless an inspected
  CultureMech source row or literature source can support hexadecane as a
  carbon source, then rerun strict, term, round-trip, component, id-label, and
  SSSOM validation.
