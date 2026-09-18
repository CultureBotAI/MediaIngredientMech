# `data/ingredients/mapped/Vanillylmandelic_Acid.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, structure fields, synonym, aggregate
row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vanillylmandelic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:20106` with matching
  `ontology_mapping.ontology_id`, label `vanillylmandelic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `55-10-7`.
- Synonyms: one exact IUPAC synonym.
- Chemical fields: formula `C9H10O5` and ChEBI-backed SMILES/InChI.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vanillyl_Alcohol` through `Veratric_Acid`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Vanillyl_Alcohol`, `Vanillylmandelic_Acid`,
  `Verapamil_Hydrochloride`, and `Veratric_Acid`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:20106` returns active label
  `vanillylmandelic acid`, CAS xref `55-10-7`, formula `C9H10O5`, and the same
  SMILES/InChI as the YAML.
- The exported `2-hydroxy-2-(4-hydroxy-3-methoxyphenyl)acetic acid` synonym is
  present on `CHEBI:20106`.
- The final SSSOM row correctly has
  `MIM:Vanillylmandelic_Acid skos:exactMatch CHEBI:20106`, with that synonym
  and `CAS:55-10-7` in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, synonym, aggregate copy,
  and final SSSOM row agree.

## Recommended Edits

None.
