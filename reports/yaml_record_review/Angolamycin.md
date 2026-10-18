# `data/ingredients/mapped/Angolamycin.yaml`

## Verdict

Needs curation. The exact `mesh:C002547` Angolamycin identity, SSSOM row, and
prefix-specific row-review disposition pass, but the active record has an
unsupported provisional `SELECTIVE_AGENT` role inferred from the name pattern.

## Identity

- Reviewed record: `data/ingredients/mapped/Angolamycin.yaml`.
- Identifier and grounding: `identifier: mesh:C002547` with
  `ontology_mapping.ontology_id: mesh:C002547`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` confirms that the
  prefix-specific EBI OLS lookup resolves `mesh:C002547` exactly as
  `angolamycin`; the `UNKNOWN_TERM` trailer came from earlier validator prefix
  coverage rather than a mapping defect.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Andrographolide.yaml data/ingredients/mapped/Anethole.yaml data/ingredients/mapped/Angolamycin.yaml data/ingredients/mapped/Angustmycin.yaml data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Angolamycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` row 427 maps `MIM:Angolamycin` to
  `mesh:C002547` with `skos:exactMatch` and preserves the MeSH `UNKNOWN_TERM`
  trailer.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the MeSH
  `UNKNOWN_TERM` trailer as missing prefix coverage and points to the
  prefix-specific exact OLS resolution in
  `mappings/ingredient_mappings_unknown_term_triage.tsv`.
- The only role is a `SELECTIVE_AGENT` computational prediction inferred from a
  curated name-pattern rule; no medium or source claim demonstrates that
  Angolamycin was curated as a selective agent in this record.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, CultureMech memberships, and batch
  review reports found the active YAML, aggregate copy, SSSOM row, row-review
  disposition, and no `culturemech_recipe_membership.tsv` rows.

## Completeness

- The MeSH exact mapping, curation history, row-review disposition, and
  `ingredient_type` are populated.
- Chemical-structure slots are empty because the current primary grounding is a
  MeSH term, not ChEBI.
- No synonym, component, environmental context, discussion, or dataset entry is
  needed.
- The unsupported selective-agent role is the active gap.

## Recommended Edits

- In `data/ingredients/mapped/Angolamycin.yaml`, replace the
  `SELECTIVE_AGENT` computational prediction with source-backed evidence, or
  remove it.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Angolamycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
