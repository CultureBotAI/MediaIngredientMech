# `data/ingredients/mapped/Starch.yaml`

## Verdict

Needs curation - major. The starch identity, CAS, CultureMech carbon-source
role, soluble-starch aliases, and occurrence counts agree, but the final SSSOM
row still exports `degradation: starch` as a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Starch.yaml`.
- Identifier and grounding: `identifier: CHEBI:28017` with
  `ontology_mapping.ontology_id: CHEBI:28017`, label `starch`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 9005-25-8`.
- Occurrences: 741 source occurrences across 741 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Stallimycin` through `Stearic_Acid`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:28017` with label `starch`, matching
  the stored CHEBI target after the earlier alpha-maltose repair.
- PubChem does not resolve the generic polymer CAS `9005-25-8`, but the CAS
  value is the same one retained after the duplicate-merge conflict was
  resolved against the OAK canonical xref.
- The `nutritional_roles.CARBON_SOURCE` assertion is backed by CultureMech
  `Carbon source` source text rather than a pure name-pattern inference.
- Curated soluble-starch and catalog labels in final `other` are all starch
  surface forms.
- Major: `degradation: starch` is a process-qualified phrase, not a synonym for
  starch, but it remains an `EXACT_SYNONYM` and is exported in final SSSOM
  `other`.

## Completeness

- Raw parenthetical and `Role: Carbon source` import labels are correctly
  filtered from final SSSOM.
- The only unsupported active synonym or final SSSOM payload found is
  `degradation: starch`.

## Recommended Edits

- Major: remove `degradation: starch` from
  `data/ingredients/mapped/Starch.yaml` or retype it as rejected/non-exported
  provenance so regenerated SSSOM publishes only same-ingredient starch labels.
