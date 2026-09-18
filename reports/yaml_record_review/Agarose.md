# `data/ingredients/mapped/Agarose.yaml`

## Verdict

Needs curation. The exact `CHEBI:2511` identity, CAS xref, formula, structure,
occurrence count, SSSOM row, and aggregate copy pass, but two CultureMech recipe
annotations remain as raw synonyms and the `CARBON_SOURCE` role is still only a
provisional carbohydrate-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Agarose.yaml`.
- Identifier and grounding: `identifier: CHEBI:2511` with
  `ontology_mapping.ontology_id: CHEBI:2511`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:2511` to `agarose` with
  formula `(C12H18O9)n.C12H20O10`, CAS `9012-36-6`, SMILES, InChI, and
  InChIKey `MJQHZNBUODTQTK-WKGBVCLCSA-N`.
- `kg_microbe_node_id: CHEBI:2511` matches the ontology identifier, and
  `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adipate.yaml data/ingredients/mapped/Adipic_Acid.yaml data/ingredients/mapped/Aesculetin.yaml data/ingredients/mapped/Agar.yaml data/ingredients/mapped/Agarose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Agarose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned canonical `agarose` plus the expected kg-microbe alias strings for
  `CHEBI:2511`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass,
  monoisotopic mass, and WURCS metadata for `CHEBI:2511`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 29 rows for
  `CHEBI:2511`, matching both `occurrence_statistics` counters.
- `mappings/ingredient_mappings.sssom.tsv` row 354 maps `MIM:Agarose` to
  `CHEBI:2511` with `skos:exactMatch`, preserves CAS `9012-36-6`, and exports
  only the kg-microbe aliases in `other`.
- The raw synonyms `(for solid medium, alternative)` and
  `Role: Solidifying component` are CultureMech recipe annotations, not names
  of the `CHEBI:2511` substance.
- The `CARBON_SOURCE` role is still only a computational prediction from ChEBI
  carbohydrate ancestry. The record has no source showing a medium or organism
  consuming agarose as a carbon source.
- The hidden/ignored-inclusive searches over active `data` surfaces, `mappings`,
  `reports`, `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`
  found the active YAML, aggregate copy, SSSOM row, synonym-enrichment review
  row, occurrence-membership rows, generated indexes, and ignored aggregate
  backups.

## Completeness

- CAS, formula, SMILES, InChI, kg-microbe node, occurrence statistics, curation
  history, and `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Agarose.yaml`, remove or move the two CultureMech
  raw annotation fragments out of the synonym list.
- Delete the provisional `CARBON_SOURCE` role unless a source supports agarose
  utilization in the intended scope; add a claim-level evidence object if such
  a source is curated.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Agarose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
