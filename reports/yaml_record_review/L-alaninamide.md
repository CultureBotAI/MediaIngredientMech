# `data/ingredients/mapped/L-alaninamide.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI identity, active ChEBI term, PubChem
structure, reviewed promotion, empty occurrence count, and final SSSOM row are
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-alaninamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:21217` with
  `ontology_mapping.ontology_id: CHEBI:21217`, label `L-alaninamide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C3H8N2O`, InChI, SMILES, and
  molecular weight `88.11`.

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

- EBI OLS4 resolves `CHEBI:21217` as active `L-alaninamide`, supporting the
  exact MicrobeDecoder grounding.
- PubChem resolves `L-alaninamide` to CID `444939` with formula `C3H8N2O` and
  the same InChI as the YAML record.
- `mappings/microbedecoder_auto_mapped_review.tsv` records this row as
  `APPROVED` after review by `promote_microbedecoder_reviewed.py`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:21217` with no
  noisy `other` tokens.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row,
  MicrobeDecoder import source rows, docs projections, and MicrobeDecoder review
  approval.

## Completeness

- The active ChEBI identity, MicrobeDecoder review, aggregate copy, empty
  occurrence count, source occurrence count, and final SSSOM row are present and
  consistent.
- The record has no provisional roles, component decomposition, or occurrence
  rows to resolve.

## Recommended Edits

- None.
