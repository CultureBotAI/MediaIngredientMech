# `data/ingredients/mapped/Lactalbumin_Hydrolysate.yaml`

## Verdict

Needs curation. The exact MICRO:0001365 identity, undefined-mixture type,
occurrence count, empty final `other` field, and final SSSOM row pass, but the
protein-source role is still a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Lactalbumin_Hydrolysate.yaml`.
- Identifier and grounding: `identifier: MICRO:0001365` with
  `ontology_mapping.ontology_id: MICRO:0001365`, label
  `lactalbumin hydrolysate`, source `MICRO`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Source provenance: imported from the `mim-queue` row for
  `mediadive.ingredient:2143`, then auto-upgraded from `UNMAPPED_0420` by an
  exact MICRO label match.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacidipine` through `Lacto-N-fucopentaose_I`: exited 0 and wrote zero ERROR
  rows.
- LinkML term validation was skipped for this MICRO-primary record because the
  successful batch check covered only the CHEBI-primary records.

## Evidence

- OLS resolves `MICRO:0001365` exactly as `lactalbumin hydrolysate`.
- The `UNDEFINED_MIXTURE` type agrees with a protein hydrolysate ingredient.
- The final SSSOM publishes one `skos:exactMatch` row to `MICRO:0001365`; its
  `other` field is empty.
- Major: `nutritional_roles.PROTEIN_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule and
  explicitly says review is recommended. The label is suggestive, but the record
  lacks inspected medium-level evidence that exact lactalbumin hydrolysate was
  supplied as a protein source.
- Minor: `notes` and the import history still say no CAS-RN or CHEBI/NCIT match
  and that curator review is needed. The current primary ID is the exact
  `MICRO:0001365` term, so those stale import notes should be narrowed or
  superseded.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lactalbumin
  hydrolysate identity.

## Completeness

- The MICRO grounding, occurrence count, mixture classification, and final SSSOM
  row are present and consistent.
- The provisional protein-source role needs curation before it can be treated
  as a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.PROTEIN_SOURCE` in
  `data/ingredients/mapped/Lactalbumin_Hydrolysate.yaml` with inspected source
  evidence for exact lactalbumin hydrolysate use, or remove the provisional
  role.
- Minor: update the stale `notes` import text in the same maintained YAML if it
  remains misleading after the role review.
- Sync the aggregate copy and regenerate derived products after any YAML
  changes; rerun strict, round-trip, component, and SSSOM validation.
