# `data/ingredients/mapped/Sodium_Thiophosphate_Tribasic_Hydrate.yaml`

## Verdict

Pass. The CAS hydrate identity, trisodium phosphorothioate hydrate structure,
close ChEBI parent row, and exact CAS registry row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sodium_Thiophosphate_Tribasic_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:10489-48-2` with
  `ontology_mapping.ontology_id: CHEBI:46612`, label `phosphorothioic acid`,
  source `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 current CultureMech occurrences; the record is retained from
  the CultureBotHT compounds input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Salicylate` through `Sodium_Thiophosphate_Tribasic_Hydrate`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:46612` as
  `phosphorothioic acid`, agreeing with the close ChEBI parent row retained
  after the #342 hydrate regrade.
- Fresh PubChem lookup for CAS `10489-48-2` resolves CID `53442939` with the
  same trisodium hydrate formula, InChI, and SMILES as the record.
- The final SSSOM preserves the close ChEBI parent row and exact CAS row; both
  rows keep only the same-substance `CAS:10489-48-2` in `other`.

## Completeness

- The CAS RN, hydrate formula, structure, parent mapping, exact registry row,
  and final SSSOM rows agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
