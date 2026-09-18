# `data/ingredients/mapped/MME_Trace_Minerals.yaml`

## Verdict

Pass. The named local trace-mineral stock identity, complete 9-component recipe
transcription, source-backed trace-element role, CultureBotHT occurrence count,
aggregate copy, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/MME_Trace_Minerals.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mme_trace_minerals` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:mme_trace_minerals`,
  label `MME Trace Minerals`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Solution type: `TRACE_METAL_MIX`.
- Occurrences: 3 total occurrences in 3 CultureBotHT media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `MH_agar` through `Macro_Component_1_For_J_Medium`: exited 0 and wrote zero
  ERROR rows.
- Local `kgmicrobe.ingredient` identifiers are outside the CHEBI/OBO
  `linkml-term-validator` adapter scope; whole-corpus component partonomy
  validation was run after the previous batch and passed.

## Evidence

- The 2026-09-08 curation transcribed the CultureBotHT media definitions Mixes
  tab recipe for `MME Trace Minerals`.
- `components` lists all nine trace-mineral stock constituents at their
  source concentrations, and `component_assertion.completeness` is `COMPLETE`.
- `nutritional_roles.TRACE_ELEMENT` is backed by a `DATABASE_ENTRY` reference to
  the same CultureBotHT Mixes tab.
- The final SSSOM publishes one local `skos:exactMatch` row to
  `kgmicrobe.ingredient:mme_trace_minerals`; its `other` field is empty.

## Completeness

- The local fallback identity, occurrence count, complete component partonomy,
  source-backed trace-element role, aggregate copy, and final SSSOM row are
  present and consistent.

## Recommended Edits

- None.
