# `data/ingredients/mapped/Diaminopimelic_Acid.yaml`

## Verdict

Needs curation. The record exact-matches active `CHEBI:23673`
2,6-diaminopimelic acid through a ChEBI synonym, and final SSSOM exports only
the exact synonym plus the CAS RN. The amino-acid-source role is still inferred
only from ChEBI ancestry.

## Identity

- Reviewed record: `data/ingredients/mapped/Diaminopimelic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:23673` with
  `ontology_mapping.ontology_id: CHEBI:23673`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:23673` to active canonical label
  `2,6-diaminopimelic acid`, exact synonym
  `2,6-diaminoheptanedioic acid`, related synonym `Diaminopimelic acid`, CAS
  xref `583-93-7`, formula, InChI, SMILES, and mass.
- The stored formula, InChI, SMILES, and molecular weight agree with local
  ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:23673`:
  returned the canonical label, synonyms, CAS xref, formula, InChI, SMILES,
  charge, and mass for `CHEBI:23673`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected live record and stale `CHEBI:23674` row-review entries
  that were already classified as `ALREADY_REPRESENTED`.
- `mappings/culturemech_recipe_membership.tsv` has six `CHEBI:23673` rows,
  matching `occurrence_statistics.total_occurrences: 6` and `media_count: 6`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Diaminopimelic_Acid` to `CHEBI:23673` with `skos:exactMatch`, canonical
  object label `2,6-diaminopimelic acid`, CHEBI object source, exact synonym
  `2,6-diaminoheptanedioic acid`, and `CAS:583-93-7` in `other`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is supported only by an
  `infer_roles_from_chebi_ancestry` `COMPUTATIONAL_PREDICTION` whose curator
  note explicitly calls the assignment provisional.

## Completeness

- CAS RN, formula, InChI, SMILES, molecular weight, occurrence statistics,
  synonym, and the dead-ChEBI repair history are populated.
- Mixture components, supplied forms, and environmental contexts are correctly
  empty for this single ChEBI chemical.

## Recommended Edits

- Major: source or remove `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/Diaminopimelic_Acid.yaml`, then synchronize
  `data/curated/mapped_ingredients.yaml`.
