# `data/ingredients/mapped/Lysocellin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:212437 identity, active ChEBI and PubChem
structure, MicrobeDecoder source occurrence, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lysocellin.yaml`.
- Identifier and grounding: `identifier: CHEBI:212437` with
  `ontology_mapping.ontology_id: CHEBI:212437`, label `Lysocellin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C34H60O10`, InChI, SMILES, and
  molecular weight.
- Occurrences: one MicrobeDecoder source occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lydimycin` through `Lysozyme`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:212437` as active `Lysocellin` and records the same
  formula as the YAML record.
- PubChem resolves lysocellin to CID `10258453` with formula `C34H60O10` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:212437`; its
  `other` field is empty.

## Completeness

- The active CHEBI identity, MicrobeDecoder source occurrence, formula,
  structure block, aggregate copy, and final SSSOM row are present and
  consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
