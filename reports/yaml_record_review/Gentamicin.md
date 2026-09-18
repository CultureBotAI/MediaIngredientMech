# `data/ingredients/mapped/Gentamicin.yaml`

## Verdict

Needs curation, with a major final-SSSOM synonym issue. The curator-ratified
grounding to `CHEBI:17833` gentamycin passes, but final SSSOM exports the raw
CultureMech phrase `gentamicin (if needed)` as if it were a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Gentamicin.yaml`.
- Identifier and grounding: `identifier: CHEBI:17833` with matching
  `ontology_mapping.ontology_id`, canonical label `gentamycin`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, and
  `mapping_status: MAPPED`.
- OLS4 resolved `CHEBI:17833` as active gentamycin with `Gentamicin` as a
  related synonym and CAS xref `1403-66-3`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Geneticin_G418.yaml data/ingredients/mapped/Gentamicin.yaml data/ingredients/mapped/Gentamicin_C2b.yaml data/ingredients/mapped/Gentamicin_Sulfate_Salt.yaml data/ingredients/mapped/Gentibiose.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Geneticin_G418.yaml data/ingredients/mapped/Gentamicin.yaml data/ingredients/mapped/Gentamicin_C2b.yaml data/ingredients/mapped/Gentamicin_Sulfate_Salt.yaml data/ingredients/mapped/Gentibiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI synonym match, CultureMech occurrence count, MicrobeDecoder
  source occurrences, raw `gentamicin (if needed)` synonym, and mapping
  evidence as the per-record YAML.
- The curation history records the final issue `#207` ruling: this record must
  stay on locally resolvable `CHEBI:17833` and must not be moved back to
  `CHEBI:759884` without a new curator decision.
- The final SSSOM row maps `MIM:Gentamicin` to `CHEBI:17833` by
  `skos:exactMatch`, with object label `gentamycin` and the expected manual
  promotion marker.
- Major: final SSSOM exports `gentamicin (if needed)` in `other`. That token
  comes from a CultureMech recipe surface form, includes conditional recipe
  prose, and is not an OLS4 synonym of `CHEBI:17833`.
- Minor: the first `ontology_mapping.evidence` note still repeats the outdated
  premise that `CHEBI:759884` "does not resolve in CHEBI at all"; the later
  manual evidence and curator ruling correct that claim, but the active
  mapping evidence remains internally stale.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, the residual/deferred rows for `CHEBI:759884`, the issue `#207`
  grounding script, generated indexes, ignored aggregate backups, and the
  CultureMech residual alias row for `gentamicin (if needed)`.

## Completeness

- The gentamicin identity, explicit curator ruling, CultureMech occurrences,
  MicrobeDecoder source occurrences, and final SSSOM row are populated.
- One raw recipe phrase needs cleanup before the final SSSOM `other` field is
  clean.

## Recommended Edits

- Major: remove or retag `gentamicin (if needed)` so final SSSOM stops
  exporting conditional recipe text as a synonym.
- Minor: update the first mapping-evidence note so it no longer says
  `CHEBI:759884` does not resolve in ChEBI at all, while preserving the final
  issue `#207` curator ruling.
