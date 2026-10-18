# `data/ingredients/mapped/Fe_Iii_Citrate.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym issues. The ChEBI iron(III)
citrate identity, CAS-backed structure, CultureMech iron-source role, and core
exact synonyms pass, but the final SSSOM `other` column still exports
concentration-bearing preparation strings as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fe_Iii_Citrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:144421` with matching
  `ontology_mapping.ontology_id`, canonical label `iron(III) citrate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `3522-50-7` resolved to CID 61300 with formula
  `C6H5FeO7` and the same InChI recorded under `chemical_properties`.
- `nutritional_roles.IRON_SOURCE` is supported by a `DATABASE_ENTRY` reference
  to CultureMech's original `Mineral source` role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml --out /tmp/mim_fe2_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, structure fields, resolved risky-CAS history,
  supported `IRON_SOURCE` role, and refreshed occurrence counts as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fe_Iii_Citrate` to `CHEBI:144421` with `skos:exactMatch`.
- The core final SSSOM `other` tokens, including `Auryxia`, `Fe(3+)-citrate`,
  `Ferric citrate`, `Eisencitrat`, `KRX-0502`, `Zerenex`, and
  `CAS:3522-50-7`, are real iron(III) citrate synonyms.
- Major: the final SSSOM `other` column also exports
  `Ferric citrate (0.1%, w/v)` and `Fe(III)-citrate (19% Fe)`, which are
  concentration-bearing preparation labels rather than exact synonyms of the
  compound.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Fe_Iii_Citrate`,
  `CHEBI:144421`, and iron(III) citrate labels found the active YAML,
  aggregate copy, final SSSOM row, row-review provenance, CultureMech recipe
  memberships, component references from complex-medium records, and ignored
  aggregate backups.

## Completeness

- The iron(III) citrate identity, CAS RN, structure fields, supported role,
  ingredient type, occurrence counts, and accepted exact synonyms are
  populated.
- Concentration-bearing surfaces need removal from exact final SSSOM synonym
  export.

## Recommended Edits

- Major: remove or filter concentration-specific ferric citrate strings from
  exact final SSSOM `other` export, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
