# `data/ingredients/mapped/Dodecanol.yaml`

## Verdict

Needs curation. The CultureBotHT row carries CAS `112-53-8`, which is
1-dodecanol/dodecan-1-ol, but the record is exact-mapped to the broader
`CHEBI:23866` positional dodecanol class. Active `CHEBI:28878` is the exact
CAS-backed ChEBI target.

## Identity

- Reviewed record: `data/ingredients/mapped/Dodecanol.yaml`.
- Current identifier and grounding: `identifier: CHEBI:23866` with
  `ontology_mapping.ontology_id: CHEBI:23866`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:23866` to active `dodecanol`, a class for any
  hydroxylated unbranched saturated C12 alcohol.
- Local OAK also finds active `CHEBI:28878` `dodecan-1-ol`, whose definition is
  dodecane substituted by a hydroxy group at one terminal carbon and whose CAS
  xref `112-53-8` matches the CultureBotHT source row.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dodecanol.yaml data/ingredients/mapped/Dopamine_Hydrochloride.yaml data/ingredients/mapped/Dopsisamine.yaml data/ingredients/mapped/Doripenem.yaml data/ingredients/mapped/Dotriacontane.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dodecanol.yaml data/ingredients/mapped/Dopamine_Hydrochloride.yaml data/ingredients/mapped/Doripenem.yaml data/ingredients/mapped/Dotriacontane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4 CHEBI files; `Dopsisamine.yaml` was skipped because `mesh:`
  identifiers are outside this CHEBI/OBO-focused batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:23866 CHEBI:4698 CHEBI:135928 CHEBI:36020`:
  returned local metadata for the current `CHEBI:23866` parent.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28878`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref, formula,
  InChI, SMILES, charge, and mass for the exact `CHEBI:28878` target.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `112-53-8` to CID 8193 with formula `C12H26O` and the
  same InChIKey as `CHEBI:28878`.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:23866` and `112-53-8` found only the active Dodecanol
  YAML plus the expected row-review and final SSSOM rows.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dodecanol` to `CHEBI:23866` with `skos:exactMatch`, but the CAS RN
  proves the CultureBotHT subject is the narrower terminal alcohol
  `CHEBI:28878`, not only the positional dodecanol parent.

## Completeness

- CAS RN and CultureBotHT provenance are populated.
- Occurrences, supplied forms, mixture components, nutritional roles,
  physicochemical roles, biological roles, and environmental contexts are
  correctly empty.

## Recommended Edits

- Major: remap `data/ingredients/mapped/Dodecanol.yaml` from broad
  `CHEBI:23866` to exact `CHEBI:28878`, refresh the formula, InChI, and SMILES
  from ChEBI/PubChem, then synchronize `data/curated/mapped_ingredients.yaml`
  and regenerate `mappings/ingredient_mappings.sssom.tsv`.
