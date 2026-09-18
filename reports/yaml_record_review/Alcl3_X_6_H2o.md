# `data/ingredients/mapped/Alcl3_X_6_H2o.yaml`

## Verdict

Needs curation. The exact aluminium trichloride hexahydrate identity, CAS xref,
hydrate synonyms, ChEBI chemistry, occurrence count, SSSOM row, and aggregate
copy pass, but the record still stores a CultureMech role/property metadata
string as a raw synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Alcl3_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:30115` with
  `ontology_mapping.ontology_id: CHEBI:30115`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:30115` to
  `aluminium trichloride hexahydrate` with formula `AlCl3.6H2O`, CAS
  `7784-13-6`, SMILES, and InChIKey `JGDITNMASUZKPW-UHFFFAOYSA-K`.
- `kg_microbe_node_id: CHEBI:30115` matches the ontology identifier, and
  `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alazopeptin.yaml data/ingredients/mapped/Alboverticillin.yaml data/ingredients/mapped/Alcl3.yaml data/ingredients/mapped/Alcl3_X_6_H2o.yaml data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alcl3_X_6_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:222816 CHEBI:30114 CHEBI:30115`:
  returned canonical `aluminium trichloride hexahydrate` plus the expected
  hydrate aliases for `CHEBI:30115`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:222816 CHEBI:30114 CHEBI:30115`:
  returned the exact formula, SMILES, InChI, InChIKey, charge, average mass,
  and monoisotopic mass for `CHEBI:30115`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `reports/hydrate_grounding.tsv` classifies the same CHEBI identity as
  `OK_HYDRATE_TERM`.
- `mappings/hydrate_review.tsv` says the named hexahydrate is an established
  isolated form and that the ChEBI identity/formula agree.
- `mappings/culturemech_recipe_membership.tsv` contains 46 rows for
  `CHEBI:30115`, matching both `occurrence_statistics` counters.
- `mappings/ingredient_mappings.sssom.tsv` row 364 maps
  `MIM:Alcl3_X_6_H2o` to `CHEBI:30115` with `skos:exactMatch`, exports the
  hydrate surface forms plus CAS `7784-13-6`, and filters the CultureMech
  role/property string out of `other`.
- The raw synonym `Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component`
  is source metadata from CultureMech, not a name of aluminium trichloride
  hexahydrate.
- The `TRACE_ELEMENT` role is now represented in `nutritional_roles` with a
  database-entry evidence object, so the role source no longer needs to remain
  in `synonyms`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, hydrate-review rows, occurrence rows,
  generated indexes, and ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, kg-microbe node, hydrate-form synonyms,
  occurrence statistics, trace-element role, curation history, and
  `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove or move the CultureMech role/property raw synonym from
  `data/ingredients/mapped/Alcl3_X_6_H2o.yaml`; the curated
  `nutritional_roles.TRACE_ELEMENT` entry already captures the role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alcl3_X_6_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
