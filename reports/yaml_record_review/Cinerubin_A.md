# `data/ingredients/mapped/Cinerubin_A.yaml`

## Verdict

Needs curation, major. The local `kgmicrobe.compound:cinerubin_a` placeholder
still avoids the wrong CHEBI siblings `Cinerubin R`, `Cinerubin B`, and
`Cinerubin Y`, but current OLS now exposes an active MeSH `cinerubine A`
candidate that is not recorded in the stale May placeholder review.

## Identity

- Reviewed record: `data/ingredients/mapped/Cinerubin_A.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:cinerubin_a`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:cinerubin_a`,
  `ontology_label: Cinerubin A`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS search for `Cinerubin A` still returns CHEBI hits only for other
  cinerubin variants, matching the 2026-05-10 manual decision not to promote to
  `CHEBI:214436`, `CHEBI:218086`, or `CHEBI:224126`.
- The same live OLS search now returns active MeSH `C000481` labelled
  `cinerubine A`; direct NLM lookup confirms `C000481` is an active SCR
  chemical with that label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cimicifugoside_H1.yaml data/ingredients/mapped/Cinerubin_A.yaml data/ingredients/mapped/Cinerubin_R.yaml data/ingredients/mapped/Cinnamic_Acid.yaml data/ingredients/mapped/Cinnamycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cinerubin_R.yaml data/ingredients/mapped/Cinnamic_Acid.yaml data/ingredients/mapped/Cinnamycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three CHEBI-scoped records in this batch. `Cinerubin_A` was
  intentionally skipped because its `kgmicrobe.compound` placeholder CURIE is a
  local registry ID outside Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact local `MIM:Cinerubin_A` SSSOM row, the stale
  `NO_EXACT_CANDIDATE` 2026-05-06 placeholder search row, the 2026-05-10
  manual rejection of the wrong CHEBI R/B/Y variants, the expected local
  unknown-term triage row, and matching aggregate/docs rows.
- Hidden/ignored-inclusive search over the same tree found no active
  `mesh:C000481` or `cinerubine A` representation, so the current MeSH
  candidate has not already been reviewed into the repository.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:cinerubin_a` rows, matching the explicit 0/0
  media-recipe `occurrence_statistics`.
- The record carries no role, component, chemical-property, or environment
  claims.

## Completeness

- The local placeholder SSSOM row, zero occurrence count, aggregate copy, and
  docs row agree.
- External grounding is now incomplete because MeSH `C000481` must either be
  accepted as the exact identity for Cinerubin A or explicitly rejected as a
  non-exact spelling/variant near miss.

## Recommended Edits

- Review `mesh:C000481` against the Cinerubin A source identity; either promote
  `data/ingredients/mapped/Cinerubin_A.yaml` to that MeSH identifier or record a
  rejected-candidate discussion explaining why MeSH `cinerubine A` is not exact.
- Rerun strict validation, term/external-prefix validation as applicable,
  aggregate/roundtrip verification, and `scripts/validate_sssom_invariants.py`.
