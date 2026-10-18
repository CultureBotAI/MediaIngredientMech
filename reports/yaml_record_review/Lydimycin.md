# `data/ingredients/mapped/Lydimycin.yaml`

## Verdict

Needs curation. The exact NCIT:C90684 identity and final SSSOM row are
consistent, but `physicochemical_roles.SELECTIVE_AGENT` is supported only by a
provisional name-pattern inference.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Lydimycin.yaml`.
- Identifier and grounding: `identifier: NCIT:C90684` with
  `ontology_mapping.ontology_id: NCIT:C90684`, label `Lydimycin`, source
  `NCIT`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: none asserted.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lydimycin` through `Lysozyme`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `NCIT:C90684` as active `Lydimycin`, lists CAS RN
  `10118-85-1`, and records formula `C10H14N2O3S`.
- The final SSSOM publishes one `skos:exactMatch` row to `NCIT:C90684`; its
  `other` field is empty.

## Completeness

- The exact active NCIT identity and final SSSOM row are present and
  consistent.
- The `SELECTIVE_AGENT` facet is based on `reference_type:
  COMPUTATIONAL_PREDICTION` with `reference_text: Inferred from curated
  media-role name pattern` and a curator note marking the role as provisional.
  No literature, database, or recipe evidence supports the asserted selective
  activity in this record.

## Recommended Edits

- Curate evidence for `SELECTIVE_AGENT`, or remove the role if no supporting
  ingredient-level evidence is available.
