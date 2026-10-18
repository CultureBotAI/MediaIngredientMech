# `data/ingredients/mapped/Nafcillin_Sodium_Salt_Monohydrate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:51919` nafcillin sodium monohydrate
identity, CAS-backed structure, hydrate-specific grounding, ChEBI synonym, and
final exact SSSOM row pass, but `SELECTIVE_AGENT` is still only a provisional
name-pattern role.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Nafcillin_Sodium_Salt_Monohydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:51919` with
  `ontology_mapping.ontology_id: CHEBI:51919`, label
  `nafcillin sodium monohydrate`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media; the creation
  event traces the CAS lookup to the CultureBotHT Hans80 antibiotic panel.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nacl` through `Nah2po4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:51919` as active
  `nafcillin sodium monohydrate` with formula `C21H21N2O5S.H2O.Na`, CAS
  `7177-50-6`, and the same InChI and SMILES as the record.
- A fresh PubChem lookup for `nafcillin sodium monohydrate` resolves to a CID
  with the same InChI, and a CAS lookup for `7177-50-6` resolves to that same
  CID.
- The CAS-to-ChEBI `CAS_RN_LOOKUP` grade is appropriate because current OLS4
  still lists `7177-50-6` as an xref on `CHEBI:51919`; the SSSOM
  `skos:exactMatch` row is valid under Rule D for the record's own identifier.
- `reports/hydrate_grounding.tsv` classifies this row as `OK_HYDRATE_TERM`,
  and the final SSSOM `other` column keeps only a hydrate-specific ChEBI
  synonym plus `CAS:7177-50-6`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists`, and
  the curator note explicitly marks it provisional.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 0/0 occurrence count, and
  final exact row agree.
- The remaining consequential gap is source-backed evidence for the selective
  agent role.

## Recommended Edits

- Major: either remove `physicochemical_roles.SELECTIVE_AGENT` from
  `data/ingredients/mapped/Nafcillin_Sodium_Salt_Monohydrate.yaml` or replace
  its name-pattern placeholder with source-backed evidence from maintained
  CultureBotHT role input or literature. Rerun strict validation and the final
  SSSOM checks after the role facet change.
