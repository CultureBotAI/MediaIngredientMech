# `data/ingredients/mapped/Na2edta2h2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:64758` EDTA disodium salt dihydrate
identity, corrected CAS RN, hydrate formula, duplicate merge, occurrence count,
and final exact row pass, but the `CHELATOR` role is provisional and final
SSSOM still publishes a catalog-bearing raw label as a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2edta2h2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:64758` with
  `ontology_mapping.ontology_id: CHEBI:64758`, label
  `EDTA disodium salt dihydrate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 140 CultureMech recipe occurrences across 139 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2edta2h2o` through `Na2hpo4_X_12_H2o`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:64758` as active
  `EDTA disodium salt dihydrate`, with EDTA disodium dihydrate and hydrate
  aliases on the same ChEBI term.
- A fresh PubChem lookup for CAS RN `6381-92-6` resolves to the same EDTA
  disodium dihydrate formula and InChI stored in `chemical_properties`; the
  #114 correction moved the EC number out of `cas_rn` and left the correct CAS
  value in place.
- `reports/hydrate_grounding.tsv` classifies `CHEBI:64758` as
  `OK_HYDRATE_TERM`; the record and final SSSOM preserve the dihydrate boundary
  rather than collapsing to anhydrous `CHEBI:64734`.
- Major: `physicochemical_roles.CHELATOR` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from the `CHEBI:38161` ancestry rule, and
  the curator note explicitly marks the role provisional.
- Major: final SSSOM `other` publishes a Sigma ED255 catalog-bearing raw label.
  That token records source procurement metadata and should not publish as a
  clean EDTA disodium salt dihydrate synonym.

## Completeness

- The active ChEBI target, corrected CAS RN, formula, structure, duplicate
  merge, 140/139 occurrence count, and final exact row agree.
- The remaining consequential gaps are source-backed evidence for the
  `CHELATOR` role and filtering of the catalog-bearing final `other` token.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2edta2h2o.yaml`, either remove
  `physicochemical_roles.CHELATOR` or replace its ChEBI-ancestry placeholder
  with source-backed evidence from maintained role-text or literature inputs.
- Major: keep the Sigma ED255 source label as provenance only, or retype it to a
  catalog/provenance slot that is filtered from final SSSOM; rebuild final SSSOM
  and rerun the final SSSOM plus product label validators.
