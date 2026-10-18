# `data/ingredients/mapped/Aristolochic_Acid.yaml`

## Verdict

Pass. The record denotes CAS-backed ChEBI `aristolochic acid A`, and the CAS,
formula, SMILES, InChI, exact synonym, SSSOM row, and aggregate copy are
synchronized.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Aristolochic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:2825` with
  `ontology_mapping.ontology_id: CHEBI:2825`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:2825` to non-obsolete ChEBI `aristolochic acid A`,
  formula `C17H11NO7`, CAS `313-67-7`, KEGG Compound `C08469`, the stored
  SMILES, the stored InChI, and the stored exact structural synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the ChEBI molecular
  entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arginine.yaml data/ingredients/mapped/Argon.yaml data/ingredients/mapped/Aristolochic_Acid.yaml data/ingredients/mapped/Aromatic_Compound.yaml data/ingredients/mapped/Aromatic_Hydrocarbon.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Aristolochic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned formula, SMILES, InChI, InChIKey, CAS, and KEGG metadata for
  `CHEBI:2825`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned the canonical `aristolochic acid A` label and the stored exact ChEBI
  synonym for `CHEBI:2825`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The record was created by an explicit CultureBotHT CAS-to-ChEBI lookup, and
  the current ChEBI target carries the stored CAS `313-67-7`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Aristolochic_Acid` to `CHEBI:2825` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no mapping
  repair was needed.
- `mappings/ingredient_mappings.sssom.tsv` row 476 maps
  `MIM:Aristolochic_Acid` to `CHEBI:2825` with `skos:exactMatch`, CAS
  `313-67-7`, the exact structural synonym, and a `CONFIRMED` row-review
  trailer.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row, and
  row-review rows.

## Completeness

- CAS, formula, SMILES, InChI, exact synonym, ChEBI identity, curation history,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS import rather than a media recipe ingredient.
- No role, component, environmental context, discussion, or dataset entry is
  needed.

## Recommended Edits

- None.
