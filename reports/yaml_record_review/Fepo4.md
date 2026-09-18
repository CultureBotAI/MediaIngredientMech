# `data/ingredients/mapped/Fepo4.yaml`

## Verdict

Pass. The exact anhydrous ferric phosphate ChEBI identity, CAS-backed
structure, CultureMech mineral-source roles, and final SSSOM synonym payload
are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Fepo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:131371` with matching
  `ontology_mapping.ontology_id`, canonical label `iron(3+) phosphate`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:131371`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `10045-86-0` resolved to CID 24861 with formula
  `FeO4P` and the same anhydrous ferric phosphate InChI recorded under
  `chemical_properties`.
- `nutritional_roles.IRON_SOURCE` and `PHOSPHATE_SOURCE` are backed by a
  `DATABASE_ENTRY` derived from the CultureMech `Mineral` role; the facet
  split agrees with the ferric phosphate formula.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fecl3_X_6_H2o.yaml data/ingredients/mapped/Fepo4.yaml data/ingredients/mapped/Fermented_Rumen_Extract.yaml data/ingredients/mapped/Ferric_Ammonium_Citrate.yaml data/ingredients/mapped/Ferric_Citrate_Monohydrate.yaml`:
  exited 0 for the 5-file batch.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fepo4.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, kg-microbe node ID,
  supported nutritional roles, and refreshed occurrence counts as the
  per-record YAML.
- The row-review manifest confirms `MIM:Fepo4` to `CHEBI:131371` as an
  OAK/OLS-confirmed mapping, and the final
  `mappings/ingredient_mappings.sssom.tsv` row maps the subject to that ChEBI
  term with `skos:exactMatch`.
- The final SSSOM `other` tokens, `Ferric orthophosphate`, `Iron
  orthophosphate`, `Iron phosphate`, `ferric phosphate`, `iron(III)
  phosphate`, and `CAS:10045-86-0`, all denote the same anhydrous ferric
  phosphate identity or its CAS RN.
- The only raw CultureMech role/properties string remains a typed YAML
  provenance synonym and is not exported into final SSSOM `other`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `Fepo4`, `FePO4`,
  and `CHEBI:131371` found the active YAML, aggregate copy, final SSSOM row,
  OAK/OLS row-review provenance, the separate ferric phosphate tetrahydrate
  record, and ignored aggregate backups.

## Completeness

- The exact anhydrous identity, CAS RN, structure fields, nutrient-source
  roles, kg-microbe cross-reference, ingredient type, occurrence counts, and
  accepted exact synonyms are populated.
- I found no consequential missing component, environment, discussion, or final
  SSSOM payload for this single-ingredient anhydrous phosphate.

## Recommended Edits

- None.
