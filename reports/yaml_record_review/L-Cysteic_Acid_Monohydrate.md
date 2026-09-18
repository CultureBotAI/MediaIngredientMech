# `data/ingredients/mapped/L-Cysteic_Acid_Monohydrate.yaml`

## Verdict

Needs curation. The CAS primary identity, monohydrate PubChem structure, #342
close parent mapping, exact CAS row, and hydrate review are consistent, but
final SSSOM lacks the local KG-Microbe registry anchor expected for a
CAS-primary close-match hydrate.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Cysteic_Acid_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:23537-25-9` with
  `ontology_mapping.ontology_id: CHEBI:17285`, label `L-cysteic acid`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `23537-25-9`, molecular formula `C3H9NO6S`,
  InChI, SMILES, and PubChem CID `12308854`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Carnitine.yaml data/ingredients/mapped/L-Carnitine_Hydrochloride.yaml data/ingredients/mapped/L-Cysteic_Acid_Monohydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2330`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2330`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- Exact EBI OLS4 ChEBI search for `L-Cysteic acid monohydrate` returned zero
  hits; OLS4 resolves `CHEBI:17285` as active `L-cysteic acid`, matching the
  close parent mapping.
- PubChem resolves CAS RN `23537-25-9` to CID `12308854` with formula
  `C3H9NO6S` and the same InChI as the YAML record, supporting the exact CAS
  monohydrate identity.
- `mappings/hydrate_review.tsv` records the CAS identity as hydrate-specific
  for L-cysteic acid monohydrate.
- The final SSSOM publishes the expected parent `skos:closeMatch` row to
  `CHEBI:17285`, plus the exact CAS identity row with `CAS:23537-25-9` in
  `other`.
- Major: `reports/hydrate_grounding.tsv` still reports
  `CAS_MISSING_ANCHOR_ROWS`. Final SSSOM lacks the exact `kgmicrobe.compound`
  registry sibling expected for this CAS-primary close-match hydrate.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM rows, docs projections, hydrate review rows, unknown-term triage
  rows, and the current hydrate-grounding diagnostic.

## Completeness

- The CAS primary identifier, close ChEBI parent mapping, exact CAS row,
  aggregate copy, empty occurrence count, and PubChem structure are present and
  consistent.
- The final SSSOM registry anchoring is incomplete.

## Recommended Edits

- Major: repair final SSSOM generation for this CAS-primary close-match hydrate
  so `MIM:L-Cysteic_Acid_Monohydrate` receives an exact local
  `kgmicrobe.compound:l-cysteic_acid_monohydrate` row alongside the close
  parent and exact CAS rows; rerun hydrate, round-trip, component, and SSSOM
  validation.
