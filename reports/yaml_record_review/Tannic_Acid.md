# `data/ingredients/mapped/Tannic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS RN is cross-referenced by active `CHEBI:75211`,
the stored IUPAC synonym and structure fields match tannic acid, and the final
SSSOM exact row has only valid same-substance `other` tokens.

## Identity

- Reviewed record: `data/ingredients/mapped/Tannic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:75211` with
  `ontology_mapping.ontology_id: CHEBI:75211`, label `tannic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `1401-55-4`, formula `C76H52O46`, and
  ChEBI-derived InChI and SMILES for tannic acid.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tangeritin` through `Tartrate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:75211` as `tannic acid`, lists
  `cas:1401-55-4` as a database cross-reference, and includes the stored IUPAC
  name as an exact synonym.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Tannic_Acid`, points
  at `CHEBI:75211`, names `obo:chebi.owl`, and publishes only the curated IUPAC
  synonym plus `CAS:1401-55-4` in `other`.
- Fresh PubChem lookup by CAS `1401-55-4` found no CID, so there is no PubChem
  structure that conflicts with the stored ChEBI structure.

## Completeness

- The CAS-backed ChEBI identity, exact synonym, structure fields, aggregate
  row, and final SSSOM row agree.
- No components, roles, environmental contexts, or CultureMech occurrence rows
  are asserted.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT import,
  aggregate, row-review, final SSSOM, and generated rows.

## Recommended Edits

- None.
