# `data/ingredients/mapped/Khco3.yaml`

## Verdict

Pass. The exact ChEBI potassium hydrogencarbonate identity, CAS value,
structure fields, occurrence count, buffer role, mineral-source role, and final
SSSOM row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Khco3.yaml`.
- Identifier and grounding: `identifier: CHEBI:81862` with
  `ontology_mapping.ontology_id: CHEBI:81862`, label
  `potassium hydrogencarbonate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `298-14-6`, molecular formula `CHO3.K`, InChI,
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

- EBI OLS4 resolves `CHEBI:81862` as active ChEBI term
  `potassium hydrogencarbonate` and lists `KHCO3`, `E501`,
  `monopotassium carbonate`, `potassium acid carbonate`,
  `potassium bicarbonate`, and `potassium hydrogen carbonate` as
  same-substance aliases.
- PubChem resolves CAS RN `298-14-6` with the same InChI and equivalent formula
  `CHKO3`, supporting the stored CAS and structure fields.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Khco3` to
  `CHEBI:81862` with only same-substance aliases and `CAS:298-14-6` in
  `other`.
- The raw CultureMech role/property pseudo-synonym is filtered out of the final
  SSSOM and does not create a published synonym defect.
- `physicochemical_roles.BUFFER` and `nutritional_roles.MINERAL_SOURCE` are
  both supported by the original CultureMech role text.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and row-review dispositions; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, structure fields, aggregate copy,
  occurrence count, buffer role, mineral-source role, and final SSSOM row are
  present and consistent.

## Recommended Edits

- None.
