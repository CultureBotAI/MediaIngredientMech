# `data/ingredients/mapped/L-Asparagine_Monohydrate.yaml`

## Verdict

Needs curation. The CAS primary identity, hydrate-specific PubChem structure,
NCIT parent mapping, registry identity rows, and hydrate review are consistent,
but `AMINO_ACID_SOURCE` is only provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Asparagine_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:5794-13-8` with
  `ontology_mapping.ontology_id: NCIT:C87433`, label
  `Asparagine Monohydrate`, source `NCIT`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `5794-13-8`, molecular formula `C4H10N2O4`, InChI,
  SMILES, and PubChem CID `170358`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Koh.yaml data/ingredients/mapped/Kscn.yaml data/ingredients/mapped/L-2-Aminobutyric_Acid.yaml data/ingredients/mapped/L-Arabinose.yaml data/ingredients/mapped/L-Asparagine_Monohydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2315`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2315`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- Exact EBI OLS4 ChEBI search for `L-Asparagine monohydrate` returned zero
  hits, while OLS4 resolves `NCIT:C87433` as active `Asparagine Monohydrate`
  with `L-Asparagine Monohydrate` as an exact synonym.
- PubChem resolves CAS RN `5794-13-8` to CID `170358` with formula
  `C4H10N2O4` and the same InChI as the YAML record, supporting the exact CAS
  hydrate identity.
- `reports/hydrate_grounding.tsv` records `cas:5794-13-8` as
  `OK_OWN_CAS_ID`, and `mappings/hydrate_review.tsv` records the CAS identity
  as hydrate-specific for L-asparagine monohydrate.
- The final SSSOM publishes the expected parent `skos:narrowMatch` row to
  `NCIT:C87433`, plus exact CAS and local KG-Microbe registry identity rows.
- The `UNKNOWN_TERM` OAK/OLS row for the NCIT parent is already triaged as
  `missing_prefix_validator_coverage_issue`; the CAS and KG-Microbe registry
  rows are expected non-ontology identifiers.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  role claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM rows, docs projections, hydrate review rows, unknown-term triage
  rows, and no same-prefix kg-microbe-node drift.

## Completeness

- The CAS primary identifier, hydrate-specific structure, parent NCIT mapping,
  exact CAS and local registry rows, aggregate copy, empty occurrence count, and
  final SSSOM rows are present and consistent.
- The record is incomplete until the amino-acid-source role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-asparagine
  monohydrate as an amino acid source, then rerun strict, term, round-trip,
  component, and SSSOM validation.
