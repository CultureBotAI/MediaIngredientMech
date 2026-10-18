# `data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml`

## Verdict

Needs curation, with major role-evidence and final-SSSOM synonym issues. The
new local variable-hydrate identity and narrow parent mapping fix the old
anhydrous ferric sulfate exactMatch, but the record still has a provisional
`TRACE_ELEMENT` role and still exports a malformed hydrate surface as an exact
`other` synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:fe2_so43_x_n_h2o` with `ontology_mapping.ontology_id:
  CHEBI:53438`, canonical parent label `iron(3+) sulfate`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The #321 curation minted the local `kgmicrobe.compound` identifier for the
  variable hydrate, kept anhydrous `CHEBI:53438` only as the nearest parent,
  and cleared the anhydrous `10028-22-5` chemical properties.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml data/ingredients/mapped/Fe4_Po42.yaml data/ingredients/mapped/Fe_Iii-edta.yaml --out /tmp/mim_fe_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because its own
  identifier uses the local `kgmicrobe.compound` prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, ChEBI parent, variable-hydrate curation history, empty
  `chemical_properties`, `TRACE_ELEMENT` role, and occurrence counts as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` payload has the intended
  two-row shape: `MIM:Fe2_So43_X_N_H2o` has `skos:narrowMatch` to
  `CHEBI:53438` and a registry-preserving `skos:exactMatch` to
  `kgmicrobe.compound:fe2_so43_x_n_h2o`.
- Major: both final SSSOM rows still export `Fe(SO4)3 x n H2O` in `other`.
  The token is missing the `2` in `Fe2` and is not a real synonym of
  `Fe2(SO4)3 x n H2O`.
- Major: `nutritional_roles.TRACE_ELEMENT` is supported only by a
  `COMPUTATIONAL_PREDICTION` reference from an in-session LLM assignment, and
  that evidence explicitly describes the assertion as provisional.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Fe2_So43_X_N_H2o`, `kgmicrobe.compound:fe2_so43_x_n_h2o`,
  `CHEBI:53438`, and `10028-22-5` found the active YAML, aggregate copy,
  hydrate review row, final SSSOM parent and registry rows, row-review
  provenance, CultureMech recipe memberships, and ignored aggregate backups.

## Completeness

- The corrected variable-hydrate identity, narrow parent, local exact registry
  row, intentionally empty structure fields, and occurrence counts are
  populated.
- The final SSSOM synonym payload and provisional nutritional role need
  curator cleanup.

## Recommended Edits

- Major: remove `Fe(SO4)3 x n H2O` from the active synonym set or exclude it
  from final SSSOM `other` export, unless source review proves it is a real
  synonym rather than a malformed formula.
- Major: either replace the provisional `TRACE_ELEMENT` inference with
  source-backed evidence or remove the role facet.
- Sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
