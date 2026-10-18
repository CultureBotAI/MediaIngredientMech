# `data/ingredients/mapped/Dihydrostreptomycin.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-matches active `CHEBI:38291`
dihydrostreptomycin, the stored formula, InChI, and SMILES agree with local
ChEBI metadata, and the final SSSOM row has no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Dihydrostreptomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:38291` with
  `ontology_mapping.ontology_id: CHEBI:38291`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and two MicrobeDecoder source
  occurrences from `BacDive_Antibiotic_resistance` and
  `BacDive_Metabolite_production`.
- Local OAK resolves `CHEBI:38291` to active `dihydrostreptomycin`, formula
  `C21H41N7O12`, InChI, SMILES, mass, CAS xref `128-46-1`, KEGG xrefs, and
  related synonym `Dihydrostreptomycin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dihydrostreptomycin.yaml data/ingredients/mapped/Dihydroxyacetone.yaml data/ingredients/mapped/Dimethyl_Disulfide.yaml data/ingredients/mapped/Dimethyl_Sulfide.yaml data/ingredients/mapped/Dimethyl_Sulfone.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dihydrostreptomycin.yaml data/ingredients/mapped/Dihydroxyacetone.yaml data/ingredients/mapped/Dimethyl_Disulfide.yaml data/ingredients/mapped/Dimethyl_Sulfide.yaml data/ingredients/mapped/Dimethyl_Sulfone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:38291 CHEBI:16016 CHEBI:4608 CHEBI:17437 CHEBI:9349`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:38291`.
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
  `CHEBI:38291` found only
  `data/ingredients/mapped/Dihydrostreptomycin.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the row as
  `APPROVED` after local OAK resolution and case-insensitive canonical-label
  confirmation.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dihydrostreptomycin` to `CHEBI:38291` with `skos:exactMatch`,
  canonical object label `dihydrostreptomycin`, CHEBI object source,
  MicrobeDecoder provenance, and no `other` tokens.

## Completeness

- Formula, InChI, SMILES, mass, PubChem/ChEBI retrieval provenance,
  MicrobeDecoder source occurrences, ingredient type, and mapping promotion
  history are populated.
- CAS RN is available as a ChEBI xref, and CultureMech occurrence statistics,
  ingredient roles, supplied forms, mixture components, and environmental
  contexts are correctly empty.

## Recommended Edits

- None.
