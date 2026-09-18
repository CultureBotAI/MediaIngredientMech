# `data/ingredients/mapped/23-butanediol.yaml`

## Verdict

Needs curation, major. The active `CHEBI:62064` identity, chemistry,
occurrence count, SSSOM row, aggregate row, and database-backed `CARBON_SOURCE`
role pass, but a raw role/property annotation remains in `synonyms` and is
therefore still exported as a label.

## Identity

- Reviewed record: `data/ingredients/mapped/23-butanediol.yaml`.
- Identifier and grounding: `identifier: CHEBI:62064` with
  `ontology_mapping.ontology_id: CHEBI:62064`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:62064`
  resolves to `butane-2,3-diol` and lists formula `C4H10O2`.
- The preferred MIM label `2,3-butanediol` is a conventional synonym for the
  same neutral diol; ChEBI also lists `2,3-Butanediol`, the populated
  `2,3-Butylene glycol` and `2,3-Dihydroxybutane` synonyms, and CAS
  `513-85-9`.
- The `3-butanediol` raw source label is intentionally retained only as
  `RAW_TEXT` after #213 documented it as a microbedecoder truncation artifact of
  `2,3-butanediol`; no separate exact row was minted for it.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/23-butanediol.yaml data/ingredients/mapped/23-dihydroxybenzoic_Acid.yaml data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml data/ingredients/mapped/24-Dichlorophenoxyacetic_acid.yaml data/ingredients/mapped/24-Dihydroxybenzoic_acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/23-butanediol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:23-butanediol` to `CHEBI:62064` row and keeps absorbed
  `3-butanediol` in the SSSOM `other` field rather than as a new subject row.

## Evidence

- The active ChEBI page and OAK/OLS review both confirm the exact identity.
- `mappings/culturemech_recipe_membership.tsv` and `occurrence_statistics` both
  report seven CultureMech recipe occurrences.
- `nutritional_roles.CARBON_SOURCE` is supported by imported CultureMech
  database-entry evidence with the original role text preserved in the curator
  note.
- Major: `synonyms` still includes the raw text `Role: Carbon source;
  Properties: Organic compound, Defined component, Simple component`, which is a
  role/property annotation rather than an ingredient label.
- Stale or advisory: `mappings/record_research_validation.tsv` still flags
  `3-butanediol` as a locant-incomplete synonym. The active YAML already keeps
  it as `RAW_TEXT` with explicit #213 provenance, so that row does not refute
  the current exact identity. The same TSV correctly flags the non-label
  role/property raw text.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, CultureMech membership, OAK/OLS review, and advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, InChI, and SMILES are populated for the active ChEBI-backed
  ingredient.
- The remaining defect is consequential because generated synonym outputs
  include non-label text.

## Recommended Edits

1. Remove `Role: Carbon source; Properties: Organic compound, Defined component,
   Simple component` from `data/ingredients/mapped/23-butanediol.yaml`
   `synonyms`.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
3. Re-run the focused strict/LinkML validators, synonym review,
   `just qc-sssom`, and `just qc-flat-coverage` after those edits.
