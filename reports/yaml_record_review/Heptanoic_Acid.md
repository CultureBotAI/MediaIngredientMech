# `data/ingredients/mapped/Heptanoic_Acid.yaml`

## Verdict

Pass. The exact `heptanoic acid` ChEBI identity, CAS RN, structure fields, and
final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Heptanoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:45571` with
  `ontology_mapping.ontology_id: CHEBI:45571`, label `heptanoic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `111-14-8`, formula `C7H14O2`, InChI
  `InChI=1S/C7H14O2/c1-2-3-4-5-6-7(8)9/h2-6H2,1H3,(H,8,9)`, and SMILES
  `CCCCCCC(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hepes.yaml data/ingredients/mapped/Heptadecane.yaml data/ingredients/mapped/Heptadecanoic_Acid.yaml data/ingredients/mapped/Heptanoic_Acid.yaml data/ingredients/mapped/Heptanol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:45571`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1421`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1421`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:45571` as active `heptanoic acid`.
- PubChem resolves CAS RN `111-14-8` to `Heptanoic Acid`, formula `C7H14O2`,
  the same SMILES, and the same InChI.
- The final SSSOM exports only `CAS:111-14-8` in `other`, matching
  `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Heptanoic_Acid` to `CHEBI:45571`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and row-review `CONFIRMED` decision.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, final SSSOM row,
  and synchronized aggregate entry are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
