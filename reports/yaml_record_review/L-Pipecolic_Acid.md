# `data/ingredients/mapped/L-Pipecolic_Acid.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS value, formula, PubChem
structure, empty occurrence count, and ChEBI synonym are consistent, but
`pipercolic acid` does not resolve as a ChEBI synonym and still publishes in
the final SSSOM `other` column.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Pipecolic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30913` with
  `ontology_mapping.ontology_id: CHEBI:30913`, label `L-pipecolic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `3105-95-1`, molecular formula `C6H11NO2`,
  InChI, and SMILES.

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

- EBI OLS4 resolves `CHEBI:30913` as active `L-pipecolic acid` and lists
  `(2S)-piperidine-2-carboxylic acid` as a synonym, supporting the exact ChEBI
  identity and the ChEBI-sourced synonym.
- PubChem resolves CAS RN `3105-95-1` to CID `439227` with formula `C6H11NO2`
  and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:30913`.
- Major: EBI OLS4 exact search for `pipercolic acid` returned zero ChEBI hits.
  The correct ChEBI term and synonyms use `pipecolic`, not `pipercolic`, but
  the current `culturebotht` synonym still exports in final SSSOM `other`.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, and the row-review entries that preserved `pipercolic acid`
  because it was already represented locally.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, aggregate copy, empty
  occurrence count, and final SSSOM row are present and consistent.
- The published synonym surface is incomplete until the non-resolving
  `pipercolic acid` token no longer publishes as a synonym.

## Recommended Edits

- Major: remove or demote `pipercolic acid` in
  `data/ingredients/mapped/L-Pipecolic_Acid.yaml`, then regenerate the aggregate
  and final SSSOM.
- Rerun strict, term, round-trip, component, and SSSOM validation after the
  synonym repair.
