# `data/ingredients/mapped/Ferric_nitrilotriacetate.yaml`

## Verdict

Pass with a minor classification gap. The CultureMech residual label was
grounded to the exact ChEBI ferric nitrilotriacetate synonym and now has
structured evidence for the SSSOM builder, but the CHEBI-primary record missed
`ingredient_type: SINGLE_INGREDIENT` backfill.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ferric_nitrilotriacetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132238` with matching
  `ontology_mapping.ontology_id`, canonical label
  `iron(III) nitrilotriacetate`, source `CHEBI`, `mapping_quality:
  SYNONYM_MATCH`, `match_level: NORMALIZED`, and `mapping_status: MAPPED`.
- The active `LEXICAL_MATCH` evidence and creation history both state that
  CultureMech carried two `Ferric nitrilotriacetate` mentions and that the
  label matched an exact synonym of `CHEBI:132238`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferric_Iron.yaml data/ingredients/mapped/Ferric_Malate_Solution.yaml data/ingredients/mapped/Ferric_nitrilotriacetate.yaml data/ingredients/mapped/Ferrihydrite.yaml data/ingredients/mapped/Ferrous_Citrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferric_nitrilotriacetate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, exact-synonym grounding, CultureMech occurrence evidence,
  and 2 occurrence counts as the per-record YAML.
- `mappings/culturemech_residual_groundings.tsv` records
  `Ferric nitrilotriacetate` as a net-new `CHEBI:132238` record created from
  the CultureMech residual sweep, and the September #541 repair restored that
  provenance to `ontology_mapping.evidence`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ferric_nitrilotriacetate` to `CHEBI:132238` with `skos:exactMatch` and
  no `other` payload.
- Minor: the record has no `ingredient_type`; as a CHEBI-primary ferric
  nitrilotriacetate record it should be `SINGLE_INGREDIENT`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for
  `Ferric_nitrilotriacetate` and `Ferric nitrilotriacetate` found the active
  YAML, aggregate copy, final SSSOM row, CultureMech residual triage and
  grounding rows, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, source occurrence, mapping evidence, occurrence
  counts, and final SSSOM row are populated.
- The only consequential gap in this new residual record is the missing
  ingredient classification.

## Recommended Edits

- Minor: set `ingredient_type: SINGLE_INGREDIENT` in
  `data/ingredients/mapped/Ferric_nitrilotriacetate.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  roundtrip gate.
