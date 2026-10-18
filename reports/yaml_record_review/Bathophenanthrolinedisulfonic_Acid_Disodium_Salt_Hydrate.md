# `data/ingredients/mapped/Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml`

## Verdict

Needs curation, major. The record correctly stopped treating the hydrate as
exactly identical to the older anhydrous `CHEBI:78157` salt, but current OLS
now resolves the hydrate label to `CHEBI:232316`, and the YAML still carries
anhydrous-parent formula and synonym data as though they described the hydrate.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:bathophenanthrolinedisulfonic_acid_disodium_salt_hydrate`
  with `ontology_mapping.ontology_id: CHEBI:78157`,
  `ontology_label: disodium 4,7-diphenyl-1,10-phenanthroline 4',4''-disulfonate`,
  `ontology_source: CHEBI`, `mapping_quality: CLOSE_MATCH`, and
  `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:78157` to the anhydrous disodium
  salt parent and returns
  `disodium 4,4'-(1,10-phenanthroline-4,7-diyl)dibenzenesulfonate` as an exact
  synonym of that anhydrous term.
- OLS exact search for the full record label
  `Bathophenanthrolinedisulfonic acid disodium salt hydrate` now returns
  `CHEBI:232316` with label
  `bathophenanthrolinedisulfonic acid disodium salt` and the hydrate label as a
  synonym. Hidden/ignored-inclusive local search over `data/ingredients`,
  `mappings`, `data/custom`, and
  `reports/kg_microbe_node_id_mismatches.tsv` found no existing mention of
  `CHEBI:232316`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Bedaquiline.yaml data/ingredients/mapped/Beef.yaml data/ingredients/mapped/Beef_Brain_Powder.yaml data/ingredients/mapped/Beef_Extract.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed against the currently stored anhydrous `CHEBI:78157` parent label.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the aggregate copy in
  `data/curated/mapped_ingredients.yaml` and the two authoritative SSSOM rows
  at `mappings/ingredient_mappings.sssom.tsv` rows 540 and 541.
- `mappings/hydrate_review.tsv` row 111 already records the unresolved hydrate
  boundary: the label says only `hydrate`, the water stoichiometry is
  unspecified, and the CAS/formula metadata did not establish a unique water
  stoichiometry.
- PubChem name lookup for CAS `52746-49-3` returned no CID during this review,
  so the CAS field remains CultureBotHT-only in the inspected evidence.
- The stored `chemical_properties.molecular_formula` value
  `C24H14N2O6S2.2Na` and the stored InChI both omit hydrate waters and match
  the anhydrous disodium salt, not the hydrate named by `preferred_term`.
- The stored exact synonym
  `disodium 4,4'-(1,10-phenanthroline-4,7-diyl)dibenzenesulfonate` belongs to
  the anhydrous `CHEBI:78157` close-match target and is not exact for the
  hydrate record itself.

## Completeness

- The kg-microbe registry identity, close-match row to `CHEBI:78157`,
  own-identifier registry row, hydrate review row, SSSOM rows, and aggregate
  copy are populated.
- The record is incomplete for the current ontology landscape: it has not been
  reviewed against the now-resolving `CHEBI:232316` candidate.

## Recommended Edits

- Major: review `CHEBI:232316` as the current exact ChEBI candidate for
  `data/ingredients/mapped/Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml`;
  if it truly represents this hydrate/salt surface, promote
  `ontology_mapping` and the primary `identifier` from the kg-microbe
  close-match pattern to `CHEBI:232316`, then regenerate the SSSOM rows.
- Major: remove or re-scope the anhydrous `CHEBI:78157` exact synonym and
  anhydrous formula/InChI fields unless the promoted `CHEBI:232316` review
  independently verifies them for the exact supplied hydrate.
