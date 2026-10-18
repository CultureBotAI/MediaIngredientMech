# `data/ingredients/mapped/Malonate.yaml`

## Verdict

Pass. The manually promoted bare anion label is grounded to an active ChEBI
malonate(2-) term, its structure agrees with ChEBI, the MicrobeDecoder source
count is preserved, and the final SSSOM row is clean.

## Identity

- Reviewed record: `data/ingredients/mapped/Malonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15792` with
  `ontology_mapping.ontology_id: CHEBI:15792`, label `malonate(2-)`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences and 131 MicrobeDecoder
  `BacDive_Metabolite_utilization` source occurrences.
- Chemical identity: formula `C3H2O4`, InChI and SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malate` through `Malondialdehyde_Tetrabutylammonium_Salt`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:15792` as active `malonate(2-)` with CAS
  `156-80-9`, formula `C3H2O4`, and the same InChI and SMILES carried in the
  YAML.
- ChEBI carries `malonate` as a synonym of `CHEBI:15792`, and the issue 213
  curation history documents the project convention that grounds bare anion
  labels to the bare-name anion class when one exists.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Malonate` to
  `CHEBI:15792` with an empty `other` field.

## Completeness

- The source count is preserved under `source_occurrences`.
- The MicrobeDecoder raw `Malonate` synonym is filtered from final SSSOM, and
  no unsupported roles publish for this record.

## Recommended Edits

- None.
