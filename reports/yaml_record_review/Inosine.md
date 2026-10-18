# `data/ingredients/mapped/Inosine.yaml`

## Verdict

Pass. The PubChem/CAS-derived ChEBI mapping, FEBA and CultureMech provenance,
CAS-backed structure fields, kg-microbe synonyms, CAS alias, and final SSSOM
row all describe inosine.

## Identity

- Reviewed record: `data/ingredients/mapped/Inosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17596` with
  `ontology_mapping.ontology_id: CHEBI:17596`, label `inosine`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `58-63-9`, formula `C10H12N4O5`, InChI
  `InChI=1S/C10H12N4O5/c15-1-4-6(16)7(17)10(19-4)14-3-13-5-8(14)11-2-12-9(5)18/h2-4,6-7,10,15-17H,1H2,(H,11,12,18)/t4-,6-,7-,10-/m1/s1`,
  and SMILES `OC[C@H]1O[C@@H](n2cnc3c(O)ncnc32)[C@H](O)[C@@H]1O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Indolmycin.yaml data/ingredients/mapped/Indoxyl_Acetate.yaml data/ingredients/mapped/Inosine.yaml data/ingredients/mapped/Inositol.yaml data/ingredients/mapped/Inulin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1610`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1610`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:17596` as the active ChEBI class `inosine`, with CAS
  xref `58-63-9`, formula `C10H12N4O5`, the same InChI and SMILES stored on
  the record, and all nine kg-microbe aliases as ChEBI synonyms.
- PubChem resolves CAS RN `58-63-9` to formula `C10H12N4O5` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Inosine` to
  `CHEBI:17596` and exports the inspected kg-microbe synonyms plus
  `CAS:58-63-9` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
