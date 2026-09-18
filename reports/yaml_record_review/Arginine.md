# `data/ingredients/mapped/Arginine.yaml`

## Verdict

Needs curation. The generic ChEBI arginine identity, formula, structure, 43
CultureMech memberships, nitrogen-source role, SSSOM row, and aggregate copy
pass, but four CultureMech role/property strings remain in `synonyms`.

## Identity

- Reviewed record: `data/ingredients/mapped/Arginine.yaml`.
- Identifier and grounding: `identifier: CHEBI:29016` with
  `ontology_mapping.ontology_id: CHEBI:29016`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:29016` to non-obsolete ChEBI `arginine`, formula
  `C6H14N4O2`, the stored SMILES, the stored InChI, and exact synonym
  `Arginine`.
- The generic `Arginine` record is intentionally separate from the
  stereospecific `data/ingredients/mapped/L-arginine.yaml` record even though
  both carry CAS `74-79-3`; the local merge notes flag this family as benign
  registry granularity.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the ChEBI molecular
  entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arginine.yaml data/ingredients/mapped/Argon.yaml data/ingredients/mapped/Aristolochic_Acid.yaml data/ingredients/mapped/Aromatic_Compound.yaml data/ingredients/mapped/Aromatic_Hydrocarbon.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arginine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned formula, SMILES, InChI, and InChIKey metadata for `CHEBI:29016`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:29016 CHEBI:49474 CHEBI:2825 CHEBI:33655 CHEBI:33658`:
  returned the canonical `arginine` label and exact/related ChEBI synonyms for
  `CHEBI:29016`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has 43 `CHEBI:29016`
  memberships, matching `occurrence_statistics: 43/43`.
- `mappings/ingredient_mappings.sssom.tsv` row 474 maps `MIM:Arginine` to
  `CHEBI:29016` with `skos:exactMatch`, the kg-microbe synonyms, CAS
  `74-79-3`, and a `CONFIRMED` row-review trailer.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the
  `L-arginine` synonym-enrichment row as already represented and the old
  kg-microbe row as an expected registry identifier.
- `nutritional_roles.NITROGEN_SOURCE` is backed by the imported CultureMech
  role text, but the four `RAW_TEXT` CultureMech synonym strings are
  role/property metadata, not ingredient labels.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row, row-review
  rows, CultureMech recipe-membership rows, and the separate `L-arginine`
  sibling.

## Completeness

- CAS, formula, SMILES, InChI, ChEBI identity, CultureMech occurrences,
  nitrogen-source role, curation history, `ingredient_type`, SSSOM, and the
  aggregate copy are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The bad raw synonym strings are the only consequential gap.

## Recommended Edits

- In `data/ingredients/mapped/Arginine.yaml`, remove the four `RAW_TEXT`
  CultureMech role/property strings from `synonyms`; keep their nitrogen-source
  content on `nutritional_roles.NITROGEN_SOURCE`.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run linkml-term-validator validate-data data/ingredients/mapped/Arginine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
