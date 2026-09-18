# `data/ingredients/mapped/Ferric_Malate_Solution.yaml`

## Verdict

Needs curation, with a major stock-solution completeness gap. The local
fallback registry identity and SSSOM row correctly preserve the recurring
ferric malate solution label while no ontology term exists, but the record is
typed as a `STOCK_SOLUTION` and still has no `components` or
`component_assertion`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ferric_Malate_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:ferric_malate_solution`, matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: OTHER`.
- The active mapping evidence documents the #114 decision: this is a named
  recurring multi-component preparation seen in 2 media, not a single compound
  and not a candidate for a CHEBI, NCIT, MeSH, FOODON, or ENVO exact term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferric_Iron.yaml data/ingredients/mapped/Ferric_Malate_Solution.yaml data/ingredients/mapped/Ferric_nitrilotriacetate.yaml data/ingredients/mapped/Ferrihydrite.yaml data/ingredients/mapped/Ferrous_Citrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Ferric_Malate_Solution.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, so Engine A term validation was skipped as expected for the local
  `kgmicrobe.ingredient:` prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local registry identifier, fallback mapping, stock-solution classification,
  and 2 CultureBot occurrences as the per-record YAML.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` records no exact OLS hit
  for the ferric malate solution label before the local fallback promotion.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ferric_Malate_Solution` to
  `kgmicrobe.ingredient:ferric_malate_solution` with `skos:exactMatch` and no
  `other` payload.
- Major: the May review classified this record as a ferric malate stock
  solution pending exact salt, complex, and concentration curation, but the
  August local-identity promotion left the stock with no has-part record of
  the ferric and malate constituents named in the solution label.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for
  `Ferric_Malate_Solution` and `ferric malate solution` found the active YAML,
  aggregate copy, final SSSOM row, MIM subject-case aliases, the no-hit OLS
  exact audit row, subject-case regression tests, and ignored aggregate
  backups.

## Completeness

- The fallback registry mapping and final SSSOM row are present and preserve
  the solution identity without mapping it to one component.
- The `STOCK_SOLUTION` representation is incomplete until its known ferric and
  malate parts, or a documented source-level reason they cannot be separated,
  are captured in `components` plus `component_assertion`.

## Recommended Edits

- Major: curate the ferric malate stock-solution composition in
  `data/ingredients/mapped/Ferric_Malate_Solution.yaml`, or add a bounded
  discussion explaining why the source recipes do not support a has-part list;
  sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv` if the identifier or mapping
  evidence changes, and rerun strict validation plus
  `scripts/validate_component_partonomy.py`.
