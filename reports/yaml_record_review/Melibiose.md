# `data/ingredients/mapped/Melibiose.yaml`

## Verdict

Pass. The exact ChEBI identity, CAS number, structure, CultureMech role, and
final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Melibiose.yaml`.
- Identifier and grounding: `identifier: CHEBI:28053` with
  `ontology_mapping.ontology_id: CHEBI:28053`, label `melibiose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: three CultureMech recipes.
- Chemical identity: `cas_rn: 585-99-9`, formula `C12H22O11`, and InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Melibiose` through `Menaquinone`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:28053` as active `melibiose` with CAS `585-99-9`,
  formula `C12H22O11`, the same InChI and SMILES carried in the YAML, and the
  exact synonyms exported in final `other`.
- PubChem resolves CAS `585-99-9` to CID 440658 with formula `C12H22O11` and
  the same InChI carried in the YAML.
- The `CARBON_SOURCE` facet is backed by the original CultureMech role text
  `Carbon Source`, so it is not only a name-derived inference.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Melibiose` to
  `CHEBI:28053`; every non-CAS `other` token is present in ChEBI, and
  `CAS:585-99-9` matches `chemical_properties.cas_rn`.

## Completeness

- The raw CultureMech role/property synonym remains in YAML as provenance but is
  filtered from final SSSOM.

## Recommended Edits

- None.
