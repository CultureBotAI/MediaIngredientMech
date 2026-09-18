# `data/ingredients/mapped/Gelrite.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym issues. The synonym-match
grounding to active `CHEBI:85248` and the source-backed solidifying-agent role
pass, but final SSSOM still exports `G Starch` plus two conditional recipe
phrases that are not clean Gelrite synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Gelrite.yaml`.
- Identifier and grounding: `identifier: CHEBI:85248` with matching
  `ontology_mapping.ontology_id`, canonical label `gellan gum`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:85248` as active gellan gum with brand-name synonyms
  `Gelrite` and `Phytagel`, plus CAS xref `71010-52-1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gamma-cyclodextrin.yaml data/ingredients/mapped/Garden_Soil.yaml data/ingredients/mapped/Gardimycin.yaml data/ingredients/mapped/Gelatine.yaml data/ingredients/mapped/Gelrite.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gamma-cyclodextrin.yaml data/ingredients/mapped/Gelatine.yaml data/ingredients/mapped/Gelrite.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI synonym match, 33 CultureMech occurrences, kg-microbe node id,
  single-ingredient type, raw aliases, and solidifying-agent role as the
  per-record YAML.
- The record was deliberately regraded from `EXACT_MATCH` to `SYNONYM_MATCH`
  in issue `#322` because Gelrite is a trade name for gellan gum rather than
  the canonical ChEBI label.
- `physicochemical_roles.SOLIDIFYING_AGENT` is supported by a
  `DATABASE_ENTRY` imported from the CultureMech pipeline with original role
  text `Solidifying Agent`.
- Major: final SSSOM exports
  `G Starch|Phytagel|Gellan gum (if needed)|Gelrite (if needed)|Gellan Gum (Phytagel)|gelrite (Gellan Gum)`
  in `other`. `Phytagel`, `Gellan Gum (Phytagel)`, and
  `gelrite (Gellan Gum)` are same-subject aliases, but `G Starch` is not an
  OLS4 synonym of `CHEBI:85248`, and `Gellan gum (if needed)` plus
  `Gelrite (if needed)` include conditional recipe prose rather than plain
  synonyms.
- `mappings/ingredient_mappings_oak_ols_review.tsv` proposed `G Starch` as a
  synonym-enrichment token, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` later marked that row
  as already represented. That accurately describes the YAML state but leaves
  the synonym validity problem unresolved.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, final SSSOM
  and row-review rows, CultureMech residual alias rows for the parenthetical
  and conditional recipe forms, generated indexes, old batch validation
  reports, and ignored aggregate backups.

## Completeness

- The Gelrite identity, role evidence, occurrence count, and final SSSOM row
  are populated.
- Three invalid synonym strings need review before the final SSSOM `other`
  field is clean.

## Recommended Edits

- Major: remove or retag `G Starch`, `Gellan gum (if needed)`, and
  `Gelrite (if needed)` so the final SSSOM row stops exporting non-synonym
  recipe text, then regenerate final SSSOM and rerun SSSOM invariants.
