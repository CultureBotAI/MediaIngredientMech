# `data/ingredients/mapped/Azacolutin.yaml`

## Verdict

Pass. The record intentionally preserves the local
`kgmicrobe.compound:azacolutin` placeholder after prior no-hit review, a current
exact OLS search still found no `CHEBI`, `MESH`, or `NCIT` candidate, and the
aggregate and SSSOM rows carry the same kg-microbe registry identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Azacolutin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:azacolutin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:azacolutin`,
  `ontology_label: Azacolutin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, and `mapping_status: MAPPED`.
- OLS4 exact search across `CHEBI`, `MESH`, and `NCIT` returned zero exact
  matches for `Azacolutin`, matching the 2026-05-06 placeholder review.
- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the expected
  placeholder review rows and no mapped duplicate that would justify replacing
  the kg-microbe identity with an external identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azacolutin.yaml data/ingredients/mapped/Azadirachtin.yaml data/ingredients/mapped/Azaserine.yaml data/ingredients/mapped/Azelaate.yaml data/ingredients/mapped/Azelaic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `kgmicrobe.compound` is a non-OBO prefix; the `just validate-terms` recipe
  documents that these prefixes are covered by product validation rather than
  OAK label lookup.
- OLS4 exact lookup for `Azacolutin` in `CHEBI`, `MESH`, and `NCIT` returned no
  exact candidate.
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
  `Azacolutin` as a no-hit placeholder that should keep the local kg-microbe
  registry identifier.
- The SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 506 is an
  own-identifier `skos:exactMatch` to
  `kgmicrobe.compound:azacolutin`, not an asserted exact match to a broader
  external term.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  individual record.

## Completeness

- The exact placeholder identifier, ontology mapping, SSSOM row, aggregate
  copy, and explanatory no-hit note are populated.
- The 0/0 occurrence count is correct for this kg-microbe placeholder-derived
  record; the hidden/ignored-inclusive search found no MicrobeDecoder,
  CultureBotHT, or CultureMech occurrence rows for `Azacolutin`.
- No chemical structure, CAS RN, roles, supplied form, or components should be
  invented while the external chemical identity remains unresolved.

## Recommended Edits

- None.
