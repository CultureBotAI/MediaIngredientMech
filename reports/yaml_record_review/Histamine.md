# `data/ingredients/mapped/Histamine.yaml`

## Verdict

Pass. The exact `histamine` ChEBI identity, CAS RN, structure fields, ChEBI
synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Histamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18295` with
  `ontology_mapping.ontology_id: CHEBI:18295`, label `histamine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `51-45-6`, formula `C5H9N3`, InChI
  `InChI=1S/C5H9N3/c6-2-1-5-3-7-4-8-5/h3-4H,1-2,6H2,(H,7,8)`, and SMILES
  `NCCc1cncn1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hexanoate.yaml data/ingredients/mapped/Hexanol.yaml data/ingredients/mapped/Hippuric_Acid.yaml data/ingredients/mapped/Histamine.yaml data/ingredients/mapped/Hitachimycin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:18295`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1428`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1428`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:18295` as active `histamine`, with
  `2-(1H-imidazol-4-yl)ethanamine` as a synonym.
- PubChem resolves CAS RN `51-45-6` to `Histamine`, formula `C5H9N3`, the same
  InChI, and an equivalent non-canonical SMILES.
- The final SSSOM exports the stored ChEBI synonym plus `CAS:51-45-6`; both
  are valid exact tokens for this subject.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Histamine` to
  `CHEBI:18295`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and row-review `CONFIRMED` decision.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, synonym, final
  SSSOM row, and synchronized aggregate entry are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
