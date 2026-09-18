# `data/ingredients/mapped/Impenum_Monohydrate.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup grounds the source label to active
`CHEBI:51799` imipenem hydrate, the CAS RN, hydrate structure, ChEBI synonym,
and final SSSOM row are consistent, and the own-identifier exact SSSOM row
follows the current CAS lookup grading rule.

## Identity

- Reviewed record: `data/ingredients/mapped/Impenum_Monohydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:51799` with
  `ontology_mapping.ontology_id: CHEBI:51799`, label `imipenem hydrate`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `74431-23-5`, formula `C12H17N3O4S.H2O`,
  InChI
  `InChI=1S/C12H17N3O4S.H2O/c1-6(16)9-7-4-8(20-3-2-14-5-13)10(12(18)19)15(7)11(9)17;/h5-7,9,16H,2-4H2,1H3,(H2,13,14)(H,18,19);1H2/t6-,7-,9-;/m1./s1`,
  and SMILES
  `[H]C(=N)NCCSC1=C(C(=O)O)N2C(=O)[C@]([H])([C@@H](C)O)[C@@]2([H])C1.[H]O[H]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Impenum_Monohydrate.yaml data/ingredients/mapped/Indigocarmine.yaml data/ingredients/mapped/Indochrome.yaml data/ingredients/mapped/Indole-3-acetate.yaml data/ingredients/mapped/Indole-3-butyric_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4-file CHEBI/OBO subset;
  `Indochrome` was outside adapter scope because it uses a local
  `kgmicrobe.compound` identifier.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1545`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1545`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:51799` as the active ChEBI class `imipenem hydrate`,
  with CAS xref `74431-23-5`, formula `C12H17N3O4S.H2O`, and the same InChI
  and SMILES stored on the record.
- PubChem resolves CAS RN `74431-23-5` to a hydrate compound with the same
  imipenem-hydrate InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Impenum_Monohydrate` to `CHEBI:51799` and exports only the inspected
  ChEBI synonym plus `CAS:74431-23-5` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and synonym-enrichment
  row review marking the proposed text already represented.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
