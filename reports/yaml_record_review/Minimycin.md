# `data/ingredients/mapped/Minimycin.yaml`

## Verdict

Needs curation. The exact `mesh:C002363` minimycin identity, MeSH triage, and
final SSSOM row pass, but the selective-agent role is only a provisional
name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Minimycin.yaml`.
- Identifier and grounding: `identifier: mesh:C002363` with
  `ontology_mapping.ontology_id: mesh:C002363`, label `minimycin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Minimycin` through `Mitomycin_C`: exited 0 and wrote zero ERROR rows.
- Direct CHEBI-focused LinkML term validation was skipped for this MeSH record
  in the mixed batch.

## Evidence

- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies this as a
  missing-prefix validator coverage issue and keeps the mapping after a
  prefix-specific EBI OLS query resolved the exact MeSH CURIE.
- A fresh MeSH-scoped EBI OLS4 lookup resolves `mesh:C002363` as active
  `minimycin`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Minimycin` to
  `mesh:C002363` with empty `other`.

## Completeness

- The MeSH target, exact identity row, triage rationale, and empty final
  `other` agree.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: add source-backed evidence that minimycin is used as a selective agent
  in media, or remove the provisional `SELECTIVE_AGENT` role.
