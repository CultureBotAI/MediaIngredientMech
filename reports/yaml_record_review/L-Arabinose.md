# `data/ingredients/mapped/L-Arabinose.yaml`

## Verdict

Needs curation. The exact ChEBI L-arabinose identity, CAS value, formula,
ChEBI synonym, occurrence count, and final SSSOM row are consistent, but
`CARBON_SOURCE` and `ENERGY_SOURCE` are only provisional computational roles.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Arabinose.yaml`.
- Identifier and grounding: `identifier: CHEBI:30849` with
  `ontology_mapping.ontology_id: CHEBI:30849`, label `L-arabinose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `5328-37-0` and molecular formula `C5H10O5`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Koh.yaml data/ingredients/mapped/Kscn.yaml data/ingredients/mapped/L-2-Aminobutyric_Acid.yaml data/ingredients/mapped/L-Arabinose.yaml data/ingredients/mapped/L-Asparagine_Monohydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2315`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2315`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:30849` as active ChEBI term `L-arabinose` and lists
  `L-arabino-pentose` as an exact synonym.
- PubChem resolves CAS RN `5328-37-0` with the same formula `C5H10O5`,
  supporting the stored CAS and formula fields.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:L-Arabinose` to
  `CHEBI:30849` with `L-arabino-pentose` and `CAS:5328-37-0` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the role claim.
- Major: `nutritional_roles.ENERGY_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a canonical energy-substrate rule,
  with no inspected claim-level evidence attached to the role claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, CultureMech membership rows, and
  row-review dispositions; it found no hits in
  `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, formula, aggregate copy, occurrence
  count, and final SSSOM row are present and consistent.
- The record is incomplete until the carbon-source and energy-source roles are
  either supported by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` unless inspected CultureMech, FEBA, Hans80,
  or literature sources can support those roles for L-arabinose, then rerun
  strict, term, round-trip, component, and SSSOM validation.
