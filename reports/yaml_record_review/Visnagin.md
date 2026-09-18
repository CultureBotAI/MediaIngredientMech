# `data/ingredients/mapped/Visnagin.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, structure fields, synonym, aggregate
row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Visnagin.yaml`.
- Identifier and grounding: `identifier: CHEBI:10002` with matching
  `ontology_mapping.ontology_id`, label `visnagin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `82-57-5`.
- Synonyms: one exact IUPAC synonym.
- Chemical fields: formula `C13H10O4` and ChEBI-backed SMILES/InChI.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Virginiamycin` through `Vitamin_K`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this 5-file CHEBI
  batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:10002` returns active label `visnagin`, CAS xref
  `82-57-5`, formula `C13H10O4`, and the same SMILES/InChI as the YAML.
- The exported `4-methoxy-7-methyl-5H-furo[3,2-g]chromen-5-one` synonym is
  present on `CHEBI:10002`.
- The final SSSOM row correctly has
  `MIM:Visnagin skos:exactMatch CHEBI:10002`, with that synonym and
  `CAS:82-57-5` in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, synonym, aggregate copy,
  and final SSSOM row agree.

## Recommended Edits

None.
