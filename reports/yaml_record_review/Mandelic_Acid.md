# `data/ingredients/mapped/Mandelic_Acid.yaml`

## Verdict

Pass. The exact ChEBI identity, CAS number, structure, exact IUPAC synonym, and
final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mandelic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:35825` with
  `ontology_mapping.ontology_id: CHEBI:35825`, label `mandelic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 90-64-2`, formula `C8H8O3`, InChI and SMILES
  copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mandelic_Acid` through `Mannitol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:35825` as active `mandelic acid` with CAS
  `90-64-2`, formula `C8H8O3`, and the same InChI and SMILES carried in the
  YAML.
- ChEBI carries `hydroxy(phenyl)acetic acid` as an exact IUPAC synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mandelic_Acid` to `CHEBI:35825` with `hydroxy(phenyl)acetic acid` and
  `CAS:90-64-2` in `other`.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
