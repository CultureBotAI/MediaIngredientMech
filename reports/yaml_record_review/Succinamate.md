# `data/ingredients/mapped/Succinamate.yaml`

## Verdict

Pass. The MicrobeDecoder label exact-matches active `CHEBI:143136`, ChEBI
structure fields agree with the YAML, and the final SSSOM row has no unsafe
`other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Succinamate.yaml`.
- Identifier and grounding: `identifier: CHEBI:143136` with
  `ontology_mapping.ontology_id: CHEBI:143136`, label `succinamate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C4H6NO3`, mass `116.096`, and ChEBI-derived
  structure fields for the monoanion.
- Occurrences: 0 CultureMech media occurrences plus 2 MicrobeDecoder source
  occurrences from `BacDive_Metabolite_utilization`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Substrate` through `Sucrose-6-monophosphate_Dipotassium_Salt`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:143136` with label `succinamate`,
  formula `C4H6NO3`, a matching InChI/SMILES payload, and synonyms scoped to
  the same monoanion.
- `mappings/microbedecoder_auto_mapped_review.tsv` shows the local
  `review-ingredients` promotion that approved the OAK label check and moved
  the record from `PENDING_REVIEW` back to `MAPPED`.
- The final SSSOM row exact-matches `CHEBI:143136` and leaves `other` empty.

## Completeness

- The exact identity, structural fields, MicrobeDecoder source occurrence,
  aggregate row, and final SSSOM row agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
