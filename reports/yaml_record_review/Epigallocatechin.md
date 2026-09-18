# `data/ingredients/mapped/Epigallocatechin.yaml`

## Verdict

Pass. Epigallocatechin preserves its CAS-to-ChEBI lookup provenance, the
recorded CAS structure matches PubChem, and the final SSSOM row uses a Rule D
exact identity predicate with safe `other` tokens.

## Identity

- Reviewed record: `data/ingredients/mapped/Epigallocatechin.yaml`.
- Identifier and grounding: `identifier: CHEBI:42255` with matching
  `ontology_mapping.ontology_id`, canonical label `(-)-epigallocatechin`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:42255` to
  `(-)-epigallocatechin`.
- PubChem resolved CAS RN `970-74-1` to CID 72277 with formula `C15H14O7` and
  the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Enrofloxacin.yaml data/ingredients/mapped/Enterobactin.yaml data/ingredients/mapped/Epiandrosterone.yaml data/ingredients/mapped/Epigallocatechin.yaml data/ingredients/mapped/Epigallocatechin_Gallate.yaml --out /tmp/mim_epi_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Epigallocatechin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym, CAS lookup
  grade, and zero occurrence count as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Epigallocatechin` to `CHEBI:42255` with `skos:exactMatch`; this is the
  record's own-identifier row, so Rule D allows the exact predicate while
  `mapping_quality` preserves `CAS_RN_LOOKUP` provenance.
- The SSSOM `other` tokens are the curated exact ChEBI synonym and
  `CAS:970-74-1`, which belongs to the same `(-)-epigallocatechin` identity.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records that the
  Epigallocatechin synonym-enrichment text was already represented.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Epigallocatechin`, `CHEBI:42255`, and
  `970-74-1` found the active YAML, aggregate copy, final SSSOM row, and
  expected row-review TSVs; it did not expose a contradictory active mapping.

## Completeness

- The exact identity, CAS RN, formula, InChI, SMILES, exact synonym, and final
  SSSOM payload are populated.
- No unsupported nutritional, physicochemical, biological, component, or
  environmental claims are asserted.

## Recommended Edits

- None.
