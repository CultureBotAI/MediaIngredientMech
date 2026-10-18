# `data/ingredients/mapped/Irigenin.yaml`

## Verdict

Pass. The CultureBotHT exact ChEBI identity, CAS RN, structure fields, empty
synonym list, and final SSSOM row all describe irigenin.

## Identity

- Reviewed record: `data/ingredients/mapped/Irigenin.yaml`.
- Identifier and grounding: `identifier: CHEBI:81409` with
  `ontology_mapping.ontology_id: CHEBI:81409`, label `irigenin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `548-76-5`, formula `C18H16O8`, InChI
  `InChI=1S/C18H16O8/c1-23-13-5-8(4-10(19)17(13)24-2)9-7-26-12-6-11(20)18(25-3)16(22)14(12)15(9)21/h4-7,19-20,22H,1-3H3`,
  and SMILES `COc1cc(-c2coc3cc(O)c(OC)c(O)c3c2=O)cc(O)c1OC`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Iodide.yaml data/ingredients/mapped/Iodonitrotetrazolium_Chloride.yaml data/ingredients/mapped/Irgasan.yaml data/ingredients/mapped/Irigenin.yaml data/ingredients/mapped/Iron.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1620`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1620`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:81409` as the active ChEBI class `irigenin`, with
  formula `C18H16O8` and the same InChI and SMILES stored on the record.
- PubChem resolves CAS RN `548-76-5` to formula `C18H16O8` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Irigenin` to
  `CHEBI:81409` and exports only `CAS:548-76-5` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and existing
  OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, aggregate copy,
  and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
