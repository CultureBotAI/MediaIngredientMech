# `data/ingredients/mapped/Itaconate.yaml`

## Verdict

Pass with minor issues. The `#213` synonym match to itaconate(2-), ChEBI
structure fields, MicrobeDecoder provenance, source-occurrence count, and final
SSSOM row pass, but the import-era `notes` still say curator review is needed.

## Identity

- Reviewed record: `data/ingredients/mapped/Itaconate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17240` with
  `ontology_mapping.ontology_id: CHEBI:17240`, label `itaconate(2-)`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C5H4O4`, InChI
  `InChI=1S/C5H6O4/c1-3(5(8)9)2-4(6)7/h1-2H2,(H,6,7)(H,8,9)/p-2`, SMILES
  `C=C(CC(=O)[O-])C(=O)[O-]`, and molecular weight `128.083`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isovitalex.yaml data/ingredients/mapped/Isovitexin.yaml data/ingredients/mapped/Itaconate.yaml data/ingredients/mapped/Itaconic_Acid.yaml data/ingredients/mapped/Izalpinin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 3 CHEBI records.
  `Isovitalex` and `Izalpinin` were outside adapter scope because their primary
  identifiers are local `kgmicrobe.ingredient` and CAS registry CURIEs.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2120`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2120`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:17240` as the active ChEBI class `itaconate(2-)`, with
  formula `C5H4O4`, the same InChI and SMILES stored on the record, and bare
  `itaconate` as an exact ChEBI synonym.
- The final SSSOM publishes one row from `MIM:Itaconate` to `CHEBI:17240` with
  empty `other`; the row records manual `#213` curation and the original
  `UNMAPPED_0638` promotion rather than a naive first OLS hit.
- Minor: top-level `notes` still describe the original MicrobeDecoder miss and
  say curator review is needed even though the `#213` promotion resolved the
  ChEBI target.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, the `UNMAPPED_0638`
  promotion, and prior research-validation rows whose identity and acid-form
  candidate findings do not contradict the current anion-specific record.

## Completeness

- The active ChEBI identifier, reviewed synonym-match decision, formula, InChI,
  SMILES, aggregate copy, and final SSSOM row are present and consistent.
- The record intentionally has no CAS RN; the neutral free acid CAS RN should
  not be forced onto the dianion record.

## Recommended Edits

- Minor: refresh top-level `notes` to stop saying that no ChEBI match exists or
  that curator review is still needed, then rerun strict, term, round-trip,
  component, id-label, and SSSOM validation.
