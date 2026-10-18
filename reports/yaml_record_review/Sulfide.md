# `data/ingredients/mapped/Sulfide.yaml`

## Verdict

Pass. The exact `CHEBI:26822` class identity, MicrobeDecoder source occurrence,
aggregate row, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfide.yaml`.
- Identifier and grounding: `identifier: CHEBI:26822` with
  `ontology_mapping.ontology_id: CHEBI:26822`, label `sulfide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: zero CultureMech recipe occurrences and 71 MicrobeDecoder
  metabolite rows.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfaquinoxaline_Sodium_Salt` through `Sulfisoxazole`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:26822` with label `sulfide`, matching
  the stored target.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `mappings/microbedecoder_auto_mapped_review.tsv` preserve the
  MicrobeDecoder import and the reviewed lexical approval for the same label.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:26822` rows,
  agreeing with `total_occurrences: 0` and `media_count: 0`.
- The final SSSOM row exact-matches `CHEBI:26822`, uses
  `semapv:LexicalMatching`, and leaves `other` empty.

## Completeness

- The generic sulfide class, aggregate row, occurrence count, and final SSSOM
  row agree.
- The record has no active synonyms, components, roles, environmental contexts,
  chemical-property block, or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder, aggregate,
  generated index, and final SSSOM rows, and no second active MIM record for
  `CHEBI:26822`.

## Recommended Edits

- None.
