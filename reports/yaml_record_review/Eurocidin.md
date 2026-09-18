# `data/ingredients/mapped/Eurocidin.yaml`

## Verdict

Pass. The local Eurocidin record intentionally represents the family-level
kg-microbe placeholder, the fresh exact OLS search did not return an exact
CHEBI or NCIT family term, and the final SSSOM row is clean.

## Identity

- Reviewed record: `data/ingredients/mapped/Eurocidin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:eurocidin` with
  matching `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The 2026-05-10 manual review notes that OLS candidates were specific
  eurocidin variants while the source label is family-level, so the
  `kgmicrobe.compound` identifier was retained without ontology promotion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Eugon_agar_BD-Difco.yaml data/ingredients/mapped/Euphol.yaml data/ingredients/mapped/Eurocidin.yaml data/ingredients/mapped/Europium_Iii_Chloride.yaml data/ingredients/mapped/Exfoliatin.yaml --out /tmp/mim_eug_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the local `kgmicrobe.compound` prefix rather than an OBO prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, placeholder provenance, manual-candidate review history,
  and notes as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Eurocidin` to `kgmicrobe.compound:eurocidin` with `skos:exactMatch`
  and an empty `other` column.
- A fresh exact OLS4 search against CHEBI and NCIT returned the specific
  `Eurocidin E` and `Eurocidin D` variants, not an exact family-level
  `Eurocidin` term.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Eurocidin`,
  `kgmicrobe.compound:eurocidin`, and `Eurocidin` found the active YAML,
  aggregate copy, final SSSOM row, UNKNOWN_TERM triage provenance, and ignored
  aggregate backups; it did not expose a contradictory active mapping.

## Completeness

- The placeholder namespace, reason promotion was deferred, ingredient type,
  and final SSSOM row are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
