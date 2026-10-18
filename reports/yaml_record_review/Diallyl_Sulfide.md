# `data/ingredients/mapped/Diallyl_Sulfide.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record exact-matches active `CHEBI:4489`
Diallyl sulfide, its stored CAS RN and structure agree with local ChEBI, and
final SSSOM exports only the same CAS RN as additional payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Diallyl_Sulfide.yaml`.
- Identifier and grounding: `identifier: CHEBI:4489` with
  `ontology_mapping.ontology_id: CHEBI:4489`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:4489` to active `Diallyl sulfide`, formula
  `C6H10S`, charge `0`, InChI, SMILES, related synonyms, and CAS xref
  `592-88-1`.
- The record's CAS RN, formula, InChI, and SMILES agree with the local ChEBI
  term metadata.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16583 CHEBI:4489 CHEBI:23673 CHEBI:91249`:
  returned the canonical label, synonyms, CAS xref, formula, InChI, SMILES,
  charge, and mass for `CHEBI:4489`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:4489` mapping as confirmed with no row-review action required.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML or stale parent-mapping row for
  `CHEBI:4489`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `CHEBI:4489`, matching
  `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Diallyl_Sulfide` to `CHEBI:4489` with `skos:exactMatch`, canonical
  object label `Diallyl sulfide`, CHEBI object source, and only
  `CAS:592-88-1` in `other`.

## Completeness

- CAS RN, formula, InChI, SMILES, curation history, and ChEBI exact identity
  are populated.
- Synonyms, mixture components, ingredient roles, supplied forms, and
  environmental contexts are correctly empty for this pure CultureBotHT
  chemical import.

## Recommended Edits

- None.
