# `data/ingredients/mapped/Daunorubicin.yaml`

## Verdict

Pass. The MicrobeDecoder import is an exact active ChEBI match for
daunorubicin; the stored formula, InChI, and SMILES agree with local ChEBI, no
unsupported roles are asserted, and the final SSSOM row has an empty synonym
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Daunorubicin.yaml`.
- Identifier and grounding: `identifier: CHEBI:41977` with
  `ontology_mapping.ontology_id: CHEBI:41977`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:41977` to active `daunorubicin`, formula
  `C27H29NO10`, charge `0`, an InChI, SMILES, and a DrugBank xref.
- The record's formula, InChI, SMILES, and molecular weight agree with the
  local ChEBI term metadata.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Das_Macro_Solution.yaml data/ingredients/mapped/Das_Vitamin_Cocktail.yaml data/ingredients/mapped/Daunorubicin.yaml data/ingredients/mapped/Day_AminoAcid20.yaml data/ingredients/mapped/Decanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Direct Engine A term validation over the same 5 files exited 1 on the local
  `kgmicrobe.ingredient` records, so the two ChEBI records were rerun as the
  Engine A subset.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Daunorubicin.yaml data/ingredients/mapped/Decanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed both ChEBI records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:41977 CHEBI:27689`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:41977`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed; all
  generated `docs/data` artifacts matched their producers and every curated
  label was resolvable.

## Evidence

- `mappings/microbedecoder_auto_mapped_review.tsv` records the
  `Daunorubicin.yaml` auto-mapping as approved after a local OAK label check.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML or stale parent-mapping row for
  `CHEBI:41977`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `CHEBI:41977`, matching
  `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The record is retained through `source_occurrences` from MicrobeDecoder:
  one `BacDive_Antibiotic_resistance` mention.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Daunorubicin` to `CHEBI:41977` with `skos:exactMatch`, canonical object
  label `daunorubicin`, CHEBI object source, and empty `other`.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence, curation history,
  and ChEBI exact identity are populated.
- Synonyms, mixture components, ingredient roles, supplied forms, and
  environmental contexts are correctly empty for this MicrobeDecoder-only
  resistance/metabolite import.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
