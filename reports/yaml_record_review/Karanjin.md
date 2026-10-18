# `data/ingredients/mapped/Karanjin.yaml`

## Verdict

Pass. The CultureBotHT-derived CAS identity, exact ChEBI grounding, structure
fields, ChEBI synonym, final SSSOM row, and empty occurrence count are
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Karanjin.yaml`.
- Identifier and grounding: `identifier: CHEBI:166631` with
  `ontology_mapping.ontology_id: CHEBI:166631`, label `Karanjin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `521-88-0`, molecular formula `C18H12O4`, InChI,
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

- EBI OLS4 resolves `CHEBI:166631` as active ChEBI term `Karanjin` and lists
  `3-methoxy-2-phenyluro[2,3-h]chromen-4-one` as an exact synonym.
- PubChem resolves CAS RN `521-88-0` with formula `C18H12O4` and the same InChI
  as the YAML record, supporting the stored CAS and structure fields.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Karanjin` to
  `CHEBI:166631` with `3-methoxy-2-phenyluro[2,3-h]chromen-4-one` and
  `CAS:521-88-0` as same-substance `other` aliases.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and row-review dispositions; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, structure fields, aggregate copy, empty
  occurrence count, and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or community role claim is present
  that would require additional claim-level evidence.

## Recommended Edits

- None.
