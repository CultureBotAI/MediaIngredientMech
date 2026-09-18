# `data/ingredients/mapped/Indole.yaml`

## Verdict

Needs curation. The kgm-metatraits synonym match to active `CHEBI:16881` and
the structure fields describe indole, but the final SSSOM exports
`produces: indole`, which is a process-qualified source phrase rather than a
synonym of the compound.

## Identity

- Reviewed record: `data/ingredients/mapped/Indole.yaml`.
- Identifier and grounding: `identifier: CHEBI:16881` with
  `ontology_mapping.ontology_id: CHEBI:16881`, label `1H-indole`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C8H7N`, InChI
  `InChI=1S/C8H7N/c1-2-4-8-7(3-1)5-6-9-8/h1-6,9H`, and SMILES
  `c1ccc2nccc2c1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Indole-3-propionic_Acid.yaml data/ingredients/mapped/Indole-3-pyruvic_Acid.yaml data/ingredients/mapped/Indole.yaml data/ingredients/mapped/Indole_3-acetic_Acid_Sodium_Salt.yaml data/ingredients/mapped/Indolicidin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI/OBO-compatible
  records; `Indole-3-pyruvic_Acid` was outside adapter scope because its
  primary identifier is a CAS registry CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1555`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1555`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:16881` as active `1H-indole`, with formula `C8H7N`,
  the same InChI and SMILES stored on the record, and `INDOLE` and `Indole`
  as exact synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Indole` to
  `CHEBI:16881`.
- Major: the final SSSOM row exports `produces: indole` in `other`; this is a
  kg-microbe process surface form and should not be published as a synonym of
  indole.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row with the non-synonym `other` token, docs
  projections, and OAK/OLS review row marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, aggregate copy, and
  identity portion of the final SSSOM row are present and consistent.
- The exported `other` token is incomplete until process-qualified
  `produces:` text is removed or filtered.

## Recommended Edits

- Major: remove `produces: indole` from the record or teach the final SSSOM
  build to filter `produces:` raw-text tokens, then rebuild SSSOM and rerun
  strict, term, round-trip, id-label, component, and SSSOM validation.
