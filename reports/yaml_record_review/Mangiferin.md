# `data/ingredients/mapped/Mangiferin.yaml`

## Verdict

Pass. The exact ChEBI identity, CAS number, structure, exact IUPAC synonym, and
final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mangiferin.yaml`.
- Identifier and grounding: `identifier: CHEBI:6682` with
  `ontology_mapping.ontology_id: CHEBI:6682`, label `mangiferin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 4773-96-0`, formula `C19H18O11`, InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mandelic_Acid` through `Mannitol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:6682` as active `mangiferin` with CAS
  `4773-96-0`, formula `C19H18O11`, and the same InChI and SMILES carried in
  the YAML.
- ChEBI carries
  `2-beta-D-glucopyranosyl-1,3,6,7-tetrahydroxy-9H-xanthen-9-one` as an exact
  IUPAC synonym.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mangiferin`
  to `CHEBI:6682` with the exact IUPAC synonym and `CAS:4773-96-0` in
  `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
