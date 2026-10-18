# `data/ingredients/mapped/Meat_peptone.yaml`

## Verdict

Needs curation. The exact MICRO identity, occurrence count, mixture
classification, and final SSSOM row pass, but `PROTEIN_SOURCE` is only a
provisional name-pattern inference.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Meat_peptone.yaml`.
- Identifier and grounding: `identifier: MICRO:0000176` with
  `ontology_mapping.ontology_id: MICRO:0000176`, label `meat peptone`, source
  `MICRO`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 90 CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meat_peptone` through `Melezitose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for the
  batch.
- Direct Engine A term validation was skipped for this MICRO-primary record
  because the CHEBI-focused adapter used here omits MICRO.

## Evidence

- EBI OLS4 resolves `MICRO:0000176` as active `meat peptone`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` records the final SSSOM
  row's `UNKNOWN_TERM` validation marker as `RESOLVED_EXACT_CURIE`; the warning
  is a synonym-review prefix coverage gap rather than a bad MICRO identifier.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Meat_peptone`
  to `MICRO:0000176` with empty `other`.
- `rg --no-ignore --hidden` over `data`, `mappings`, `reports`, `scripts`,
  `src`, and `tests` found that `MIM:Bacto_Peptone` currently exports
  `Meat peptone` in its own `other` column, but that is a separate
  Bacto-peptone synonym issue and does not make this Meat-peptone record wrong.

## Completeness

- `PROTEIN_SOURCE` is only backed by a `COMPUTATIONAL_PREDICTION` inferred from
  a media-role name pattern. No source attached to the role verifies that this
  meat-peptone record was supplied as a protein source.

## Recommended Edits

- Curate recipe or literature evidence for `PROTEIN_SOURCE`, or remove the
  provisional nutritional role.
