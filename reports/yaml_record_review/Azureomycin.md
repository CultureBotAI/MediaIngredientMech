# `data/ingredients/mapped/Azureomycin.yaml`

## Verdict

Pass. The record intentionally preserves the local
`kgmicrobe.compound:azureomycin` placeholder after prior no-hit review, current
OLS still has no exact bare `Azureomycin` term, and the aggregate plus SSSOM
rows carry the same kg-microbe registry identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Azureomycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:azureomycin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:azureomycin`,
  `ontology_label: Azureomycin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, and `mapping_status: MAPPED`.
- OLS4 exact search across `CHEBI`, `MESH`, and `NCIT` returned only the more
  specific siblings `azureomycin A` and `azureomycin B`, not a bare exact
  `Azureomycin` candidate.
- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the expected
  placeholder review rows and no normalized mapped duplicate that would justify
  replacing this kg-microbe identity with an external identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azureomycin.yaml data/ingredients/mapped/B-Glucan_From_Oat.yaml data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml data/ingredients/mapped/BHI.yaml data/ingredients/mapped/Bacillomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `kgmicrobe.compound` is a non-OBO prefix.
- OLS4 exact lookup for `Azureomycin` in `CHEBI`, `MESH`, and `NCIT` found
  narrower A/B terms but no exact bare term.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- The source and curation history consistently say this record was imported
  from kg-microbe's unmapped placeholder namespace, that CHEBI/NCIT lookup
  found no hits, and that the kg-microbe identifier was retained pending a
  later exact external match.
- `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`,
  `mappings/ingredient_mappings_unknown_term_nohit_review.tsv`,
  `mappings/ingredient_mappings_unknown_term_triage.tsv`, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` all document
  `Azureomycin` as a no-hit placeholder that should keep the local kg-microbe
  registry identifier.
- The SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 516 is an
  own-identifier `skos:exactMatch` to
  `kgmicrobe.compound:azureomycin`, not an exact match to `azureomycin A` or
  `azureomycin B`.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  individual record.

## Completeness

- The exact placeholder identifier, ontology mapping, provisional
  `SELECTIVE_AGENT` role, no-hit note, SSSOM row, and aggregate copy are
  populated.
- No chemical structure, CAS RN, supplied form, or component list should be
  invented while the exact external identity remains unresolved.

## Recommended Edits

- None.
