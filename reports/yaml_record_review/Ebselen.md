# `data/ingredients/mapped/Ebselen.yaml`

## Verdict

Pass. The CultureBotHT record maps to the exact ChEBI term for ebselen, the
CAS-derived chemistry matches PubChem, and the final SSSOM row publishes only
same-substance synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Ebselen.yaml`.
- Identifier and grounding: `identifier: CHEBI:77543` with matching
  `ontology_mapping.ontology_id`, canonical label `ebselen`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:77543` to `ebselen`.
- PubChem resolved CAS RN `60940-34-3` to CID 3194 with formula `C13H9NOSe`
  and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/E-Amino-N-Caproic_Acid.yaml data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml data/ingredients/mapped/E_4_Aminostyryl_Acetate.yaml data/ingredients/mapped/Ebselen.yaml data/ingredients/mapped/Econazole_Nitrate_Salt.yaml --out /tmp/mim_e_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ebselen.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, and exact synonym as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Ebselen` to
  `CHEBI:77543` with `skos:exactMatch`, the canonical ChEBI object label, and
  `2-phenyl-1,2-benzoselenazol-3(2H)-one|CAS:60940-34-3` in `other`; both
  tokens denote ebselen.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the OAK/OLS
  pass as `CONFIRMED_NO_ACTION`.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `CHEBI:77543`, `60940-34-3`, and the MIM
  subject found the active YAML, aggregate copy, final SSSOM row, and expected
  row-review TSVs; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, formula, InChI, SMILES, and exact synonym are
  populated.
- Occurrence counts are zero and no nutritional, physicochemical, biological,
  component, or environmental claims are asserted.

## Recommended Edits

- None.
