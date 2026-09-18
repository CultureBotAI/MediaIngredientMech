# `data/ingredients/mapped/Heptadecane.yaml`

## Verdict

Pass. The exact `heptadecane` ChEBI identity, CultureMech occurrence count,
CAS RN, structure fields, ChEBI synonyms, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Heptadecane.yaml`.
- Identifier and grounding: `identifier: CHEBI:16148` with
  `ontology_mapping.ontology_id: CHEBI:16148`, label `heptadecane`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:16148`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `629-78-7`, formula `C17H36`, InChI
  `InChI=1S/C17H36/c1-3-5-7-9-11-13-15-17-16-14-12-10-8-6-4-2/h3-17H2,1-2H3`,
  and SMILES `CCCCCCCCCCCCCCCCC`.
- Occurrence statistics: `total_occurrences: 2` and `media_count: 2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hepes.yaml data/ingredients/mapped/Heptadecane.yaml data/ingredients/mapped/Heptadecanoic_Acid.yaml data/ingredients/mapped/Heptanoic_Acid.yaml data/ingredients/mapped/Heptanol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:16148`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1421`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1421`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:16148` as active `heptadecane`, with
  `CH3-[CH2]15-CH3`, `Heptadekan`, and `n-heptadecane` as synonyms.
- PubChem resolves CAS RN `629-78-7` to `Heptadecane`, formula `C17H36`, the
  same SMILES, and the same InChI.
- The final SSSOM exports only the three ChEBI synonyms above plus
  `CAS:629-78-7` in `other`, all valid for this exact subject.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Heptadecane`
  to `CHEBI:16148`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and row-review `CONFIRMED` decision.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  count, KG-Microbe node ID, final SSSOM row, and synchronized aggregate entry
  are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
