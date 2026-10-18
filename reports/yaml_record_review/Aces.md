# `data/ingredients/mapped/Aces.yaml`

## Verdict

Pass with minor issues. This record is intentionally a rejected tombstone after
the ACES buffer was merged into `CHEBI:39060`; the live pointer, merge history,
aggregate copy, and absent SSSOM export pass. Two stale row-review TSVs still
mention the pre-merge `CHEBI:39061` grouping class.

## Identity

- Reviewed record: `data/ingredients/mapped/Aces.yaml`.
- Tombstone status: `mapping_status: REJECTED`.
- Current pointer: `identifier: CHEBI:39060` with
  `ontology_mapping.ontology_id: CHEBI:39060`, source `CHEBI`, and
  `mapping_quality: EXACT_MATCH`.
- The retained record,
  `data/ingredients/mapped/N-_2-acetamido-2-aminoethanesulfonic_Acid.yaml`,
  carries the active `CHEBI:39060` identity, the `ACES` raw synonym merged from
  `CHEBI:39061`, and the 15 CultureMech occurrences transferred to the merged
  buffer term.
- Local OAK and the official ChEBI page resolve `CHEBI:39060` to
  `N-(2-acetamido)-2-aminoethanesulfonic acid` with formula `C4H10N2O4S` and
  InChIKey `DBXNUXBLKRLWFA-UHFFFAOYSA-N`.
- Local OAK resolves `CHEBI:39061` only as the structureless `ACES` class,
  matching the merge rationale.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Abyssomicin_G.yaml data/ingredients/mapped/Abyssomicin_H.yaml data/ingredients/mapped/Acacetin.yaml data/ingredients/mapped/Aces.yaml data/ingredients/mapped/Acetaldehyde.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Aces.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15335 CHEBI:15343 CHEBI:39060 CHEBI:39061`:
  returned the expected labels, exact synonyms, and related synonyms for
  `CHEBI:15335`, `CHEBI:15343`, `CHEBI:39060`, and `CHEBI:39061`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15335 CHEBI:15343 CHEBI:39060 CHEBI:39061`:
  returned formula and structure metadata for `CHEBI:15335`, `CHEBI:15343`,
  and `CHEBI:39060`; `CHEBI:39061` resolved only as the structureless `ACES`
  class.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The `MERGED_INTO`, `REFRESHED_TOMBSTONE_ONTOLOGY_ID`, and
  `CORRECTED` history entries explain the intended tombstone shape:
  occurrences moved to `CHEBI:39060`, SSSOM rows were dropped, the stale
  `CHEBI:39061` ontology pointer was refreshed to `CHEBI:39060`, and
  `kg_microbe_node_id` was brought back into same-prefix agreement.
- Hidden/ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`
  found no active `MIM:Aces` row and no active `CHEBI:39061` row.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` still describe the old
  `MIM:Aces` to `CHEBI:39061` mapping as confirmed; those rows are stale after
  the August 2026 merge but do not currently re-export `MIM:Aces`.
- `mappings/other_cross_record_baseline.tsv` still has an `UNREVIEWED`
  cross-record row connecting the active retained record's `ACES` raw synonym
  to this rejected tombstone.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the tombstone YAML,
  the active retained YAML, aggregate copies, stale row-review rows, the stale
  cross-record baseline row, and ignored aggregate backups.

## Completeness

- The tombstone is complete enough for a rejected duplicate: no active SSSOM
  export remains, and the retained record owns CAS, formula, InChI, SMILES,
  occurrences, the `ACES` synonym, and any future buffer-role curation.
- The stale row-review TSVs and cross-record baseline row are the only
  remaining non-live references found by the bounded hidden/ignored-inclusive
  search.

## Recommended Edits

- Optionally refresh the derived row-review/cross-record review tables so
  `mappings/ingredient_mappings_oak_ols_review.tsv`,
  `mappings/ingredient_mappings_row_review_manifest.tsv`, and
  `mappings/other_cross_record_baseline.tsv` no longer describe `MIM:Aces` as
  an active `CHEBI:39061` mapping or active duplicate candidate. No tombstone,
  SSSOM, or ChEBI pointer edit is required.
