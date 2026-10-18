# `data/ingredients/mapped/Allantoin.yaml`

## Verdict

Needs curation. The exact `CHEBI:15676` identity, CAS xref, chemistry,
occurrence count, ChEBI synonyms, nitrogen-source role, SSSOM row, and
aggregate copy pass, but a CultureMech role/property metadata string still
ships as a raw synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Allantoin.yaml`.
- Identifier and grounding: `identifier: CHEBI:15676` with
  `ontology_mapping.ontology_id: CHEBI:15676`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:15676` to `allantoin`
  with formula `C4H6N4O3`, CAS `97-59-6`, SMILES `NC(=O)NC1NC(=O)NC1=O`,
  and InChIKey `POJWUDADGALRAB-UHFFFAOYSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alginate.yaml data/ingredients/mapped/Alk_So42.yaml data/ingredients/mapped/Alk_So42_X_12_H2o.yaml data/ingredients/mapped/Allantoin.yaml data/ingredients/mapped/Allopurinol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Allantoin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned canonical `allantoin` plus the expected kg-microbe synonym strings
  for `CHEBI:15676`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:15676`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 5 rows for
  `CHEBI:15676`, matching both `occurrence_statistics` counters.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 241 confirmed the
  `MIM:Allantoin` to `CHEBI:15676` mapping.
- `mappings/ingredient_mappings.sssom.tsv` row 369 maps `MIM:Allantoin` to
  `CHEBI:15676` with `skos:exactMatch`, exports CAS `97-59-6`, and filters the
  CultureMech role/property string out of `other`.
- The ChEBI page and local ChEBI metadata support the stored CAS, formula,
  SMILES, and InChI.
- The raw `Role: Nitrogen source; Properties: ...` string is CultureMech
  metadata, not a name of allantoin.
- The `NITROGEN_SOURCE` role is represented in `nutritional_roles`, so the role
  source no longer needs to remain in `synonyms`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, occurrence rows, OAK/OLS confirmation
  row, generated indexes, and ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, occurrence statistics, nitrogen-source role,
  curation history, and `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove or move the CultureMech role/property raw synonym from
  `data/ingredients/mapped/Allantoin.yaml`; the curated
  `nutritional_roles.NITROGEN_SOURCE` entry already captures the role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run linkml-term-validator validate-data data/ingredients/mapped/Allantoin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
