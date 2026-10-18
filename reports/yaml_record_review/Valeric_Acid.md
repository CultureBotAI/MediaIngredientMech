# `data/ingredients/mapped/Valeric_Acid.yaml`

## Verdict

Pass. The exact CHEBI acid identity, CAS RN, structure fields, carbon-source
role, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Valeric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17418` with matching
  `ontology_mapping.ontology_id`, label `valeric acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `109-52-4`.
- Synonyms: three filtered raw CultureMech role/property strings and 13 exact
  synonyms.
- Chemical fields: formula `C5H10O2` and ChEBI-backed SMILES/InChI for neutral
  valeric acid.
- Occurrences: 113 CultureMech recipe occurrences.
- Role: `CARBON_SOURCE` imported from CultureMech original role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Valerate` through `Vancomycin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Valerate`, `Valeric_Acid`, `Valerolactone`, and
  `Vancomycin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:17418` returns active label `valeric acid`, CAS
  xref `109-52-4`, formula `C5H10O2`, and the same InChI and SMILES as the
  YAML.
- The final SSSOM `other` values from exact synonyms are all attached to
  `CHEBI:17418`, including the KEGG-derived `Pentanoate`/`n-Pentanoate`
  strings that look like conjugate-base labels.
- The three raw `Role:`/`Properties:` CultureMech strings are filtered out of
  final SSSOM `other`, as intended.
- The `CARBON_SOURCE` role is backed by `DATABASE_ENTRY` evidence carrying the
  original CultureMech role text `Carbon Source`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, source-backed role,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
