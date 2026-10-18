# `data/ingredients/mapped/Menthol.yaml`

## Verdict

Pass. The CAS-primary identity, same-structure ChEBI identity row, local
chemistry, and final SSSOM rows pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Menthol.yaml`.
- Identifier and grounding: `identifier: cas:1490-04-6` with
  `ontology_mapping.ontology_id: CHEBI:25187`, label `p-menthan-3-ol`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 1490-04-6`, PubChem CID 1254, formula `C10H20O`,
  and matching PubChem/ChEBI InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Menthol` through `Mes_2-_N-morpholino_Ethane_Sulfonic_Acid`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CAS-primary record and its CHEBI parent.

## Evidence

- EBI OLS4 resolves `CHEBI:25187` as active `p-menthan-3-ol` with formula
  `C10H20O` and the same connectivity InChI carried in the YAML.
- PubChem resolves CAS `1490-04-6` to CID 1254 with formula `C10H20O` and the
  same InChI carried in the YAML.
- The #326 regrade notes explain why the former parent row is now a synonym
  match: the CAS row and the ChEBI row have the same structure.
- The final SSSOM publishes the expected `skos:exactMatch` row to `CHEBI:25187`
  and a registry `skos:exactMatch` row to `cas:1490-04-6`; the only `other`
  token is `CAS:1490-04-6`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
