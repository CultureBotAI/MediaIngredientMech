# `data/ingredients/mapped/Valerolactone.yaml`

## Verdict

Pass. The CAS-backed exact CHEBI identity, CAS RN, structure fields, synonym,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Valerolactone.yaml`.
- Identifier and grounding: `identifier: CHEBI:16545` with matching
  `ontology_mapping.ontology_id`, label `5-valerolactone`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `542-28-9`.
- Synonyms: one exact IUPAC synonym.
- Chemical fields: formula `C5H8O2` and ChEBI-backed SMILES/InChI.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Valerate` through `Vancomycin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Valerate`, `Valeric_Acid`, `Valerolactone`, and
  `Vancomycin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:16545` returns active label `5-valerolactone`,
  CAS xref `542-28-9`, formula `C5H8O2`, and the same SMILES/InChI as the YAML.
- The exported `tetrahydro-2H-pyran-2-one` synonym is present on
  `CHEBI:16545`.
- The final SSSOM row correctly has
  `MIM:Valerolactone skos:exactMatch CHEBI:16545`, with the IUPAC synonym and
  `CAS:542-28-9` in `other`.

## Issues

None.

## Completeness

- The CAS-backed CHEBI mapping, CAS RN, structure fields, synonym, aggregate
  copy, and final SSSOM row agree.

## Recommended Edits

None.
