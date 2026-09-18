# `data/ingredients/mapped/Vancomycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI identity, structure fields, aggregate row,
and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Vancomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28001` with matching
  `ontology_mapping.ontology_id`, label `vancomycin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical fields: formula `C66H75Cl2N9O24` and ChEBI/PubChem SMILES/InChI.
- Occurrences: one CultureMech recipe occurrence plus 251 MicrobeDecoder
  BacDive trait occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Valerate` through `Vancomycin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Valerate`, `Valeric_Acid`, `Valerolactone`, and
  `Vancomycin`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:28001` returns active label `vancomycin`, formula
  `C66H75Cl2N9O24`, the same SMILES/InChI as the YAML, and CAS xref
  `1404-90-6`.
- The final SSSOM row correctly has
  `MIM:Vancomycin skos:exactMatch CHEBI:28001`, with review provenance and no
  salt or hydrate synonyms in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, structure fields, occurrence counts, aggregate copy,
  and final SSSOM row agree.

## Recommended Edits

None.
