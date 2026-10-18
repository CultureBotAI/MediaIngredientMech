# `data/ingredients/mapped/Argon.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `argon(0)`, preserves the `#Ar` raw
duplicate as traceable source text, and the CAS, formula, structure, occurrence
counts, SSSOM row, and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Argon.yaml`.
- Identifier and grounding: `identifier: CHEBI:49474` with
  `ontology_mapping.ontology_id: CHEBI:49474`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:49474` to non-obsolete ChEBI `argon(0)`, formula
  `Ar`, CAS `7440-37-1`, SMILES `[Ar]`, and the stored InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the ChEBI atomic
  entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arginine.yaml data/ingredients/mapped/Argon.yaml data/ingredients/mapped/Aristolochic_Acid.yaml data/ingredients/mapped/Aromatic_Compound.yaml data/ingredients/mapped/Aromatic_Hydrocarbon.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Argon.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned formula, SMILES, InChI, InChIKey, and CAS metadata for
  `CHEBI:49474`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned the canonical `argon(0)` label and related `[Ar]` synonym for
  `CHEBI:49474`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ChEBI xref for `CHEBI:49474` includes the stored CAS `7440-37-1`.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` shows the absorbed
  `UNMAPPED_0307` `#Ar` raw surface had an exact synonym candidate for argon,
  matching the merge history.
- `mappings/ingredient_mappings.sssom.tsv` row 475 maps `MIM:Argon` to
  `CHEBI:49474` with `skos:exactMatch`, the retained `Ar` and `#Ar` surfaces,
  CAS `7440-37-1`, and a `SYNONYM_ENRICH` row-review trailer.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row, row-review
  rows, and duplicate-review audit row.

## Completeness

- CAS, formula, SMILES, InChI, exact ChEBI identity, raw duplicate surface,
  CultureMech occurrence counts, curation history, `ingredient_type`, SSSOM,
  and the aggregate copy are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.

## Recommended Edits

- None.
