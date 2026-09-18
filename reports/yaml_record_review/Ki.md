# `data/ingredients/mapped/Ki.yaml`

## Verdict

Needs curation. The exact potassium iodide identity, CAS value, structure
fields, occurrence count, curated `KJ` alias, and mineral-source role are
consistent, but final SSSOM exports a concentration-qualified CultureMech label
as a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Ki.yaml`.
- Identifier and grounding: `identifier: CHEBI:8346` with
  `ontology_mapping.ontology_id: CHEBI:8346`, label `potassium iodide`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7681-11-0`, molecular formula `I.K`, InChI, and
  SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Khco3.yaml data/ingredients/mapped/Ki.yaml data/ingredients/mapped/Kijanimicin.yaml data/ingredients/mapped/Kno2.yaml data/ingredients/mapped/Kno3.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2300`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2300`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:8346` as active ChEBI term `potassium iodide` and
  lists `KI` and `Kaliumiodid` as same-substance aliases.
- PubChem resolves CAS RN `7681-11-0` with the same InChI and equivalent formula
  `IK`, supporting the stored CAS and structure fields.
- The `merge_duplicate_unmapped` curation event gives recipe-context evidence
  for retaining `KJ` and `Kaliumjodid` as aliases for potassium iodide rather
  than the bad Phencyclidine CAS from the source MediaDive ingredient record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Ki` to
  `CHEBI:8346`.
- Major: final SSSOM `other` includes `KI (0.01% w/v)`, which is a
  concentration-qualified recipe label rather than an exact synonym for
  potassium iodide.
- The raw CultureMech role/property pseudo-synonyms are filtered out of the
  final SSSOM and do not themselves create a published synonym defect.
- `nutritional_roles.MINERAL_SOURCE` is supported by the original CultureMech
  `Mineral` role text and the later curation history entry that deliberately
  reclassified iodide from `TRACE_ELEMENT` to `MINERAL_SOURCE`.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, residual alias row, and row-review
  dispositions; it found no hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, structure fields, aggregate copy,
  occurrence count, and mineral-source role are present and consistent.
- The record is incomplete until the concentration-qualified KI surface form
  stops publishing as an SSSOM `other` token.

## Recommended Edits

- Major: remove or demote `KI (0.01% w/v)` in
  `data/ingredients/mapped/Ki.yaml`, then regenerate the aggregate and final
  SSSOM so it disappears from `mappings/ingredient_mappings.sssom.tsv`; rerun
  strict, term, round-trip, component, and SSSOM validation.
