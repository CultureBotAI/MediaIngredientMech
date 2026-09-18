# `data/ingredients/mapped/Sodium_Periodate.yaml`

## Verdict

Pass. The exact `CHEBI:75226` sodium periodate identity, CultureBotHT CAS
support, structure, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Periodate.yaml`.
- Identifier and grounding: `identifier: CHEBI:75226` with
  `ontology_mapping.ontology_id: CHEBI:75226`, label `sodium periodate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 current CultureMech occurrences; the record is retained from
  the CultureBotHT compounds input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Perchlorate` through `Sodium_Phosphate_Buffer`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:75226` with label
  `sodium periodate` and CAS `7790-28-5`.
- Fresh PubChem lookup for CAS `7790-28-5` resolves to sodium periodate with
  the same sodium periodate InChI and SMILES as the record.
- Final SSSOM publishes a single exact ChEBI row with `CAS:7790-28-5` in
  `other` and no unsafe role, hydrate, component, or concentration text.

## Completeness

- The ChEBI ID, label, CAS RN, formula, structure, and final exact row agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
