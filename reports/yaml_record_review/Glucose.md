# `data/ingredients/mapped/Glucose.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym and unsupported-role issues. The
generic `CHEBI:17234` glucose identity, merged occurrence counts, source-backed
carbon-source role, and anomer-specific synonym rejection pass, but final
SSSOM still exports non-generic/open-chain labels and `ENERGY_SOURCE` remains
computational.

## Identity

- Reviewed record: `data/ingredients/mapped/Glucose.yaml`.
- Identifier and grounding: `identifier: CHEBI:17234` with matching
  `ontology_mapping.ontology_id`, canonical label `glucose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:17234` as active glucose with formula `C6H12O6`, CAS xref
  `50-99-7`, and live synonyms including `DL-glucose`, `Glc`, `Glucose`,
  `Glukose`, and `gluco-hexose`.

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
  the same ChEBI exact mapping, 2752 CultureMech occurrences, CAS RN, formula,
  kg-microbe synonyms, rejected anomer-specific label, single-ingredient type,
  and nutritional roles as the per-record YAML.
- The `merge_glucose_family` history explains the collapse of a duplicate
  lowercase glucose record that pointed at the open-chain aldehydo-D-glucose
  term. The separate alpha-D-glucose synonym has also been marked
  `REJECTED_LABEL` and no longer reaches the final SSSOM `other` field.
- `nutritional_roles.CARBON_SOURCE` is source-backed by a CultureMech
  `DATABASE_ENTRY` with original role text `Carbon Source`.
- Major: final SSSOM still exports
  `(2R,3S,4R,5R)-2,3,4,5,6-pentahydroxyhexanal`,
  `D-GLUCOSE IN LINEAR FORM`, the D-glucose surface form,
  `aldehydo-D-gluco-hexose`, and `fermentation: glucose` in `other`. OLS4 does
  not list these as `CHEBI:17234` synonyms; the first three chemical strings
  are specific to the D/open-chain form, and the fermentation token is assay
  prose rather than a synonym.
- Major: `nutritional_roles.ENERGY_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` whose reference text is a generic energy-substrate
  assertion and whose curator note says review is recommended.
- Minor: one active identity evidence item is an auto-proposed literature
  snippet about EGF withdrawal and glucose/glutamine consumption in mammary
  epithelial cells. It is not needed for the exact ChEBI grounding and still
  says a curator should rephrase or remove it.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, the rejected Glucose_2
  tombstone, sibling D-glucose and alpha-D-glucose records, many decomposed
  glucose-containing local records, final SSSOM rows, row-review rows,
  generated indexes, old batch validation reports, and ignored aggregate
  backups.

## Completeness

- The generic glucose identity, CAS RN, formula, CultureMech occurrence count,
  source-backed carbon-source role, rejected alpha-D-glucose label, and final
  SSSOM row are populated.
- Several final SSSOM `other` tokens, the energy-source role, and one
  auto-proposed literature evidence item need curator review.

## Recommended Edits

- Major: remove or retag the open-chain/D-form synonyms and
  `fermentation: glucose` so final SSSOM exports only real `CHEBI:17234`
  glucose synonyms, then regenerate final SSSOM and rerun SSSOM invariants.
- Major: replace `ENERGY_SOURCE` with source-backed evidence or remove the role.
- Minor: remove or rewrite the auto-proposed PubMed evidence item so the exact
  ChEBI mapping is supported only by relevant provenance.
