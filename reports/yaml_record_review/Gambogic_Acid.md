# `data/ingredients/mapped/Gambogic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup maps uniquely to active `(-)-gambogic acid`,
the stored structure agrees with ChEBI and PubChem, and the final SSSOM row
publishes only the valid CAS alias.

## Identity

- Reviewed record: `data/ingredients/mapped/Gambogic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:67521` with matching
  `ontology_mapping.ontology_id`, canonical label `(-)-gambogic acid`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:67521` as an active ChEBI term with CAS xref
  `2752-65-0`, formula `C38H44O8`, and the same InChI and SMILES recorded in
  `chemical_properties`.
- PubChem lookup by CAS RN `2752-65-0` resolved to CID 9852185 titled
  `Gambogic Acid` with formula `C38H44O8` and the same InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gallate_Formate.yaml data/ingredients/mapped/Gallic_Acid.yaml data/ingredients/mapped/Gallium_Iiichloride.yaml data/ingredients/mapped/Gambogic_Acid.yaml data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gallic_Acid.yaml data/ingredients/mapped/Gambogic_Acid.yaml data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS lookup provenance, CAS RN, structure fields, and
  ingredient type as the per-record YAML.
- The row-review manifest marks the `Gambogic Acid` to `CHEBI:67521` row as
  `ALREADY_REPRESENTED` after synonym review, so the label difference from
  `(-)-gambogic acid` was already covered.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Gambogic_Acid` to `CHEBI:67521` with `skos:exactMatch` and exports only
  `CAS:2752-65-0` in `other`.
- The record has no inferred nutritional, physicochemical, component, synonym,
  source-occurrence, or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, synonym-enrichment review row, generated indexes, and ignored aggregate
  backups.

## Completeness

- The exact gambogic-acid identity, single-ingredient type, CAS RN, structure
  fields, CultureBotHT provenance, and final SSSOM row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
