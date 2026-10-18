# `data/ingredients/mapped/Amphotericin_A.yaml`

## Verdict

Needs curation. The `mesh:C041989` Amphotericin A identity, MeSH SSSOM row, and
prefix-specific row-review disposition pass, but the active record has an
unsupported provisional `SELECTIVE_AGENT` role inferred from the name pattern.

## Identity

- Reviewed record: `data/ingredients/mapped/Amphotericin_A.yaml`.
- Identifier and grounding: `identifier: mesh:C041989` with
  `ontology_mapping.ontology_id: mesh:C041989`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` confirms that the
  prefix-specific EBI OLS lookup resolves `mesh:C041989` exactly as
  `amphotericin A`; the `UNKNOWN_TERM` trailer came from earlier validator
  prefix coverage rather than a mapping defect.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amphotericin_A.yaml data/ingredients/mapped/Amphotericin_B.yaml data/ingredients/mapped/Ampicillin.yaml data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml data/ingredients/mapped/Amygdalin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amphotericin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` row 412 maps
  `MIM:Amphotericin_A` to `mesh:C041989` with `skos:exactMatch` and preserves
  the MeSH `UNKNOWN_TERM` trailer.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the MeSH
  `UNKNOWN_TERM` trailer as missing prefix coverage and points to the
  prefix-specific exact OLS resolution in
  `mappings/ingredient_mappings_unknown_term_triage.tsv`.
- The only role is a `SELECTIVE_AGENT` computational prediction inferred from a
  curated name-pattern rule; no medium or source claim demonstrates that
  Amphotericin A was curated as a selective agent in this record.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, MicrobeDecoder imports, and hydrate
  review files found the active YAML, aggregate copy, SSSOM row, and row-review
  disposition.

## Completeness

- The MeSH exact mapping, curation history, row-review disposition, and
  `ingredient_type` are populated.
- No synonym, component, environmental context, discussion, or dataset entry is
  needed.
- Chemical-structure slots are empty because the current primary grounding is a
  MeSH term, not ChEBI.
- The unsupported selective-agent role is the only active gap.

## Recommended Edits

- In `data/ingredients/mapped/Amphotericin_A.yaml`, replace the
  `SELECTIVE_AGENT` computational prediction with source-backed evidence, or
  remove it.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amphotericin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
