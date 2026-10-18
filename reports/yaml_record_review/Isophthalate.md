# `data/ingredients/mapped/Isophthalate.yaml`

## Verdict

Pass with minor issues. The `#213` synonym match to isophthalate(2-), ChEBI
structure fields, MicrobeDecoder provenance, source-occurrence count, and final
SSSOM row pass, but the import-era `notes` still say curator review is needed.

## Identity

- Reviewed record: `data/ingredients/mapped/Isophthalate.yaml`.
- Identifier and grounding: `identifier: CHEBI:30803` with
  `ontology_mapping.ontology_id: CHEBI:30803`, label `isophthalate(2-)`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C8H4O4`, InChI
  `InChI=1S/C8H6O4/c9-7(10)5-2-1-3-6(4-5)8(11)12/h1-4H,(H,9,10)(H,11,12)/p-2`,
  SMILES `O=C([O-])c1cccc(C(=O)[O-])c1`, and molecular weight `164.116`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isomaltose.yaml data/ingredients/mapped/Isoniazid.yaml data/ingredients/mapped/Isoorientin.yaml data/ingredients/mapped/Isophthalate.yaml data/ingredients/mapped/Isopropionate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI records.
  `Isopropionate` was outside adapter scope because its primary identifier is a
  local `kgmicrobe.compound` CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2100`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2100`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:30803` as the active ChEBI class
  `isophthalate(2-)`, with formula `C8H4O4`, the same InChI and SMILES stored
  on the record, and bare `isophthalate` as an exact ChEBI synonym.
- The final SSSOM publishes one row from `MIM:Isophthalate` to `CHEBI:30803`
  with empty `other`; the row records manual `#213` curation and the original
  `UNMAPPED_0820` promotion rather than a naive first OLS hit.
- Minor: top-level `notes` still describe the original MicrobeDecoder miss and
  say curator review is needed even though the `#213` promotion resolved the
  ChEBI target.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, the `UNMAPPED_0820`
  promotion, and prior research-validation rows whose identity and missing
  chemistry findings are already resolved in the current YAML.

## Completeness

- The active ChEBI identifier, reviewed synonym-match decision, formula, InChI,
  SMILES, aggregate copy, and final SSSOM row are present and consistent.
- OLS4 exposes no CAS RN for this deprotonated ChEBI term, and the free acid
  CAS RN should not be forced onto the anion record.

## Recommended Edits

- Minor: refresh top-level `notes` to stop saying that no ChEBI match exists
  or that curator review is still needed, then rerun strict, term, round-trip,
  component, id-label, and SSSOM validation.
