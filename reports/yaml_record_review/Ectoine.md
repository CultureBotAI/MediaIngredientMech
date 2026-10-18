# `data/ingredients/mapped/Ectoine.yaml`

## Verdict

Pass. Ectoine is grounded to the exact ChEBI term, its CAS-derived chemistry
matches PubChem, its aggregate copy is synchronized, and its final SSSOM row
publishes only same-substance synonyms plus the matching CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/Ectoine.yaml`.
- Identifier and grounding: `identifier: CHEBI:27592` with matching
  `ontology_mapping.ontology_id`, canonical label `ectoine`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, 14 CultureMech
  source occurrences, and `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:27592` to `ectoine`.
- PubChem resolved CAS RN `96702-03-3` to CID 126041 with formula `C6H10N2O2`
  and the same stereospecific InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ectoine.yaml data/ingredients/mapped/Edta.yaml data/ingredients/mapped/Edta_Acid_Form.yaml data/ingredients/mapped/Edta_Chelating_Agent.yaml data/ingredients/mapped/Edta_Stock.yaml --out /tmp/mim_edta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ectoine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms, occurrence
  counts, and curation history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Ectoine`
  to `CHEBI:27592` with `skos:exactMatch`, the canonical ChEBI object label,
  both curated exact synonyms, and `CAS:96702-03-3`; all `other` tokens denote
  ectoine.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the OAK/OLS
  pass as `CONFIRMED_NO_ACTION`.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Ectoine`, `CHEBI:27592`, and
  `96702-03-3` found the active YAML, the aggregate copy, the 14 CultureMech
  membership rows, the final SSSOM row, and the expected row-review TSVs; it
  did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, stereochemistry-bearing structure, occurrence
  count, exact synonyms, and final SSSOM payload are populated.
- No unsupported nutritional, physicochemical, biological, component, or
  environmental claims are asserted.

## Recommended Edits

- None.
