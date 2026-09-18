# `data/ingredients/mapped/Uridine.yaml`

## Verdict

Pass. The CAS-backed exact CHEBI identity, CAS RN, structure fields, synonyms,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Uridine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16704` with matching
  `ontology_mapping.ontology_id`, label `uridine`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `58-96-8`.
- Synonyms: five uridine synonyms.
- Occurrences: 16 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uranyl_Acetate` through `Uridine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:16704` returns active label `uridine`, CAS xref
  `58-96-8`, formula `C9H12N2O6`, the same InChI and SMILES as the YAML, and
  the exported SSSOM `other` labels as CHEBI synonyms.
- The final SSSOM row correctly has
  `MIM:Uridine skos:exactMatch CHEBI:16704`, with uridine synonyms and
  `CAS:58-96-8` in `other`.

## Issues

None.

## Completeness

- The CAS-backed CHEBI mapping, CAS RN, structure fields, synonyms, occurrence
  count, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
