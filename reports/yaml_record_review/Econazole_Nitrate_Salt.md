# `data/ingredients/mapped/Econazole_Nitrate_Salt.yaml`

## Verdict

Pass. The record preserves the CAS-to-ChEBI lookup provenance for econazole
nitrate, the formula matches the PubChem CAS record, and the final SSSOM row
uses an exact identity predicate with true same-substance `other` tokens.

## Identity

- Reviewed record: `data/ingredients/mapped/Econazole_Nitrate_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:4755` with matching
  `ontology_mapping.ontology_id`, canonical label `econazole nitrate`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- A direct EBI OLS query resolved `CHEBI:4755` to the canonical label
  `econazole nitrate` and the exact synonym
  `1-{2-[(4-chlorobenzyl)oxy]-2-(2,4-dichlorophenyl)ethyl}-1H-imidazole
  nitrate`.
- PubChem resolved CAS RN `24169-02-6` to CID 68589 with formula
  `C18H16Cl3N3O4`, matching the formula recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/E-Amino-N-Caproic_Acid.yaml data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml data/ingredients/mapped/E_4_Aminostyryl_Acetate.yaml data/ingredients/mapped/Ebselen.yaml data/ingredients/mapped/Econazole_Nitrate_Salt.yaml --out /tmp/mim_e_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Econazole_Nitrate_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, CAS lookup grade, and exact synonym as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Econazole_Nitrate_Salt` to `CHEBI:4755` with `skos:exactMatch`. This is
  the record's own-identifier row, so Rule D allows the exact predicate even
  though `mapping_quality` preserves `CAS_RN_LOOKUP` provenance.
- The row's `other` tokens are the inspected long ChEBI exact synonym and
  `CAS:24169-02-6`, which belongs to the same econazole nitrate identity.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records that the
  proposed synonym-enrichment text was already represented.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `CHEBI:4755`, `24169-02-6`, and the MIM
  subject found the active YAML, aggregate copy, final SSSOM row, and expected
  row-review TSVs; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, formula, and exact synonym are populated.
- No unsupported nutritional, physicochemical, biological, component, or
  environmental claims are asserted.

## Recommended Edits

- None.
