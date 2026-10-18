# `data/ingredients/mapped/Streptomycin.yaml`

## Verdict

Pass. The MicrobeDecoder source label exact-matches active `CHEBI:17076`, the
base-antibiotic structure fields agree, occurrence counts are refreshed, and
the final SSSOM row has no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Streptomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:17076` with
  `ontology_mapping.ontology_id: CHEBI:17076`, label `streptomycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C21H39N7O12` with ChEBI/PubChem structure
  values.
- Occurrences: 2 source occurrences across 2 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Steffimycin` through `Streptomycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:17076` with label `streptomycin`,
  matching the stored exact target.
- `mappings/microbedecoder_auto_mapped_review.tsv` shows the prior
  `review-ingredients` promotion that approved the local OAK label check.
- The final SSSOM row exact-matches `CHEBI:17076` and has empty `other`, so it
  does not conflate the base with the adjacent
  `Streptomycin_Sulfate_Salt` record.

## Completeness

- The record has no active synonyms or role assertions to verify, and the
  exact identity plus structure fields agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
