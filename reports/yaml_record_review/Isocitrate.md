# `data/ingredients/mapped/Isocitrate.yaml`

## Verdict

Pass with minor issues. The `#213` bare-label close match to isocitrate(3-),
MicrobeDecoder provenance, source-occurrence count, and final SSSOM row pass,
but the ChEBI structure fields and stale import-era `notes` need backfill.

## Identity

- Reviewed record: `data/ingredients/mapped/Isocitrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16087` with
  `ontology_mapping.ontology_id: CHEBI:16087`, label `isocitrate(3-)`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The reviewed `#213` decision intentionally grounds the bare
  `kgmicrobe.trait:isocitrate` label to the fully deprotonated isocitrate(3-)
  species present at growth-medium pH, while preserving `CLOSE_MATCH` because
  bare `Isocitrate` is not a registered ChEBI synonym of this term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isobutyrate.yaml data/ingredients/mapped/Isobutyric_Acid.yaml data/ingredients/mapped/Isocaproate.yaml data/ingredients/mapped/Isocitrate.yaml data/ingredients/mapped/Isoliquiritigenin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2050`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2050`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:16087` as the active ChEBI class `isocitrate(3-)`, with
  formula `C6H5O7`, InChI
  `InChI=1S/C6H8O7/c7-3(8)1-2(5(10)11)4(9)6(12)13/h2,4,9H,1H2,(H,7,8)(H,10,11)(H,12,13)/p-3`,
  and SMILES `O=C([O-])CC(C(=O)[O-])C(O)C(=O)[O-]`.
- The final SSSOM publishes one row from `MIM:Isocitrate` to `CHEBI:16087`
  with empty `other`; the row records manual curation and the original
  `UNMAPPED_0685` promotion rather than a naive exact lexical import.
- Minor: the record is an active ChEBI single-ingredient mapping but lacks a
  `chemical_properties` block for the inspected isocitrate(3-) formula, InChI,
  SMILES, and molecular weight.
- Minor: top-level `notes` still describe the original MicrobeDecoder miss and
  say curator review is needed even though the `#213` promotion resolved the
  ChEBI target.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, the `UNMAPPED_0685`
  promotion, and prior research-validation rows that also identify the missing
  `chemical_properties` block as an enrichment gap.

## Completeness

- The active ChEBI identifier, reviewed close-match decision, aggregate copy,
  and final SSSOM row are present and consistent.
- The record is missing ChEBI-derived `chemical_properties`; OLS4 exposes no
  CAS RN for this ChEBI term.

## Recommended Edits

- Minor: backfill `chemical_properties` from `CHEBI:16087`, including formula,
  InChI, SMILES, and molecular weight, then rerun strict, term, round-trip,
  component, id-label, and SSSOM validation.
- Minor: refresh top-level `notes` to stop saying that no ChEBI match exists
  or that curator review is still needed.
