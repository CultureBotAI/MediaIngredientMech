# `data/ingredients/mapped/Sodium_Phosphite_Dibasic_Pentahydrate.yaml`

## Verdict

Pass. The CAS identity, pentahydrate phosphite form, close ChEBI parent row, and
exact CAS registry row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sodium_Phosphite_Dibasic_Pentahydrate.yaml`.
- Identifier and grounding: `identifier: cas:13517-23-2` with
  `ontology_mapping.ontology_id: CHEBI:36361`, label `phosphorous acid`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 current CultureMech occurrences; the record is retained from
  the CultureBotHT compounds input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Phosphate_Dibasic` through `Sodium_Pyrophosphate_Dibasic`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:36361` as `phosphorous acid`,
  agreeing with the close ChEBI parent row retained after the #342 hydrate
  regrade.
- Fresh PubChem lookup for CAS `13517-23-2` resolves the same sodium phosphite
  pentahydrate identity.
- Final SSSOM preserves the close ChEBI parent row and exact CAS registry row;
  both rows keep only the same-substance `CAS:13517-23-2` in `other`.

## Completeness

- The CAS RN, pentahydrate/source label boundary, parent mapping, registry row,
  and final SSSOM rows agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
