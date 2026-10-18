# `data/ingredients/mapped/Alpha-d-glucose.yaml`

## Verdict

Needs curation. The exact `CHEBI:17925` alpha-D-glucose identity, CAS xref,
chemistry, occurrence count, corrected Unicode-Greek synonym, SSSOM row, and
aggregate copy pass, but a CultureMech growth-note string remains in
`synonyms`, the 393 MicrobeDecoder alpha-D-glucose mentions are not represented
in `source_occurrences`, and both nutrient roles remain provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Alpha-d-glucose.yaml`.
- Identifier and grounding: `identifier: CHEBI:17925` with
  `ontology_mapping.ontology_id: CHEBI:17925`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:17925` to
  `alpha-D-glucose` with formula `C6H12O6`, CAS `492-62-6`, SMILES
  `OC[C@H]1O[C@H](O)[C@H](O)[C@@H](O)[C@@H]1O`, and InChIKey
  `WQZGKKKJIJFFOK-DVKNGEFBSA-N`.
- The `#518` Unicode-Greek alpha synonym correction belongs here because that
  spelling names the alpha anomer rather than generic glucose.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-Tocopherol.yaml data/ingredients/mapped/Alpha-aminobutyrate.yaml data/ingredients/mapped/Alpha-bisabolol.yaml data/ingredients/mapped/Alpha-d-glucose.yaml data/ingredients/mapped/Alpha-hydroxyglutarate-gamma-lactone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-d-glucose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:18145 CHEBI:86508 CHEBI:125 CHEBI:17925`:
  returned canonical `alpha-D-glucose` and the expected ChEBI anomer aliases
  for `CHEBI:17925`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18145 CHEBI:86508 CHEBI:125 CHEBI:17925`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:17925`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 7 rows for
  `CHEBI:17925`, matching both stored `occurrence_statistics` counters.
- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:alpha_d_glucose` in `BacDive_Metabolite_utilization` with
  count `393`, but the active YAML has no `source_occurrences` entry for
  MicrobeDecoder alpha-D-glucose.
- `mappings/ingredient_mappings.sssom.tsv` row 379 maps `MIM:Alpha-d-glucose`
  to `CHEBI:17925` with `skos:exactMatch`, exports CAS `492-62-6`, and
  includes the `#518` Unicode-Greek alpha anomer synonym.
- The raw synonym `(not required but growth enhancing)` is CultureMech
  comment prose, not a name of alpha-D-glucose.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` row 64 still treats
  that raw comment as an already represented synonym-enrichment proposal.
- The `CARBON_SOURCE` and `ENERGY_SOURCE` roles are both provisional
  computational predictions and still say review is recommended.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, occurrence rows, raw MicrobeDecoder
  alpha-D-glucose row, synonym-enrichment review row, generated indexes, and
  ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, CultureMech occurrence statistics, ChEBI
  synonyms, curation history, and `ingredient_type` are populated.
- MicrobeDecoder source occurrence provenance and source-backed carbon/energy
  role evidence are missing.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove the `(not required but growth enhancing)` raw synonym from
  `data/ingredients/mapped/Alpha-d-glucose.yaml` and correct
  `mappings/ingredient_mappings_synonym_enrich_review.tsv` so the row no longer
  treats CultureMech comment prose as a represented synonym.
- Add or recover a `source_occurrences` entry for
  `kgmicrobe.trait:alpha_d_glucose` so the 393 MicrobeDecoder utilization
  mentions are represented.
- Curate claim-level support for `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE`, or remove them until source-backed.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-d-glucose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
