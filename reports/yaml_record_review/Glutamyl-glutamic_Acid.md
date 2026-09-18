# `data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml`

## Verdict

Pass with a minor stale-note issue. The MicrobeDecoder label was intentionally
promoted to the ChEBI `Glu-Glu` synonym target, its structure fields match the
chosen dipeptide, and the final SSSOM row emits no unsafe `other` synonyms, but
the top-level note still describes the original unmapped import.

## Identity

- Reviewed record: `data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:5390` with matching
  `ontology_mapping.ontology_id`, canonical label `Glu-Glu`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C10H16N2O7`, ChEBI/PubChem SMILES and InChI,
  and molecular weight `276.245`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glutamate.yaml data/ingredients/mapped/Glutamic_Acid.yaml data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml data/ingredients/mapped/Glutaraldehyde.yaml data/ingredients/mapped/Glutarate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glutamate.yaml data/ingredients/mapped/Glutamic_Acid.yaml data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml data/ingredients/mapped/Glutaraldehyde.yaml data/ingredients/mapped/Glutarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI synonym match, MicrobeDecoder source occurrence, formula,
  structure fields, singleton type, and stale top-level note as the per-record
  YAML.
- OLS4 resolves `CHEBI:5390` as `Glu-Glu`, matching the YAML
  `ontology_mapping`.
- The #213 promotion evidence records the intended synonym match from
  `Glutamyl-glutamic acid` to the dipeptide `Glu-Glu`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glutamyl-glutamic_Acid` to `CHEBI:5390` by `skos:exactMatch` and leaves
  `other` empty.
- Minor: top-level `notes` still carry the original MicrobeDecoder import text
  and say curator review is needed even though the record has been promoted,
  classified, and exported.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, row-review validation for the #213 promotion, generated indexes, old
  batch validation reports, and ignored aggregate backups.

## Completeness

- The ChEBI synonym identity, structure fields, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM row are populated.

## Recommended Edits

- Minor: refresh `notes` in
  `data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml` so it describes the
  reviewed `CHEBI:5390` synonym match rather than the original unresolved
  import.
