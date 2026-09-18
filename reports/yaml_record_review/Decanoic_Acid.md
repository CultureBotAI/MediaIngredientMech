# `data/ingredients/mapped/Decanoic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ChEBI identity denotes decanoic acid
exactly, the stored CAS, formula, InChI, and SMILES agree with local ChEBI, and
the final SSSOM `other` values are the same-substance raw label plus the same
CAS RN.

## Identity

- Reviewed record: `data/ingredients/mapped/Decanoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30813` with
  `ontology_mapping.ontology_id: CHEBI:30813`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:30813` to active `decanoic acid`, a neutral
  C10 straight-chain saturated fatty acid, with formula `C10H20O2`, charge
  `0`, InChI, SMILES, and CAS xref `334-48-5`.
- The curated raw synonym `Capric acid (decanoic acid)` denotes the same acid
  and does not erase a hydrate, salt, stereochemical, or mixture boundary.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the four CHEBI/MeSH rows, including this record, then failed on
  `MICRO:0001572` with the known local sqlite `rdfs_label_statement` lookup
  error.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30813 CHEBI:191094 CHEBI:28903`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:30813`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:30813` mapping as confirmed with no row-review action required.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML or stale parent-mapping row for
  `CHEBI:30813`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `CHEBI:30813`,
  matching `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Decanoic_Acid` to `CHEBI:30813` with `skos:exactMatch`, canonical
  object label `decanoic acid`, CHEBI object source, `Capric acid (decanoic acid)`
  and `CAS:334-48-5` in `other`, and an OAK/OLS confirmed validation stamp.

## Completeness

- CAS RN, formula, InChI, SMILES, curated raw synonym, curation history, and
  ChEBI exact identity are populated.
- Mixture components, ingredient roles, supplied forms, and environmental
  contexts are correctly empty for this pure CultureBotHT chemical import.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
