# `data/ingredients/mapped/Kasugamycin.yaml`

## Verdict

Pass. The reviewed MicrobeDecoder import now has an exact ChEBI identity, the
stored ChEBI structure matches the active term metadata, and the final SSSOM
row is internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Kasugamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:81419` with
  `ontology_mapping.ontology_id: CHEBI:81419`, label `kasugamycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C14H25N3O9`, molecular weight
  `379.366`, SMILES, and InChI from the ChEBI and PubChem enrichment pass.

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

- EBI OLS4 resolves `CHEBI:81419` as active ChEBI term `kasugamycin`, with the
  same formula, InChI, SMILES, and mass as the YAML `chemical_properties`.
- The MicrobeDecoder review row for `Kasugamycin.yaml` records the
  case-insensitive canonical-label check that promoted this record from
  `PENDING_REVIEW` to `MAPPED`; the fresh OLS4 and Engine A checks re-confirm
  the same active ChEBI identifier and label.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kasugamycin` to
  `CHEBI:81419` with no `other` synonyms.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and MicrobeDecoder review row; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, structure fields, aggregate copy, MicrobeDecoder
  source occurrence, empty CultureMech occurrence count, and final SSSOM row are
  present and consistent.
- No nutritional, physicochemical, cellular, or community role claim is present
  that would require additional claim-level evidence.

## Recommended Edits

- None.
