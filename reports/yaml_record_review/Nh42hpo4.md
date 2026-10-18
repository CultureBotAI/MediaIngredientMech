# `data/ingredients/mapped/Nh42hpo4.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63051` diammonium hydrogen phosphate
identity, CAS-backed structure, `NITROGEN_SOURCE` role, occurrence count, and
core final row pass, but final SSSOM still publishes a Fisher catalog label as
an exact synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh42hpo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:63051` with
  `ontology_mapping.ontology_id: CHEBI:63051`, label
  `diammonium hydrogen phosphate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 35 CultureMech recipe occurrences across 35 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh42hpo4` through `Nh43_Citrate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63051` as active
  `diammonium hydrogen phosphate` with formula `2H4N.HO4P`, CAS `7783-28-0`,
  the same InChI and SMILES as the record, and the `Ammonium phosphate` and
  `diazanium hydrogen phosphate` aliases.
- A fresh PubChem CAS lookup for `7783-28-0` resolves to diammonium hydrogen
  phosphate with the same InChI, confirming the chemical block.
- `NITROGEN_SOURCE` is supported by the imported CultureMech `Nitrogen Source`
  role text, and raw `Role:`/`Properties:` labels are filtered from final
  SSSOM.
- Major: final SSSOM `other` still publishes `(NH4)2HPO4(Fisher A686)`. That
  is a vendor/catalog surface, not an unconstrained synonym for `CHEBI:63051`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 35/35 occurrence count,
  role evidence, and final exact row otherwise agree.
- The remaining consequential gap is the catalog-bearing duplicate surface in
  final SSSOM.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nh42hpo4.yaml`, reject or demote
  `(NH4)2HPO4(Fisher A686)`, then rebuild final SSSOM so vendor/catalog labels
  are no longer exported as exact synonyms.
