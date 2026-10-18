# `data/ingredients/mapped/Decoyinine.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-matches active `CHEBI:191094`
Decoyinine, the stored structure fields agree with local ChEBI, no unsupported
roles are asserted, and the final SSSOM row has an empty synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Decoyinine.yaml`.
- Identifier and grounding: `identifier: CHEBI:191094` with
  `ontology_mapping.ontology_id: CHEBI:191094`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:191094` to active `Decoyinine`, formula
  `C11H13N5O4`, charge `0`, InChI, SMILES, and an exact systematic synonym.
- The record's formula, InChI, SMILES, and molecular weight agree with the
  local ChEBI term metadata.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the four CHEBI/MeSH rows, including this record, then failed on
  `MICRO:0001572` with the known local sqlite `rdfs_label_statement` lookup
  error.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30813 CHEBI:191094 CHEBI:28903`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:191094`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/microbedecoder_auto_mapped_review.tsv` records the
  `Decoyinine.yaml` auto-mapping as approved after a local OAK label check.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML or stale parent-mapping row for
  `CHEBI:191094`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `CHEBI:191094`,
  matching `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The record is retained through `source_occurrences` from MicrobeDecoder:
  one `BacDive_Metabolite_production` mention.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Decoyinine` to `CHEBI:191094` with `skos:exactMatch`, canonical object
  label `Decoyinine`, CHEBI object source, and empty `other`.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence, curation history,
  and ChEBI exact identity are populated.
- Synonyms, mixture components, ingredient roles, supplied forms, and
  environmental contexts are correctly empty for this MicrobeDecoder-only
  metabolite-production import.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
