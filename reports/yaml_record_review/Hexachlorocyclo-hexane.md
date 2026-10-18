# `data/ingredients/mapped/Hexachlorocyclo-hexane.yaml`

## Verdict

Pass. The exact `hexachlorocyclohexane` ChEBI identity, CAS RN, structure
fields, ChEBI synonyms, occurrence count, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Hexachlorocyclo-hexane.yaml`.
- Identifier and grounding: `identifier: CHEBI:24536` with
  `ontology_mapping.ontology_id: CHEBI:24536`, label
  `hexachlorocyclohexane`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `27154-44-5`, formula `C6H6Cl6`, InChI
  `InChI=1S/C6H6Cl6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-6H`, and SMILES
  `ClC1C(Cl)C(Cl)C(Cl)C(Cl)C1Cl`.
- Occurrence statistics: `total_occurrences: 3` and `media_count: 3`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hesperidin.yaml data/ingredients/mapped/Hexachlorocyclo-hexane.yaml data/ingredients/mapped/Hexadecane.yaml data/ingredients/mapped/Hexadecanoate.yaml data/ingredients/mapped/Hexane.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:24536`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1424`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1424`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:24536` as active `hexachlorocyclohexane`, with `BHC`,
  `HCH`, `Hexachlorcyclohexan`, `Hexachlorzyklohexan`,
  `1,2,3,4,5,6-hexachlorocyclohexane`, and plural
  `hexachlorocyclohexanes` as synonyms.
- PubChem resolves CAS RN `27154-44-5` to `Hexachlorocyclohexane`, formula
  `C6H6Cl6`, the same InChI, and an equivalent non-canonical SMILES.
- The final SSSOM exports only the supported ChEBI synonyms above plus
  `CAS:27154-44-5`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hexachlorocyclo-hexane` to `CHEBI:24536`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and the synonym-enrich review row that
  considered `Hexachlorocyclo-hexane` already represented.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  count, final SSSOM row, and synchronized aggregate entry are present and
  consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
