# `data/ingredients/mapped/Nh4-oxalate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:91241` ammonium oxalate identity,
CAS-backed structure, occurrence count, and final exact SSSOM row pass, but
`NITROGEN_SOURCE` remains only a provisional in-session LLM role assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh4-oxalate.yaml`.
- Identifier and grounding: `identifier: CHEBI:91241` with
  `ontology_mapping.ontology_id: CHEBI:91241`, label `ammonium oxalate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 5 CultureMech recipe occurrences across 5 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Netropsin` through `Nh42co3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:91241` as active
  `ammonium oxalate` with formula `C2O4.2H4N`, CAS `1113-38-8`, and the same
  InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `1113-38-8` resolves to ammonium oxalate with
  the same InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Nh4-oxalate` exactly to `CHEBI:91241`, keeps
  true ammonium oxalate aliases plus `CAS:1113-38-8` in `other`, and filters no
  unsafe raw CultureMech text.
- Major: `nutritional_roles.NITROGEN_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from in-session Claude reasoning, and
  the evidence note explicitly marks the role provisional.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 5/5 occurrence count, and
  final exact row agree.
- The remaining consequential gap is source evidence for, or removal of, the
  provisional `NITROGEN_SOURCE` role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nh4-oxalate.yaml`, either replace the
  provisional `NITROGEN_SOURCE` assertion with database or publication
  evidence at the role claim or remove it before rebuilding downstream
  products.
