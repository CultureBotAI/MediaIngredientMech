# `data/ingredients/mapped/Methylamine.yaml`

## Verdict

Pass. The exact `CHEBI:16830` methylamine identity, CAS value, ChEBI/PubChem
structure, CultureMech carbon-source role, MicrobeDecoder typo merge, and final
SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methylamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16830` with
  `ontology_mapping.ontology_id: CHEBI:16830`, label `methylamine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: twelve CultureMech recipe occurrences.
- Chemical identity: CAS `74-89-5`, formula `CH5N`, SMILES, and InChI for
  methylamine.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Methanesulfonate` through `Methylcobalamin`: exited 0 and wrote zero
  ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:16830` as active `methylamine` with CAS `74-89-5`,
  formula `CH5N`, the same SMILES and InChI carried in the YAML, and the
  kg-microbe aliases `CH3-NH2`, `MeNH2`, `Methanamine`, `aminomethane`, and
  `monomethylamine` as synonyms.
- PubChem resolves CAS `74-89-5` to CID 6329 with the same formula and InChI
  carried in the YAML.
- The `CARBON_SOURCE` role preserves the CultureMech original role text as
  `DATABASE_ENTRY` evidence on the nutritional role itself.
- The issue #213 raw label `Methyamine` is documented in curation history as a
  same-subject MicrobeDecoder typo merge.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Methylamine` to
  `CHEBI:16830`; its `other` column excludes the CultureMech `(alternative)`
  and raw `Role:`/`Properties:` strings while keeping same-subject aliases,
  `Methyamine`, and `CAS:74-89-5`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
