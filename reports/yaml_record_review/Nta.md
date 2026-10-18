# `data/ingredients/mapped/Nta.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:39054` `NTA` identity, CAS alias, 4/4
occurrence count, and final SSSOM row pass, but `CHELATOR` is still backed only
by imported `Mineral` role text.

## Identity

- Reviewed record: `data/ingredients/mapped/Nta.yaml`.
- Identifier and grounding: `identifier: CHEBI:39054` with
  `ontology_mapping.ontology_id: CHEBI:39054`, label `NTA`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4 CultureMech recipe occurrences across 4 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:39054` as active `NTA`.
- The final SSSOM row maps `MIM:Nta` exactly to `CHEBI:39054`; the raw
  `Role:` and `Properties:` synonym is filtered from final `other`, leaving
  only `CAS:139-13-9`.
- Major: `physicochemical_roles.CHELATOR` cites a `DATABASE_ENTRY` whose
  curator note preserves only the original CultureMech role text `Mineral`.
  That source text does not itself support a chelator role.

## Completeness

- The active ChEBI term, CAS value, occurrence count, and final exact row
  otherwise agree.
- The remaining consequential gap is the unsupported chelator role evidence.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nta.yaml`, replace the `CHELATOR` role
  evidence with inspected source-backed chelation evidence, or remove the role
  until that evidence exists.
