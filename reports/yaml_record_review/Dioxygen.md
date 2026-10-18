# `data/ingredients/mapped/Dioxygen.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-matches active `CHEBI:15379`, the
stored formula, InChI, SMILES, and mass agree with ChEBI metadata, and the
final SSSOM row has no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Dioxygen.yaml`.
- Identifier and grounding: `identifier: CHEBI:15379` with
  `ontology_mapping.ontology_id: CHEBI:15379`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 17 MicrobeDecoder source
  occurrences from `BacDive_Metabolite_utilization`.
- Local OAK resolves `CHEBI:15379` to active `dioxygen`, CAS xref
  `7782-44-7`, formula `O2`, the stored InChI, the stored SMILES, and
  related synonyms for molecular oxygen.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Glutarate.yaml data/ingredients/mapped/Disodium_Malate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Malate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the 4 CHEBI-label records in the batch; the lowercase MeSH parent
  in `Disodium_Glutarate.yaml` was left to Engine B/product validation.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15379`:
  returned the canonical label, synonyms, CAS xref, formula, InChI, SMILES,
  charge, and mass for `CHEBI:15379`.
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
  found the expected active record, aggregate copy, generated products,
  MicrobeDecoder review rows, and ignored aggregate backups.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:15379` found only `data/ingredients/mapped/Dioxygen.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the row as
  `APPROVED` after local OAK resolution and case-insensitive canonical-label
  confirmation.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Dioxygen`
  to `CHEBI:15379` with `skos:exactMatch`, canonical object label
  `dioxygen`, CHEBI object source, MicrobeDecoder provenance, and no `other`
  tokens.

## Completeness

- Formula, InChI, SMILES, mass, PubChem/ChEBI retrieval provenance,
  MicrobeDecoder source occurrence, ingredient type, and mapping promotion
  history are populated.
- CAS RN is available as a ChEBI xref, and CultureMech occurrence statistics,
  ingredient roles, supplied forms, mixture components, and environmental
  contexts are correctly empty.

## Recommended Edits

- None.
