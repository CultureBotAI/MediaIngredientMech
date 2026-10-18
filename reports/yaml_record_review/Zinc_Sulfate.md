# `data/ingredients/mapped/Zinc_Sulfate.yaml`

## Verdict

Pass. The CultureMech mineral-source record maps exactly to active
`CHEBI:35176` anhydrous zinc sulfate, the CAS conflict was resolved to the
canonical anhydrous CAS RN, raw role strings are filtered from final SSSOM, and
the CultureMech `TRACE_ELEMENT` role is source-backed.

## Identity

- Reviewed record: `data/ingredients/mapped/Zinc_Sulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:35176` with matching
  `ontology_mapping.ontology_id`, canonical label `zinc sulfate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `7733-02-0`.
- Structure: formula `O4S.Zn` with populated InChI and SMILES for anhydrous
  zinc sulfate.
- Synonyms: exact ChEBI or kg-microbe labels plus raw CultureMech
  `Role: Mineral source` provenance strings.
- Role: source-backed `TRACE_ELEMENT` evidence from the CultureMech original
  `Mineral source` role.
- Occurrences: 250 CultureMech occurrences across 250 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `zinc sulfate` in CHEBI returned
  `CHEBI:35176` with active label `zinc sulfate`.

## Evidence

- The final SSSOM row correctly exports
  `MIM:Zinc_Sulfate skos:exactMatch CHEBI:35176`.
- The final `other` field contains only true zinc-sulfate synonyms plus
  matching `CAS:7733-02-0`; raw `Role:` and `Properties:` strings from the YAML
  are filtered.
- The 2026-04-19 CAS conflict resolution retained `7733-02-0`, the canonical
  OAK/ChEBI xref for anhydrous zinc sulfate, instead of the duplicate-record
  heptahydrate CAS.

## Issues

None.

## Completeness

- The exact CHEBI identifier, CAS, structure fields, single-ingredient type,
  CultureMech role evidence, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
