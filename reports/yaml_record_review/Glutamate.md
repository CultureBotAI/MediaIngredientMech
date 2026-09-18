# `data/ingredients/mapped/Glutamate.yaml`

## Verdict

Pass with a minor stale-note issue. The MicrobeDecoder bare-glutamate label was
intentionally promoted to the ChEBI `glutamate(2-)` synonym target, the
structure fields match that dianion, and the final SSSOM row emits no unsafe
`other` synonyms, but the top-level note still describes the original unmapped
import.

## Identity

- Reviewed record: `data/ingredients/mapped/Glutamate.yaml`.
- Identifier and grounding: `identifier: CHEBI:29987` with matching
  `ontology_mapping.ontology_id`, canonical label `glutamate(2-)`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C5H7NO4`, SMILES
  `NC(CCC(=O)[O-])C(=O)[O-]`, and molecular weight `145.114`.

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
- OLS4 resolves `CHEBI:29987` as `glutamate(2-)`, matching the YAML
  `ontology_mapping`.
- The #213 promotion evidence records the intended synonym match from the
  source label `Glutamate` to `CHEBI:29987` `glutamate(2-)`; no salt or
  stereochemical identity is being collapsed in this bare anion record.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Glutamate`
  to `CHEBI:29987` by `skos:exactMatch` and leaves `other` empty.
- Minor: top-level `notes` still carry the original MicrobeDecoder import text
  and say curator review is needed even though the record has been promoted,
  classified, and exported.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, related glutamate salt and stereoisomer records, generated indexes, old
  batch validation reports, and ignored aggregate backups.

## Completeness

- The ChEBI synonym identity, structure fields, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM row are populated.

## Recommended Edits

- Minor: refresh `notes` in `data/ingredients/mapped/Glutamate.yaml` so it
  describes the reviewed `CHEBI:29987` synonym match rather than the original
  unresolved import.
