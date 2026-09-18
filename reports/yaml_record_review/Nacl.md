# `data/ingredients/mapped/Nacl.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:26710` sodium chloride identity,
structure, occurrence count, environment contexts, and `MINERAL_SOURCE` role
pass, but the final SSSOM row still publishes vendor and concentration labels
as synonyms for the plain salt.

## Identity

- Reviewed record: `data/ingredients/mapped/Nacl.yaml`.
- Identifier and grounding: `identifier: CHEBI:26710` with
  `ontology_mapping.ontology_id: CHEBI:26710`, label `sodium chloride`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 8,191 source occurrences across 7,695 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nacl` through `Nah2po4`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:26710` as active `sodium chloride`
  with formula `Cl.Na`, CAS `7647-14-5`, and the same InChI and SMILES as the
  record.
- A fresh PubChem CAS lookup for `7647-14-5` resolves to sodium chloride with
  the same InChI, confirming the chemical block.
- The kg-microbe synonym payload names active OLS synonyms for the same ChEBI
  term, so the simple salt aliases pass.
- The `MINERAL_SOURCE` role is supported by imported CultureMech `Mineral`
  source role text, and the sea-water and hypersaline-lake contexts are scoped
  as `ENVIRONMENT_MIMIC` rather than natural occurrence claims.
- Major: the final SSSOM `other` column still publishes
  `NaCl (Fisher S271-500)`, `NaCl(Fisher S271-500)`, and
  `1% Sodium Chloride`. The Fisher labels are vendor/catalog variants, and the
  1% label is a concentration-qualified preparation, not a clean synonym for
  `CHEBI:26710`.
- Minor: the auto-proposed `pmid: 40820329` mapping evidence is redundant and
  weak as an identity source. It is not needed to ground the active CHEBI row,
  which is already supported by the CultureMech import and ChEBI itself.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 7,695/8,191 occurrence
  count, role evidence, and environment context scopes agree.
- Raw role/property strings and autoclave/adjustment parentheticals remain
  filtered from final SSSOM `other`; the remaining consequential gap is the
  unfiltered vendor and concentration text.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nacl.yaml`, reject or delete the two
  Fisher catalog strings and `1% Sodium Chloride`, then rebuild final SSSOM so
  `other` contains only real sodium chloride synonyms and `CAS:7647-14-5`.
- Minor: remove `pmid: 40820329` from
  `ontology_mapping.evidence` unless a curator finds it materially supports
  the identity decision better than the existing database evidence.
