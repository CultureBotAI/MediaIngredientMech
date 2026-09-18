# `data/ingredients/mapped/Emodin.yaml`

## Verdict

Pass. Emodin is grounded to the exact ChEBI term, the CAS-derived structure
matches PubChem, and the final SSSOM row publishes only a same-substance ChEBI
synonym plus the matching CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/Emodin.yaml`.
- Identifier and grounding: `identifier: CHEBI:42223` with matching
  `ontology_mapping.ontology_id`, canonical label `emodin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:42223` to `emodin`.
- PubChem resolved CAS RN `518-82-1` to CID 3220 with formula `C15H10O5` and
  the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Egg_Yolk.yaml data/ingredients/mapped/Elastin.yaml data/ingredients/mapped/Emodin.yaml data/ingredients/mapped/Enoxacin.yaml data/ingredients/mapped/Enrichment_Solution_For_Seawater_Medium.yaml --out /tmp/mim_e2_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Emodin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym, and zero
  occurrence count as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Emodin` to
  `CHEBI:42223` with `skos:exactMatch`, the canonical ChEBI object label, and
  `1,3,8-trihydroxy-6-methylanthra-9,10-quinone|CAS:518-82-1`; both `other`
  tokens denote emodin.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the OAK/OLS
  pass as `CONFIRMED_NO_ACTION`.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Emodin`, `CHEBI:42223`, and
  `518-82-1` found the active YAML, aggregate copy, final SSSOM row, and
  expected row-review TSVs; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, formula, InChI, SMILES, exact synonym, and final
  SSSOM payload are populated.
- No unsupported nutritional, physicochemical, biological, component, or
  environmental claims are asserted.

## Recommended Edits

- None.
