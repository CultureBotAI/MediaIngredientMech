# `data/ingredients/mapped/Terpene_Hydrate.yaml`

## Verdict

Needs curation - major. The CAS identity, close parent to active
`CHEBI:134806`, aggregate row, and exact CAS registry row pass, but the record
is missing the exact `kgmicrobe.compound:terpene_hydrate` registry sibling that
the hydrate anchoring intended.

## Identity

- Reviewed record: `data/ingredients/mapped/Terpene_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:2451-01-6` with
  `ontology_mapping.ontology_id: CHEBI:134806`, label `terpin`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `2451-01-6`.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Teicoplanin` through `Tertiomycin_A`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:134806` as the anhydrous parent
  `terpin`.
- Fresh PubChem lookup by CAS `2451-01-6` resolves CID 17141, confirms formula
  `C10H22O3`, and lists CAS `2451-01-6` for terpin hydrate.
- The final SSSOM correctly publishes a `skos:closeMatch` row to
  `CHEBI:134806` and an exact CAS registry row to `cas:2451-01-6`.
- Major: `reports/hydrate_grounding.tsv` reports this record as
  `CAS_MISSING_ANCHOR_ROWS`; the curated evidence says the hydrate anchor added
  a `kgmicrobe.compound:terpene_hydrate` registry row, but the final SSSOM has
  no exact KG-Microbe sibling for `MIM:Terpene_Hydrate`.

## Completeness

- The CAS identity, CHEBI close parent, aggregate row, and final CAS row agree.
- The final product is incomplete until the exact local registry row that
  preserves the hydrated identity is present alongside the close parent.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT fallback,
  hydrate-anchor plan, hydrate-grounding report, aggregate, final SSSOM, and
  row-review rows.

## Recommended Edits

- Major: add the missing exact `kgmicrobe.compound:terpene_hydrate` registry
  sibling for `MIM:Terpene_Hydrate` through the maintained SSSOM builder or a
  targeted reconcile of the hydrate-anchor product.
- Major: regenerate `mappings/ingredient_mappings.sssom.tsv`, rerun
  `scripts/report_hydrate_grounding.py`, and confirm this row no longer reports
  `CAS_MISSING_ANCHOR_ROWS`.
