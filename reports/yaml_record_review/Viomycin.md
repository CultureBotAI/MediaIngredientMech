# `data/ingredients/mapped/Viomycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI identity, structure fields, aggregate row,
and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Viomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:15782` with matching
  `ontology_mapping.ontology_id`, label `viomycin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical fields: formula `C25H43N13O10` and ChEBI/PubChem SMILES/InChI.
- Occurrences: one MicrobeDecoder metabolite-production occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Veratrine_Hydrochloride` through `Viomycin`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Verbascose`, `Vibriostat`, and `Viomycin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:15782` returns active label `viomycin`, formula
  `C25H43N13O10`, and the same SMILES/InChI as the YAML.
- The final SSSOM row correctly has
  `MIM:Viomycin skos:exactMatch CHEBI:15782`, with review provenance and no
  unsupported labels in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, structure fields, MicrobeDecoder occurrence count,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
