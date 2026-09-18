# `data/ingredients/mapped/Vanillin.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, structure fields, synonym, aggregate
row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vanillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:18346` with matching
  `ontology_mapping.ontology_id`, label `vanillin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `121-33-5`.
- Synonyms: one exact KEGG/ChEBI synonym.
- Chemical fields: formula `C8H8O3` and ChEBI-backed SMILES/InChI.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vancomycin_Hydrochloride_From_Streptomyces_Orientalis` through `Vanillin`:
  exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI-primary
  subset of this batch exited 0 for `Vancomycin_Hydrochloride_From_Streptomyces_Orientalis`,
  `Vancoresmycin`, `Vanillic_Acid`, and this file.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:18346` returns active label `vanillin`, CAS xref
  `121-33-5`, formula `C8H8O3`, and the same SMILES/InChI as the YAML.
- The exported `4-Hydroxy-3-methoxybenzaldehyde` synonym is present on
  `CHEBI:18346`.
- The final SSSOM row correctly has
  `MIM:Vanillin skos:exactMatch CHEBI:18346`, with that synonym and
  `CAS:121-33-5` in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, synonym, aggregate copy,
  and final SSSOM row agree.

## Recommended Edits

None.
