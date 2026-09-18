# `data/ingredients/mapped/Fecl3_X_4_H2o.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The #344 cleanup correctly
keeps `FeCl3 x 4 H2O` as a local unresolved MediaDive hydrate identity with
only an anhydrous `closeMatch` parent, but the `IRON_SOURCE` role is still
backed only by a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Fecl3_X_4_H2o.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:fecl3_x_4_h2o`
  with `ontology_mapping.ontology_id: CHEBI:30808`, canonical parent label
  `iron trichloride`, source `CHEBI`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- The #344 curation retained the local `kgmicrobe.compound` identity for
  MediaDive compound 922, marked anhydrous synonyms as `REJECTED_LABEL`,
  cleared unverified inherited structure fields, and left
  `chemical_properties: {}`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fecl2_X_4_H2o.yaml data/ingredients/mapped/Fecl2_X_6_H2o.yaml data/ingredients/mapped/Fecl2_X_7_H2o.yaml data/ingredients/mapped/Fecl3.yaml data/ingredients/mapped/Fecl3_X_4_H2o.yaml --out /tmp/mim_fecl_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because its own
  identifier uses the local `kgmicrobe.compound` prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, anhydrous ChEBI parent, hydrate-localization history,
  empty `chemical_properties`, `REJECTED_LABEL` provenance, provisional
  `IRON_SOURCE` role, and occurrence counts as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` payload has the intended
  two-row shape: `MIM:Fecl3_X_4_H2o` has `skos:closeMatch` to `CHEBI:30808`
  and a registry-preserving `skos:exactMatch` to
  `kgmicrobe.compound:fecl3_x_4_h2o`.
- `mappings/hydrate_review.tsv` marks this as a correctly retained local
  identity for malformed MediaDive compound 922, with no exact formula, CAS,
  InChI, or SMILES published pending upstream correction.
- The rejected anhydrous labels are absent from the final SSSOM `other`
  fields.
- Major: `nutritional_roles.IRON_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` reference from a curated name-pattern rule, and
  that evidence explicitly describes the assertion as provisional.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Fecl3_X_4_H2o`,
  `kgmicrobe.compound:fecl3_x_4_h2o`, `CHEBI:30808`, and `FeCl3 x 4 H2O`
  found the active YAML, aggregate copy, hydrate review row, final SSSOM parent
  and registry rows, row-review provenance, sibling ferric chloride rows, and
  ignored aggregate backups.

## Completeness

- The local hydrate identity, close parent, exact registry row, rejected-label
  guards, intentionally empty structure fields, and occurrence counts are
  populated.
- The nutritional role needs curator evidence or removal.

## Recommended Edits

- Major: either replace the provisional `IRON_SOURCE` inference with
  source-backed evidence or remove the role facet, sync
  `data/curated/mapped_ingredients.yaml`, regenerate downstream artifacts if
  the role changes, and rerun strict validation.
