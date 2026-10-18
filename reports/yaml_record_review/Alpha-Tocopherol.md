# `data/ingredients/mapped/Alpha-Tocopherol.yaml`

## Verdict

Needs curation. The `CHEBI:18145` all-R alpha-tocopherol identity and restored
CultureMech residual grounding pass, but this newer residual record has not
been through the ingredient-type and ChEBI chemistry backfills, and its single
CultureMech occurrence is still absent from the refreshed recipe-membership
table.

## Identity

- Reviewed record: `data/ingredients/mapped/Alpha-Tocopherol.yaml`.
- Identifier and grounding: `identifier: CHEBI:18145` with
  `ontology_mapping.ontology_id: CHEBI:18145`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:18145` to
  `(R,R,R)-alpha-tocopherol` with formula `C29H50O2`, CAS `59-02-9`, SMILES
  `Cc1c(C)c2c(c(C)c1O)CC[C@@](C)(CCC[C@H](C)CCC[C@H](C)CCCC(C)C)O2`, and
  InChIKey `GVJHHUAWPYXKBD-IEOSBIPESA-N`.
- ChEBI lists `alpha-Tocopherol` as a related synonym of
  `(R,R,R)-alpha-tocopherol`, matching the `#541` restored residual grounding.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-Tocopherol.yaml data/ingredients/mapped/Alpha-aminobutyrate.yaml data/ingredients/mapped/Alpha-bisabolol.yaml data/ingredients/mapped/Alpha-d-glucose.yaml data/ingredients/mapped/Alpha-hydroxyglutarate-gamma-lactone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-Tocopherol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:18145 CHEBI:86508 CHEBI:125 CHEBI:17925`:
  returned canonical `(R,R,R)-alpha-tocopherol` plus ChEBI aliases for
  `CHEBI:18145`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18145 CHEBI:86508 CHEBI:125 CHEBI:17925`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for `CHEBI:18145`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_residual_groundings.tsv` records one residual
  `alpha-Tocopherol` mention across one recipe and grounds it to `CHEBI:18145`.
- `mappings/ingredient_mappings.sssom.tsv` row 376 maps
  `MIM:Alpha-Tocopherol` to `CHEBI:18145` with `skos:exactMatch`, the
  CultureMech residual occurrence source, and the `#541` evidence-restoration
  curator tag.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found no
  `CHEBI:18145` row in `mappings/culturemech_recipe_membership.tsv`; the stored
  `1/1` counters are therefore not represented in that refreshed membership
  table.
- The ChEBI page and local ChEBI metadata can supply formula, SMILES, InChI,
  InChIKey, CAS, and mass values, but `chemical_properties` is still missing
  from the active YAML.
- The active YAML also lacks `ingredient_type`, so it missed the
  `classify_ingredient_type` pass that older CHEBI primaries received.

## Completeness

- Mapping evidence, occurrence statistics, and append-only creation/restoration
  history are populated.
- Formula, SMILES, InChI, CAS, molecular weight, and `ingredient_type` are
  missing despite the exact ChEBI identity.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the missing chemistry and type fields.

## Recommended Edits

- Backfill `chemical_properties` in
  `data/ingredients/mapped/Alpha-Tocopherol.yaml` from `CHEBI:18145`.
- Add `ingredient_type: SINGLE_INGREDIENT` and an audit event reflecting the
  classification.
- Refresh CultureMech membership so the one residual alpha-tocopherol recipe is
  represented in `mappings/culturemech_recipe_membership.tsv`.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-Tocopherol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
