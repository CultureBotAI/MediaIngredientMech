# `data/ingredients/mapped/Sodium_Salicylate.yaml`

## Verdict

Pass. The exact `CHEBI:9180` sodium salicylate identity, CultureBotHT CAS
support, structure, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Salicylate.yaml`.
- Identifier and grounding: `identifier: CHEBI:9180` with
  `ontology_mapping.ontology_id: CHEBI:9180`, label `Sodium salicylate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 current CultureMech occurrences; the record is retained from
  the CultureBotHT compounds input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Salicylate` through `Sodium_Thiophosphate_Tribasic_Hydrate`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:9180` with label
  `Sodium salicylate` and CAS `54-21-7`.
- Fresh PubChem lookup for CAS `54-21-7` resolves to sodium salicylate with the
  same InChI and SMILES as the record.
- Final SSSOM publishes a single exact ChEBI row with only `CAS:54-21-7` in
  `other`.

## Completeness

- The ChEBI ID, label, CAS RN, formula, structure, and final exact row agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
