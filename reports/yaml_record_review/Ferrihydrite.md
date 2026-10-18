# `data/ingredients/mapped/Ferrihydrite.yaml`

## Verdict

Needs curation, with major synonym issues. The direct ChEBI `ferrihydrite`
identity and refreshed occurrence counts pass, but the record and final SSSOM
still treat role-prefixed assay labels and `goethite` labels as exact synonyms
of ferrihydrite.

## Identity

- Reviewed record: `data/ingredients/mapped/Ferrihydrite.yaml`.
- Identifier and grounding: `identifier: CHEBI:192761` with matching
  `ontology_mapping.ontology_id`, canonical label `ferrihydrite`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:192761`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- The raw CultureMech `Role: Mineral source` string is kept as typed
  provenance and is filtered out of the final SSSOM payload.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferric_Iron.yaml data/ingredients/mapped/Ferric_Malate_Solution.yaml data/ingredients/mapped/Ferric_nitrilotriacetate.yaml data/ingredients/mapped/Ferrihydrite.yaml data/ingredients/mapped/Ferrous_Citrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferrihydrite.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, synonym set, kg-microbe node ID, and 5 occurrence counts as
  the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ferrihydrite` to `CHEBI:192761` with `skos:exactMatch`.
- Major: `electron acceptor: amorphous fe(iii) oxyhydroxid`,
  `electron acceptor: amorphous iron (iii) oxide`,
  `reduction: amorphous fe(iii) oxyhydroxid`, and
  `reduction: amorphous iron (iii) oxide` are assay-role strings, not exact
  synonyms for the ferrihydrite identity.
- Major: `growth: goethite` is also a role-prefixed assay string, and bare
  `goethite` denotes a distinct iron oxyhydroxide mineral rather than
  ferrihydrite.
- The other final SSSOM `other` tokens are plain iron oxyhydroxide surface
  labels from the kg-microbe enrichment pass and do not carry role prefixes or
  concentration payloads.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `Ferrihydrite` found
  the active YAML, aggregate copy, final SSSOM row, CultureMech residual triage
  for a separate ferrihydrite-suspension label, row-review provenance, the
  synonym-enrichment review row, and ignored aggregate backups.

## Completeness

- The exact ferrihydrite identity, kg-microbe cross-reference, ingredient type,
  occurrence counts, and accepted iron oxyhydroxide labels are populated.
- The final SSSOM synonym payload needs filtering for role-prefixed and
  goethite-specific tokens.

## Recommended Edits

- Major: remove or retype the role-prefixed assay labels and `goethite` labels
  in `data/ingredients/mapped/Ferrihydrite.yaml` so they no longer export as
  exact synonyms, sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
