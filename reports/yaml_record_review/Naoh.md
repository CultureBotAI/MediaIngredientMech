# `data/ingredients/mapped/Naoh.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:32145` sodium hydroxide identity,
CAS-backed structure, occurrence count, and ChEBI synonyms pass, but final
SSSOM still publishes concentration-qualified solution labels as synonyms for
the plain salt.

## Identity

- Reviewed record: `data/ingredients/mapped/Naoh.yaml`.
- Identifier and grounding: `identifier: CHEBI:32145` with
  `ontology_mapping.ontology_id: CHEBI:32145`, label `sodium hydroxide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1,210 source occurrences across 1,209 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nano` through `Naphthalene`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:32145` as active `sodium hydroxide`
  with formula `HO.Na`, CAS `1310-73-2`, and the same InChI and SMILES as the
  record.
- A fresh PubChem CAS lookup for `1310-73-2` resolves to sodium hydroxide with
  the same InChI, confirming the chemical block.
- The simple kg-microbe aliases that publish in final SSSOM are listed as OLS
  synonyms for the same ChEBI term.
- Major: final SSSOM `other` still includes `NaOH (1N)` and `NaOH (0.38 M)`;
  these are concentration-qualified solutions, not exact synonyms for plain
  `CHEBI:32145`.
- Minor: the auto-proposed `pmid: 37817899` mapping evidence is redundant and
  weak as an identity source. It mentions a sodium hydroxide concentration but
  does not materially improve the ChEBI database grounding.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 1,209/1,210 occurrence
  count, and final exact row otherwise agree.
- The remaining consequential gap is the pair of concentration-qualified
  active synonyms.

## Recommended Edits

- Major: in `data/ingredients/mapped/Naoh.yaml`, reject or delete
  `NaOH (1N)` and `NaOH (0.38 M)`, then rebuild final SSSOM so `other`
  contains only real sodium hydroxide synonyms plus `CAS:1310-73-2`.
- Minor: remove `pmid: 37817899` from
  `ontology_mapping.evidence` unless a curator finds it materially supports
  the identity decision better than the existing database evidence.
