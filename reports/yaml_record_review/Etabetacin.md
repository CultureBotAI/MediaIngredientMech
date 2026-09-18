# `data/ingredients/mapped/Etabetacin.yaml`

## Verdict

Pass. The unresolved kg-microbe placeholder is intentionally retained as a
local registry identity, a fresh exact OLS query still finds no CHEBI or NCIT
replacement, and the final SSSOM row has no unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Etabetacin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:etabetacin` with
  matching `ontology_mapping.ontology_id`, local source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The local placeholder review kept this record pending curator promotion only
  after finding no exact OLS candidate and no normalized local duplicate.
- A fresh exact OLS4 query for `Etabetacin` against CHEBI and NCIT returned 0
  documents.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Etabetacin.yaml data/ingredients/mapped/Etamycin.yaml data/ingredients/mapped/Ethambutol.yaml data/ingredients/mapped/Ethambutol_Dihydrochloride.yaml data/ingredients/mapped/Ethanol.yaml --out /tmp/mim_eta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the local `kgmicrobe.compound` prefix rather than an OBO prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local placeholder identifier, review note, and local-registry history as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Etabetacin` to `kgmicrobe.compound:etabetacin` with
  `skos:exactMatch`, `object_source: kgm:compound`, and an empty `other`
  column.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` records
  `expected_registry_identifier`, and
  `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` records
  `NO_LOCAL_DUPLICATE_NO_OLS_CANDIDATE` for this file.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Etabetacin` and
  `kgmicrobe.compound:etabetacin` found the active YAML, aggregate copy, final
  SSSOM row, expected UNKNOWN_TERM triage rows, and ignored aggregate backups;
  it did not expose a contradictory active mapping.

## Completeness

- The local registry identity, placeholder provenance, and final SSSOM row are
  populated.
- CAS RN, roles, components, occurrence claims, environmental contexts, and
  final SSSOM synonyms are correctly empty.

## Recommended Edits

- None.
