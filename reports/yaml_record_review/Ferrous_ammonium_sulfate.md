# `data/ingredients/mapped/Ferrous_ammonium_sulfate.yaml`

## Verdict

Pass with a minor classification gap. The CultureMech residual label was
grounded to the exact ChEBI synonym for anhydrous ferrous ammonium sulfate and
now has structured evidence for the SSSOM builder, but the CHEBI-primary record
missed `ingredient_type: SINGLE_INGREDIENT` backfill.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ferrous_ammonium_sulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:76243` with matching
  `ontology_mapping.ontology_id`, canonical label
  `ferrous ammonium sulfate (anhydrous)`, source `CHEBI`, `mapping_quality:
  SYNONYM_MATCH`, `match_level: NORMALIZED`, and `mapping_status: MAPPED`.
- The active `LEXICAL_MATCH` evidence and creation history both state that
  CultureMech carried six `Ferrous ammonium sulfate` mentions and that the
  label matched an exact synonym of anhydrous `CHEBI:76243`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferrous_Ion.yaml data/ingredients/mapped/Ferrous_ammonium_sulfate.yaml data/ingredients/mapped/Ferroverdin.yaml data/ingredients/mapped/Ferulate.yaml data/ingredients/mapped/Ferulic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferrous_ammonium_sulfate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, exact-synonym grounding, CultureMech occurrence evidence,
  and 6 occurrence counts as the per-record YAML.
- `mappings/culturemech_residual_groundings.tsv` records
  `Ferrous ammonium sulfate` as a net-new `CHEBI:76243` record created from
  the CultureMech residual sweep, and the September #541 repair restored that
  provenance to `ontology_mapping.evidence`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ferrous_ammonium_sulfate` to `CHEBI:76243` with `skos:exactMatch` and
  no `other` payload.
- Minor: the record has no `ingredient_type`; as a CHEBI-primary ferrous
  ammonium sulfate record it should be `SINGLE_INGREDIENT`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for
  `Ferrous_ammonium_sulfate` and `Ferrous ammonium sulfate` found the active
  YAML, aggregate copy, final SSSOM row, CultureMech residual triage and
  grounding rows, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, source occurrence, mapping evidence, occurrence
  counts, and final SSSOM row are populated.
- The only consequential gap in this new residual record is the missing
  ingredient classification.

## Recommended Edits

- Minor: set `ingredient_type: SINGLE_INGREDIENT` in
  `data/ingredients/mapped/Ferrous_ammonium_sulfate.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  roundtrip gate.
