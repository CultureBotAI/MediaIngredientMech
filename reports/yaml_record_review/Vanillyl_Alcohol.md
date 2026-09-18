# `data/ingredients/mapped/Vanillyl_Alcohol.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, structure fields, synonym, aggregate
row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vanillyl_Alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:18353` with matching
  `ontology_mapping.ontology_id`, label `vanillyl alcohol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `498-00-0`.
- Synonyms: one exact IUPAC synonym.
- Chemical fields: formula `C8H10O3` and ChEBI-backed SMILES/InChI.
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

- Fresh OLS4 lookup for `CHEBI:18353` returns active label `vanillyl alcohol`,
  CAS xref `498-00-0`, formula `C8H10O3`, and the same SMILES/InChI as the
  YAML.
- The exported `4-(hydroxymethyl)-2-methoxyphenol` synonym is present on
  `CHEBI:18353`.
- The final SSSOM row correctly has
  `MIM:Vanillyl_Alcohol skos:exactMatch CHEBI:18353`, with that synonym and
  `CAS:498-00-0` in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, synonym, aggregate copy,
  and final SSSOM row agree.

## Recommended Edits

None.
