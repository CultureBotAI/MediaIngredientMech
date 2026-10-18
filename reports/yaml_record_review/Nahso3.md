# `data/ingredients/mapped/Nahso3.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:26709` sodium hydrogensulfite
identity, CAS-backed structure, occurrence count, ChEBI synonyms, and final
exact SSSOM row pass, but `REDUCING_AGENT` is still only a provisional
in-session LLM role.

## Identity

- Reviewed record: `data/ingredients/mapped/Nahso3.yaml`.
- Identifier and grounding: `identifier: CHEBI:26709` with
  `ontology_mapping.ontology_id: CHEBI:26709`, label
  `sodium hydrogensulfite`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 5 CultureMech recipe occurrences across 5 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nah2po4_X_2_H2o` through `Nalidixic_Acid_Sodium_Salt`: exited 0 and left
  `reports/instance_validation_failures.tsv` header-only.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:26709` as active
  `sodium hydrogensulfite` with formula `HO3S.Na`, CAS `7631-90-5`, and the
  same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `7631-90-5` resolves to sodium bisulfite with
  the same InChI, confirming the chemical block.
- The kg-microbe aliases that publish in final SSSOM `other` are listed as OLS
  synonyms for the same ChEBI term.
- Major: `physicochemical_roles.REDUCING_AGENT` is backed only by a
  `COMPUTATIONAL_PREDICTION` whose reference text says it was assigned by
  in-session Claude reasoning with no external API, and the curator note
  explicitly marks it provisional.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 5/5 occurrence count, and
  final exact SSSOM row agree.
- The remaining consequential gap is source-backed evidence for the reducing
  agent role.

## Recommended Edits

- Major: either remove `physicochemical_roles.REDUCING_AGENT` from
  `data/ingredients/mapped/Nahso3.yaml` or replace its LLM-only placeholder
  with source-backed evidence from maintained role-text or literature inputs.
  Rerun strict validation and final SSSOM validation after the role facet
  change.
