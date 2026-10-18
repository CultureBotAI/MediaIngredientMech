# `data/ingredients/mapped/Kbr.yaml`

## Verdict

Needs curation. The exact potassium bromide identity, CAS value, structure
fields, occurrence count, mineral-source role, and final SSSOM row mostly agree,
but the active synonym `K HPO` is not a potassium bromide synonym and is
published in final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Kbr.yaml`.
- Identifier and grounding: `identifier: CHEBI:32030` with
  `ontology_mapping.ontology_id: CHEBI:32030`, label `potassium bromide`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7758-02-3`, molecular formula `Br.K`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Kao_And_Michayluk_Vitamin_Solution.yaml data/ingredients/mapped/Karanjin.yaml data/ingredients/mapped/Kasugamycin.yaml data/ingredients/mapped/Kawain.yaml data/ingredients/mapped/Kbr.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for `Karanjin`, `Kasugamycin`,
  `Kawain`, and `Kbr`; `Kao_And_Michayluk_Vitamin_Solution` was skipped because
  MICRO is intentionally outside the OBO-safe Engine A adapter set.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2200`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2200`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:32030` as active ChEBI term `potassium bromide` and
  lists `KBr`, `Kaliumbromid`, and `Potassium bromide` as same-substance
  aliases.
- PubChem resolves CAS RN `7758-02-3` with the same InChI as the YAML record
  and the equivalent disconnected salt SMILES `[K+].[Br-]`.
- Major: `synonyms[]` contains active `EXACT_SYNONYM` value `K HPO`, which is
  not a ChEBI synonym for `CHEBI:32030` and does not denote potassium bromide.
  The bad token is also exported in final SSSOM `other`.
- The raw CultureMech role/property pseudo-synonyms are filtered out of the
  final SSSOM and do not themselves create a published synonym defect.
- `nutritional_roles.MINERAL_SOURCE` is consistent with the original
  CultureMech `Mineral source` role and the later curation history entry that
  deliberately reclassified bromide from `TRACE_ELEMENT` to `MINERAL_SOURCE`.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, KBr components in Marine Broth/Agar 2216,
  and synonym-enrichment review rows; it found no hits in
  `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, formula, structure fields, aggregate
  copy, occurrence count, and mineral-source role are present and consistent.
- The record is incomplete until the non-identity `K HPO` synonym is removed or
  demoted to a rejected-label provenance field that does not publish to final
  SSSOM `other`.

## Recommended Edits

- Major: remove or demote `K HPO` in `data/ingredients/mapped/Kbr.yaml`, then
  regenerate the aggregate and final SSSOM so the bad token disappears from
  `mappings/ingredient_mappings.sssom.tsv`; rerun strict, term, round-trip,
  component, and SSSOM validation.
