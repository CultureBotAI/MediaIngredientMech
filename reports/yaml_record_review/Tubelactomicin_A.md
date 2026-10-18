# `data/ingredients/mapped/Tubelactomicin_A.yaml`

## Verdict

Pass. The MicrobeDecoder exact-label match, exact CHEBI identity, structure
fields, source occurrence count, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Tubelactomicin_A.yaml`.
- Identifier and grounding: `identifier: CHEBI:66279` with matching
  `ontology_mapping.ontology_id`, label `tubelactomicin A`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: 1 MicrobeDecoder trait occurrence and no CultureMech recipe
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tryptoneyeastbeef_(tyb)` through `Tuberactinamine_A`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:66279` returns active label `tubelactomicin A`,
  formula `C29H42O6`, and the same InChI and SMILES as the YAML.
- The final SSSOM row correctly has
  `MIM:Tubelactomicin_A skos:exactMatch CHEBI:66279` and no `other` synonyms.

## Issues

None.

## Completeness

- The CHEBI identity, structure fields, MicrobeDecoder occurrence count,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
