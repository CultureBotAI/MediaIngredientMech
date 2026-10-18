# `data/ingredients/mapped/4-hydroxybutyrate.yaml`

## Verdict

Pass, none. The `CHEBI:16724` anion identity, exact ChEBI label grounding,
microbedecoder occurrence provenance, chemistry, SSSOM row, and aggregate copy
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-hydroxybutyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16724` with
  `ontology_mapping.ontology_id: CHEBI:16724`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI search resolves `CHEBI:16724` to active
  `4-hydroxybutyrate`, defined as the anion formed by removing the carboxyl
  proton from 4-hydroxybutyric acid.
- PubChem lookup for `4-hydroxybutyrate` resolves to CID `3037032` with formula
  `C4H7O3-` and the same deprotonated InChI stored in the record.
- The record intentionally denotes the anion, not the separate neutral
  `4-hydroxybutyric_Acid.yaml` record.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-hydroxybutyrate.yaml data/ingredients/mapped/4-hydroxybutyric_Acid.yaml data/ingredients/mapped/4-hydroxychalcone.yaml data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml data/ingredients/mapped/4-methylumbelliferone_Beta-d-glucuronide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-hydroxybutyrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed in the immediately preceding batch; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The active microbedecoder import row is exact-label evidence:
  `kgmicrobe.trait:4_hydroxybutyrate` supplied raw label `4-hydroxybutyrate`
  in `BacDive_Metabolite_utilization` with count 64.
- The OLS search hit is active and exact-label to both the source string and
  `ontology_label`.
- The stored formula, SMILES, InChI, and molecular weight all describe
  monoanionic 4-hydroxybutyrate rather than neutral 4-hydroxybutyric acid.
- The `source_occurrences` block correctly keeps the 64 microbedecoder
  occurrences separate from verified CultureMech recipe counts
  `total_occurrences: 0` and `media_count: 0`.
- The SSSOM row maps `MIM:4-hydroxybutyrate` to `CHEBI:16724` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and the
  `manual:review-ingredients|APPROVED|2026-08-04` review marker.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, microbedecoder source row, generated
  docs, stale advisory rows, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence counts, and
  `ingredient_type` are populated.
- CAS is correctly absent; the current ChEBI anion search result does not carry
  a CAS xref.
- No synonyms, roles, components, environment, or discussion entries need
  review.

## Recommended Edits

No YAML edit is required for this record.
