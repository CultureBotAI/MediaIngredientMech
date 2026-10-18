# `data/ingredients/mapped/Nh4no3.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63038` ammonium nitrate identity,
CAS-backed structure, source-backed `NITROGEN_SOURCE` role, occurrence count,
and core final row pass, but final SSSOM still publishes malformed and
CAS-decorated source labels as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh4no3.yaml`.
- Identifier and grounding: `identifier: CHEBI:63038` with
  `ontology_mapping.ontology_id: CHEBI:63038`, label `ammonium nitrate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 301 CultureMech recipe occurrences across 301 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh4cl` through `Nh4no3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63038` as active
  `ammonium nitrate` with formula `H4N.NO3`, CAS `6484-52-2`, and the same
  InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `6484-52-2` resolves to ammonium nitrate with
  the same InChI, confirming the chemical block and resolved CAS.
- `NITROGEN_SOURCE` is supported by imported CultureMech `Nitrogen source`
  role text, and raw `Role:`/`Properties:` labels are filtered from final
  SSSOM.
- Major: final SSSOM `other` still publishes malformed `NH4NO` and
  CAS-decorated `NH4NO3(CAS: 6484-52-2)`. Neither is an unconstrained synonym
  for `CHEBI:63038`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 301/301 occurrence count,
  role evidence, and final exact row otherwise agree.
- The remaining consequential gap is the malformed and CAS-decorated text in
  final SSSOM `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nh4no3.yaml`, reject or demote `NH4NO`
  and `NH4NO3(CAS: 6484-52-2)`, then rebuild final SSSOM so the row exports
  only real ammonium nitrate synonyms plus `CAS:6484-52-2`.
