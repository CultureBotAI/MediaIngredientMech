# `data/ingredients/mapped/Nh4mgpo.yaml`

## Verdict

Needs curation - major. The promoted `CHEBI:149425` ammonium magnesium
phosphate identity and structure agree with the source formula shorthand, but
the active preferred term is still the truncated `NH4MgPO` and final SSSOM
publishes a Sigma catalog label as an exact synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh4mgpo.yaml`.
- Identifier and grounding: `identifier: CHEBI:149425` with
  `ontology_mapping.ontology_id: CHEBI:149425`, label
  `ammonium magnesium phosphate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 CultureMech recipe occurrences across 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh4cl` through `Nh4no3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:149425` as active
  `ammonium magnesium phosphate` with formula `H4N.Mg.O4P`, CAS `7785-21-9`,
  and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `7785-21-9` resolves to ammonium magnesium
  phosphate with the same InChI, supporting the #461 promotion from the source
  `NH4MgPO4(Sigma 529354)` shorthand.
- Major: `preferred_term: NH4MgPO` and final SSSOM `subject_label: NH4MgPO`
  are still missing the phosphate oxygen while the mapped identity is the
  `NH4MgPO4` salt.
- Major: final SSSOM `other` still publishes `NH4MgPO4(Sigma 529354)`, a
  vendor/catalog source label rather than an unconstrained synonym.

## Completeness

- The active ChEBI term, formula, structure, 2/2 occurrence count, and final
  exact target otherwise agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nh4mgpo.yaml`, rename the preferred term
  to an untruncated formula or the ChEBI label.
- Major: in the same maintained YAML, reject or demote
  `NH4MgPO4(Sigma 529354)`, then rebuild final SSSOM so the row no longer
  exports a supplier catalog label in `other`.
