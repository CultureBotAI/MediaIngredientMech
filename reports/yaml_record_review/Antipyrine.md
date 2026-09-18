# `data/ingredients/mapped/Antipyrine.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `antipyrine`; the CAS, formula,
kg-microbe synonyms, four CultureMech recipe memberships, SSSOM row, and
aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Antipyrine.yaml`.
- Identifier and grounding: `identifier: CHEBI:31225` with
  `ontology_mapping.ontology_id: CHEBI:31225`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:31225` to non-obsolete ChEBI
  `antipyrine` with CAS `60-80-0`, formula `C11H12N2O`, the exact synonym
  `1,5-dimethyl-2-phenyl-1,2-dihydro-3H-pyrazol-3-one`, SMILES, and the stored
  InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Antimonate.yaml data/ingredients/mapped/Antimycin_A.yaml data/ingredients/mapped/Antimycin_A3.yaml data/ingredients/mapped/Antipyrine.yaml data/ingredients/mapped/Aphidicolin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Antipyrine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30295 CHEBI:2762 CHEBI:197950 CHEBI:31225 CHEBI:2766`:
  returned formula, SMILES, InChI, InChIKey, CAS, KEGG, and HMDB metadata for
  `CHEBI:31225`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:30295 CHEBI:2762 CHEBI:197950 CHEBI:31225 CHEBI:2766`:
  returned the canonical `antipyrine` label and ChEBI aliases corresponding to
  the stored synonyms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ChEBI xref for `CHEBI:31225` includes the stored CAS `60-80-0`, and the
  exact/related ChEBI alias set covers the six exact synonym strings imported
  from kg-microbe.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Antipyrine` to `CHEBI:31225` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no mapping
  repair was needed.
- `mappings/culturemech_recipe_membership.tsv` has four `CHEBI:31225` rows,
  matching `total_occurrences: 4` and `media_count: 4`.
- `mappings/ingredient_mappings.sssom.tsv` row 440 maps `MIM:Antipyrine` to
  `CHEBI:31225` with `skos:exactMatch`, the CAS, all six stored synonyms, and
  a `CONFIRMED` trailer.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, `scripts`, and non-review `reports` found the active YAML,
  aggregate copy, SSSOM row, CultureMech membership rows, and row-review rows.

## Completeness

- CAS, formula, SMILES, InChI, synonyms, CultureMech occurrence counts,
  curation history, `ingredient_type`, SSSOM, and the aggregate copy are
  populated.
- No component, role, environmental context, discussion, or dataset entry is
  needed.

## Recommended Edits

- None.
