# `data/ingredients/mapped/Nh42_Citrate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63076` diammonium citrate identity,
CAS-backed structure, occurrence count, and final exact SSSOM row pass, but
`NITROGEN_SOURCE` remains only a provisional in-session LLM role assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh42_Citrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:63076` with
  `ontology_mapping.ontology_id: CHEBI:63076`, label `diammonium citrate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 63 CultureMech recipe occurrences across 63 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Netropsin` through `Nh42co3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63076` as active
  `diammonium citrate` with formula `C6H6O7.2H4N`, CAS `3012-65-5`, the
  retained kg-microbe aliases, and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `3012-65-5` resolves to diammonium citrate
  with the same InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Nh42_Citrate` exactly to `CHEBI:63076`, keeps
  real diammonium citrate aliases plus `CAS:3012-65-5` in `other`, and filters
  the raw CultureMech `Role:`/`Properties:` labels.
- Major: `nutritional_roles.NITROGEN_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from in-session Claude reasoning, and
  the evidence note explicitly marks the role provisional.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 63/63 occurrence count,
  duplicate merge, and final exact row agree.
- The remaining consequential gap is source evidence for, or removal of, the
  provisional `NITROGEN_SOURCE` role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nh42_Citrate.yaml`, either replace the
  provisional `NITROGEN_SOURCE` assertion with database or publication
  evidence at the role claim or remove it before rebuilding downstream
  products.
