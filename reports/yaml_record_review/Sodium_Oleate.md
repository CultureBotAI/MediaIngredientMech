# `data/ingredients/mapped/Sodium_Oleate.yaml`

## Verdict

Pass. The exact `CHEBI:81860` sodium oleate identity, CAS-backed structure,
CultureMech carbon-source role, occurrence count, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Oleate.yaml`.
- Identifier and grounding: `identifier: CHEBI:81860` with
  `ontology_mapping.ontology_id: CHEBI:81860`, label `Sodium oleate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 source occurrences across 3 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Nitrate_Nitrogen_Source` through `Sodium_Pantothenate`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/run_shared_evidence_validator.py` is
  unavailable because the sibling `culturebotai-claw` checkout is absent.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:81860` with label
  `Sodium oleate` and CAS `143-19-1`.
- Fresh PubChem lookup for CAS `143-19-1` resolves to sodium oleate with the
  same sodium oleate InChI as the record.
- The `CARBON_SOURCE` role is traced to imported CultureMech `Carbon Source`
  role text with `reference_type: DATABASE_ENTRY`.
- Final SSSOM publishes only `CAS:143-19-1` in `other`; the raw role and
  property text is correctly filtered out.

## Completeness

- The ChEBI ID, label, CAS RN, formula, structure, occurrence count,
  carbon-source role, and final exact row agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
