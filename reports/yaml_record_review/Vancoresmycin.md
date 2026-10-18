# `data/ingredients/mapped/Vancoresmycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI identity, structure fields, aggregate row,
and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vancoresmycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:213208` with matching
  `ontology_mapping.ontology_id`, label `Vancoresmycin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical fields: formula `C71H126N2O21` and ChEBI/PubChem SMILES/InChI.
- Occurrences: one MicrobeDecoder metabolite-production occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vancomycin_Hydrochloride_From_Streptomyces_Orientalis` through `Vanillin`:
  exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI-primary
  subset of this batch exited 0 for `Vancomycin_Hydrochloride_From_Streptomyces_Orientalis`,
  this file, `Vanillic_Acid`, and `Vanillin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:213208` returns active label `Vancoresmycin`,
  formula `C71H126N2O21`, and the same SMILES/InChI as the YAML.
- The final SSSOM row correctly has
  `MIM:Vancoresmycin skos:exactMatch CHEBI:213208`, with review provenance and
  no unsupported labels in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, structure fields, MicrobeDecoder occurrence count,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
