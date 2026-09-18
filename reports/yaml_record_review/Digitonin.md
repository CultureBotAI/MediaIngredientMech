# `data/ingredients/mapped/Digitonin.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-matches active `CHEBI:27729` digitonin,
the stored formula, InChI, and SMILES agree with local ChEBI metadata, and the
final SSSOM row has no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Digitonin.yaml`.
- Identifier and grounding: `identifier: CHEBI:27729` with
  `ontology_mapping.ontology_id: CHEBI:27729`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and one MicrobeDecoder source
  occurrence from `BacDive_Antibiotic_sensitivity`.
- Local OAK resolves `CHEBI:27729` to active `digitonin`, formula
  `C56H92O29`, InChI, SMILES, mass, CAS xref `11024-24-1`, KEGG xref
  `C00765`, and related synonym `Digitonin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydro_Azathymidine.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Digitonin.yaml data/ingredients/mapped/Digoxigenin.yaml data/ingredients/mapped/Dihydrocelastrol.yaml data/ingredients/mapped/Dihydrojasmonic_Acid_Methyl_Ester.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 4-record CHEBI subset; the local
  `kgmicrobe.compound:` placeholder record is outside Engine A's OBO prefix
  scope.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27729 CHEBI:42098 CHEBI:132340 CHEBI:89741`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:27729`.
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
  found the expected active record, generated/indexed copies,
  MicrobeDecoder review rows, and source-provenance references.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:27729` found only `data/ingredients/mapped/Digitonin.yaml`.
- `reports/microbedecoder_auto_mapped_review.tsv` records the row as
  `APPROVED` after local OAK resolution and case-insensitive canonical-label
  confirmation.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Digitonin` to `CHEBI:27729` with `skos:exactMatch`, canonical object
  label `digitonin`, CHEBI object source, MicrobeDecoder provenance, and no
  `other` tokens.

## Completeness

- Formula, InChI, SMILES, mass, PubChem/ChEBI retrieval provenance,
  MicrobeDecoder source occurrence, ingredient type, and mapping promotion
  history are populated.
- CAS RN is available as a ChEBI xref, and CultureMech occurrence statistics,
  ingredient roles, supplied forms, mixture components, and environmental
  contexts are correctly empty.

## Recommended Edits

- None.
