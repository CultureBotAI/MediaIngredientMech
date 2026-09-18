# `data/ingredients/mapped/Tazobactam.yaml`

## Verdict

Pass. The MicrobeDecoder surface `Tazobactam` maps exactly to active
`CHEBI:9421`, its structure fields describe tazobactam, and the final SSSOM has
a single clean exact CHEBI row.

## Identity

- Reviewed record: `data/ingredients/mapped/Tazobactam.yaml`.
- Identifier and grounding: `identifier: CHEBI:9421` with
  `ontology_mapping.ontology_id: CHEBI:9421`, label `tazobactam`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C10H12N4O5S`, ChEBI/PubChem InChI and SMILES,
  and molecular weight `300.296`.
- Occurrences: zero CultureMech recipe occurrences and 4 MicrobeDecoder
  antibiotic-trait rows.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Taurine` through `Tea`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:9421` as `tazobactam`.
- The structured mapping evidence preserves the MicrobeDecoder OLS
  label-exact import for `kgmicrobe.trait:tazobactam`, and the promotion
  history records a later `review-ingredients` approval.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Tazobactam`, points
  at `CHEBI:9421`, names `obo:chebi.owl`, and publishes no unsafe `other`
  synonyms.

## Completeness

- The CHEBI identity, structure fields, aggregate row, MicrobeDecoder source
  occurrence, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder import,
  promotion, aggregate, final SSSOM, and generated rows.

## Recommended Edits

- None.
