# `data/ingredients/mapped/Parachlorophenylalanine.yaml`

## Verdict

Pass. The CAS-primary record was correctly regraded from a false parent edge to
the exact `CHEBI:110187` identity, and the final SSSOM preserves both the CHEBI
and CAS exact rows.

## Identity

- Reviewed record: `data/ingredients/mapped/Parachlorophenylalanine.yaml`.
- Identifier and grounding: `identifier: cas:7424-00-2` with
  `ontology_mapping.ontology_id: CHEBI:110187`, label
  `2-amino-3-(4-chlorophenyl)propanoic acid`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- The existing OAK/OLS row review confirmed that the CHEBI exact row's synonym
  is already represented.
- A local CAS checksum calculation confirmed that `7424-00-2` has the expected
  check digit.
- The final SSSOM rows were inspected directly: the record publishes an exact
  row to `CHEBI:110187` and an exact CAS registry row to `cas:7424-00-2`.

## Evidence

- The structured CAS-RN, formula, SMILES, InChI, and PubChem CID agree with the
  same substance represented by `CHEBI:110187`.
- The #326 regrade correctly changed the old PubChem-xref parent assignment
  into identity after confirming identical formula and InChIKey.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the final
  CAS registry row as expected, not as an ontology repair.
- The final SSSOM keeps only `CAS:7424-00-2` in `other`.

## Completeness

- The exact CHEBI row plus CAS registry row preserve both the public term and
  the source CAS identity.

## Recommended Edits

- None.
