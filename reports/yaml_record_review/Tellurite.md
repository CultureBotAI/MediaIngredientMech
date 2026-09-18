# `data/ingredients/mapped/Tellurite.yaml`

## Verdict

Pass. The generic MicrobeDecoder surface `Tellurite` maps exactly to active
`CHEBI:30477`, the structure fields describe the tellurite dianion, and the
final SSSOM has a single clean exact CHEBI row.

## Identity

- Reviewed record: `data/ingredients/mapped/Tellurite.yaml`.
- Identifier and grounding: `identifier: CHEBI:30477` with
  `ontology_mapping.ontology_id: CHEBI:30477`, label `tellurite`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `O3Te`, ChEBI/PubChem InChI and SMILES, and
  molecular weight `175.597`.
- Occurrences: zero CultureMech recipe occurrences and 1 MicrobeDecoder
  metabolite-utilization row.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Teicoplanin` through `Tertiomycin_A`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:30477` as `tellurite`.
- The structured mapping evidence preserves the MicrobeDecoder OLS
  label-exact import for `kgmicrobe.trait:tellurite`, and the promotion history
  records a later `review-ingredients` approval.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Tellurite`, points
  at `CHEBI:30477`, names `obo:chebi.owl`, and publishes no unsafe `other`
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
