# `data/ingredients/mapped/Esculin_Monohydrate.yaml`

## Verdict

Needs curation, with a major final-SSSOM synonym issue. The ChEBI hydrate
identity, hydrate formula, structure fields, and exact IUPAC synonym are
correct after the #321 repair, but `hydrolysis: esculin` is still exported as a
published synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Esculin_Monohydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:73111` with matching
  `ontology_mapping.ontology_id`, canonical label `esculin hydrate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:73111` to active
  `esculin hydrate`, and OLS reports `C15H16O9.H2O` plus the same hydrate InChI
  and SMILES now recorded under `chemical_properties`.
- PubChem lookup by the old source CAS RN `531-75-9` resolved to anhydrous
  `C15H16O9`; the record no longer records that CAS RN after the exact hydrate
  promotion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Erythrose.yaml data/ingredients/mapped/Escin.yaml data/ingredients/mapped/Esculin_Ferric_Citrate.yaml data/ingredients/mapped/Esculin_Monohydrate.yaml data/ingredients/mapped/Estragole.yaml --out /tmp/mim_esc_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Esculin_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI hydrate identifier, hydrate formula, InChI, SMILES, exact IUPAC
  synonym, and #321 promotion history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Esculin_Monohydrate` to `CHEBI:73111` with `skos:exactMatch` and the
  canonical ChEBI object label.
- The row's `7-hydroxy-2-oxo-2H-chromen-6-yl beta-D-glucopyranoside--water
  (1/1)` `other` token is an exact ChEBI synonym for `CHEBI:73111`.
- Major: the same SSSOM row also exports `hydrolysis: esculin` in `other`.
  That token describes an assay reaction using esculin; it is not a synonym of
  esculin monohydrate and violates the final SSSOM synonym policy.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Esculin_Monohydrate`, `CHEBI:73111`, `531-75-9`, and
  `hydrolysis: esculin` found the active YAML, aggregate copy, final SSSOM row,
  hydrate-review provenance, and expected row-review TSVs; it did not expose a
  contradictory active mapping.

## Completeness

- The exact hydrate identity, hydrate structure fields, exact IUPAC synonym,
  and final SSSOM identity row are populated.
- CAS RN, roles, components, occurrence claims, and environmental contexts are
  correctly empty.

## Recommended Edits

- Major: remove the assay text `hydrolysis: esculin` from the active synonyms
  in `data/ingredients/mapped/Esculin_Monohydrate.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
