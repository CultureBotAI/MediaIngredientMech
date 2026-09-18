# `data/ingredients/mapped/Staurosporine.yaml`

## Verdict

Pass. The MicrobeDecoder source label exact-matches active `CHEBI:15738`,
ChEBI/PubChem structure fields agree, and the final SSSOM row has no unsafe
`other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Staurosporine.yaml`.
- Identifier and grounding: `identifier: CHEBI:15738` with
  `ontology_mapping.ontology_id: CHEBI:15738`, label `staurosporine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C28H26N4O3` with ChEBI/PubChem structure
  values.
- Occurrences: 0 CultureMech occurrences, with a MicrobeDecoder source
  occurrence for one `BacDive_Metabolite_production` trait.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Stallimycin` through `Stearic_Acid`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:15738` with label `staurosporine`,
  matching the stored exact target.
- `mappings/microbedecoder_auto_mapped_review.tsv` shows the prior
  `review-ingredients` promotion that approved the local OAK label check.
- The final SSSOM row exact-matches `CHEBI:15738` and has empty `other`.

## Completeness

- The record has no active synonyms or role assertions to verify, and the
  exact identity plus structure fields agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
