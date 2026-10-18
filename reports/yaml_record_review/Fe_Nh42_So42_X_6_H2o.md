# `data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym issues. The ChEBI ferrous
ammonium sulfate hexahydrate identity, supported CultureMech iron-source role,
and core hydrate synonyms pass, but concentration-bearing surfaces and an
anhydrous formula still export as exact `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:76181` with matching
  `ontology_mapping.ontology_id`, canonical label
  `ferrous ammonium sulfate hexahydrate`, source `CHEBI`, `mapping_quality:
  EXACT_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- The structure fields record formula `Fe.6H2O.2H4N.2O4S` and the
  CHEBI-backed InChI for ferrous ammonium sulfate hexahydrate.
- `nutritional_roles.IRON_SOURCE` is supported by a `DATABASE_ENTRY` reference
  to CultureMech's original `Mineral source` role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml --out /tmp/mim_fe2_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, structure fields, supported `IRON_SOURCE` role, merged
  duplicate history, and refreshed occurrence counts as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fe_Nh42_So42_X_6_H2o` to `CHEBI:76181` with `skos:exactMatch`.
- `mappings/hydrate_review.tsv` marks the named hexahydrate and
  `CHEBI:76181` mapping as correct and high-confidence.
- Major: the final SSSOM `other` column exports
  `Fe(NH4)2(SO4)2 x 6 H2O (0.01% w/v)`,
  `Fe(NH4)2(SO4)2 x 6 H2O (0.1% w/v)`, and
  `Fe(NH4)2(SO4)2 x 6 H2O (2% v/v)`, which are concentration-specific
  preparations rather than synonyms of the compound.
- Major: the final SSSOM `other` column also exports `Fe(NH4)2(SO4)2`, the
  anhydrous formula string rather than a synonym of the hexahydrate.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Fe_Nh42_So42_X_6_H2o`, `CHEBI:76181`, and hexahydrate labels found the
  active YAML, aggregate copy, final SSSOM row, hydrate review row, row-review
  provenance, CultureMech recipe memberships, and ignored aggregate backups.

## Completeness

- The exact hexahydrate identity, structure fields, accepted hydrate-form
  synonyms, supported role, ingredient type, occurrence counts, and final SSSOM
  row are populated.
- The final SSSOM synonym payload needs filtering for preparation-specific and
  anhydrous tokens.

## Recommended Edits

- Major: remove or filter concentration-specific strings and the anhydrous
  `Fe(NH4)2(SO4)2` token from exact final SSSOM `other` export, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
