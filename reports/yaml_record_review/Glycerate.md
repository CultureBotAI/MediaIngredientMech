# `data/ingredients/mapped/Glycerate.yaml`

## Verdict

Pass. The MicrobeDecoder exact match to active `CHEBI:33871` glycerate is
structurally consistent, the record has no unsupported roles, and the final
SSSOM row exports no `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycerate.yaml`.
- Identifier and grounding: `identifier: CHEBI:33871` with matching
  `ontology_mapping.ontology_id`, canonical label `glycerate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C3H5O4`, SMILES `O=C([O-])C(O)CO`, InChI
  `InChI=1S/C3H6O4/c4-1-2(5)3(6)7/h2,4-5H,1H2,(H,6,7)/p-1`, and molecular
  weight `105.069`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gly-Glu.yaml data/ingredients/mapped/Glycerate.yaml data/ingredients/mapped/Glycerol.yaml data/ingredients/mapped/Glycerol_2.yaml data/ingredients/mapped/Glycerol_3-phosphate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Gly-Glu.yaml data/ingredients/mapped/Glycerate.yaml data/ingredients/mapped/Glycerol.yaml data/ingredients/mapped/Glycerol_2.yaml data/ingredients/mapped/Glycerol_3-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact mapping, MicrobeDecoder source occurrence, formula,
  mass, structure fields, single-ingredient type, and empty synonym set as the
  per-record YAML.
- OLS4 resolves `CHEBI:33871` as `glycerate`, matching the YAML
  `ontology_mapping`.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved
  `Glycerate.yaml` after the local OAK id resolved and its canonical label
  exact-matched the stored `ontology_label` case-insensitively.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycerate` to `CHEBI:33871` by `skos:exactMatch`, keeps object label
  `glycerate`, records the manual MicrobeDecoder approval, and leaves `other`
  empty.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, the MicrobeDecoder review row, the separate D-glycerate sibling,
  generated indexes, old batch validation reports, and ignored aggregate
  backups.

## Completeness

- The exact glycerate identity, formula, mass, structure fields, MicrobeDecoder
  source occurrence, ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
