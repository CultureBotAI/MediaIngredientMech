# `data/ingredients/mapped/Monazomycin.yaml`

## Verdict

Needs curation. The exact `CHEBI:201539` Monazomycin identity, formula, active
ChEBI term, and final exact row pass, but the final SSSOM still exports
process text as `other` and the selective-agent role is only a provisional
name-pattern prediction.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Monazomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:201539` with
  `ontology_mapping.ontology_id: CHEBI:201539`, label `Monazomycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Modified_Wolfes_Minerals` through `Mono-_And_Disaccharides`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:201539` as active `Monazomycin` and
  exposes the stored IUPAC name as an exact synonym.
- A fresh PubChem lookup for `monazomycin` resolves a compound with molecular
  formula `C72H133NO22`, matching the formula stored from ChEBI.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Monazomycin`
  to `CHEBI:201539`.

## Completeness

- The ChEBI target, exact identity row, formula, and ChEBI IUPAC synonym agree.
- The final SSSOM `other` field still exports `produces: monazomycin`, which
  is process-qualified source text rather than a clean synonym.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from a curated
  media-role name pattern with a provisional curator note.

## Recommended Edits

- Major: mark `produces: monazomycin` as `REJECTED_LABEL`, or otherwise retain
  it only as provenance while filtering it from final SSSOM `other`.
- Major: add source-backed evidence that monazomycin is used as a selective
  agent in media, or remove the provisional `SELECTIVE_AGENT` role.
