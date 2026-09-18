# `data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml`

## Verdict

Pass. The CultureMech ferric phosphate tetrahydrate label maps to the exact
active ChEBI tetrahydrate term, the hydrate audit agrees with the CAS-backed
tetrahydrate identity, and the final SSSOM `other` tokens are safe.

## Identity

- Reviewed record: `data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:131372` with matching
  `ontology_mapping.ontology_id`, canonical label
  `iron(3+) phosphate tetrahydrate`, source `CHEBI`, `mapping_quality:
  EXACT_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- The structure fields record CAS RN `31096-47-6`, formula
  `Fe.4H2O.O4P`, and the CHEBI/PubChem-backed InChI for iron(3+) phosphate
  tetrahydrate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml --out /tmp/mim_fe2_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fe_Iii_Citrate.yaml data/ingredients/mapped/Fe_Iiipo4_X_4_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_6_H2o.yaml data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml data/ingredients/mapped/Fecl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms, and
  occurrence counts as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fe_Iiipo4_X_4_H2o` to `CHEBI:131372` with `skos:exactMatch`; its
  hydrate/formula synonyms and `CAS:31096-47-6` `other` token denote the same
  tetrahydrate.
- `mappings/hydrate_review.tsv` marks the named tetrahydrate and
  `CHEBI:131372` mapping as correct and high-confidence.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Fe_Iiipo4_X_4_H2o`, `CHEBI:131372`, and
  `Fe(III)PO4 x 4 H2O` found the active YAML, aggregate copy, final SSSOM row,
  hydrate review row, row-review provenance, CultureMech recipe memberships,
  and ignored aggregate backups; it did not expose a contradictory active
  mapping.

## Completeness

- The exact tetrahydrate identity, CAS RN, structure fields, hydrate-form
  synonyms, ingredient type, occurrence counts, and final SSSOM payload are
  populated.
- No unsupported roles, components, or environmental contexts are asserted.

## Recommended Edits

- None.
