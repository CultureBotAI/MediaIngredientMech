# `data/ingredients/mapped/Fecl2_X_4_H2o.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym issues. The ChEBI ferrous
chloride tetrahydrate identity, CAS-backed hydrate structure, supported
CultureMech iron-source role, and core hydrate synonyms pass, but the final
SSSOM `other` column still exports concentration-bearing preparation strings
and an anhydrous malformed formula as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fecl2_X_4_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86249` with matching
  `ontology_mapping.ontology_id`, canonical label
  `iron dichloride tetrahydrate`, source `CHEBI`, `mapping_quality:
  EXACT_MATCH`, `mapping_status: MAPPED`, `kg_microbe_node_id:
  CHEBI:86249`, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `13478-10-9` resolved to CID 16211588 with formula
  `Cl2FeH8O4` and the same InChI recorded under `chemical_properties`.
- `nutritional_roles.IRON_SOURCE` is supported by a `DATABASE_ENTRY` reference
  to CultureMech's original `Mineral source` role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fecl2_X_4_H2o.yaml data/ingredients/mapped/Fecl2_X_6_H2o.yaml data/ingredients/mapped/Fecl2_X_7_H2o.yaml data/ingredients/mapped/Fecl3.yaml data/ingredients/mapped/Fecl3_X_4_H2o.yaml --out /tmp/mim_fecl_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fecl2_X_4_H2o.yaml data/ingredients/mapped/Fecl3.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the CHEBI-primary subset in this mixed batch.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, kg-microbe node ID,
  supported `IRON_SOURCE` role, and refreshed occurrence counts as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fecl2_X_4_H2o` to `CHEBI:86249` with `skos:exactMatch`.
- `mappings/hydrate_review.tsv` marks the named tetrahydrate and
  `CHEBI:86249` mapping as correct and high-confidence.
- Major: the final SSSOM `other` column exports
  `FeCl2 x 4 H2O (0.1% w/v in 0.2 N HCl)` and
  `FeCl2 x 4 H2O (0.2% w/v in 0.02 N HCl)`, which are
  concentration-and-solvent preparations rather than exact synonyms of the
  tetrahydrate.
- Major: the final SSSOM `other` column also exports `FeCl 2`, which is an
  anhydrous and malformed formula, not a synonym of `FeCl2 x 4 H2O`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Fecl2_X_4_H2o`,
  `CHEBI:86249`, `13478-10-9`, and ferrous chloride tetrahydrate labels found
  the active YAML, aggregate copy, final SSSOM row, hydrate review row,
  row-review provenance, stock-solution component references, and ignored
  aggregate backups.

## Completeness

- The exact tetrahydrate identity, CAS RN, structure fields, supported
  iron-source role, ingredient type, occurrence counts, and accepted hydrate
  synonyms are populated.
- The final SSSOM synonym payload needs filtering for preparation-specific and
  anhydrous malformed tokens.

## Recommended Edits

- Major: remove or filter the concentration-specific hydrate strings and
  `FeCl 2` from exact final SSSOM `other` export, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
