# `data/ingredients/mapped/Sorbitol.yaml`

## Verdict

Pass. The exact `CHEBI:30911` glucitol identity, CAS-backed formula, ChEBI
synonyms, CultureMech carbon-source role, occurrence count, and final SSSOM row
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sorbitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:30911` with
  `ontology_mapping.ontology_id: CHEBI:30911`, label `glucitol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 22 source occurrences across 22 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Soil_Extract` through `Sorbose`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:30911` with label `glucitol` and
  the curated sorbitol aliases.
- Fresh PubChem lookup for CAS `50-70-4` resolves to sorbitol with formula
  `C6H14O6`, matching the stored formula.
- The `CARBON_SOURCE` role is traced to imported CultureMech `Carbon Source`
  role text with `reference_type: DATABASE_ENTRY`.
- Final SSSOM publishes only same-substance ChEBI aliases plus `CAS:50-70-4`;
  the raw role and property text is correctly filtered out.

## Completeness

- The ChEBI ID, label, CAS RN, formula, carbon-source role, 22/22 occurrence
  count, active synonyms, and final exact row agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
