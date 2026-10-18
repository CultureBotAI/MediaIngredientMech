# `data/ingredients/mapped/L-Meta-tyrosine.yaml`

## Verdict

Pass. The CAS-backed identity, #326 same-formula repair, exact ChEBI mapping,
ChEBI synonyms, PubChem structure, empty occurrence count, and final SSSOM rows
are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Meta-tyrosine.yaml`.
- Identifier and grounding: `identifier: cas:587-33-7` with
  `ontology_mapping.ontology_id: CHEBI:44303`, label `L-m-tyrosine`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `587-33-7`, molecular formula `C9H11NO3`,
  InChI, SMILES, and PubChem CID `6950578`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/L-Homoserine.yaml data/ingredients/mapped/L-Malic_Acid.yaml data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Meta-tyrosine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 exact search resolves `CHEBI:44303` as `L-m-tyrosine`, matching the
  YAML grounding and final SSSOM object label.
- PubChem resolves CAS RN `587-33-7` to CID `6950578` with formula `C9H11NO3`
  and the same InChI as the YAML record, supporting the #326 same-formula
  repair from broad parent to exact synonym match.
- EBI OLS4 exact synonym searches resolve both
  `(2S)-2-amino-3-(3-hydroxyphenyl)propanoic acid` and
  `3-hydroxy-L-phenylalanine` to `CHEBI:44303`, supporting the curated
  synonyms.
- The final SSSOM publishes the expected `skos:exactMatch` row to
  `CHEBI:44303` and the exact CAS identity row with only CAS or ChEBI synonyms
  in `other`.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM rows, docs
  projections, unknown-term triage rows for the CAS and retired KG-Microbe
  registry rows, and the synonym-enrich row-review confirmation.

## Completeness

- The exact ChEBI identity, CAS RN, formula, structure, curated synonyms,
  aggregate copy, empty occurrence count, and final SSSOM rows are present and
  consistent.
- The record has no provisional roles, component decomposition, or occurrence
  rows to resolve.

## Recommended Edits

- None.
