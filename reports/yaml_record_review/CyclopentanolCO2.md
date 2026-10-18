# `data/ingredients/mapped/CyclopentanolCO2.yaml`

## Verdict

Needs curation; minor. The local fallback identity, two-component
`cyclopentanol`/`carbon dioxide` decomposition, 3 MicrobeDecoder source
occurrences, and final SSSOM row pass, but the top-level and mapping-evidence
notes still describe the older unresolved label-split state.

## Identity

- Reviewed record: `data/ingredients/mapped/CyclopentanolCO2.yaml`.
- Current identifier and grounding:
  `identifier: kgmicrobe.ingredient:cyclopentanol_co2` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:cyclopentanol_co2`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- This is intentionally a local registry identity for the full
  `Cyclopentanol+CO2` combination. It does not falsely exact-match either
  component.
- Live OLS checks confirm the two curated components: `CHEBI:16133` resolves to
  `cyclopentanol`, and `CHEBI:16526` resolves to `carbon dioxide`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using
  `kgmicrobe.ingredient:cyclopentanol_co2` as its primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cycloheximid.yaml data/ingredients/mapped/Cyclomaltoheptaose.yaml data/ingredients/mapped/Cyclopamine.yaml data/ingredients/mapped/CyclopentanolCO2.yaml data/ingredients/mapped/Cycloviracin_B1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cycloheximid.yaml data/ingredients/mapped/Cyclomaltoheptaose.yaml data/ingredients/mapped/Cyclopamine.yaml data/ingredients/mapped/Cycloviracin_B1.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  This local fallback record was intentionally skipped because its primary
  identifier is not an OBO-backed CHEBI term.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed for
  the whole corpus before this read-only report batch, covering this record's
  `component_assertion` and component scopes.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` records
  `cyclopentanol+CO2` with count 3 from `bergey:substrates`, matching the
  record's `source_occurrences` entry.
- `mappings/microbedecoder_residual_research_decomposition.tsv` contains the
  curated high-confidence split into `CHEBI:16133:cyclopentanol` and
  `CHEBI:16526:carbon dioxide`, matching the active `components`.
- The final SSSOM row publishes `MIM:CyclopentanolCO2 skos:exactMatch
  kgmicrobe.ingredient:cyclopentanol_co2` with an empty `other` column.
- Stale: top-level `notes` still say no match was found and curator review was
  needed.
- Stale: `ontology_mapping.evidence[0].notes` still comes from the earlier
  label split and says only one of two constituents resolved plus
  `ingredient_type=DEFINED_MEDIUM`; the current curated decomposition has two
  identified components and `ingredient_type: NAMED_MEDIUM`.

## Completeness

- Both source-label constituents are represented exactly and no concentrations
  were invented.
- Empty role and chemical-property slots are acceptable for this local
  two-component substrate pair.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the original MicrobeDecoder source
  row, the curated decomposition row, the active YAML/aggregate/SSSOM rows, and
  stale generated batch findings for the local `kgmicrobe.ingredient` CURIE.

## Recommended Edits

- Minor: replace the stale top-level `notes` with the current
  fallback/decomposition rationale.
- Minor: replace `ontology_mapping.evidence[0].notes` with the current
  post-curated-decomposition statement so it no longer says only one component
  resolved.
- Run strict validation, component partonomy QC, SSSOM QC, flat export
  coverage, aggregate roundtrip, and `git diff --check` after that curation
  edit.
