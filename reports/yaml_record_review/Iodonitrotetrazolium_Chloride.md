# `data/ingredients/mapped/Iodonitrotetrazolium_Chloride.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived exact ChEBI identity, structure fields, exact
systematic synonym, CAS alias, and final SSSOM row all describe
iodonitrotetrazolium chloride.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Iodonitrotetrazolium_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:75421` with
  `ontology_mapping.ontology_id: CHEBI:75421`, label
  `iodonitrotetrazolium chloride`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `146-68-9`, formula `C19H13IN5O2.Cl`, InChI
  `InChI=1S/C19H13IN5O2.ClH/c20-15-6-8-16(9-7-15)23-21-19(14-4-2-1-3-5-14)22-24(23)17-10-12-18(13-11-17)25(26)27;/h1-13H;1H/q+1;/p-1`,
  and SMILES
  `O=[N+]([O-])c1ccc(-n2nc(-c3ccccc3)n[n+]2-c2ccc(I)cc2)cc1.[Cl-]`.

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

- OLS4 resolves `CHEBI:75421` as active `iodonitrotetrazolium chloride`, with
  formula `C19H13IN5O2.Cl`, the same InChI and SMILES stored on the record, and
  the recorded systematic name as an exact ChEBI synonym.
- PubChem resolves CAS RN `146-68-9` to formula `C19H13ClIN5O2` and the same
  InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Iodonitrotetrazolium_Chloride` to `CHEBI:75421` and exports only the
  inspected exact synonym plus `CAS:146-68-9`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and existing
  OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
