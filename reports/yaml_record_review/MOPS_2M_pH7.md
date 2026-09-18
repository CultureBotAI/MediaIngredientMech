# `data/ingredients/mapped/MOPS_2M_pH7.yaml`

## Verdict

Pass. The local MOPS buffer-stock identity, narrow CHEBI:39074 parent mapping,
exact local registry rows, CultureBotHT occurrence count, aggregate copy, and
final SSSOM rows are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/MOPS_2M_pH7.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:mops_2m_ph7` with
  `ontology_mapping.ontology_id: CHEBI:39074`, label `MOPS`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Solution type: `BUFFER_SOLUTION`.
- Occurrences: 24 total occurrences in 24 CultureBotHT media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `MH_agar` through `Macro_Component_1_For_J_Medium`: exited 0 and wrote zero
  ERROR rows.
- Local `kgmicrobe.ingredient` identifiers are outside the CHEBI/OBO
  `linkml-term-validator` adapter scope; EBI OLS4 was used for the CHEBI parent
  label check instead.

## Evidence

- EBI OLS4 resolves `CHEBI:39074` as active `MOPS`.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `CHEBI:39074` and exact registry rows to
  `kgmicrobe.ingredient:mops_2m_ph7` and `kgmicrobe.compound:mops_2m_ph7`.
- The raw `MOPS_2M_pH7` synonym is not exported into the final SSSOM `other`
  payload.

## Completeness

- The buffer-stock local identity, CHEBI parent, occurrence count, aggregate
  copy, and three final SSSOM rows are present and consistent.
- No nutritional, physicochemical, cellular, or environmental role is asserted.

## Recommended Edits

- None.
