# `data/ingredients/mapped/Vanillic_Acid.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, structure fields, synonym, aggregate
row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vanillic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30816` with matching
  `ontology_mapping.ontology_id`, label `vanillic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `121-34-6`.
- Synonyms: one exact KEGG/ChEBI synonym.
- Chemical fields: formula `C8H8O4` and ChEBI-backed SMILES/InChI.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vancomycin_Hydrochloride_From_Streptomyces_Orientalis` through `Vanillin`:
  exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI-primary
  subset of this batch exited 0 for `Vancomycin_Hydrochloride_From_Streptomyces_Orientalis`,
  `Vancoresmycin`, this file, and `Vanillin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:30816` returns active label `vanillic acid`, CAS
  xref `121-34-6`, formula `C8H8O4`, and the same SMILES/InChI as the YAML.
- The exported `4-Hydroxy-3-methoxybenzoic acid` synonym is present on
  `CHEBI:30816`.
- The final SSSOM row correctly has
  `MIM:Vanillic_Acid skos:exactMatch CHEBI:30816`, with that synonym and
  `CAS:121-34-6` in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, synonym, aggregate copy,
  and final SSSOM row agree.

## Recommended Edits

None.
