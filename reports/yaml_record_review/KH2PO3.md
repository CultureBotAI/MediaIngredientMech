# `data/ingredients/mapped/KH2PO3.yaml`

## Verdict

Pass with minor issues. The CAS primary identifier for potassium phosphite
monobasic, the parent `skos:narrowMatch` to ChEBI phosphonic acid, the registry
identity rows, final SSSOM rows, and occurrence count are consistent, but the
import-era notes still say curator review is needed and that the record was
left unmapped.

## Identity

- Reviewed record: `data/ingredients/mapped/KH2PO3.yaml`.
- Identifier and grounding: `identifier: cas:13977-65-6` with
  `ontology_mapping.ontology_id: CHEBI:44976`, label `phosphonic acid`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `13977-65-6` from Edison literature research,
  intentionally without ChEBI-derived formula, InChI, or SMILES for an exact
  ontology term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/K2so4_X_7_H2o.yaml data/ingredients/mapped/KH2PO3.yaml data/ingredients/mapped/Kanamycin.yaml data/ingredients/mapped/Kanamycin_Sulfate.yaml data/ingredients/mapped/Kanchanomycin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2150`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2150`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- Engine A resolved `CHEBI:44976` with label `phosphonic acid`; fresh exact
  OLS4 ChEBI search for `KH2PO3` returned zero exact hits, matching the CAS
  registry identifier plus parent-term mapping shape.
- PubChem resolves CAS RN `13977-65-6`, which supports retaining the CAS
  registry identity even though the record has no exact public ontology CURIE.
- The final SSSOM publishes one `skos:narrowMatch` row from `MIM:KH2PO3` to
  `CHEBI:44976` plus exact CAS and local kgmicrobe registry rows. The exact
  rows are the expected identity siblings for a narrow parent mapping and carry
  `CAS:13977-65-6` only on the registry rows.
- Minor: `notes` still repeats the April and May text saying no CAS RN existed,
  curator review was needed, and the record was left unmapped, even though the
  August Edison CAS enrichment and `promote_resolved_unmapped` pass resolved the
  CAS identity and promoted the record.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current
  per-record YAML, final SSSOM rows, docs projections, record-research
  validation row, and three current CultureMech membership rows.

## Completeness

- The CAS primary identifier, parent ChEBI mapping, exact CAS and local registry
  rows, aggregate copy, occurrence count, and final SSSOM rows are present and
  consistent.
- Only the stale explanatory `notes` text is left from the pre-promotion state.

## Recommended Edits

- Minor: refresh or remove the stale `notes` text in
  `data/ingredients/mapped/KH2PO3.yaml`, then synchronize the aggregate and rerun
  strict, term, round-trip, component, and SSSOM validation.
