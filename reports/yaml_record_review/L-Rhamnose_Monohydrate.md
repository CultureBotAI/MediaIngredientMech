# `data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml`

## Verdict

Needs curation. The CAS primary identity, PubChem monohydrate structure, close
ChEBI parent mapping, exact CAS row, and hydrate review are consistent, but
final SSSOM lacks the local KG-Microbe registry anchor and the carbon-source
role is only provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:10030-85-0` with
  `ontology_mapping.ontology_id: CHEBI:62345`, label `L-rhamnose`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `10030-85-0`, molecular formula `C6H14O6`,
  InChI, SMILES, and PubChem CID `20849066`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Pipecolic_Acid.yaml data/ingredients/mapped/L-Pyroglutamic_Acid.yaml data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml data/ingredients/mapped/L-Xylose.yaml data/ingredients/mapped/L-_-ergothioneine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- Exact EBI OLS4 ChEBI search for `L-Rhamnose monohydrate` returned zero hits;
  OLS4 resolves `CHEBI:62345` as active `L-rhamnose`, matching the close parent
  mapping.
- PubChem resolves CAS RN `10030-85-0` to CID `20849066` with formula
  `C6H14O6` and the same hydrate InChI as the YAML record.
- `mappings/hydrate_review.tsv` records the CAS identity as hydrate-specific
  for L-rhamnose monohydrate.
- The final SSSOM publishes the expected parent `skos:closeMatch` row to
  `CHEBI:62345`, plus the exact CAS identity row with `CAS:10030-85-0` in
  `other`.
- Major: `reports/hydrate_grounding.tsv` still reports
  `CAS_MISSING_ANCHOR_ROWS`. Final SSSOM lacks the exact
  `kgmicrobe.compound:l-rhamnose_monohydrate` registry sibling expected for
  this CAS-primary close-match hydrate.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM rows, docs
  projections, hydrate review rows, unknown-term triage rows, and the current
  hydrate-grounding diagnostic.

## Completeness

- The CAS primary identifier, close ChEBI parent mapping, exact CAS row,
  PubChem structure, hydrate review, empty occurrence count, and aggregate copy
  are present and consistent.
- The final SSSOM registry anchoring is incomplete.
- The record is incomplete until the carbon-source role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: repair final SSSOM generation for this CAS-primary close-match hydrate
  so `MIM:L-Rhamnose_Monohydrate` receives an exact local
  `kgmicrobe.compound:l-rhamnose_monohydrate` row alongside the close parent and
  exact CAS rows.
- Major: remove `nutritional_roles.CARBON_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-rhamnose
  monohydrate as a carbon source.
- Rerun strict, term, hydrate, round-trip, role, component, and SSSOM validation
  after those changes.
