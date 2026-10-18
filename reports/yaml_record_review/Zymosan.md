# `data/ingredients/mapped/Zymosan.yaml`

## Verdict

Pass. The CultureBotHT CAS fallback preserves `cas:9010-72-4` as the exact
identity, keeps `NCIT:C183132` Zymosan as a narrow parent, publishes the
expected local registry exact row, and exports no unsupported synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Zymosan.yaml`.
- Primary identifier: `cas:9010-72-4`, with matching
  `chemical_properties.cas_rn`.
- Parent grounding: `ontology_mapping.ontology_id: NCIT:C183132`, label
  `Zymosan`, source `NCIT`, and `mapping_quality: NARROW_MATCH`.
- `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: none recorded, which is coherent for a CultureBotHT-only
  chemical import.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- Focused Engine A label validation was skipped for this record because its
  primary identity is a CAS registry CURIE and the companion exact row is local
  `kgmicrobe.compound`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `Zymosan` in NCIT returned active `NCIT:C183132`
  label `Zymosan`.

## Evidence

- The final SSSOM exports
  `MIM:Zymosan skos:narrowMatch NCIT:C183132`.
- The final SSSOM exports the CAS identity row
  `MIM:Zymosan skos:exactMatch cas:9010-72-4`.
- The final SSSOM also exports the expected local registry row
  `MIM:Zymosan skos:exactMatch kgmicrobe.compound:zymosan`.
- The final `other` field is either empty or limited to matching
  `CAS:9010-72-4`.

## Issues

None.

## Completeness

- CAS identity, NCIT parent mapping, single-ingredient type, aggregate copy, and
  all three final SSSOM rows agree.

## Recommended Edits

None.
