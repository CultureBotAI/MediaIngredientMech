# `data/ingredients/mapped/Mannose.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI identity, reviewed promotion, structure,
occurrence count, empty synonym surface, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mannose.yaml`.
- Identifier and grounding: `identifier: CHEBI:37684` with
  `ontology_mapping.ontology_id: CHEBI:37684`, label `mannose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1,180 MicrobeDecoder metabolite-utilization occurrences.
- Chemical formula: `C6H12O6`, molecular weight `180.156`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mannobiose` through `Marine_Broth_2216`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:37684` as active `mannose` with formula `C6H12O6`
  and molecular weight `180.156`.
- The local `review-ingredients` promotion says the MicrobeDecoder
  `ols-label-exact` import was held at `PENDING_REVIEW`, then promoted after
  local OAK confirmed the term and canonical label.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mannose` to
  `CHEBI:37684` with empty `other`.

## Completeness

- The record does not assert provisional roles, CAS numbers, or synonyms that
  would need narrower support.

## Recommended Edits

- None.
