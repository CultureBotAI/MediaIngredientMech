# `data/ingredients/mapped/Valerate.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI anion identity, structure fields,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Valerate.yaml`.
- Identifier and grounding: `identifier: CHEBI:31011` with matching
  `ontology_mapping.ontology_id`, label `valerate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical fields: formula `C5H9O2` and ChEBI/PubChem SMILES/InChI for the
  deprotonated anion.
- Occurrences: 45 MicrobeDecoder metabolite-utilization occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Valerate` through `Vancomycin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Valerate`, `Valeric_Acid`, `Valerolactone`, and
  `Vancomycin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:31011` returns active label `valerate`, formula
  `C5H9O2`, the same InChI and SMILES as the YAML, and CAS xref `10023-74-2`.
- The record is correctly separate from neutral `CHEBI:17418` valeric acid.
- The final SSSOM row correctly has
  `MIM:Valerate skos:exactMatch CHEBI:31011` with review provenance and no
  parent or neutral-acid synonyms in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, anion structure, MicrobeDecoder occurrence count,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
