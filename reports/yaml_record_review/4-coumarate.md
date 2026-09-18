# `data/ingredients/mapped/4-coumarate.yaml`

## Verdict

Pass, none. The `CHEBI:32373` anion identity, exact ChEBI label grounding,
microbedecoder occurrence provenance, chemistry, SSSOM row, and aggregate copy
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-coumarate.yaml`.
- Identifier and grounding: `identifier: CHEBI:32373` with
  `ontology_mapping.ontology_id: CHEBI:32373`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:32373` is active, resolves to
  `4-coumarate`, is defined as the conjugate base of 4-coumaric acid, has
  formula `C9H7O3`, charge `-1`, SMILES `[H]C(=Cc1ccc(O)cc1)C(=O)[O-]`, and
  the stored InChI.
- The record intentionally denotes the anion, not neutral 4-coumaric acid.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-coumarate.yaml data/ingredients/mapped/4-dihydroxy-biphenyl.yaml data/ingredients/mapped/4-guanidinobutyric_Acid.yaml data/ingredients/mapped/4-hydroxy-L-proline.yaml data/ingredients/mapped/4-hydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-coumarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2,951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, K; Rule B4 was skipped because the
  sibling `kg-microbe` ontology transforms are absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed;
  `docs/data/` is fresh and every curated label is published.

## Evidence

- The active microbedecoder import row is exact-label evidence:
  `kgmicrobe.trait:4_coumarate` supplied raw label `4-coumarate` in
  `BacDive_Metabolite_utilization` with count 1.
- The OLS/ChEBI term is active and exactly matches both the raw label and the
  record's `ontology_label`.
- The stored formula, SMILES, InChI, and molecular weight match the current
  ChEBI term and all describe the same singly deprotonated anion.
- The `source_occurrences` block correctly keeps the single microbedecoder
  occurrence separate from verified CultureMech recipe counts
  `total_occurrences: 0` and `media_count: 0`.
- The SSSOM row maps `MIM:4-coumarate` to `CHEBI:32373` with
  `skos:exactMatch`, `semapv:LexicalMatching`, source `MIM:microbedecoder`,
  and the `manual:review-ingredients|APPROVED|2026-08-04` review marker.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, microbedecoder source row, generated
  docs, stale advisory research rows, and ignored aggregate backups.

## Completeness

- CAS is correctly absent; the current ChEBI anion record has no CAS xref.
- No synonyms, roles, components, environment, datasets, or discussion entries
  are expected for this exact anion-only microbedecoder import.
- No unresolved source-form issue remains in active curated data; the stale
  research-validation rows predate the explicit single-ingredient
  classification and did not inspect a contradictory source.

## Recommended Edits

No YAML edit is required for this record.
