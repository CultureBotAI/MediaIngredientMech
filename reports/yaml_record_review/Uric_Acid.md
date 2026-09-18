# `data/ingredients/mapped/Uric_Acid.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, formula, synonym, aggregate row, and
final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Uric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:27226` with matching
  `ontology_mapping.ontology_id`, label `uric acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `69-93-2`.
- Synonyms: raw CultureMech role/property text plus one uric-acid synonym.
- Occurrences: 5 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uranyl_Acetate` through `Uridine`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:27226` returns active label `uric acid`, formula
  `C5H4N4O3`, and `uric acids` as a CHEBI synonym.
- ChEBI does not carry CAS `69-93-2` on this term, but fresh PubChem lookup for
  `69-93-2` resolves to uric acid CID 1175 with the same formula.
- The final SSSOM row correctly has
  `MIM:Uric_Acid skos:exactMatch CHEBI:27226`, with `uric acids` and
  `CAS:69-93-2` in `other`.

## Issues

None.

## Completeness

- The CHEBI identity, CAS RN, formula, synonym, occurrence count, aggregate
  copy, and final SSSOM row agree.
- Raw `Role:` / `Properties:` CultureMech strings are kept out of final SSSOM
  `other`.

## Recommended Edits

None.
