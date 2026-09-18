# `data/ingredients/mapped/Docosanol.yaml`

## Verdict

Needs curation. The CultureBotHT row carries CAS `661-19-8`, which is
1-docosanol/docosan-1-ol, but the record is exact-mapped to the broader
`CHEBI:197511` positional docosanol class. Active `CHEBI:31000` is the exact
CAS-backed ChEBI target.

## Identity

- Reviewed record: `data/ingredients/mapped/Docosanol.yaml`.
- Current identifier and grounding: `identifier: CHEBI:197511` with
  `ontology_mapping.ontology_id: CHEBI:197511`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:197511` to active `docosanol`, a class for
  hydroxylated unbranched saturated C22 alcohols with a CAS xref for the class.
- Local OAK also finds active `CHEBI:31000` `docosan-1-ol`, whose definition is
  docosane substituted by a hydroxy group at position 1 and whose CAS xref
  `661-19-8` matches the CultureBotHT source row.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Docosane.yaml data/ingredients/mapped/Docosanol.yaml data/ingredients/mapped/Dodecandioic_Acid.yaml data/ingredients/mapped/Dodecane.yaml data/ingredients/mapped/Dodecanoate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Docosane.yaml data/ingredients/mapped/Docosanol.yaml data/ingredients/mapped/Dodecandioic_Acid.yaml data/ingredients/mapped/Dodecane.yaml data/ingredients/mapped/Dodecanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:46050 CHEBI:197511 CHEBI:4676 CHEBI:28817 CHEBI:18262`:
  returned local metadata for the current `CHEBI:197511` parent.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:31000`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref, formula,
  InChI, SMILES, charge, and mass for the exact `CHEBI:31000` target.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `661-19-8` to CID 12620 with formula `C22H46O`, the same
  InChIKey as `CHEBI:31000`, and synonyms including `1-DOCOSANOL`,
  `docosan-1-ol`, and `CHEBI:31000`.
- A focused hidden/ignored-inclusive search over `data/ingredients` and
  `mappings` for `CHEBI:197511` and `661-19-8` found only the active Docosanol
  YAML plus the expected row-review and final SSSOM rows.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Docosanol` to `CHEBI:197511` with `skos:exactMatch`, but the CAS RN
  proves the CultureBotHT subject is the narrower terminal alcohol
  `CHEBI:31000`, not only the positional docosanol parent.

## Completeness

- CAS RN and CultureBotHT provenance are populated.
- Occurrences, supplied forms, mixture components, nutritional roles,
  physicochemical roles, biological roles, and environmental contexts are
  correctly empty.

## Recommended Edits

- Major: remap `data/ingredients/mapped/Docosanol.yaml` from broad
  `CHEBI:197511` to exact `CHEBI:31000`, refresh the formula, InChI, and SMILES
  from ChEBI/PubChem, then synchronize `data/curated/mapped_ingredients.yaml`
  and regenerate `mappings/ingredient_mappings.sssom.tsv`.
