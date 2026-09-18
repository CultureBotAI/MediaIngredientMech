# `data/ingredients/mapped/Metals_44_see_below.yaml`

## Verdict

Needs curation. The exact MICRO identity and restored CultureMech evidence pass,
but raw quoted recipe labels are being exported as final SSSOM synonyms.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Metals_44_see_below.yaml`.
- Identifier and grounding: `identifier: MICRO:0000456` with
  `ontology_mapping.ontology_id: MICRO:0000456`, label `trace metals 44`,
  source `MICRO`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`,
  and `mapping_status: MAPPED`.
- Occurrences: one CultureMech recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meso-Erythritol` through `Methane`: exited 0 and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this MICRO-primary record
  because the CHEBI-focused adapter used here omits MICRO.

## Evidence

- EBI OLS4 resolves `MICRO:0000456` as active `trace metals 44` with exact
  synonyms for `metals 44` and the quoted-44 form of that label.
- `mappings/culturemech_residual_groundings.tsv` records both CultureMech
  residual labels as new-record groundings to `MICRO:0000456`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Metals_44_see_below` to `MICRO:0000456`, but the `other` column contains
  raw quoted source labels: one wraps the whole label in literal quote
  characters and the other also includes a `see below` recipe instruction.

## Completeness

- The raw CultureMech labels are useful provenance, but they are not true
  published synonyms for the stock identity and should not appear in final
  SSSOM `other`.

## Recommended Edits

- Keep the raw quoted CultureMech labels as provenance-only aliases or
  rejected labels, and update the SSSOM synonym builder or YAML synonym types so
  final `other` exports only true MICRO synonyms such as `metals 44`.
