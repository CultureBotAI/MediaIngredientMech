# `data/ingredients/mapped/1-propanolCO2.yaml`

## Verdict

Needs curation. The current local fallback identity and curated
`propan-1-ol`/`carbon dioxide` decomposition are structurally sound, but
top-level and ontology-mapping notes still describe the older unresolved
label-split state.

## Identity

- Reviewed record: `data/ingredients/mapped/1-propanolCO2.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:1_propanol_co2` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:1_propanol_co2`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Component decomposition: the record uses complete `LABEL_ENUMERATION`
  partonomy with `CHEBI:28831`/`propan-1-ol` and
  `CHEBI:16526`/`carbon dioxide`, both scoped as `MIM_CATALOG`.
- Official ChEBI checks: the current EMBL-EBI pages for `CHEBI:28831` and
  `CHEBI:16526` resolve to `propan-1-ol` and `carbon dioxide`, respectively.
- Boundary checked: active local siblings include
  `1-butanolCO2.yaml`, `2-butanolCO2.yaml`, `2-propanolCO2.yaml`, and
  `CyclopentanolCO2.yaml`; this record's local identifier prevents a false
  exact identity collapse onto either component.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-propanolCO2.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  skipped this record because the mapping target is the local
  `kgmicrobe.ingredient:` prefix, which is covered by generated-product
  validators instead of Engine A OBO label checks.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-naphtylacetic_Acid.yaml data/ingredients/mapped/1-o-methyl_Alpha-galactopyranoside.yaml data/ingredients/mapped/1-octen-3-ol.yaml data/ingredients/mapped/1-phenazinecarboxamide.yaml data/ingredients/mapped/1-propanolCO2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Whole-corpus checks run earlier in this review pass passed:
  `scripts/validate_strict.py`, `scripts/validate_all.py --mode both`,
  `scripts/validate_sssom_invariants.py`,
  `scripts/check_flat_export_coverage.py`,
  `scripts/audit_duplicate_identifiers.py --check`,
  `scripts/audit_kg_microbe_node_ids.py --check`,
  `scripts/validate_component_partonomy.py`, and
  `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact local
  `kgmicrobe.ingredient:1_propanol_co2` row, and generated docs include both
  component labels in the search surface.
- `scripts/validate_component_partonomy.py` passed for the whole corpus earlier
  in this review pass, covering the `MIM_CATALOG` component scope and the
  `component_assertion` structure.

## Evidence

- The active local identifier is correct. `1-propanol+CO2` names a donor plus
  acceptor combination, not one single ChEBI substance, so preserving a local
  identity avoids mapping the whole to either `propan-1-ol` or `carbon dioxide`.
- The component assertion is now complete: the maintained
  `mappings/microbedecoder_residual_research_decomposition.tsv` row for
  `1-propanol+CO2` lists `CHEBI:28831:propan-1-ol` and
  `CHEBI:16526:carbon dioxide`.
- Minor: top-level `notes` still say no CAS-RN or CHEBI/NCIT match was
  available and that curator review was needed.
- Minor: `ontology_mapping.evidence[0].notes` still contains the initial
  label-split explanation claiming that only one of two constituents resolved
  and that 1-propanol carried no component ID. The later curated decomposition
  superseded that state and both components now have active MIM catalog IDs.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM rows,
  sibling alcohol-plus-CO2 records, the decomposition table row, and active
  catalog rows for both component IDs.

## Completeness

- Empty role slots are acceptable. This record records a decomposed substrate
  pair, not a full culturing recipe or a context-specific nutritional role.
- Missing concentrations are acceptable because the microbedecoder label states
  none.
- There is no need for an external ontology exact mapping; the local
  `kgmicrobe.ingredient:` ID is the exact identity channel.

## Recommended Edits

1. Update `notes` and `ontology_mapping.evidence[0].notes` in
   `data/ingredients/mapped/1-propanolCO2.yaml` to describe the current curated
   decomposition with both component IDs resolved. Then regenerate the
   aggregate, SSSOM, and docs through the maintained recipes.
2. No component ID, component assertion, fallback identifier, SSSOM predicate,
   or docs edit is needed for the active decomposition.
