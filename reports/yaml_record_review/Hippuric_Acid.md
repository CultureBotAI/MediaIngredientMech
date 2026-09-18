# `data/ingredients/mapped/Hippuric_Acid.yaml`

## Verdict

Pass. The CAS-derived `N-benzoylglycine` ChEBI identity, CAS RN, structure
fields, raw hippurate merge, surface-form synonym, and final SSSOM row are
internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Hippuric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:18089` with
  `ontology_mapping.ontology_id: CHEBI:18089`, label `N-benzoylglycine`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `495-69-2`, formula `C9H9NO3`, InChI
  `InChI=1S/C9H9NO3/c11-8(12)6-10-9(13)7-4-2-1-3-5-7/h1-5H,6H2,(H,10,13)(H,11,12)`,
  and SMILES `O=C(O)CNC(=O)c1ccccc1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hexanoate.yaml data/ingredients/mapped/Hexanol.yaml data/ingredients/mapped/Hippuric_Acid.yaml data/ingredients/mapped/Histamine.yaml data/ingredients/mapped/Hitachimycin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:18089`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1428`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1428`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:18089` as active `N-benzoylglycine`, with
  `Hippuric acid` and `Hippurate` as synonyms.
- PubChem resolves CAS RN `495-69-2` to `Hippuric Acid`, formula `C9H9NO3`,
  the same InChI, and an equivalent non-canonical SMILES.
- The final SSSOM exports `Hippurate`, `Hippuric acid (N-benzoylglycine)`, and
  `CAS:495-69-2` in `other`; all are resolving surface forms for the published
  subject.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hippuric_Acid` to `CHEBI:18089`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and row-review `CONFIRMED` decision.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, final SSSOM row,
  and synchronized aggregate entry are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
