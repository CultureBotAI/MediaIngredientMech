# `data/ingredients/mapped/Exfoliatin.yaml`

## Verdict

Pass. The kg-microbe Exfoliatin placeholder has no exact CHEBI or NCIT
replacement candidate in the current exact OLS search, and the final SSSOM row
is clean.

## Identity

- Reviewed record: `data/ingredients/mapped/Exfoliatin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:exfoliatin` with
  matching `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The 2026-05-10 UNKNOWN_TERM placeholder review retained the local primary
  identifier because no exact OLS candidate or normalized local duplicate
  supported external ontology promotion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Eugon_agar_BD-Difco.yaml data/ingredients/mapped/Euphol.yaml data/ingredients/mapped/Eurocidin.yaml data/ingredients/mapped/Europium_Iii_Chloride.yaml data/ingredients/mapped/Exfoliatin.yaml --out /tmp/mim_eug_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the local `kgmicrobe.compound` prefix rather than an OBO prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, no-hit placeholder provenance, UNKNOWN_TERM review
  history, and notes as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Exfoliatin` to `kgmicrobe.compound:exfoliatin` with `skos:exactMatch`
  and an empty `other` column.
- A fresh exact OLS4 search against CHEBI and NCIT returned no documents for
  `Exfoliatin`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Exfoliatin`,
  `kgmicrobe.compound:exfoliatin`, and `Exfoliatin` found the active YAML,
  aggregate copy, final SSSOM row, UNKNOWN_TERM no-hit provenance, and ignored
  aggregate backups; it did not expose a contradictory active mapping.

## Completeness

- The placeholder namespace, reason promotion was deferred, ingredient type,
  and final SSSOM row are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
