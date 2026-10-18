# `data/ingredients/mapped/Dihydrocelastrol.yaml`

## Verdict

Pass. The record maps the CultureBotHT surface to active `CHEBI:132340`
triptohypol C through the curated local ChEBI exact-alias review, the InChI
and mass agree with local ChEBI metadata, and the final SSSOM row exports only
a true ChEBI synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Dihydrocelastrol.yaml`.
- Identifier and grounding: `identifier: CHEBI:132340` with
  `ontology_mapping.ontology_id: CHEBI:132340`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:132340` to active `triptohypol C`, formula
  `C29H40O4`, InChI, SMILES, and the exact IUPAC synonym already present in
  the YAML; it also lists `dihydrocelastrol` as a related synonym for the
  same ChEBI term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydro_Azathymidine.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 4-record CHEBI subset; the local
  `kgmicrobe.compound:` placeholder record is outside Engine A's OBO prefix
  scope.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27729 CHEBI:42098 CHEBI:132340 CHEBI:89741`:
  returned the canonical ChEBI label, definition, synonyms, formula, InChI,
  SMILES, charge, and mass for `CHEBI:132340`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus
  plausibility warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record and generated/indexed copies, with no live
  duplicate per-record YAML for `CHEBI:132340`.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:132340` found only
  `data/ingredients/mapped/Dihydrocelastrol.yaml`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dihydrocelastrol` to `CHEBI:132340` with `skos:exactMatch`,
  canonical object label `triptohypol C`, CHEBI object source, and the exact
  IUPAC ChEBI synonym in `other`.

## Completeness

- The exact ChEBI identity, same-substance synonyms, kg-microbe node ID,
  curated promotion history, InChI, mass, and ChEBI/PubChem retrieval
  provenance are populated.
- CAS RN, ingredient roles, supplied forms, mixture components, and
  environmental contexts are correctly empty.

## Recommended Edits

- None.
