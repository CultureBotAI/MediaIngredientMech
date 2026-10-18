# `data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml`

## Verdict

Needs curation, major. The CAS primary identifier, monohydrate PubChem
structure, and close parent `CHEBI:16388` mapping are coherent, but the record
promotes an exact synonym from the anhydrous ChEBI parent and exports that
parent-acid label through SSSOM.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:184901-84-6` with a close
  `ontology_mapping.ontology_id: CHEBI:16388`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:16388` is active, resolves to the anhydrous
  parent `4-hydroxymandelic acid`, and has formula `C8H8O4`, SMILES
  `O=C(O)C(O)c1ccc(O)cc1`, and the anhydrous InChI.
- PubChem CID `12677290` resolves to formula `C8H10O5`, SMILES
  `C1=CC(=CC=C1C(C(=O)O)O)O.O`, and the stored monohydrate InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml data/ingredients/mapped/4-Hydroxynonanoic_Acid.yaml data/ingredients/mapped/4-Hydroxynonenal.yaml data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml data/ingredients/mapped/4-Hydroxynonanoic_Acid.yaml data/ingredients/mapped/4-Hydroxynonenal.yaml data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  expected close ChEBI parent row plus the exact CAS registry row.

## Evidence

- Supported: retaining `cas:184901-84-6` as the exact registry identity and
  `CHEBI:16388` as a close parent is consistent with the hydrate-specific
  PubChem structure and the anhydrous official ChEBI target.
- Supported: the row-review manifest correctly keeps the `cas:` SSSOM row as
  an expected registry identifier rather than treating it as a failed OBO term.
- Major: `synonyms[0]` is `hydroxy(4-hydroxyphenyl)acetic acid` with
  `synonym_type: EXACT_SYNONYM`, but that is an exact synonym on the anhydrous
  `CHEBI:16388` parent, not on the named monohydrate form. It also publishes in
  the close-match SSSOM row's `other` field beside `CAS:184901-84-6`.
- Stale: `mappings/record_research_validation.tsv` predates the #342
  `CLOSE_MATCH` repair and still recommends non-identity treatment that is now
  already represented by the active parent mapping plus CAS registry row.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM rows, OAK/OLS and unknown-term review rows,
  hydrate review surfaces, generated docs, stale advisory rows, and ignored
  aggregate backups.

## Completeness

- CAS, PubChem CID, formula, InChI, SMILES, and `ingredient_type` are populated.
- The active parent is necessarily non-exact, but that loss is explicit in
  `mapping_quality: CLOSE_MATCH` and the exact CAS row preserves the supplied
  monohydrate identity.
- This CultureBotHT fallback has no recipe-count occurrence; no role,
  component, environment, or discussion entries need review.

## Recommended Edits

1. Remove `hydroxy(4-hydroxyphenyl)acetic acid` from `synonyms`, or replace it
   with an explicit non-exact parent-label representation if the schema gains
   one.
2. Resync `data/curated/mapped_ingredients.yaml`, rebuild SSSOM and docs, then
   verify the parent-acid label no longer publishes as a monohydrate synonym in
   `mappings/ingredient_mappings.sssom.tsv`.
