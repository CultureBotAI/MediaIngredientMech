# `data/ingredients/mapped/Delta-Decalactone.yaml`

## Verdict

Pass. CAS `705-86-2` grounds the CultureBotHT delta-decalactone label to active
`CHEBI:87327` 6-pentyloxan-2-one, the stored formula, InChI, and SMILES agree
with local ChEBI, and the final SSSOM `other` payload is limited to the same
CAS RN.

## Identity

- Reviewed record: `data/ingredients/mapped/Delta-Decalactone.yaml`.
- Identifier and grounding: `identifier: CHEBI:87327` with
  `ontology_mapping.ontology_id: CHEBI:87327`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:87327` to active `6-pentyloxan-2-one`, formula
  `C10H18O2`, charge `0`, InChI, SMILES, exact synonym `6-pentyloxan-2-one`,
  related synonym `delta-decalactone`, and CAS xref `705-86-2`.
- The record's formula, InChI, and SMILES agree with the local ChEBI term
  metadata.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Defibrinated_sheep_blood.yaml data/ingredients/mapped/Delamanid.yaml data/ingredients/mapped/Delta-Decalactone.yaml data/ingredients/mapped/Delta-Dodecalactone.yaml data/ingredients/mapped/Delta-Nonalactone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- The direct 5-file Engine A term-validation run failed on `MICRO:0001570`
  before it reached this ChEBI record.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:134742 CHEBI:87327 CHEBI:171817 CHEBI:171747`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:87327`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:87327` mapping as confirmed with no row-review action required.
- The 2026-08-24 curation event preserves the CAS-to-ChEBI lookup provenance in
  `mapping_quality: CAS_RN_LOOKUP`; this is the method that established the
  exact mapping, even though the label also matches a ChEBI synonym.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML or stale parent-mapping row for
  `CHEBI:87327`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `CHEBI:87327`,
  matching `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Delta-Decalactone` to `CHEBI:87327` with `skos:exactMatch`, canonical
  object label `6-pentyloxan-2-one`, CHEBI object source, and `CAS:705-86-2`
  in `other`.

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
