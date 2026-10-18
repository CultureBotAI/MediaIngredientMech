# `data/ingredients/mapped/Inulin.yaml`

## Verdict

Needs curation. The CultureMech exact ChEBI mapping, polymer formula, kg-microbe
synonyms, raw-role filtering, and final SSSOM row pass, but `CARBON_SOURCE` is
still only a provisional ChEBI-ancestry assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Inulin.yaml`.
- Identifier and grounding: `identifier: CHEBI:15443` with
  `ontology_mapping.ontology_id: CHEBI:15443`, label `inulin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `9005-80-5` and polymer formula `(C12H20O11)n`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Indolmycin.yaml data/ingredients/mapped/Indoxyl_Acetate.yaml data/ingredients/mapped/Inosine.yaml data/ingredients/mapped/Inositol.yaml data/ingredients/mapped/Inulin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1610`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1610`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:15443` as the active ChEBI class `inulin`, with CAS xref
  `9005-80-5`, formula `(C12H20O11)n`, and both kg-microbe aliases as ChEBI
  synonyms.
- PubChem does not resolve CAS RN `9005-80-5`, matching the absence of
  small-molecule InChI, SMILES, and CID fields on this polymer record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Inulin` to
  `CHEBI:15443` and exports the two inspected kg-microbe synonyms plus
  `CAS:9005-80-5` in `other`; the raw `Role: Carbon source` string is
  correctly filtered.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the claim.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, polymer CAS RN, formula, exact synonyms,
  aggregate copy, and final SSSOM row are present and consistent.
- The record is incomplete until the carbon-source role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support inulin as a
  carbon source, then rerun strict, term, round-trip, id-label, component, and
  SSSOM validation.
