# `data/ingredients/mapped/Marmite.yaml`

## Verdict

Pass with minor issues. The exact MeSH identity, occurrence count, and final
SSSOM row pass, but the record is missing the expected `UNDEFINED_MIXTURE`
classification for a commercial yeast-extract preparation.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Marmite.yaml`.
- Identifier and grounding: `identifier: mesh:C008328` with
  `ontology_mapping.ontology_id: mesh:C008328`, label `marmite`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: two CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Marine_agar_2216` through `Mc_general_salts`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  MeSH-primary record.

## Evidence

- NLM MeSH resolves `C008328` as active `marmite` and describes it as a
  commercial yeast extract, matching the exact local label.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Marmite` to
  `mesh:C008328` with empty `other`.
- The row-review triage for the `UNKNOWN_TERM` validation stamp says a
  prefix-specific EBI OLS query resolved the exact MeSH CURIE and the warning
  came from synonym-review dispatcher coverage rather than a failed lookup.

## Completeness

- `ingredient_type` is absent. This is a classification gap rather than an
  identity problem because the exact MeSH row remains active and the final SSSOM
  does not export roles or noisy synonyms from this record.

## Recommended Edits

- Set `ingredient_type: UNDEFINED_MIXTURE` in
  `data/ingredients/mapped/Marmite.yaml` and regenerate
  `data/curated/mapped_ingredients.yaml` plus docs products.
