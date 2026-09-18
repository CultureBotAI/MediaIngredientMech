# `data/ingredients/mapped/Mannobiose.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS number, ChEBI structure, exact
IUPAC synonyms, and final SSSOM row pass, but `CARBON_SOURCE` is only a
provisional ChEBI-ancestry inference.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mannobiose.yaml`.
- Identifier and grounding: `identifier: CHEBI:25164` with
  `ontology_mapping.ontology_id: CHEBI:25164`, label `mannobiose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 14417-51-7`, formula `C12H22O11`, InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mannobiose` through `Marine_Broth_2216`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:25164` as active `mannobiose` with formula
  `C12H22O11`, the same InChI and SMILES carried in the YAML, and the two
  exact IUPAC synonyms exported through the final SSSOM.
- PubChem resolves the YAML CAS `14417-51-7` to CID 152109, the same
  `C12H22O11` mannobiose structure also reached through the CAS xref carried
  by ChEBI.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mannobiose` to
  `CHEBI:25164` with the two exact IUPAC synonyms and `CAS:14417-51-7` in
  `other`.

## Completeness

- The record does not publish unsupported exact synonyms or raw non-synonym
  payload in final SSSOM.
- `CARBON_SOURCE` is only backed by a `COMPUTATIONAL_PREDICTION` inferred from
  `CHEBI:16646` carbohydrate ancestry. No source attached to the role verifies
  that mannobiose was deliberately supplied as a carbon source in a medium.

## Recommended Edits

- Curate recipe or literature evidence for `CARBON_SOURCE`, or remove the
  provisional nutritional role.
