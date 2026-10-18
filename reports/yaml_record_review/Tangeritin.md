# `data/ingredients/mapped/Tangeritin.yaml`

## Verdict

Pass. The CultureBotHT CAS RN resolves through ChEBI to active
`CHEBI:9400`, the synonym and structure fields match tangeretin, the aggregate
row is synchronized, and the final SSSOM publishes only real same-substance
aliases.

## Identity

- Reviewed record: `data/ingredients/mapped/Tangeritin.yaml`.
- Identifier and grounding: `identifier: CHEBI:9400` with
  `ontology_mapping.ontology_id: CHEBI:9400`, label `tangeretin`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `481-53-8`, formula `C20H20O7`, and ChEBI/PubChem
  InChI and SMILES for tangeretin.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tangeritin` through `Tartrate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:9400` as `tangeretin`, lists
  `cas:481-53-8` as a database cross-reference, and includes both
  `tangeritin` and the stored IUPAC synonym for the same term.
- Fresh PubChem lookup by CAS `481-53-8` resolves CID 68077, confirms the same
  `C20H20O7` formula and InChI, and lists CAS `481-53-8`.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Tangeritin`, points
  at `CHEBI:9400`, names `obo:chebi.owl`, and publishes only the curated IUPAC
  synonym plus `CAS:481-53-8` in `other`.

## Completeness

- The CAS-backed ChEBI identity, exact synonym, structure fields, aggregate
  row, and final SSSOM row agree.
- No components, roles, environmental contexts, or CultureMech occurrence rows
  are asserted.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CAS import, mapping-grade
  repair, aggregate, row-review, final SSSOM, and generated rows.

## Recommended Edits

- None.
