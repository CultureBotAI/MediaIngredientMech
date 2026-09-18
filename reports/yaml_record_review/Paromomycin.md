# `data/ingredients/mapped/Paromomycin.yaml`

## Verdict

Pass. The MicrobeDecoder import maps exactly to active `CHEBI:7934`
paromomycin, and the absorbed `Neomycin E` synonym is a true same-substance
label.

## Identity

- Reviewed record: `data/ingredients/mapped/Paromomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:7934` with
  `ontology_mapping.ontology_id: CHEBI:7934`, label `paromomycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 MicrobeDecoder `BacDive_Metabolite_production` occurrences
  and no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Paromomycin` resolves `CHEBI:7934`
  `paromomycin`.
- The final SSSOM row was inspected directly and maps `MIM:Paromomycin`
  exactly to `CHEBI:7934`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, SMILES, and
  InChI all describe paromomycin.
- The absorbed `Neomycin E` MicrobeDecoder residual is backed by #208 research
  as a synonym of paromomycin.
- The final SSSOM exports only `Neomycin E` in `other`, which is a legitimate
  synonym for this subject.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
