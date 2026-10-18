# `data/ingredients/mapped/Oxalic_Acid.yaml`

## Verdict

Needs curation; major. The `CHEBI:16995` oxalic-acid identity and structure
pass, but `chemical_properties.cas_rn` stores invalid CAS `144-62-1`, and the
final SSSOM exports that invalid value as `CAS:144-62-1`.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxalic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16995` with
  `ontology_mapping.ontology_id: CHEBI:16995`, label `oxalic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences; the record was imported from
  CultureBotHT.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps `MIM:Oxalic_Acid`
  exactly to `CHEBI:16995`, with the bad CAS token in `other`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:16995` as active `oxalic acid` and
  reports the same formula, InChI, and SMILES stored in the YAML.
- ChEBI cross-references CAS `144-62-7`, not the YAML value `144-62-1`.
- A local CAS checksum calculation also rejects `144-62-1`: the expected check
  digit for prefix `144-62` is `7`.
- Because the final SSSOM row exports the structured YAML value as
  `CAS:144-62-1`, the typo is a published non-synonym rather than an isolated
  metadata issue.
- No roles, supplied forms, components, or free-text synonyms are asserted.

## Completeness

- The active ChEBI term, formula, structure, and exact SSSOM object agree.
- The CAS value needs correction before the final row's `other` column can be
  treated as true same-subject synonym payload.

## Recommended Edits

- Major: in `data/ingredients/mapped/Oxalic_Acid.yaml`, change
  `chemical_properties.cas_rn` from `144-62-1` to `144-62-7`, preserve the
  reason in curation history, rebuild the final SSSOM, and rerun
  `scripts/validate_sssom_invariants.py` plus the id-label product check so
  `mappings/ingredient_mappings.sssom.tsv` exports `CAS:144-62-7`.
