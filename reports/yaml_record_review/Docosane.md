# `data/ingredients/mapped/Docosane.yaml`

## Verdict

Pass. The MicrobeDecoder identity exact-matches active `CHEBI:46050`
docosane, the ChEBI formula, InChI, SMILES, and mass agree with the record, and
the final SSSOM row is a clean exact match with no noisy synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Docosane.yaml`.
- Identifier and grounding: `identifier: CHEBI:46050` with
  `ontology_mapping.ontology_id: CHEBI:46050`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 1 MicrobeDecoder source occurrence.
- Local OAK resolves `CHEBI:46050` to active `docosane`, formula `C22H46`, the
  expected InChI and SMILES, CAS xref `629-97-0`, and docosane synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Docosane.yaml data/ingredients/mapped/Docosanol.yaml data/ingredients/mapped/Dodecandioic_Acid.yaml data/ingredients/mapped/Dodecane.yaml data/ingredients/mapped/Dodecanoate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Docosane.yaml data/ingredients/mapped/Docosanol.yaml data/ingredients/mapped/Dodecandioic_Acid.yaml data/ingredients/mapped/Dodecane.yaml data/ingredients/mapped/Dodecanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:46050 CHEBI:197511 CHEBI:4676 CHEBI:28817 CHEBI:18262`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:46050`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:46050` found only the active Docosane per-record YAML,
  its MicrobeDecoder approval row, and its final SSSOM row.
- `mappings/microbedecoder_auto_mapped_review.tsv` records this ChEBI lexical
  match as `APPROVED`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Docosane`
  to `CHEBI:46050` with `skos:exactMatch`, canonical object label `docosane`,
  CHEBI object source, and no `other` tokens.

## Completeness

- Formula, InChI, SMILES, molecular weight, ChEBI structure provenance, and
  MicrobeDecoder source occurrence are populated.
- CAS RN, supplied forms, mixture components, nutritional roles,
  physicochemical roles, biological roles, and environmental contexts are
  correctly empty.

## Recommended Edits

- None.
