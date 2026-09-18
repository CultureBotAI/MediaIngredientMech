# `data/ingredients/mapped/Alcl3.yaml`

## Verdict

Needs curation. The exact `CHEBI:30114` anhydrous aluminium trichloride
identity, CAS xref, chemistry, occurrence count, SSSOM row, and aggregate copy
pass, but the record still stores a CultureMech role/property metadata string
as a raw synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Alcl3.yaml`.
- Identifier and grounding: `identifier: CHEBI:30114` with
  `ontology_mapping.ontology_id: CHEBI:30114`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:30114` to
  `aluminium trichloride` with formula `AlCl3`, CAS `7446-70-0`, SMILES
  `[Cl][Al]([Cl])[Cl]`, and InChIKey `VSCWAEJMTAWNJL-UHFFFAOYSA-K`.
- `kg_microbe_node_id: CHEBI:30114` matches the ontology identifier, and
  `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alazopeptin.yaml data/ingredients/mapped/Alboverticillin.yaml data/ingredients/mapped/Alcl3.yaml data/ingredients/mapped/Alcl3_X_6_H2o.yaml data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alcl3.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:222816 CHEBI:30114 CHEBI:30115`:
  returned canonical `aluminium trichloride` plus the expected kg-microbe
  synonym strings for `CHEBI:30114`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:222816 CHEBI:30114 CHEBI:30115`:
  returned the exact formula, SMILES, InChI, InChIKey, charge, average mass,
  and monoisotopic mass for `CHEBI:30114`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 77 rows for
  `CHEBI:30114`, matching both `occurrence_statistics` counters.
- `mappings/ingredient_mappings.sssom.tsv` row 363 maps `MIM:Alcl3` to
  `CHEBI:30114` with `skos:exactMatch`, exports CAS `7446-70-0`, and filters
  the CultureMech role/property string out of `other`.
- The first PubChem name lookup recorded CAS `231-208-1`, but the current
  `chemical_properties.cas_rn` has the correct `7446-70-0` value from the later
  ChEBI-based PubChem enrichment.
- The raw synonym `Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component`
  is source metadata from CultureMech, not a name of anhydrous aluminium
  trichloride.
- The `TRACE_ELEMENT` role is now represented in `nutritional_roles` with a
  database-entry evidence object, so the role source no longer needs to remain
  in `synonyms`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, occurrence rows, generated indexes,
  and ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, kg-microbe node, occurrence statistics, trace
  element role, curation history, and `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove or move the CultureMech role/property raw synonym from
  `data/ingredients/mapped/Alcl3.yaml`; the curated
  `nutritional_roles.TRACE_ELEMENT` entry already captures the role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alcl3.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
