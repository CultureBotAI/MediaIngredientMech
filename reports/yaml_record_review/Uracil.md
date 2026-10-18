# `data/ingredients/mapped/Uracil.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, structure fields, synonyms, aggregate
row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Uracil.yaml`.
- Identifier and grounding: `identifier: CHEBI:17568` with matching
  `ontology_mapping.ontology_id`, label `uracil`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `66-22-8`.
- Synonyms: raw CultureMech role/cross-reference text plus exact uracil
  synonyms.
- Occurrences: 35 CultureMech recipe occurrences.
- KG-Microbe node: `CHEBI:17568`, matching the identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `UW_Concentrated_Base` through `Uracil`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:17568` returns active label `uracil`, CAS xref
  `66-22-8`, formula `C4H4N2O2`, the same InChI and SMILES as the YAML, and
  the exported SSSOM `other` labels as CHEBI synonyms.
- The final SSSOM row correctly has
  `MIM:Uracil skos:exactMatch CHEBI:17568`, with only CHEBI-derived synonyms
  and `CAS:66-22-8` in `other`.

## Issues

None.

## Completeness

- The CHEBI identity, CAS RN, structure fields, synonyms, occurrence count,
  KG-Microbe node, aggregate copy, and final SSSOM row agree.
- The raw `Cross-references:` and `Role:` / `Properties:` CultureMech strings
  are kept out of final SSSOM `other`.

## Recommended Edits

None.
