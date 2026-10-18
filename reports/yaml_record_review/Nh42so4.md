# `data/ingredients/mapped/Nh42so4.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:62946` ammonium sulfate identity,
CAS-backed structure, source-backed `NITROGEN_SOURCE` role, occurrence count,
and core final row pass, but final SSSOM still publishes a malformed formula
and a Fisher catalog label as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh42so4.yaml`.
- Identifier and grounding: `identifier: CHEBI:62946` with
  `ontology_mapping.ontology_id: CHEBI:62946`, label `ammonium sulfate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1807 CultureMech recipe occurrences across 1807 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh42hpo4` through `Nh43_Citrate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:62946` as active
  `ammonium sulfate` with formula `2H4N.O4S`, CAS `7783-20-2`, and the same
  InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `7783-20-2` resolves to ammonium sulfate with
  the same InChI, confirming the chemical block.
- `NITROGEN_SOURCE` is supported by imported CultureMech `Nitrogen source`
  role text, and raw `Role:`/`Properties:` labels are filtered from final
  SSSOM.
- Major: final SSSOM `other` still publishes `(NH4)2S4`, a malformed formula
  from a merged duplicate, and `(NH4)2SO4(Fisher A 702)`, a vendor/catalog
  surface. Neither is an unconstrained synonym for `CHEBI:62946`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 1807/1807 occurrence
  count, role evidence, and final exact row otherwise agree.
- The remaining consequential gap is the malformed and catalog-bearing text in
  final SSSOM `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nh42so4.yaml`, reject or demote
  `(NH4)2S4` and `(NH4)2SO4(Fisher A 702)`, then rebuild final SSSOM so the
  row exports only real ammonium sulfate synonyms plus `CAS:7783-20-2`.
