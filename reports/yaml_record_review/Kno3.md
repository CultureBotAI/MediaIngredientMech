# `data/ingredients/mapped/Kno3.yaml`

## Verdict

Needs curation. The corrected potassium nitrate identity, CAS value, structure
fields, occurrence count, and mineral-source role are consistent, but final
SSSOM still exports stale Renilla luciferyl sulfate aliases and malformed
`KNO` as synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Kno3.yaml`.
- Identifier and grounding: `identifier: CHEBI:63043` with
  `ontology_mapping.ontology_id: CHEBI:63043`, label `potassium nitrate`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7757-79-1`, molecular formula `K.NO3`, InChI,
  and SMILES.

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

- EBI OLS4 resolves `CHEBI:63043` as active ChEBI term `potassium nitrate` and
  lists `Kaliumnitrat`, `Nitrate of potash`, `Nitre`,
  `Nitric acid, potassium salt`, `Saltpeter`, and `saltpetre` as same-substance
  aliases.
- PubChem resolves CAS RN `7757-79-1` with the same InChI and equivalent formula
  `KNO3`, supporting the stored CAS and structure fields.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kno3` to
  `CHEBI:63043`.
- Major: final SSSOM `other` includes
  `2,8-dibenzyl-6-(4-hydroxyphenyl)imidazo[1,2-a]pyrazin-3-yl sulfate` and
  `Renilla luciferyl sulfate anion`, which are stale aliases from the old
  unrelated `CHEBI:58242` mapping.
- Major: final SSSOM `other` includes `KNO`, which is not a ChEBI synonym for
  potassium nitrate and loses the nitrate formula digit.
- The raw CultureMech role/property pseudo-synonyms and `(enhances growth)` are
  filtered out of the final SSSOM and do not themselves create a published
  synonym defect.
- `nutritional_roles.MINERAL_SOURCE` is supported by the original CultureMech
  `Mineral` role text and the current occurrence count.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, duplicate-review rows, and the
  synonym-enrichment review row; it found no hits in
  `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, structure fields, aggregate copy,
  occurrence count, and mineral-source role are present and consistent.
- The record is incomplete until the stale Renilla aliases and malformed `KNO`
  token stop publishing as SSSOM `other` tokens.

## Recommended Edits

- Major: remove or demote the Renilla luciferyl sulfate aliases and `KNO` in
  `data/ingredients/mapped/Kno3.yaml`, then regenerate the aggregate and final
  SSSOM so they disappear from `mappings/ingredient_mappings.sssom.tsv`; rerun
  strict, term, round-trip, component, and SSSOM validation.
