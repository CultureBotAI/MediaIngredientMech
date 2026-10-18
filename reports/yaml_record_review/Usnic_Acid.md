# `data/ingredients/mapped/Usnic_Acid.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, structure fields, IUPAC synonym,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Usnic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:38319` with matching
  `ontology_mapping.ontology_id`, label `usnic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `125-46-2`.
- Synonyms: one exact IUPAC synonym.
- Chemical fields: formula `C18H16O7` and CHEBI-backed SMILES/InChI.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uridine_5-monophosphate_Disodium_Salt` through `V-8_Juice`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Urocanic_Acid` and `Usnic_Acid`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:38319` returns active label `usnic acid`, CAS
  xref `125-46-2`, formula `C18H16O7`, and the same SMILES/InChI as the YAML.
- The exported IUPAC synonym is present on `CHEBI:38319`, so the SSSOM `other`
  value is a real exact label rather than a sibling or parent-class synonym.
- The final SSSOM row correctly has
  `MIM:Usnic_Acid skos:exactMatch CHEBI:38319`, with the IUPAC synonym and
  `CAS:125-46-2` in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, CAS RN, structure fields, synonym, aggregate copy,
  and final SSSOM row agree.

## Recommended Edits

None.
