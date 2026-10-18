# `data/ingredients/mapped/Kijanimicin.yaml`

## Verdict

Needs curation. The exact ChEBI kijanimicin identity, ChEBI structure fields,
and IUPAC synonym are consistent, but final SSSOM exports a process-qualified
`produces:` token as a synonym and `SELECTIVE_AGENT` is only provisional
name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Kijanimicin.yaml`.
- Identifier and grounding: `identifier: CHEBI:220048` with
  `ontology_mapping.ontology_id: CHEBI:220048`, label `Kijanimicin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C67H100N2O24`, InChI, and SMILES from
  the ChEBI enrichment pass.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Khco3.yaml data/ingredients/mapped/Ki.yaml data/ingredients/mapped/Kijanimicin.yaml data/ingredients/mapped/Kno2.yaml data/ingredients/mapped/Kno3.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2300`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2300`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:220048` as active ChEBI term `Kijanimicin` with the
  same formula, InChI, and SMILES as the YAML `chemical_properties`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kijanimicin` to
  `CHEBI:220048`.
- Major: final SSSOM `other` includes `produces: kijanimicin`, a process
  payload recovered from historical SSSOM rather than a real synonym for the
  compound.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected kg-microbe, CultureMech, FEBA, Hans80, or literature evidence
  attached to the claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and row-review dispositions; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, structure fields, aggregate copy, empty occurrence
  count, and final SSSOM identity row are present and consistent.
- The record is incomplete until the process-qualified synonym is removed and
  the selective-agent role is either supported by inspected claim-level evidence
  or removed.

## Recommended Edits

- Major: remove or demote `produces: kijanimicin` in
  `data/ingredients/mapped/Kijanimicin.yaml`, then regenerate the aggregate and
  final SSSOM so it disappears from `mappings/ingredient_mappings.sssom.tsv`.
- Major: remove `physicochemical_roles.SELECTIVE_AGENT` unless an inspected
  kg-microbe, CultureMech, FEBA, Hans80, or literature source can support
  kijanimicin as a selective agent.
- Rerun strict, term, round-trip, component, and SSSOM validation after those
  changes.
