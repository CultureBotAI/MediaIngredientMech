# `data/ingredients/mapped/2-propanolCO2.yaml`

## Verdict

Needs curation, minor. The local fallback identity and propan-2-ol/carbon
dioxide decomposition are correct, but top-level and mapping-evidence notes
still describe the older unresolved split state.

## Identity

- Reviewed record: `data/ingredients/mapped/2-propanolCO2.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:2_propanol_co2`
  with the same `ontology_mapping.ontology_id`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- This is intentionally a local registry identity for the full
  `2-propanol+CO2` combination. It does not falsely exact-match either
  component.
- Official ChEBI checks confirm the two curated components:
  `CHEBI:17824` resolves to `propan-2-ol`, and `CHEBI:16526` resolves to
  `carbon dioxide`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-oxobutanoate.yaml data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/2-oxopentanoate.yaml data/ingredients/mapped/2-pentyl-furan.yaml data/ingredients/mapped/2-propanolCO2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-propanolCO2.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  skipped as expected because `kgmicrobe.ingredient` is not an OBO-backed prefix
  for Engine A.
- Whole-corpus checks run earlier in this review pass passed, including the
  Engine B id/label product gate and component partonomy gate; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-propanolCO2` to `kgmicrobe.ingredient:2_propanol_co2` row.

## Evidence

- `mappings/microbedecoder_residual_research_decomposition.tsv` contains the
  curated high-confidence split into `CHEBI:17824:propan-2-ol` and
  `CHEBI:16526:carbon dioxide`, matching the active `components`.
- The current `component_assertion` puts the source-label and curated-dataset
  evidence on the has-part assertion rather than on either component as a false
  identity for the whole mixture.
- `data/ingredients/mapped/Isopropyl_Alcohol.yaml` owns the
  `CHEBI:17824`/`propan-2-ol` component, and
  `data/ingredients/mapped/Carbon_dioxide_gas.yaml` owns the
  `CHEBI:16526`/`carbon dioxide` component.
- Stale: top-level `notes` still say no match was found and curator review was
  needed.
- Stale: `ontology_mapping.evidence[0].notes` still comes from the earlier
  label split and says `ingredient_type=DEFINED_MEDIUM`; the current curated
  decomposition is `ingredient_type: NAMED_MEDIUM`.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the original
  microbedecoder source row, the curated decomposition row, component owner
  records, active YAML/aggregate/SSSOM rows, and stale generated batch findings
  for the local `kgmicrobe.ingredient` CURIE.

## Completeness

- Both source-label constituents are represented exactly and no concentrations
  were invented.
- The non-media `microbedecoder` source occurrence count, 8, is represented
  under `occurrence_statistics.source_occurrences`.
- Empty role and chemical-property slots are acceptable for this local
  two-component mixture.

## Recommended Edits

1. In `data/ingredients/mapped/2-propanolCO2.yaml`, replace stale top-level
   notes with the current fallback/decomposition rationale.
2. In the same file, replace `ontology_mapping.evidence[0].notes` with the
   current post-curated-decomposition statement so it no longer says
   `ingredient_type=DEFINED_MEDIUM`.
3. Run `just sync-curated`, `just validate-strict
   data/ingredients/mapped/2-propanolCO2.yaml`, `just qc-component-partonomy`,
   `just qc-sssom`, and `just qc-flat-coverage` after that curation edit.
