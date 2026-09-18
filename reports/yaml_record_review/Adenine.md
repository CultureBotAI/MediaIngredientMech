# `data/ingredients/mapped/Adenine.yaml`

## Verdict

Needs curation. The exact `CHEBI:16708` identity, exact synonym, CAS, chemistry,
and occurrence count pass, but the final SSSOM row still exports the sibling
hydrate label `Adenine hydrochloride hydrate` as an `other` surface on adenine.

## Identity

- Reviewed record: `data/ingredients/mapped/Adenine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16708` with
  `ontology_mapping.ontology_id: CHEBI:16708`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:16708` to `adenine` with
  formula `C5H5N5`, CAS `73-24-5`, SMILES `Nc1ncnc2ncnc12`, InChI, and
  InChIKey `GFFGJBXGBJISGV-UHFFFAOYSA-N`.
- The stored `9H-purin-6-amine` synonym is the ChEBI exact synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Actinomycin_D.yaml data/ingredients/mapped/Actinomycin_X.yaml data/ingredients/mapped/Actinotiocin.yaml data/ingredients/mapped/Activated_Charcoal.yaml data/ingredients/mapped/Adenine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Adenine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:27666 CHEBI:16708`:
  returned the expected labels and exact synonyms for actinomycin D and
  adenine.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27666 CHEBI:16708`:
  returned formula and structure metadata for both ChEBI terms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT CAS import, official ChEBI record, and local OAK metadata
  support the exact adenine identity, CAS, formula, SMILES, and InChI.
- `mappings/culturemech_recipe_membership.tsv` contains 3 rows for
  `CHEBI:16708`, matching `occurrence_statistics`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirms `CHEBI:16708`;
  `mappings/ingredient_mappings.sssom.tsv` row 343 maps `MIM:Adenine` to
  `CHEBI:16708` with the confirmed trailer.
- SSSOM row 343 also exports `Adenine hydrochloride hydrate` in `other`, even
  though `data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml` already
  models that hydrate as a distinct close match with a CAS registry identity.
- `mappings/other_cross_record_baseline.tsv` tracks the same cross-record
  surface as `HYDRATE_FAMILY_UNREVIEWED`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, OAK/OLS confirmation row, occurrence rows,
  hydrate-cross-record baseline, generated indexes, and ignored aggregate
  backups.

## Completeness

- CAS, formula, SMILES, InChI, exact ChEBI synonym, occurrence statistics,
  curation history, and `ingredient_type` are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove `Adenine hydrochloride hydrate` from the final SSSOM `other` surfaces
  for `MIM:Adenine` through the maintained alias or SSSOM source that feeds
  `mappings/ingredient_mappings.sssom.tsv`.
- Optionally annotate the stale 2026-05-01 history `changes` prose in
  `data/ingredients/mapped/Adenine.yaml`; the active `chemical_properties`
  fields are already correct.
