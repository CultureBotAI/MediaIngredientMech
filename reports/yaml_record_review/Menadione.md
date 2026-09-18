# `data/ingredients/mapped/Menadione.yaml`

## Verdict

Pass. The exact ChEBI identity, CAS number, structure, CultureMech vitamin role,
and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Menadione.yaml`.
- Identifier and grounding: `identifier: CHEBI:28869` with
  `ontology_mapping.ontology_id: CHEBI:28869`, label `menadione`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 107 CultureMech recipes.
- Chemical identity: `cas_rn: 58-27-5`, formula `C11H8O2`, and InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Melibiose` through `Menaquinone`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:28869` as active `menadione` with CAS `58-27-5`,
  formula `C11H8O2`, the same InChI and SMILES carried in the YAML, and the
  exact synonyms exported in final `other`.
- PubChem resolves CAS `58-27-5` to CID 4055 with formula `C11H8O2` and the
  same InChI carried in the YAML.
- The `VITAMIN_SOURCE` facet is backed by the original CultureMech role text
  `Vitamin Source`, so it is not only a name-derived inference.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Menadione` to
  `CHEBI:28869`; every non-CAS `other` token is present in ChEBI, and
  `CAS:58-27-5` matches `chemical_properties.cas_rn`.

## Completeness

- The raw CultureMech role/property and KEGG cross-reference synonyms remain in
  YAML as provenance but are filtered from final SSSOM.

## Recommended Edits

- None.
