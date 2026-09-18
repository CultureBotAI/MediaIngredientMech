# `data/ingredients/mapped/Malate.yaml`

## Verdict

Needs curation. The exact ChEBI identity and two exact ChEBI synonyms pass, but
the final SSSOM exports a neutral malic-acid CAS value on the malate anion
record and the carbon/energy roles are still provisional name-list
predictions.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Malate.yaml`.
- Identifier and grounding: `identifier: CHEBI:25115` with
  `ontology_mapping.ontology_id: CHEBI:25115`, label `malate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: two total occurrences in two CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malate` through `Malondialdehyde_Tetrabutylammonium_Salt`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:25115` as active `malate` with exact related
  synonyms `malates` and `malic acid anion`.
- PubChem resolves CAS `6915-15-7` to CID 525 with formula `C4H6O5` and IUPAC
  name `2-hydroxybutanedioic acid`, i.e. neutral malic acid, not the malate
  anion class.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Malate` to
  `CHEBI:25115`; its `other` field contains `malates`, `malic acid anion`, and
  `CAS:6915-15-7`.

## Completeness

- `malates` and `malic acid anion` are exact enough for final SSSOM output on
  `CHEBI:25115`.
- The CAS token is not exact for the anion term and should not publish as an
  `other` value for `MIM:Malate`.
- `CARBON_SOURCE` and `ENERGY_SOURCE` are backed only by
  `COMPUTATIONAL_PREDICTION` evidence from curated name-pattern rules with
  provisional curator notes. Neither role has source-specific evidence in the
  record.

## Recommended Edits

- Remove `chemical_properties.cas_rn: 6915-15-7` from `Malate` or replace it
  only with an exact registry identifier for `CHEBI:25115`.
- Remove the provisional `CARBON_SOURCE` and `ENERGY_SOURCE` facets unless
  source-backed evidence can be attached.
