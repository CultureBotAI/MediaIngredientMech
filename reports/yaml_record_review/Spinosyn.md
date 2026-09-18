# `data/ingredients/mapped/Spinosyn.yaml`

## Verdict

Pass. The MicrobeDecoder source label exact-matches the active CHEBI spinosyn
class, and no unsupported synonym, role, or final SSSOM synonym is present.

## Identity

- Reviewed record: `data/ingredients/mapped/Spinosyn.yaml`.
- Identifier and grounding: `identifier: CHEBI:39207` with
  `ontology_mapping.ontology_id: CHEBI:39207`, label `spinosyn`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and no
  active `ingredient_type`.
- Occurrences: 0 CultureMech occurrences, with a MicrobeDecoder source
  occurrence for one `BacDive_Metabolite_production` trait.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sphondin` through `Spiramycin_II`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:39207` with label `spinosyn` and a
  definition for the spinosyn macrolide natural-product family, matching the
  MicrobeDecoder lexical source label.
- `mappings/microbedecoder_auto_mapped_review.tsv` shows the prior
  `review-ingredients` promotion that approved the local OAK label check.
- The final SSSOM row exact-matches `CHEBI:39207` and has empty `other`, so no
  non-synonym payload is published.

## Completeness

- The record has no chemical properties or role assertions to verify; that is
  acceptable for this MicrobeDecoder-only trait import.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
