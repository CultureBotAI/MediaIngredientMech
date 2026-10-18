# `data/ingredients/mapped/Ethanolamine.yaml`

## Verdict

Needs curation, with a major final-SSSOM synonym issue. The ChEBI identity, CAS
RN, structure fields, occurrence refresh, and `2-aminoethanol` synonym pass,
but `2-aminethanol` is a non-resolving typo that remains active in final
SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Ethanolamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16000` with matching
  `ontology_mapping.ontology_id`, canonical label `ethanolamine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, three
  CultureMech occurrences, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `141-43-5` resolved to CID 700 with formula
  `C2H7NO` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethanolamine.yaml data/ingredients/mapped/Ethidium_Bromide.yaml data/ingredients/mapped/Ethionamide.yaml data/ingredients/mapped/Ethyl_Acetate.yaml data/ingredients/mapped/Ethyl_Benzoate.yaml --out /tmp/mim_eth_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ethanolamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, structure fields, occurrence count, and active
  synonyms as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethanolamine` to `CHEBI:16000` with `skos:exactMatch`.
  `2-aminoethanol` is a curated same-substance synonym and `CAS:141-43-5`
  belongs to ethanolamine.
- Major: the same SSSOM row also exports `2-aminethanol`, a typo from
  `sssom_other_backfill`; exact OLS4 and PubChem lookups found no resolving
  `2-aminethanol` entry, so this token should not remain in the published
  synonym surface.
- `mappings/culturemech_recipe_membership.tsv` has three rows for
  `CHEBI:16000`, matching the refreshed `occurrence_statistics`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Ethanolamine`,
  `CHEBI:16000`, `141-43-5`, and `2-aminethanol` found the active YAML,
  aggregate copy, final SSSOM row, CultureMech occurrence rows, row-review
  provenance, and ignored aggregate backups; it did not expose a contradictory
  active mapping.

## Completeness

- The exact identity, CAS RN, structure fields, occurrence count, exact synonym,
  and final SSSOM identity row are populated.
- Roles, components, and environmental contexts are correctly empty.

## Recommended Edits

- Major: remove `2-aminethanol` from the active synonyms in
  `data/ingredients/mapped/Ethanolamine.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
