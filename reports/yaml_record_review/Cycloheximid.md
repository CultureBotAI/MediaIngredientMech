# `data/ingredients/mapped/Cycloheximid.yaml`

## Verdict

Needs curation; major. The exact `CHEBI:27641` cycloheximide identity, CAS RN,
structure fields, 10/10 CultureMech count, and final SSSOM synonyms pass, but
the `SELECTIVE_AGENT` role is still only a provisional in-session LLM
assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Cycloheximid.yaml`.
- Current identifier and grounding: `identifier: CHEBI:27641`,
  `ontology_mapping.ontology_id: CHEBI:27641`,
  `ontology_label: cycloheximide`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:27641` returns active `CHEBI:27641` labelled
  `cycloheximide` with CAS `66-81-9`, formula `C15H23NO4`, matching
  InChI/SMILES strings, and the expected cycloheximide aliases.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:27641` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cycloheximid.yaml data/ingredients/mapped/Cyclomaltoheptaose.yaml data/ingredients/mapped/Cyclopamine.yaml data/ingredients/mapped/CyclopentanolCO2.yaml data/ingredients/mapped/Cycloviracin_B1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cycloheximid.yaml data/ingredients/mapped/Cyclomaltoheptaose.yaml data/ingredients/mapped/Cyclopamine.yaml data/ingredients/mapped/Cycloviracin_B1.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  `CyclopentanolCO2` was intentionally skipped because its primary identifier
  is a local `kgmicrobe.ingredient` fallback rather than an OBO-backed CHEBI
  term.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The record's CAS RN, formula, InChI, and SMILES match live `CHEBI:27641`.
- `mappings/culturemech_recipe_membership.tsv` contains 10 distinct recipes
  and 10 total occurrences for `CHEBI:27641`, matching
  `occurrence_statistics.media_count` and `.total_occurrences`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `Cyclohexemid` OAK/OLS synonym suggestion as already represented by the YAML.
- The final SSSOM row publishes `MIM:Cycloheximid skos:exactMatch
  CHEBI:27641` and exports only cycloheximide aliases or `CAS:66-81-9` in
  `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` still cites
  `COMPUTATIONAL_PREDICTION` with `Assigned by in-session Claude reasoning (no
  external API)`, so the role is not backed by a database or literature
  source.

## Completeness

- Identity, structure, count, and graph-facing synonym content are complete.
  The remaining curation gap is the unsupported selective-agent role.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found no current duplicate
  `Cycloheximide.yaml` record and no final SSSOM synonym artifact for this row.

## Recommended Edits

- Major: either replace the provisional `SELECTIVE_AGENT` role evidence with a
  source-backed database or literature reference, or remove the role until
  direct use as a selective agent is curated.
- Regenerate synchronized products and rerun strict validation, LinkML term
  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
