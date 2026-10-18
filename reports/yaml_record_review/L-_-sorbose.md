# `data/ingredients/mapped/L-_-sorbose.yaml`

## Verdict

Needs curation. The CAS-to-ChEBI lookup identity, active ChEBI term, formula,
PubChem identity, ChEBI synonyms, occurrence count, and final SSSOM row are
consistent, but `CARBON_SOURCE` is only provisional ChEBI-ancestry evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/L-_-sorbose.yaml`.
- Identifier and grounding: `identifier: CHEBI:17266` with
  `ontology_mapping.ontology_id: CHEBI:17266`, label `L-sorbose`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `87-79-6` and molecular formula `C6H12O6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-_-erythrulose.yaml data/ingredients/mapped/L-_-sorbose.yaml data/ingredients/mapped/L-alaninamide.yaml data/ingredients/mapped/L-alanine.yaml data/ingredients/mapped/L-alanine_4-nitroanilide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 ChEBI records; Engine A was
  intentionally skipped for the `kgmicrobe.compound` fallback.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:17266` as active `L-sorbose` and lists
  `(3S,4R,5S)-1,3,4,5,6-pentahydroxyhexan-2-one` plus
  `L-xylo-hex-2-ulose` as synonyms, supporting the CAS lookup identity and
  curated synonyms.
- PubChem resolves CAS RN `87-79-6` to CID `6904` with formula `C6H12O6`,
  supporting the stored formula.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:17266` with
  only the two curated ChEBI synonyms and `CAS:87-79-6` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, and OAK/OLS row-review confirmation.

## Completeness

- The active ChEBI identity, CAS RN, formula, ChEBI synonyms, aggregate copy,
  1/1 occurrence count, and final SSSOM row are present and consistent.
- The record is incomplete until the carbon-source role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-(-)-sorbose as
  a carbon source.
- Rerun strict, term, round-trip, role, component, and SSSOM validation after
  the role change.
