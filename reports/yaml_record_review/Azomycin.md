# `data/ingredients/mapped/Azomycin.yaml`

## Verdict

Needs curation; severity minor. The MicrobeDecoder raw label was correctly
promoted to `CHEBI:67135` `2-nitroimidazole` by the documented
`SYNONYM_MATCH`, and the chemistry, SSSOM row, and aggregate copy pass, but the
top-level `notes` still repeat stale pre-promotion text claiming there was no
CHEBI match and curator review was needed.

## Identity

- Reviewed record: `data/ingredients/mapped/Azomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:67135` with
  `ontology_mapping.ontology_id: CHEBI:67135`,
  `ontology_label: 2-nitroimidazole`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:67135` to non-obsolete `2-nitroimidazole` with exact
  synonym `Azomycin`, CAS `527-73-1`, formula `C3H3N3O2`, and the same InChI
  and SMILES stored locally.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azithromycin.yaml data/ingredients/mapped/Azlocillin.yaml data/ingredients/mapped/Azlocillin_Sodium_Salt.yaml data/ingredients/mapped/Azomycin.yaml data/ingredients/mapped/Aztreonam.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Azomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:67135` confirmed that `Azomycin` is a synonym of the
  active ChEBI `2-nitroimidazole` term and that the local structure fields
  match ChEBI.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 514 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The 2026-08-06 curation event records the promotion from `UNMAPPED_0798` to
  `CHEBI:67135` and the `SYNONYM_MATCH` decision.
- The raw `Azomycin` synonym preserves the MicrobeDecoder source text, and
  `data/custom/microbedecoder/unmapped_labels.tsv` plus
  `data/custom/microbedecoder/ingredient_candidates.tsv` record one
  `azomycin` source occurrence in `BacDive_Metabolite_production`.
- `mappings/record_research_validation.tsv` still contains advisory stale-note
  findings for this record; those findings agree that the promoted
  `CHEBI:67135` term is active and that the old free-text import note is stale.

## Completeness

- The exact synonym-grounded identifier, raw synonym, formula, InChI, SMILES,
  source occurrence, SSSOM row, and aggregate copy are populated.
- The top-level `notes` field is stale and should no longer say that no CHEBI
  match was found.

## Recommended Edits

- Remove or rewrite the top-level `notes` in
  `data/ingredients/mapped/Azomycin.yaml`, synchronize
  `data/curated/mapped_ingredients.yaml`, and rerun focused strict and term
  validation plus flat-export coverage.
