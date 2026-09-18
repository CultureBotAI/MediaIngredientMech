# `data/ingredients/mapped/Na2b4o7.yaml`

## Verdict

Pass. The record maps exactly to active `CHEBI:38892` disodium tetraborate,
keeps the CAS-backed formula and structure on the same anhydrous salt identity,
and carries a source-backed `TRACE_ELEMENT` role from the imported CultureMech
mineral-source role text.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2b4o7.yaml`.
- Identifier and grounding: `identifier: CHEBI:38892` with
  `ontology_mapping.ontology_id: CHEBI:38892`, label
  `disodium tetraborate`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 9 CultureMech recipe occurrences across 9 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2_Alpha-ketoglutarate` through `Na2co3`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:38892` as active
  `disodium tetraborate`, with `cas:1330-43-4`, formula `H4B4O9.2Na`, the
  stored structure, and the accepted disodium tetraborate synonyms.
- `nutritional_roles.TRACE_ELEMENT` is supported by the migrated CultureMech
  role evidence: the raw CultureMech role text was `Mineral`, and boron is the
  trace element supplied by this tetraborate salt.
- The final SSSOM row maps `MIM:Na2b4o7` exactly to `CHEBI:38892`; the
  published synonym and `CAS:1330-43-4` token are synonyms or registry aliases
  for the same anhydrous disodium tetraborate subject.

## Completeness

- The exact ChEBI target, canonical CAS RN, formula, structure, 9/9 occurrence
  count, role evidence, and final exact row agree.
- The raw CultureMech role/property strings are filtered out of the final
  SSSOM as expected.

## Recommended Edits

- None.
