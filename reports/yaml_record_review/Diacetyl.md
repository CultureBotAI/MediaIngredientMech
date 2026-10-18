# `data/ingredients/mapped/Diacetyl.yaml`

## Verdict

Needs curation. The MicrobeDecoder residual was promoted to the correct
`CHEBI:16583` butane-2,3-dione identity and its formula, InChI, and SMILES
match ChEBI. The final SSSOM row still exports `2,3-butanone`, which is not a
ChEBI synonym or valid exact synonym for butane-2,3-dione.

## Identity

- Reviewed record: `data/ingredients/mapped/Diacetyl.yaml`.
- Identifier and grounding: `identifier: CHEBI:16583` with
  `ontology_mapping.ontology_id: CHEBI:16583`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:16583` to active `butane-2,3-dione`, exact synonym
  `butane-2,3-dione`, related synonyms including `Diacetyl` and `Biacetyl`,
  formula `C4H6O2`, InChI, SMILES, and CAS xref `431-03-8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16583 CHEBI:4489 CHEBI:23673 CHEBI:91249`:
  returned the canonical label, synonyms, CAS xref, formula, InChI, SMILES,
  charge, and mass for `CHEBI:16583`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/microbedecoder_residual_research_proposed.tsv` and
  `mappings/microbedecoder_residual_research_proposed.sssom.tsv` record
  `diacetyl` as an exact `CHEBI:16583` match and reject adjacent
  `NCIT:C210295` Diacetyl Measurement.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML for `CHEBI:16583`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Diacetyl` to `CHEBI:16583` with `skos:exactMatch`, canonical object
  label `butane-2,3-dione`, and CHEBI object source.
- Major: the final SSSOM row also emits `2,3-butanone` in `other`. That token
  comes from `sssom_other_backfill` and is absent from the `CHEBI:16583`
  synonym set.

## Completeness

- The ChEBI identity, MicrobeDecoder source occurrence, chemistry, and
  promotion history are populated.
- Ingredient roles, supplied forms, mixture components, and environmental
  contexts are correctly empty.

## Recommended Edits

- Major: remove or demote `2,3-butanone` from
  `data/ingredients/mapped/Diacetyl.yaml`, synchronize
  `data/curated/mapped_ingredients.yaml`, and regenerate SSSOM so `other`
  contains only genuine diacetyl synonyms.
