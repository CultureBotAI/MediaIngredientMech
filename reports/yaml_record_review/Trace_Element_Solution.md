# `data/ingredients/mapped/Trace_Element_Solution.yaml`

## Verdict

Pass. The generic trace-element stock solution is intentionally represented as
a local `kgmicrobe.ingredient` identity with a broad NCIT close match and no
component decomposition.

## Identity

- Reviewed record: `data/ingredients/mapped/Trace_Element_Solution.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:trace_element_solution`, close parent
  `ontology_mapping.ontology_id: NCIT:C896`, label `Trace Element`, source
  `NCIT`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: kgmicrobe.ingredient:trace_element_solution`, and
  `ingredient_type: STOCK_SOLUTION`.
- Solution type: `TRACE_METAL_MIX`.
- Synonyms: raw mim-queue source form `Trace element solution`.
- Occurrences: 7 CultureMech recipe occurrences in 7 media.
- Roles: reviewed `nutritional_roles.TRACE_ELEMENT` facet with MediaDive
  ingredient 96 database evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tomato_Juice` through `Trace_Element_Solution`: exited 0 and wrote zero
  ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this row because
  `NCIT` and `kgmicrobe.ingredient` are outside the CHEBI-focused OBO term
  subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Prefix-specific OLS validation resolves `NCIT:C896`, and fresh exact OLS4
  search for `Trace Element` returns `NCIT:C896` with label `Trace Element`.
- The curation history records the September correction from the NCIT parent to
  a local stock-solution identity, keeping `NCIT:C896` only as a close match
  because MediaDive ingredient 96 is a generic stock-solution surface rather
  than one elemental trace compound.
- The final SSSOM has a close row to `NCIT:C896` and an exact identity row for
  `kgmicrobe.ingredient:trace_element_solution`; both rows leave `other`
  empty.

## Completeness

- The local identity, NCIT close match, `STOCK_SOLUTION` and
  `TRACE_METAL_MIX` classifications, MediaDive trace-element role, occurrence
  count, aggregate copy, and final SSSOM rows agree.
- Components are intentionally unset because the generic MediaDive source label
  does not identify a complete stock formulation.

## Recommended Edits

- None.
