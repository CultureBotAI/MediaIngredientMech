# `data/ingredients/mapped/Fecl3.yaml`

## Verdict

Needs curation, with a major final-SSSOM synonym issue. The ChEBI ferric
chloride identity, CAS-backed anhydrous structure, supported CultureMech
iron-source role, and core exact synonyms pass, but a concentration-specific
surface still exports as an exact `other` synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Fecl3.yaml`.
- Identifier and grounding: `identifier: CHEBI:30808` with matching
  `ontology_mapping.ontology_id`, canonical label `iron trichloride`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:30808`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `7705-08-0` resolved to CID 24380 with formula
  `Cl3Fe` and the same InChI recorded under `chemical_properties`.
- `nutritional_roles.IRON_SOURCE` is supported by a `DATABASE_ENTRY` reference
  to CultureMech's original `Mineral` role text.

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
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fecl3` to
  `CHEBI:30808` with `skos:exactMatch`.
- The core final SSSOM `other` tokens, including `[FeCl3]`,
  `ferric chloride`, `iron(3+) chloride`, `iron(III) chloride`, and
  `CAS:7705-08-0`, all denote anhydrous ferric chloride.
- Major: the final SSSOM `other` column also exports `FeCl3 (25mM)`, which is
  a concentration-bearing preparation label rather than an exact synonym of
  the compound.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Fecl3`,
  `CHEBI:30808`, `7705-08-0`, and `FeCl3` found the active YAML, aggregate
  copy, final SSSOM row, row-review provenance, the localized ferric chloride
  tetrahydrate, ferric chloride hexahydrate, an unmapped FeCl3/EDTA tombstone,
  and ignored aggregate backups.

## Completeness

- The exact anhydrous identity, CAS RN, structure fields, supported role,
  kg-microbe cross-reference, ingredient type, occurrence counts, and accepted
  exact synonyms are populated.
- The final SSSOM synonym payload needs filtering for the concentration-specific
  token.

## Recommended Edits

- Major: remove or filter `FeCl3 (25mM)` from exact final SSSOM `other`
  export, sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
