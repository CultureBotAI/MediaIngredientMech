# `data/ingredients/mapped/Glucose_1-phosphate.yaml`

## Verdict

Pass with minor cleanup issues. The manually chosen close match to
`CHEBI:16077` D-glucopyranose 1-phosphate is intentionally narrower than the
underspecified Glucose 1-phosphate source label, but the record still lacks
available ChEBI structure fields and carries a stale top-level import note.

## Identity

- Reviewed record: `data/ingredients/mapped/Glucose_1-phosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16077` with matching
  `ontology_mapping.ontology_id`, canonical label
  `D-glucopyranose 1-phosphate`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:16077` as active D-glucopyranose 1-phosphate with
  formula `C6H13O9P`, mass `260.135`, and synonyms including
  `D-Glucose 1-phosphate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gluconic_Acid.yaml data/ingredients/mapped/Glucosamine.yaml data/ingredients/mapped/Glucose.yaml data/ingredients/mapped/Glucose_1-phosphate.yaml data/ingredients/mapped/Glucose_2.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gluconic_Acid.yaml data/ingredients/mapped/Glucosamine.yaml data/ingredients/mapped/Glucose.yaml data/ingredients/mapped/Glucose_1-phosphate.yaml data/ingredients/mapped/Glucose_2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI close match, 7 MicrobeDecoder source occurrences, raw source
  synonym, single-ingredient type, and stale top-level note as the per-record
  YAML.
- The curation history and mapping evidence explicitly document the intended
  close match: the source label does not state D series or anomeric
  configuration, while `CHEBI:16077` denotes D-glucopyranose 1-phosphate.
- The final SSSOM row maps `MIM:Glucose_1-phosphate` to `CHEBI:16077`, records
  the manual promotion from unmapped, and leaves `other` empty.
- Minor: `chemical_properties` is absent even though OLS4 supplies formula,
  mass, InChI, InChIKey, and SMILES for the chosen ChEBI term.
- Minor: the top-level `notes` still repeat the original MicrobeDecoder import
  text saying the row had no CAS-RN or CHEBI/NCIT match and needed curator
  review. That is stale after the issue `#213` close-match promotion.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, row-review validation noting the missing structure fields,
  generated indexes, old batch validation reports, and ignored aggregate
  backups.

## Completeness

- The close-match identity, MicrobeDecoder source occurrence, and final SSSOM
  row are populated.
- ChEBI structure fields and stale notes need cleanup.

## Recommended Edits

- Minor: backfill `chemical_properties` from `CHEBI:16077` and remove or update
  the stale top-level `notes`.
