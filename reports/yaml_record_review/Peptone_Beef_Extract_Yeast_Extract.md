# `data/ingredients/mapped/Peptone_Beef_Extract_Yeast_Extract.yaml`

## Verdict

Pass. The MicrobeDecoder residual is represented as a local undefined-mixture
registry record with a complete label-enumeration decomposition into peptone,
beef extract, and yeast extract.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Peptone_Beef_Extract_Yeast_Extract.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:peptone_beef_extract_yeast_extract` with
  the same local registry `ontology_mapping.ontology_id`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Components: `Peptone` / `MICRO:0000178`, `Beef Extract` /
  `FOODON:03302088`, and `Yeast Extract` / `FOODON:03315426`, all with
  `reference_scope: MIM_CATALOG`.
- Occurrences: 1 MicrobeDecoder `literature:substrates` occurrence and no
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Fresh OLS4 lookups resolved all three component identifiers.
- A fresh OLS4 exact search found no term for the full
  `Peptone + Beef Extract + Yeast Extract` label.
- The final SSSOM row was inspected directly and maps
  `MIM:Peptone_Beef_Extract_Yeast_Extract` exactly to the local kg-microbe
  registry identifier.

## Evidence

- The plus-delimited source label explicitly enumerates all three retained
  top-level parts.
- The curated `DECOMPOSED_TO_COMPONENTS` event records that the source label
  was split on plus signs rather than inferred from an ontology parent.
- `component_assertion.method: LABEL_ENUMERATION` and
  `component_assertion.completeness: COMPLETE` accurately describe the local
  mixture assertion.
- The final SSSOM row exports no `other` tokens.

## Completeness

- No concentrations are present in the source label, so they are correctly
  absent from the components.

## Recommended Edits

- None.
