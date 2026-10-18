# `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`

## Verdict

Needs curation. `mesh:D014131` is a valid MeSH term for the generic class
`Trace Elements`, but the MIM subject is a recipe-local
`Desulfovibrio trace elements` stock or reagent group. The current exactMatch
therefore erases specificity, omits stock components, and publishes
`Trace elements (see below)` as an unsafe final SSSOM synonym.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml`.
- Current grounding: `identifier: mesh:D014131` with
  `ontology_mapping.ontology_id: mesh:D014131`, label `Trace Elements`,
  source `MESH`, `mapping_quality: LEXICAL_MATCH`, and
  `mapping_status: MAPPED`.
- Live prefix-specific OLS resolves `mesh:D014131` exactly to MeSH
  `Trace Elements`, and a live exact MeSH search for
  `Desulfovibrio trace elements` returned no class.
- The source label is a named Desulfovibrio trace-elements preparation, not
  the generic MeSH trace-element class. This should be a local
  `kgmicrobe.ingredient:desulfovibrio_trace_elements` identity if no
  formulation-specific ontology term exists.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Destomycin.yaml data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml data/ingredients/mapped/Deuterated_Glucose.yaml data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ...` over the mixed
  five-record batch aborted before the MeSH record at the local
  `kgmicrobe.compound:destomycin` registry identifier.
- `curl -L ... q=Trace Elements&ontology=mesh&exact=true`: live OLS returned
  exact `mesh:D014131`.
- `curl -L ... q=Desulfovibrio trace elements&ontology=mesh&exact=true`: live
  OLS returned 0 rows.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  the full corpus had 2,951 records, 83 decompositions, 505 components, and 0
  violations.

## Evidence

- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` confirms
  that `mesh:D014131` resolves through prefix-specific OLS, but that only
  validates the target CURIE. It does not support treating a named
  Desulfovibrio trace-element preparation as exact identity with the generic
  MeSH class.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, and `scripts` found no
  component list for this stock record and no exact OLS hit for
  `Desulfovibrio trace elements`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Desulfovibrio_Trace_Elements` to `mesh:D014131` with
  `skos:exactMatch` and `Trace elements (see below)` in `other`. That `other`
  token is a recipe-local pointer, not a real synonym for the modeled MIM
  subject.
- `mappings/culturemech_residual_triage.tsv` still carries
  `Trace elements (see below)` as a stale unresolved alias even though the
  alias is now on this record and leaks into final SSSOM.
- Major: `nutritional_roles.TRACE_ELEMENT` is supported only by an in-session
  `COMPUTATIONAL_PREDICTION` role assignment and needs source-backed role
  evidence if it is retained.

## Completeness

- The occurrence count and raw source labels preserve the legacy CultureBotHT
  provenance: the record was created from `consolidated_media.json`, used in 3
  CultureBot media, and names `MoLS4`, `Dv_base_medium`, and
  `MoLS4_no_vitamins` as samples.
- Major: the stock has no `components` or `component_assertion`, so a reader
  cannot recover which trace elements are meant.

## Recommended Edits

- Major: retarget
  `data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml` to a local
  stock identity such as
  `kgmicrobe.ingredient:desulfovibrio_trace_elements`, keep
  `mesh:D014131` at most as a `NARROW_MATCH` parent, synchronize
  `data/curated/mapped_ingredients.yaml`, and regenerate SSSOM so a
  registry/identity row is emitted beside the MeSH parent row.
- Major: add source-backed `components` and a `component_assertion` from the
  maintained CultureBotHT or CultureMech formulation evidence, or document the
  formulation as unresolved in `discussions` if the exact stock recipe cannot
  be recovered.
- Major: remove `Trace elements (see below)` from final SSSOM `other` by
  demoting it out of active synonym export or by proving it is a true alias for
  this exact stock.
- Major: source or remove `nutritional_roles.TRACE_ELEMENT`.
