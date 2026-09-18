# `data/ingredients/mapped/Ethanol.yaml`

## Verdict

Needs curation, with a major final-SSSOM synonym issue. The current ChEBI
ethanol identity, CAS RN, structure fields, occurrence refresh, and duplicate
merge are coherent, but `produces: ethanol` is still exported as a published
synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:16236` with matching
  `ontology_mapping.ontology_id`, canonical label `ethanol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, 193 CultureMech
  occurrences, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `64-17-5` resolved to CID 702 with formula `C2H6O`
  and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Etabetacin.yaml data/ingredients/mapped/Etamycin.yaml data/ingredients/mapped/Ethambutol.yaml data/ingredients/mapped/Ethambutol_Dihydrochloride.yaml data/ingredients/mapped/Ethanol.yaml --out /tmp/mim_eta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, structure fields, kg-microbe node ID, occurrence
  count, duplicate-merge history, and active synonyms as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Ethanol`
  to `CHEBI:16236` with `skos:exactMatch`; most `other` tokens are curated
  same-substance synonyms or the same CAS RN.
- Major: the same SSSOM row also exports `produces: ethanol` in `other`. That
  token is a reaction-output assertion, not a synonym of ethanol, and the
  repository policy only filters `Role:`/`Properties:`, `Original Amount:`, and
  bare parenthetical raw labels from final SSSOM today.
- `mappings/culturemech_recipe_membership.tsv` has CultureMech membership rows
  for `CHEBI:16236`, agreeing with the refreshed nonzero occurrence statistics.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Ethanol`,
  `CHEBI:16236`, `64-17-5`, and `produces: ethanol` found the active YAML,
  aggregate copy, final SSSOM row, CultureMech occurrence rows, OAK/OLS
  synonym-enrichment review, and ignored aggregate backups; it did not expose a
  contradictory active mapping.

## Completeness

- The exact identity, CAS RN, structure, occurrence count, duplicate-merge
  provenance, and final SSSOM identity row are populated.
- The old `Role:`/`Properties:` and parenthetical raw labels are correctly
  filtered from final SSSOM `other`.

## Recommended Edits

- Major: remove `produces: ethanol` from the active synonyms in
  `data/ingredients/mapped/Ethanol.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
