# `data/ingredients/mapped/Neomycin.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:7507` neomycin identity, CAS support,
occurrence count, and final exact SSSOM row pass, but `SELECTIVE_AGENT` remains
only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Neomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:7507` with
  `ontology_mapping.ontology_id: CHEBI:7507`, label `neomycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 CultureMech recipe occurrences across 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Natural_Sea_Water` through `Neomycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:7507` as active `neomycin` and lists
  CAS `1404-04-2`, matching the record.
- A fresh PubChem CAS lookup for `1404-04-2` resolves to neomycin, confirming
  the CAS identity; the record stores only the CAS RN and does not assert a
  formula or structure that would need cross-checking.
- The final SSSOM row maps `MIM:Neomycin` exactly to `CHEBI:7507` and keeps
  only `CAS:1404-04-2` in `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence inferred from a name-pattern rule, and
  the evidence note explicitly marks the role provisional.

## Completeness

- The active ChEBI term, CAS RN, 2/2 occurrence count, and final exact row
  agree.
- The remaining consequential gap is source evidence for, or removal of, the
  provisional `SELECTIVE_AGENT` role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Neomycin.yaml`, either replace the
  provisional `SELECTIVE_AGENT` assertion with database or publication evidence
  at the role claim or remove it before rebuilding downstream products.
