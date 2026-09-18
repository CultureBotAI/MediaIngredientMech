# `data/ingredients/mapped/Methylamine_Hydrochloride.yaml`

## Verdict

Pass. The exact `CHEBI:59337` methylamine hydrochloride salt identity, CAS
value, ChEBI/PubChem structure, CultureMech carbon-source role, and final SSSOM
row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methylamine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:59337` with
  `ontology_mapping.ontology_id: CHEBI:59337`, label
  `methylamine hydrochloride`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: thirteen CultureMech recipe occurrences.
- Chemical identity: CAS `593-51-1`, formula `CH6N.Cl`, SMILES, and InChI for
  the hydrochloride salt.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Methanesulfonate` through `Methylcobalamin`: exited 0 and wrote zero
  ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:59337` as active `methylamine hydrochloride` with
  CAS `593-51-1`, formula `CH6N.Cl`, the same SMILES and InChI carried in the
  YAML, and all six kg-microbe aliases as synonyms.
- PubChem resolves CAS `593-51-1` to CID 6364545 with the same salt InChI as
  the YAML and ChEBI target.
- The `CARBON_SOURCE` role preserves the CultureMech original role text as
  `DATABASE_ENTRY` evidence on the nutritional role itself.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methylamine_Hydrochloride` to `CHEBI:59337`; its `other` column excludes
  the raw `Role:`/`Properties:` string while keeping exact salt aliases and
  `CAS:593-51-1`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
