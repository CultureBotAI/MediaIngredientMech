# `data/ingredients/mapped/Fecl2.yaml`

## Verdict

Pass. The CultureMech ferrous chloride label maps to active ChEBI iron
dichloride, PubChem confirms the recorded anhydrous structure, the
CultureMech iron-source role is supported, and the final SSSOM `other` tokens
are safe.

## Identity

- Reviewed record: `data/ingredients/mapped/Fecl2.yaml`.
- Identifier and grounding: `identifier: CHEBI:30812` with matching
  `ontology_mapping.ontology_id`, canonical label `iron dichloride`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:30812`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `7758-94-3` resolved to CID 24458 with formula
  `Cl2Fe` and the same InChI recorded under `chemical_properties`.
- `nutritional_roles.IRON_SOURCE` is supported by a `DATABASE_ENTRY` reference
  to CultureMech's original `Mineral` role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml --out /tmp/mim_fe2_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, kg-microbe node ID,
  supported `IRON_SOURCE` role, and refreshed occurrence counts as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fecl2` to
  `CHEBI:30812` with `skos:exactMatch`; `Ferrous chloride`,
  `Iron(II) chloride`, `[FeCl2]`, `iron(2+) chloride`, and `CAS:7758-94-3`
  all denote the same compound.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms that the
  OAK/OLS row review found no curation action for this CHEBI mapping.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Fecl2`,
  `CHEBI:30812`, and `7758-94-3` found the active YAML, aggregate copy, final
  SSSOM row, row-review provenance, anhydrous/ferrous chloride hydrate sibling
  rows, CultureMech recipe memberships, and ignored aggregate backups; it did
  not expose a contradictory active mapping for the anhydrous row.

## Completeness

- The exact identity, CAS RN, structure fields, accepted exact synonyms,
  supported iron-source role, kg-microbe cross-reference, ingredient type, and
  final SSSOM payload are populated.
- No unsupported roles, components, or environmental contexts are asserted.

## Recommended Edits

- None.
