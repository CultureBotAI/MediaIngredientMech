# `data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml`

## Verdict

Needs curation, major. The `CHEBI:355715` beta-D-galactoside identity, synonym
mapping, chemistry, and SSSOM exact-match row pass, but two action-prefixed
source labels are stored and exported as exact synonyms of the chemical.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:355715` with
  `ontology_mapping.ontology_id: CHEBI:355715`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:355715` is active, resolves to
  `4-nitrophenyl-beta-D-galactoside`, has formula `C12H15NO8`, neutral charge,
  CAS `3150-24-1`, the stored SMILES, the stored InChI, and the IUPAC synonym
  `4-nitrophenyl-beta-D-galactopyranoside`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-nitrophenyl_6-O-phosphono-beta-D-galactoside.yaml data/ingredients/mapped/4-nitrophenyl_Alpha-D-galactoside.yaml data/ingredients/mapped/4-nitrophenyl_Alpha-D-glucopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-glucopyranoside.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed earlier in this all-record review; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The active ChEBI term, formula, CAS, SMILES, InChI, and IUPAC synonym all
  support the record's synonym-level grounding to `CHEBI:355715`.
- The exact ChEBI synonym
  `4-nitrophenyl-beta-D-galactopyranoside` is acceptable as an
  `EXACT_SYNONYM`.
- Major: the `RAW_TEXT` synonyms
  `degradation: 4-nitrophenyl beta-D-galactopyranoside` and
  `hydrolysis: 4-nitrophenyl beta-D-galactopyranoside` include upstream
  assay-action prefixes and are not exact chemical names. They leak through
  the aggregate copy, the SSSOM `other` column, and generated `label_index`
  as synonyms for `CHEBI:355715`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, `src`,
  `scripts`, `tests`, `conf`, `.github`, and `.claude` found only the active
  YAML, aggregate copy, SSSOM row, generated docs, and ignored aggregate
  backups for the two action-prefixed strings.

## Completeness

- Formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type` are
  populated.
- No roles, components, environment, or discussion entries need review.
- `occurrence_statistics` has no `source_occurrences`; the created-from-import
  history still preserves the kgm-metatraits source preset and source ID for
  this legacy metatraits special record.

## Recommended Edits

1. Remove or reject the two action-prefixed `RAW_TEXT` synonyms in
   `data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml` and
   `data/curated/mapped_ingredients.yaml`, then regenerate SSSOM and docs so
   `degradation:` and `hydrolysis:` strings no longer publish as exact synonym
   labels.
