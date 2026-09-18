# `data/ingredients/mapped/Aromatic_Hydrocarbon.yaml`

## Verdict

Pass. The record now denotes ChEBI `arene`, the ChEBI class that exactly names
aromatic hydrocarbons; the retired `polycyclic arene` over-narrowing is confined
to history and row-review artifacts.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Aromatic_Hydrocarbon.yaml`.
- Identifier and grounding: `identifier: CHEBI:33658` with
  `ontology_mapping.ontology_id: CHEBI:33658`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:33658` to non-obsolete ChEBI `arene`, with the
  definition `Any monocyclic or polycyclic aromatic hydrocarbon` and exact
  synonyms `arene` and `arenes`.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the imported
  kgm-metatraits chemical class.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arginine.yaml data/ingredients/mapped/Argon.yaml data/ingredients/mapped/Aristolochic_Acid.yaml data/ingredients/mapped/Aromatic_Compound.yaml data/ingredients/mapped/Aromatic_Hydrocarbon.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Aromatic_Hydrocarbon.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned ChEBI definition metadata for `CHEBI:33658`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned the canonical `arene` label and exact ChEBI synonyms for
  `CHEBI:33658`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `scripts/reground_aromatic_hydrocarbon.py` records the maintained repair from
  the old `CHEBI:33848`/`kgmicrobe.compound:aromatic_hydrocarbon` shape to
  `CHEBI:33658`, and the active curation history has the same
  `reground_aromatic_hydrocarbon` event.
- `mappings/ingredient_mappings.sssom.tsv` row 478 now maps
  `MIM:Aromatic_Hydrocarbon` to `CHEBI:33658` with `skos:exactMatch`.
- The lingering `CHEBI:33848` row-review entries are stale review artifacts for
  the pre-repair polycyclic-arene target; a hidden, ignored-inclusive search
  across the full checkout, excluding the old `data/curated/backups` snapshots
  and noncanonical batch-review output, found no active YAML or active SSSOM row
  that still maps `Aromatic_Hydrocarbon` to `CHEBI:33848`.

## Completeness

- ChEBI class identity, curation history, `ingredient_type`, SSSOM, and the
  aggregate copy are populated.
- Chemical properties are correctly absent because the record denotes a ChEBI
  class rather than one fixed molecular structure.
- No role, component, environmental context, discussion, or dataset entry is
  needed.

## Recommended Edits

- None.
