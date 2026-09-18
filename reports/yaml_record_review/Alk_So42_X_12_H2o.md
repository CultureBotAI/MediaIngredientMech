# `data/ingredients/mapped/Alk_So42_X_12_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:86465` dodecahydrate identity, CAS xref,
hydrate-specific chemistry, occurrence count, hydrate audit, SSSOM row, and
aggregate copy pass, but a CultureMech role/property metadata string still
ships as a raw synonym and the trace-element role evidence retains a stale
occurrence count.

## Identity

- Reviewed record: `data/ingredients/mapped/Alk_So42_X_12_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86465` with
  `ontology_mapping.ontology_id: CHEBI:86465`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:86465` to
  `potassium aluminium sulfate dodecahydrate` with formula
  `Al.12H2O.K.2O4S`, charge `0`, SMILES
  `O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]`,
  and InChIKey `GNHOJBNSNUXZQA-UHFFFAOYSA-J`.
- OAK metadata carries CAS `7784-24-9`, matching
  `chemical_properties.cas_rn`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alginate.yaml data/ingredients/mapped/Alk_So42.yaml data/ingredients/mapped/Alk_So42_X_12_H2o.yaml data/ingredients/mapped/Allantoin.yaml data/ingredients/mapped/Allopurinol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alk_So42_X_12_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned canonical `potassium aluminium sulfate dodecahydrate` and the
  expected alum hydrate aliases for `CHEBI:86465`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:86465`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings.

## Evidence

- `mappings/hydrate_review.tsv` and `reports/hydrate_grounding.tsv` both
  confirm that `CHEBI:86465` is the established dodecahydrate identity for
  `AlK(SO4)2 x 12 H2O`.
- `mappings/culturemech_recipe_membership.tsv` contains 812 rows for
  `CHEBI:86465` and they sum to 813 occurrences, matching
  `media_count: 812` and `total_occurrences: 813`.
- `mappings/ingredient_mappings.sssom.tsv` row 368 maps
  `MIM:Alk_So42_X_12_H2o` to `CHEBI:86465` with `skos:exactMatch`, exports CAS
  `7784-24-9`, and filters the CultureMech role/property string out of
  `other`.
- The stored hydrate formulas and `KAl(SO4)2` aliases denote the same
  dodecahydrate form.
- The raw `Role: Mineral source; Properties: ...` string is CultureMech
  metadata, not a name of potassium aluminium sulfate dodecahydrate.
- The `TRACE_ELEMENT` role is represented in `nutritional_roles`, but its
  evidence text still says `750 occurrences` from the importer era; the
  refreshed occurrence count is `813`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, occurrence rows, hydrate audit rows,
  generated indexes, records that use `CHEBI:86465` as a mixture component, and
  ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, hydrate-specific synonyms, occurrence
  statistics, trace-element role, curation history, and `ingredient_type` are
  populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove or move the CultureMech role/property raw synonym from
  `data/ingredients/mapped/Alk_So42_X_12_H2o.yaml`; the curated
  `nutritional_roles.TRACE_ELEMENT` entry already captures the role.
- Refresh the `TRACE_ELEMENT` evidence text from the current
  `mappings/culturemech_recipe_membership.tsv` count.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run linkml-term-validator validate-data data/ingredients/mapped/Alk_So42_X_12_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
