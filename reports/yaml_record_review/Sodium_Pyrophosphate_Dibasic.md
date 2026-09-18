# `data/ingredients/mapped/Sodium_Pyrophosphate_Dibasic.yaml`

## Verdict

Pass. The `cas:7758-16-9` disodium pyrophosphate identity, close NCIT parent
row, exact CAS row, exact kg-microbe registry row, and final SSSOM payload pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Pyrophosphate_Dibasic.yaml`.
- Identifier and grounding: `identifier: cas:7758-16-9` with
  `ontology_mapping.ontology_id: NCIT:C77500`, label `Sodium Pyrophosphate`,
  source `NCIT`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 current CultureMech occurrences; the record is retained from
  the CultureBotHT compounds input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Phosphate_Dibasic` through `Sodium_Pyrophosphate_Dibasic`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `NCIT:C77500` as
  `Sodium Pyrophosphate`, matching the stored parent target.
- Fresh PubChem lookup for CAS `7758-16-9` resolves to disodium pyrophosphate
  with the same formula, PubChem CID, InChI, and SMILES as the record.
- Final SSSOM preserves the NCIT parent row plus exact rows for
  `cas:7758-16-9` and
  `kgmicrobe.compound:sodium_pyrophosphate_dibasic`; the CAS rows use only the
  same-substance `CAS:7758-16-9` in `other`.

## Completeness

- The CAS RN, NCIT parent, formula, structure, PubChem CID, registry rows, and
  final SSSOM rows agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
