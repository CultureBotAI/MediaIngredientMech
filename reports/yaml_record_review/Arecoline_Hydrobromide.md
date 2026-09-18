# `data/ingredients/mapped/Arecoline_Hydrobromide.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `arecoline hydrobromide`, and its CAS,
formula, SMILES, InChI, exact synonym, SSSOM row, and aggregate copy are
synchronized.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Arecoline_Hydrobromide.yaml`.
- Identifier and grounding: `identifier: CHEBI:233150` with
  `ontology_mapping.ontology_id: CHEBI:233150`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:233150` to non-obsolete ChEBI
  `arecoline hydrobromide`, formula `C8H13NO2.HBr`, CAS `300-08-3`, the stored
  SMILES, the stored InChI, and the stored exact structural synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arbutin.yaml data/ingredients/mapped/Ardacin_A.yaml data/ingredients/mapped/Ardacin_B.yaml data/ingredients/mapped/Ardacin_C.yaml data/ingredients/mapped/Arecoline_Hydrobromide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arecoline_Hydrobromide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:233150`:
  returned formula, SMILES, InChI, InChIKey, and CAS metadata for
  `CHEBI:233150`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:233150`: returned
  the canonical `arecoline hydrobromide` label and the stored exact ChEBI
  synonym.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ChEBI xref for `CHEBI:233150` includes the stored CAS `300-08-3`, and the
  exact structural synonym is also an exact ChEBI synonym.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Arecoline_Hydrobromide` to `CHEBI:233150` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no mapping
  repair was needed.
- `mappings/ingredient_mappings.sssom.tsv` row 473 maps
  `MIM:Arecoline_Hydrobromide` to `CHEBI:233150` with `skos:exactMatch`, CAS
  `300-08-3`, the exact structural synonym, and a `CONFIRMED` row-review
  trailer.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row, and
  row-review rows.

## Completeness

- CAS, formula, SMILES, InChI, exact synonym, ChEBI identity, curation history,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  import rather than a media recipe ingredient.
- No role, component, environmental context, discussion, or dataset entry is
  needed.

## Recommended Edits

- None.
