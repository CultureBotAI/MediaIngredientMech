# `data/ingredients/mapped/Alk_So42.yaml`

## Verdict

Needs curation. The exact anhydrous `CHEBI:86463` identity, CAS xref,
chemistry, occurrence count, SSSOM row, and aggregate copy pass, but the record
still exports two unrelated formula fragments and two CultureMech role/property
metadata strings as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Alk_So42.yaml`.
- Identifier and grounding: `identifier: CHEBI:86463` with
  `ontology_mapping.ontology_id: CHEBI:86463`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:86463` to
  `potassium aluminium sulfate` with formula `Al.K.2O4S`, charge `0`, SMILES
  `O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]`, and InChIKey
  `GRLPQNLYRHEGIJ-UHFFFAOYSA-J`.
- OAK metadata carries CAS `10043-67-1`, matching
  `chemical_properties.cas_rn`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alginate.yaml data/ingredients/mapped/Alk_So42.yaml data/ingredients/mapped/Alk_So42_X_12_H2o.yaml data/ingredients/mapped/Allantoin.yaml data/ingredients/mapped/Allopurinol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alk_So42.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned canonical `potassium aluminium sulfate` and the expected ChEBI
  sulfate/alum aliases for `CHEBI:86463`; it did not return `Na SiO .9H O` or
  `ZnSO .7H O`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:86463`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 240 rows for
  `CHEBI:86463` and they sum to 240 occurrences, matching both stored
  `occurrence_statistics` counters.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 239 classifies
  `MIM:Alk_So42` as `SYNONYM_ENRICH` with proposals
  `Na SiO .9H O|ZnSO .7H O|KAl(SO4)2`; row 61 of
  `mappings/ingredient_mappings_synonym_enrich_review.tsv` then incorrectly
  treats all three strings as already represented.
- `Na SiO .9H O` and `ZnSO .7H O` are not aliases of potassium aluminium
  sulfate in the OAK metadata; they are unrelated sodium silicate and zinc
  sulfate hydrate fragments that now sit in `synonyms` as `EXACT_SYNONYM`.
- `mappings/ingredient_mappings.sssom.tsv` row 367 maps `MIM:Alk_So42` to
  `CHEBI:86463` with `skos:exactMatch` but exports the two wrong aliases in
  `other`, so the final SSSOM output is contaminated.
- The two raw `Role: Mineral source; Properties: ...` strings are CultureMech
  metadata, not names of anhydrous potassium aluminium sulfate.
- The `TRACE_ELEMENT` role is represented in `nutritional_roles`, but its
  evidence text still says `146 occurrences` from the importer era; the
  refreshed occurrence count is `240`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, occurrence rows, OAK/OLS synonym
  review rows, generated indexes, and ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, occurrence statistics, trace-element role,
  curation history, and `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove `Na SiO .9H O` and `ZnSO .7H O` from
  `data/ingredients/mapped/Alk_So42.yaml`, and correct
  `mappings/ingredient_mappings_synonym_enrich_review.tsv` so the row does not
  claim those false aliases are represented.
- Remove or move the two CultureMech role/property raw synonyms from
  `data/ingredients/mapped/Alk_So42.yaml`; the curated
  `nutritional_roles.TRACE_ELEMENT` entry already captures the role.
- Refresh the `TRACE_ELEMENT` evidence text from the current
  `mappings/culturemech_recipe_membership.tsv` count.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run linkml-term-validator validate-data data/ingredients/mapped/Alk_So42.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
