# `data/ingredients/mapped/Heptadecanoic_Acid.yaml`

## Verdict

Pass. The exact `heptadecanoic acid` ChEBI identity, stripped CAS RN, margarinic
acid synonym, structure fields, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Heptadecanoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:32365` with
  `ontology_mapping.ontology_id: CHEBI:32365`, label `heptadecanoic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `506-12-7`, formula `C17H34O2`, InChI
  `InChI=1S/C17H34O2/c1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17(18)19/h2-16H2,1H3,(H,18,19)`,
  and SMILES `CCCCCCCCCCCCCCCCC(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hepes.yaml data/ingredients/mapped/Heptadecane.yaml data/ingredients/mapped/Heptadecanoic_Acid.yaml data/ingredients/mapped/Heptanoic_Acid.yaml data/ingredients/mapped/Heptanol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:32365`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1421`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1421`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:32365` as active `heptadecanoic acid`, with
  `margaric acid` as a synonym.
- PubChem resolves the stripped CAS RN `506-12-7` to `Heptadecanoic Acid`,
  formula `C17H34O2`, the same SMILES, and the same InChI.
- The final SSSOM exports `Margaric acid` and `CAS:506-12-7` in `other`; both
  are valid for this exact subject.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Heptadecanoic_Acid` to `CHEBI:32365`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and row-review `CONFIRMED` decision.

## Completeness

- The active ChEBI identifier, normalized CAS RN, formula, InChI, SMILES,
  final SSSOM row, and synchronized aggregate entry are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
