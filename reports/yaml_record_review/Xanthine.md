# `data/ingredients/mapped/Xanthine.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:17712` xanthine identity, structure fields, CAS RN,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Xanthine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17712` with matching
  `ontology_mapping.ontology_id`, label `9H-xanthine`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `69-89-6`.
- Chemical fields: formula `C5H4N4O2` with populated InChI and SMILES strings.
- Synonyms: seven clean kg-microbe synonyms for xanthine.
- Occurrences: 21 CultureMech recipe occurrences across 21 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wolfes_Vitamin_Mix` through `Xanthine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the two
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:17712` returns active label `9H-xanthine`, CAS
  `69-89-6`, formula `C5H4N4O2`, matching structure strings, and synonym
  coverage for the clean kg-microbe labels.
- The final SSSOM row correctly has
  `MIM:Xanthine skos:exactMatch CHEBI:17712`.

## Issues

None.

## Completeness

- The CAS-backed CHEBI mapping, structure fields, CAS RN, occurrence count,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
