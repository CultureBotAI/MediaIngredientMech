# `data/ingredients/mapped/Taurocholate.yaml`

## Verdict

Pass. The generic MicrobeDecoder surface `Taurocholate` maps exactly to active
`CHEBI:36257`, the structure fields describe taurocholate, and the final SSSOM
has a single clean exact CHEBI row.

## Identity

- Reviewed record: `data/ingredients/mapped/Taurocholate.yaml`.
- Identifier and grounding: `identifier: CHEBI:36257` with
  `ontology_mapping.ontology_id: CHEBI:36257`, label `taurocholate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C26H44NO7S`, ChEBI/PubChem InChI and SMILES,
  and molecular weight `514.705`.
- Occurrences: zero CultureMech recipe occurrences and 1 MicrobeDecoder
  metabolite-production row.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Taurine` through `Tea`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:36257` as `taurocholate`.
- The structured mapping evidence preserves the MicrobeDecoder OLS
  label-exact import for `kgmicrobe.trait:taurocholate`, and the promotion
  history records a later `review-ingredients` approval.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Taurocholate`,
  points at `CHEBI:36257`, names `obo:chebi.owl`, and publishes no unsafe
  `other` synonyms.

## Completeness

- The CHEBI identity, structure fields, aggregate row, MicrobeDecoder source
  occurrence, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder import,
  promotion, aggregate, final SSSOM, and generated rows.

## Recommended Edits

- None.
