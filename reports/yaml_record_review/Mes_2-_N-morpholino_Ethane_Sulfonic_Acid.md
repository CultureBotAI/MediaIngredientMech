# `data/ingredients/mapped/Mes_2-_N-morpholino_Ethane_Sulfonic_Acid.yaml`

## Verdict

Pass. The exact ChEBI identity, CAS number, structure, CultureMech buffer role,
and final SSSOM row all pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Mes_2-_N-morpholino_Ethane_Sulfonic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:39005` with
  `ontology_mapping.ontology_id: CHEBI:39005`, label
  `2-(N-morpholino)ethanesulfonic acid`, source `CHEBI`, `mapping_quality:
  SYNONYM_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- Occurrences: 24 CultureMech recipes.
- Chemical identity: `cas_rn: 4432-31-9`, formula `C6H13NO4S`, and InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Menthol` through `Mes_2-_N-morpholino_Ethane_Sulfonic_Acid`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:39005` as active
  `2-(N-morpholino)ethanesulfonic acid` with CAS `4432-31-9`, formula
  `C6H13NO4S`, the same InChI and SMILES carried in the YAML, and the exact MES
  acid synonyms exported in final `other`.
- PubChem resolves CAS `4432-31-9` to CID 78165 with formula `C6H13NO4S` and
  the same InChI carried in the YAML.
- The `BUFFER` facet is backed by the original CultureMech role text `Buffer`,
  so it is not only a name-derived inference.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mes_2-_N-morpholino_Ethane_Sulfonic_Acid` to `CHEBI:39005`; every
  non-CAS `other` token is a same-substance MES acid label and `CAS:4432-31-9`
  matches `chemical_properties.cas_rn`.

## Completeness

- The raw CultureMech role/property synonym remains in YAML as provenance but is
  filtered from final SSSOM.

## Recommended Edits

- None.
