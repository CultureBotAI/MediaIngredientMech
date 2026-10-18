# `data/ingredients/mapped/4_Carbon_Mix.yaml`

## Verdict

Pass, none. The local `kgmicrobe.ingredient:4_carbon_mix` registry identity,
complete four-component recipe, CultureBotHT occurrence counts, carbon-source
role, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4_Carbon_Mix.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:4_carbon_mix`
  with `ontology_mapping.ontology_id: kgmicrobe.ingredient:4_carbon_mix`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- The local registry identity is intentional: the checked note records that
  ChEBI, NCIT, MeSH, FOODON, and ENVO had no term for this named lab
  preparation, so the record mints a kg-microbe ingredient rather than mapping
  the mixture to one component.
- `ingredient_type: STOCK_SOLUTION` and `solution_type: CARBON_SOURCE_MIX` are
  present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-vinylphenol.yaml data/ingredients/mapped/4_Carbon_Mix.yaml data/ingredients/mapped/4h-pyran-4-one.yaml data/ingredients/mapped/5-Aminolevulinic_Acid.yaml data/ingredients/mapped/5-Azacytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/4_Carbon_Mix.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited non-zero, so Engine A term-label validation is skipped as documented
  for a non-OBO `kgmicrobe.ingredient` prefix.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- The record models a mixture rather than a false exact match to a component:
  `component_assertion.completeness: COMPLETE` lists sodium L-lactate, sodium
  acetate, glutamic acid, and benzoic acid, each at 1.25 mM, and the full
  component partonomy validator accepts the decomposition.
- The CultureBotHT import history records 8 CultureBot media, and the active
  occurrence statistics preserve `total_occurrences: 8` and `media_count: 8`.
- The carbon-source role is source-backed by the same Mixes-tab recipe that
  defines all four constituents as organic-acid carbon sources.
- The SSSOM row maps `MIM:4_Carbon_Mix` to
  `kgmicrobe.ingredient:4_carbon_mix` with `skos:exactMatch`,
  `semapv:ManualMappingCuration`, and no parent ontology row, which is
  consistent with a local identity that does not narrow to any single compound.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`,
  `UNIFIED_INGREDIENT_MAPPING.tsv`, `src`, `scripts`, `tests`, `conf`,
  `.github`, and `.claude` found the active YAML, aggregate copy, SSSOM row,
  generated docs, a stale pre-promotion unmapped audit row, stale advisory
  rows, and ignored aggregate backups.

## Completeness

- Components, concentrations, units, source record, local registry mapping,
  exact raw label, occurrence counts, and the nutritional role are populated.
- No chemical properties, environment, or discussion entries are required for
  this named stock-solution mixture.

## Recommended Edits

No YAML edit is required for this record.
