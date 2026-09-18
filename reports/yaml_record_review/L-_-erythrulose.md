# `data/ingredients/mapped/L-_-erythrulose.yaml`

## Verdict

Needs curation. The CAS-to-ChEBI lookup identity, active ChEBI term, formula,
PubChem structure, ChEBI synonyms, empty occurrence count, and final SSSOM row
are consistent, but `CARBON_SOURCE` is only provisional ChEBI-ancestry
evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/L-_-erythrulose.yaml`.
- Identifier and grounding: `identifier: CHEBI:23958` with
  `ontology_mapping.ontology_id: CHEBI:23958`, label `erythrulose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `533-50-6`, molecular formula `C4H8O4`, InChI,
  and SMILES.

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

- EBI OLS4 resolves `CHEBI:23958` as active `erythrulose` and lists
  `1,3,4-trihydroxybutan-2-one` plus `glycero-tetrulose` as synonyms,
  supporting the CAS lookup identity and curated synonyms.
- PubChem resolves CAS RN `533-50-6` to CID `5460032` with formula `C4H8O4` and
  an InChI matching the ChEBI identity.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:23958` with
  only the two curated ChEBI synonyms and `CAS:533-50-6` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, and OAK/OLS row-review confirmation.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, ChEBI synonyms,
  aggregate copy, empty occurrence count, and final SSSOM row are present and
  consistent.
- The record is incomplete until the carbon-source role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-(+)-erythrulose
  as a carbon source.
- Rerun strict, term, round-trip, role, component, and SSSOM validation after
  the role change.
