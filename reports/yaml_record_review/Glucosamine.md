# `data/ingredients/mapped/Glucosamine.yaml`

## Verdict

Needs curation, with a major final-SSSOM synonym issue. The MicrobeDecoder exact
match to active `CHEBI:5417` glucosamine is structurally consistent, but final
SSSOM exports `(+)-d-glucosamine`, which is a D-form surface string rather than
a synonym of the generic ChEBI parent.

## Identity

- Reviewed record: `data/ingredients/mapped/Glucosamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:5417` with matching
  `ontology_mapping.ontology_id`, canonical label `glucosamine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:5417` as active glucosamine with formula `C6H13NO5` and
  mass `179.171`, matching the YAML.

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
  the same ChEBI exact mapping, MicrobeDecoder source occurrence, formula, mass,
  single-ingredient type, and recovered `(+)-d-glucosamine` surface form as the
  per-record YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Glucosamine.yaml` after the local OAK id resolved and its canonical label
  exact-matched the stored `ontology_label` case-insensitively.
- The final SSSOM row maps `MIM:Glucosamine` to `CHEBI:5417` by
  `skos:exactMatch` and records the manual MicrobeDecoder approval.
- Major: final SSSOM exports `(+)-d-glucosamine` in `other`; OLS4 does not list
  that string as a `CHEBI:5417` synonym, and it encodes the D series while
  `CHEBI:5417` is the broader glucosamine parent.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, the MicrobeDecoder review row, generated indexes, and ignored
  aggregate backups.

## Completeness

- The exact glucosamine identity, formula, mass, MicrobeDecoder source
  occurrence, ingredient type, and final SSSOM row are populated.
- The D-form surface string needs curator review before the final SSSOM `other`
  field is clean.

## Recommended Edits

- Major: remove or retag `(+)-d-glucosamine` so final SSSOM no longer exports a
  D-specific surface string as a generic glucosamine synonym, then regenerate
  final SSSOM and rerun SSSOM invariants.
