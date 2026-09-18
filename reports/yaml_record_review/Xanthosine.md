# `data/ingredients/mapped/Xanthosine.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:18107` xanthosine identity, structure fields, CAS
RN, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Xanthosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18107` with matching
  `ontology_mapping.ontology_id`, label `xanthosine`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `146-80-5`.
- Chemical fields: formula `C10H12N4O6` with populated InChI and SMILES
  strings.
- Synonyms: four clean kg-microbe synonyms for xanthosine.
- Occurrences: 10 FEBA media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xanthocidin` through `Xylan_From_Beechwood`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the four
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:18107` returns active label `xanthosine`, CAS
  `146-80-5`, formula `C10H12N4O6`, matching structure strings, and synonym
  coverage for the clean kg-microbe labels.
- The final SSSOM row correctly has
  `MIM:Xanthosine skos:exactMatch CHEBI:18107`.

## Issues

None.

## Completeness

- The CAS-backed CHEBI mapping, structure fields, CAS RN, FEBA occurrence,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
