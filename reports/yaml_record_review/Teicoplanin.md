# `data/ingredients/mapped/Teicoplanin.yaml`

## Verdict

Pass. The MicrobeDecoder antibiotic surface `Teicoplanin` maps exactly to
active `CHEBI:29687`, the aggregate row is synchronized, and the final SSSOM
has a single clean exact CHEBI row.

## Identity

- Reviewed record: `data/ingredients/mapped/Teicoplanin.yaml`.
- Identifier and grounding: `identifier: CHEBI:29687` with
  `ontology_mapping.ontology_id: CHEBI:29687`, label `teicoplanin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: zero CultureMech recipe occurrences and 10 MicrobeDecoder
  antibiotic-trait rows.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Teicoplanin` through `Tertiomycin_A`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:29687` as `teicoplanin`.
- The structured mapping evidence preserves the MicrobeDecoder OLS
  label-exact import for `kgmicrobe.trait:teicoplanin`, and the promotion
  history records a later `review-ingredients` approval.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Teicoplanin`, points
  at `CHEBI:29687`, names `obo:chebi.owl`, and publishes no unsafe `other`
  synonyms.

## Completeness

- The CHEBI identity, aggregate row, MicrobeDecoder source occurrence, and
  final SSSOM row agree.
- No components, roles, chemical-property fields, or environmental contexts are
  asserted.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder import,
  promotion, aggregate, final SSSOM, and generated rows.

## Recommended Edits

- None.
