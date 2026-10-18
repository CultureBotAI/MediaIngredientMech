# `data/ingredients/mapped/Lysine.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:25094 identity, generic ChEBI structure,
CultureMech occurrence count, MicrobeDecoder source count, and final SSSOM row
are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lysine.yaml`.
- Identifier and grounding: `identifier: CHEBI:25094` with
  `ontology_mapping.ontology_id: CHEBI:25094`, label `lysine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C6H14N2O2`, InChI, SMILES, and
  molecular weight.
- Occurrences: 11 total occurrences in 11 CultureMech recipes, plus 285
  MicrobeDecoder source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lydimycin` through `Lysozyme`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:25094` as active `lysine` and records the same
  generic formula and InChIKey as the YAML structure.
- A PubChem name lookup for `lysine` resolves to stereospecific L-lysine, so
  ChEBI is the supporting source for the generic non-stereospecific structure
  in this record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:25094`; its
  `other` field is empty.

## Completeness

- The active CHEBI identity, occurrence statistics, MicrobeDecoder source
  occurrence count, formula, structure block, aggregate copy, and final SSSOM
  row are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
