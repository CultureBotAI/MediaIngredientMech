# `data/ingredients/mapped/Mc_trace_minerals.yaml`

## Verdict

Needs curation. The local trace-mineral-stock identity, Mixes-tab
transcription, trace-element role, occurrence count, and final SSSOM row pass,
but the attached `compounds-to-CAS` evidence block cites chloride crosswalk rows
for three sulfate components.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mc_trace_minerals.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mc_trace_minerals` with matching
  `ontology_mapping.ontology_id`, label `Mc_trace_minerals`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: TRACE_METAL_MIX`.
- Occurrences: three CultureBotHT media.
- Components: 12 trace-mineral stock constituents.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mc_general_salts_SO4free` through `Meat_Extract`: exited 0 and wrote zero
  ERROR rows.
- Engine A term validation was skipped for this record because
  `kgmicrobe.ingredient` is a local non-OBO registry prefix covered by the
  product id-label validator rather than by `linkml-term-validator`.

## Evidence

- The FEBA media definitions Google Sheet exported from the recorded source URL
  has `Mixes!1099:1110` for the 12 `Mc_trace_minerals` constituents with the
  same labels and g/L concentrations recorded in the YAML.
- The `unmapped_ingredients_ols_exact_audit.tsv` row for this slug reports no
  exact OLS hit for `Mc_trace_minerals` or `Mc trace minerals`, supporting the
  local registry mint.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mc_trace_minerals` to `kgmicrobe.ingredient:mc_trace_minerals` with
  empty `other`.

## Completeness

- The `TRACE_ELEMENT` role is supported by the CultureBotHT Mixes-tab entry,
  which identifies this as a 1000X trace-mineral stock for Mc media.
- The component IDs for `manganese(II) sulfate dihydrate`,
  `copper sulfate pentahydrate`, and `AlK(SO4)2 12H2O` point at sulfate salts,
  but the attached `CURATED_DATASET` source record cites the sulfate-free
  sibling's rows for manganese chloride tetrahydrate, copper chloride
  dihydrate, and aluminum chloride hydrate. Those three crosswalk rows do not
  support the sulfate identities used in this stock.

## Recommended Edits

- Replace the `component_assertion.evidence` `compounds-to-CAS` row list with
  evidence for the sulfate-specific manganese, copper, and aluminum/potassium
  salts actually listed in `Mixes!1099:1110`.
