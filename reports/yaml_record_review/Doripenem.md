# `data/ingredients/mapped/Doripenem.yaml`

## Verdict

Pass. The MicrobeDecoder antibiotic identity exact-matches active
`CHEBI:135928` doripenem, the formula and structure agree with PubChem, and the
final SSSOM row is a clean exact match with no noisy synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Doripenem.yaml`.
- Identifier and grounding: `identifier: CHEBI:135928` with
  `ontology_mapping.ontology_id: CHEBI:135928`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 2 MicrobeDecoder source
  occurrences.
- OLS resolves `CHEBI:135928` to active `doripenem` with synonyms `doribax` and
  `doripenem hydrate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dodecanol.yaml data/ingredients/mapped/Dopamine_Hydrochloride.yaml data/ingredients/mapped/Dopsisamine.yaml data/ingredients/mapped/Doripenem.yaml data/ingredients/mapped/Dotriacontane.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dodecanol.yaml data/ingredients/mapped/Dopamine_Hydrochloride.yaml data/ingredients/mapped/Doripenem.yaml data/ingredients/mapped/Dotriacontane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4 CHEBI files; `Dopsisamine.yaml` was skipped because `mesh:`
  identifiers are outside this CHEBI/OBO-focused batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:23866 CHEBI:4698 CHEBI:135928 CHEBI:36020`:
  did not return local metadata for `CHEBI:135928`.
- Prefix-specific `curl -L 'https://www.ebi.ac.uk/ols4/api/search?q=CHEBI:135928&ontology=chebi'`:
  resolved `CHEBI:135928` to active `doripenem`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves `Doripenem` to CID 73303 with formula `C15H24N4O6S2` and
  the same InChIKey as the record.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:135928` found only the active Doripenem YAML, its
  MicrobeDecoder approval row, and its final SSSOM row.
- `mappings/microbedecoder_auto_mapped_review.tsv` records this ChEBI lexical
  match as `APPROVED`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Doripenem`
  to `CHEBI:135928` with `skos:exactMatch`, canonical object label
  `doripenem`, CHEBI object source, and no `other` tokens.

## Completeness

- Formula, InChI, SMILES, molecular weight, ChEBI/PubChem structure provenance,
  and MicrobeDecoder source occurrences are populated.
- CAS RN, supplied forms, mixture components, nutritional roles,
  physicochemical roles, biological roles, and environmental contexts are
  correctly empty.

## Recommended Edits

- None.
