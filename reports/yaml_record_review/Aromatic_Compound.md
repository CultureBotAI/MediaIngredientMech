# `data/ingredients/mapped/Aromatic_Compound.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `aromatic compound`, retains the
kgm-metatraits degradation surface as raw text, and the class grounding, SSSOM
row, and aggregate copy are synchronized.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Aromatic_Compound.yaml`.
- Identifier and grounding: `identifier: CHEBI:33655` with
  `ontology_mapping.ontology_id: CHEBI:33655`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:33655` to non-obsolete ChEBI
  `aromatic compound`, with exact synonyms `aromatic compounds` and
  `aromatic molecular entity`.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the imported
  kgm-metatraits chemical class.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arginine.yaml data/ingredients/mapped/Argon.yaml data/ingredients/mapped/Aristolochic_Acid.yaml data/ingredients/mapped/Aromatic_Compound.yaml data/ingredients/mapped/Aromatic_Hydrocarbon.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Aromatic_Compound.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned ChEBI metadata for `CHEBI:33655`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned the canonical `aromatic compound` label and exact ChEBI synonyms for
  `CHEBI:33655`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The record was imported from `kgm.metatraits.special:aromatic_compound` and
  exact-matches the ChEBI class with the same label.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Aromatic_Compound` to `CHEBI:33655` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no mapping
  repair was needed.
- `mappings/ingredient_mappings.sssom.tsv` row 477 maps
  `MIM:Aromatic_Compound` to `CHEBI:33655` with `skos:exactMatch`, the two
  ChEBI synonyms, the raw `degradation: aromatic compound` surface, and a
  `CONFIRMED` row-review trailer.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row, and
  row-review rows.

## Completeness

- ChEBI class identity, synonyms, recovered raw kgm-metatraits surface,
  curation history, `ingredient_type`, SSSOM, and the aggregate copy are
  populated.
- Chemical properties are correctly absent because the record denotes a ChEBI
  class rather than one fixed molecular structure.
- No role, component, environmental context, discussion, or dataset entry is
  needed.

## Recommended Edits

- None.
