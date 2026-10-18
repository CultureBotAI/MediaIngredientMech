# `data/ingredients/mapped/Nh43_Citrate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63037` triammonium citrate identity,
CAS-backed structure, `NITROGEN_SOURCE` role, occurrence count, and core final
row pass, but final SSSOM still publishes malformed `(NH4) citrate` as an
exact synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Nh43_Citrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:63037` with
  `ontology_mapping.ontology_id: CHEBI:63037`, label `triammonium citrate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 64 CultureMech recipe occurrences across 64 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nh42hpo4` through `Nh43_Citrate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63037` as active
  `triammonium citrate` with formula `C6H5O7.3H4N`, CAS `3458-72-8`, the
  retained triammonium citrate aliases, and the same InChI and SMILES as the
  record.
- A fresh PubChem CAS lookup for `3458-72-8` resolves to triammonium citrate
  with the same InChI, confirming the chemical block.
- `NITROGEN_SOURCE` is supported by imported CultureMech `Nitrogen Source` role
  text, and raw `Role:`/`Properties:` labels are filtered from final SSSOM.
- Major: final SSSOM `other` still publishes `(NH4) citrate`, a shorthand from
  the merged `Nh4_Citrate` duplicate that does not encode the three ammonium
  counterions of exact `CHEBI:63037`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 64/64 occurrence count,
  role evidence, and final exact row otherwise agree.
- The remaining consequential gap is the malformed merged synonym in final
  SSSOM.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nh43_Citrate.yaml`, reject or delete
  `(NH4) citrate`, then rebuild final SSSOM so `other` keeps only real
  triammonium citrate synonyms plus `CAS:3458-72-8`.
