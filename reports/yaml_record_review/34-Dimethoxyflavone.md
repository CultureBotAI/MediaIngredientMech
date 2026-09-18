# `data/ingredients/mapped/34-Dimethoxyflavone.yaml`

## Verdict

Needs curation, major. The CAS-backed mapping to `CHEBI:232299` is correct for
CAS `4143-62-8`, and the stored formula, SMILES, and InChI match ChEBI; however,
the record preferred term and SSSOM subject label say `3,4'-Dimethoxyflavone`
while ChEBI and the CAS-backed structure identify the molecule as
`3',4'-dimethoxyflavone`.

## Identity

- Reviewed record: `data/ingredients/mapped/34-Dimethoxyflavone.yaml`.
- Identifier and grounding: `identifier: CHEBI:232299` with
  `ontology_mapping.ontology_id: CHEBI:232299`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:232299` resolves to
  `3',4'-dimethoxyflavone`, formula `C17H14O4`, SMILES
  `COc1ccc(-c2cc(=O)c3ccccc3o2)cc1OC`, InChI
  `InChI=1S/C17H14O4/c1-19-15-8-7-11(9-17(15)20-2)16-10-13(18)12-5-3-4-6-14(12)21-16/h3-10H,1-2H3`,
  and CAS `4143-62-8`.
- The record's `chemical_properties` match the ChEBI target.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` agree with
  the YAML and therefore also carry the wrong `3,4'-Dimethoxyflavone` subject
  label into the SSSOM exact row.

## Evidence

- CAS `4143-62-8` resolves by ChEBI xref to `CHEBI:232299`, and the stored
  structure is ChEBI's `3',4'-dimethoxyflavone` structure.
- Major: `3,4'-Dimethoxyflavone` and `3',4'-dimethoxyflavone` place the first
  methoxy substituent on different rings. The current `preferred_term`,
  filename stem, SSSOM `subject_label`, and
  `mappings/ingredient_mappings_synonym_enrich_review.tsv` row preserve the
  wrong isomer string even though the CAS-backed target is for the primed
  `3',4'` isomer.
- The history correctly explains that `CAS_RN_LOOKUP` is the evidence path and
  that a lexical grade would discard that provenance; this is a label/slug
  defect rather than a bad CAS-to-ChEBI target.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, generated docs, synonym-enrichment
  advisory row, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, CAS RN, mapping evidence, and `ingredient_type` are
  populated for `3',4'-dimethoxyflavone`.
- The source occurrence was a CultureBotHT CAS lookup with no recipe-count
  occurrence, so `total_occurrences: 0` and `media_count: 0` are expected.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

1. Rename the preferred term and any synchronized subject-label surfaces from
   `3,4'-Dimethoxyflavone` to `3',4'-Dimethoxyflavone`.
2. Regenerate the aggregate, SSSOM, and docs so the corrected isomer label
   replaces the stale subject label everywhere.
3. Revisit `mappings/ingredient_mappings_synonym_enrich_review.tsv` if it is
   regenerated from current data; `3,4'-Dimethoxyflavone` should not be treated
   as already represented after the preferred term is corrected.
4. Run `just sync-curated`, rebuild SSSOM and docs, then verify with
   `just validate-all`, `just qc-sssom`, `just qc-roundtrip`, and
   `just validate-terms data/ingredients/mapped/34-Dimethoxyflavone.yaml`.
