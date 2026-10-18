# `data/ingredients/mapped/L-Xylose.yaml`

## Verdict

Needs curation. The exact ChEBI identity, repaired CAS value, formula, PubChem
identity, empty occurrence count, and final SSSOM row are consistent, but
`CARBON_SOURCE` and `ENERGY_SOURCE` are only provisional computational roles.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Xylose.yaml`.
- Identifier and grounding: `identifier: CHEBI:65328` with
  `ontology_mapping.ontology_id: CHEBI:65328`, label `L-xylose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `609-06-3` and molecular formula `C5H10O5`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Pipecolic_Acid.yaml data/ingredients/mapped/L-Pyroglutamic_Acid.yaml data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml data/ingredients/mapped/L-Xylose.yaml data/ingredients/mapped/L-_-ergothioneine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:65328` as active `L-xylose`, supporting the exact
  ChEBI identity.
- PubChem resolves the stripped CAS RN `609-06-3` to CID `95259` with formula
  `C5H10O5`, supporting the #310 leading-zero CAS repair and the stored
  formula.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:65328` with
  only `CAS:609-06-3` in `other`, which belongs to the same subject identity.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` have only `COMPUTATIONAL_PREDICTION`
  evidence from ChEBI ancestry and paired carbon-source inference, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to either
  role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, and OAK/OLS row-review confirmation.

## Completeness

- The active ChEBI identity, stripped CAS RN, formula, aggregate copy, empty
  occurrence count, and final SSSOM row are present and consistent.
- The record is incomplete until the carbon-source and energy-source roles are
  either supported by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` unless inspected CultureMech, FEBA, Hans80,
  or literature sources can support L-xylose as a carbon and energy source.
- Rerun strict, term, round-trip, role, component, and SSSOM validation after
  the role changes.
