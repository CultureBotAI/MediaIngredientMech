# `data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix.yaml`

## Verdict

Pass, none. The ATCC Wolfe's mineral stock identity, component transcription,
mineral and trace-element roles, local registry SSSOM row, and aggregate copy
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:atcc_wolfes_mineral_mix` with the same local
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The record intentionally represents a named ATCC multi-component stock
  solution as `ingredient_type: STOCK_SOLUTION` and
  `solution_type: MINERAL_STOCK`.
- It has 13 transcribed components, including distilled water, and cites ATCC
  Medium 2672 Wolfe's Mineral Solution as complete recipe-transcription
  evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix.yaml data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix_Minus_Iron.yaml data/ingredients/mapped/ATCC_Wolfes_Vitamin_Mix.yaml data/ingredients/mapped/A_Trace_Components.yaml data/ingredients/mapped/Abietic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed because the validator tried to resolve registry CURIE
  `kgmicrobe.ingredient:atcc_wolfes_mineral_mix` through the OAK sqlite label
  table and raised `sqlite3.OperationalError: no such table:
  rdfs_label_statement`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:28987 CHEBI:4735 CHEBI:31795 CHEBI:86364 CHEBI:26710 CHEBI:75836 CHEBI:53503 CHEBI:3312 CHEBI:32312 CHEBI:31440 CHEBI:86465 CHEBI:33118 CHEBI:75213 CHEBI:15377 CHEBI:15956 CHEBI:27470 CHEBI:30961 CHEBI:49105 CHEBI:17015 CHEBI:15940 CHEBI:31345 CHEBI:176843 CHEBI:30753 CHEBI:16494`:
  resolved every ChEBI component CURIE in this record.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ATCC Medium 2672 PDF resolved and lists Wolfe's Mineral Solution,
  Trace Mineral Supplement catalog `MD-TMS`, and the same per-liter component
  amounts transcribed in `components`.
- Local OAK resolves all mineral component IDs used by the record, including
  the hydrate-specific sulfate salts, alum dodecahydrate, boric acid, sodium
  molybdate dihydrate, and water.
- The `MINERAL_SOURCE` and `TRACE_ELEMENT` roles attach the same ATCC Medium
  2672 source and are scoped to the mineral stock rather than inferred from
  class ancestry.
- The SSSOM row maps `MIM:ATCC_Wolfes_Mineral_Mix` to
  `kgmicrobe.ingredient:atcc_wolfes_mineral_mix` with `skos:exactMatch` and
  the expected #114 local-registry provenance.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, subject-case
  alias rows, unmapped exact-audit row, related Wolfe's mix records, and
  ignored aggregate backups.

## Completeness

- The local identity, stock-solution classification, component recipe,
  component evidence, mineral/trace roles, occurrence count, and SSSOM local
  registry row are populated.
- A neat-chemical ontology parent and `chemical_properties` are correctly absent
  for this multi-component ATCC preparation.

## Recommended Edits

No YAML edit is required for this record.
