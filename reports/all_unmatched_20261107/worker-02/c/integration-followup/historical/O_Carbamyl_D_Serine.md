# `data/ingredients/mapped/O_Carbamyl_D_Serine.yaml`

## Verdict

Pass. The former kg-microbe placeholder has been promoted to a resolving MeSH
supplemental record, and the remaining final `UNKNOWN_TERM` stamp is tracked as
validator-prefix coverage rather than a mapping error.

## Identity

- Reviewed record: `data/ingredients/mapped/O_Carbamyl_D_Serine.yaml`.
- Identifier and grounding: `identifier: mesh:C000366` with
  `ontology_mapping.ontology_id: mesh:C000366`, label `O-carbamylserine`,
  source `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: `O-carbamyl-D-serine`, merged from the duplicate unmapped record
  in the May 2026 duplicate review.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this MeSH-primary
  record.

## Evidence

- A fresh EBI OLS4 exact search for `O Carbamyl D Serine` in MeSH returns
  `mesh:C000366` as active `O-carbamylserine`, matching the current identifier
  and label.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` records
  `mesh:C000366` as `RESOLVED_EXACT_CURIE` and classifies the final SSSOM
  `UNKNOWN_TERM` stamp as missing prefix coverage in the synonym-review
  dispatcher.
- The final SSSOM row maps `MIM:O_Carbamyl_D_Serine` exactly to
  `mesh:C000366`; its single `other` token, `O-carbamyl-D-serine`, is a
  curated exact synonym.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The MeSH identifier, canonical label, exact-synonym evidence, duplicate-merge
  provenance, UNKNOWN_TERM triage row, and final SSSOM row agree.
- The hidden and ignored-inclusive search over `data/ingredients`,
  `data/curated`, `mappings`, `reports`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found historical kg-microbe placeholder
  output only; the active YAML now uses the promoted MeSH CURIE.

## Recommended Edits

- None.
