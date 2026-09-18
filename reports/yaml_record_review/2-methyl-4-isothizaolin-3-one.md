# `data/ingredients/mapped/2-methyl-4-isothizaolin-3-one.yaml`

## Verdict

Needs curation, minor. The CAS-backed `CHEBI:53620` methylisothiazolinone
identity and chemistry pass, but the local preferred term and slug retain the
misspelling `isothizaolin`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-methyl-4-isothizaolin-3-one.yaml`.
- Identifier and grounding: `identifier: CHEBI:53620` with
  `ontology_mapping.ontology_id: CHEBI:53620`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:53620`
  resolves to `methylisothiazolinone`, lists formula `C4H5NOS`, lists CAS RN
  `2682-20-4`, and lists `2-Methyl-4-isothiazolin-3-one` with the expected
  `isothiazolin` spelling.
- Formula, InChI, and SMILES are populated and exactly match the ChEBI
  structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-methyl-1-butanol.yaml data/ingredients/mapped/2-methyl-4-isothizaolin-3-one.yaml data/ingredients/mapped/2-n-Heptyl-4-hydroxyquinoline_N-oxide.yaml data/ingredients/mapped/2-naphthyl_Dihydrogen_Phosphate.yaml data/ingredients/mapped/2-naphthyl_Tetradecanoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-methyl-4-isothizaolin-3-one.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-methyl-4-isothizaolin-3-one` to `CHEBI:53620` row, with
  `CAS:2682-20-4` represented in the SSSOM `other` field.

## Evidence

- The active ChEBI term confirms the current CAS-backed
  methylisothiazolinone identity.
- Minor: the active `preferred_term` and filename contain `isothizaolin`, while
  the official ChEBI synonym contains the expected `2-Methyl-4-isothiazolin-3-one`
  spelling. The hidden/ignored-inclusive search over `data/custom`,
  `data/curated`, `data/ingredients`, `mappings`, and `reports` found no live
  source row requiring the misspelling to remain the record name.
- The July OAK/OLS row marked `2-methyl-4-isothizaolin-3-one` as a synonym
  enrichment candidate and the row-review manifest treated it as already
  represented because the candidate text was already the misspelled local
  preferred term.
- `mappings/record_research_validation.tsv` already flags the same spelling
  problem in the label and slug. Its identity concerns are stale because the
  current CAS RN, ChEBI target, formula, InChI, and SMILES agree.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- The core chemistry needed for the active neutral compound is populated.
- Empty occurrence counts are expected for this CultureBotHT CAS import.

## Recommended Edits

1. Rename `data/ingredients/mapped/2-methyl-4-isothizaolin-3-one.yaml` and the
   local `preferred_term` to a correctly spelled source label, or to ChEBI's
   canonical `methylisothiazolinone`, while preserving the CAS-backed
   `CHEBI:53620` grounding.
2. Consider adding the official `2-Methyl-4-isothiazolin-3-one` synonym if the
   canonical label remains `methylisothiazolinone`.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
4. Re-run the focused strict/LinkML validators, `just qc-sssom`, and
   `just qc-flat-coverage` after the rename.
