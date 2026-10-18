# `data/ingredients/mapped/Epinephrine.yaml`

## Verdict

Pass. The record preserves the CAS-to-ChEBI lookup for the `(-)-Epinephrine`
surface form, the CAS-derived structure matches PubChem, and the final SSSOM
row uses an exact identity predicate with safe `other` tokens.

## Identity

- Reviewed record: `data/ingredients/mapped/Epinephrine.yaml`.
- Identifier and grounding: `identifier: CHEBI:28918` with matching
  `ontology_mapping.ontology_id`, canonical label `(R)-adrenaline`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:28918` to `(R)-adrenaline`.
- PubChem name lookup for `Epinephrine` resolved to CID 5816 with formula
  `C9H13NO3` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Epinephrine.yaml data/ingredients/mapped/Ertapenem.yaml data/ingredients/mapped/Erythromycin.yaml data/ingredients/mapped/Erythromycin_A.yaml data/ingredients/mapped/Erythromycin_B.yaml --out /tmp/mim_ery_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Epinephrine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym, and CAS
  lookup grade as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Epinephrine` to `CHEBI:28918` with `skos:exactMatch`; this is the
  record's own-identifier row, so Rule D allows the exact predicate while
  `mapping_quality` preserves `CAS_RN_LOOKUP` provenance.
- The row's `other` tokens are the curated exact ChEBI synonym and
  `CAS:51-43-4`, which belongs to the same `(R)-adrenaline` identity.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records that the
  synonym-enrichment text was already represented, and
  `mappings/mim_curie_aliases.tsv` preserves the historical parenthesized MIM
  subject as an alias of the current subject.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` for `MIM:Epinephrine`, `CHEBI:28918`, and
  `51-43-4` found the active YAML, aggregate copy, final SSSOM row, historical
  MIM alias, and expected row-review TSVs; it did not expose a contradictory
  active mapping.

## Completeness

- The exact identity, CAS RN, formula, InChI, SMILES, exact synonym, and final
  SSSOM payload are populated.
- No unsupported nutritional, physicochemical, biological, component, or
  environmental claims are asserted.

## Recommended Edits

- None.
