# `data/ingredients/mapped/Decyl_Alcohol.yaml`

## Verdict

Pass. CAS `112-30-1` uniquely grounds the CultureBotHT `decyl alcohol` label to
active `CHEBI:28903` decan-1-ol, the stored formula, InChI, and SMILES agree
with local ChEBI, and the final SSSOM `other` payload is limited to the same
CAS RN.

## Identity

- Reviewed record: `data/ingredients/mapped/Decyl_Alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:28903` with
  `ontology_mapping.ontology_id: CHEBI:28903`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:28903` to active `decan-1-ol`, a fatty alcohol with
  a hydroxy group at C-1 of an unbranched saturated 10-carbon chain, with
  formula `C10H22O`, charge `0`, InChI, SMILES, related synonym
  `Decyl alcohol`, and CAS xref `112-30-1`.
- The record's formula, InChI, and SMILES agree with the local ChEBI term
  metadata.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the four CHEBI/MeSH rows, including this record, then failed on
  `MICRO:0001572` with the known local sqlite `rdfs_label_statement` lookup
  error.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30813 CHEBI:191094 CHEBI:28903`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:28903`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:28903` mapping as confirmed with no row-review action required.
- The 2026-08-24 curation event preserves the important method provenance:
  this record was established through an explicit CAS-to-ChEBI lookup, so
  `CAS_RN_LOOKUP` is retained rather than downgrading the evidence to lexical
  agreement with the ChEBI synonym `Decyl alcohol`.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML or stale parent-mapping row for
  `CHEBI:28903`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `CHEBI:28903`,
  matching `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Decyl_Alcohol` to `CHEBI:28903` with `skos:exactMatch`, canonical
  object label `decan-1-ol`, CHEBI object source, and `CAS:112-30-1` in
  `other`.

## Completeness

- CAS RN, formula, InChI, SMILES, curation history, and ChEBI exact identity
  are populated.
- Synonyms, mixture components, ingredient roles, supplied forms, and
  environmental contexts are correctly empty for this pure CultureBotHT
  chemical import.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
