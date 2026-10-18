# `data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml`

## Verdict

Needs curation. The CAS primary identity, potassium-salt PubChem structure,
ChEBI parent mapping, registry rows, and occurrence count are consistent, but
parent L-aspartic acid synonyms publish on the salt mapping and
`AMINO_ACID_SOURCE` is only provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:1115-63-5` with
  `ontology_mapping.ontology_id: CHEBI:17053`, label `L-aspartic acid`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `1115-63-5`, molecular formula `C4H6KNO4`,
  InChI, SMILES, and PubChem CID `23672742`.

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

- Exact EBI OLS4 ChEBI search for `L-Aspartic acid potassium salt` returned zero
  hits; OLS4 resolves `CHEBI:17053` as active `L-aspartic acid`, matching the
  parent mapping.
- PubChem resolves CAS RN `1115-63-5` to CID `23672742` with formula
  `C4H6KNO4` and the same InChI as the YAML record, supporting the exact CAS
  salt identity.
- The final SSSOM publishes the expected parent `skos:narrowMatch` row to
  `CHEBI:17053`, plus exact CAS and local KG-Microbe registry identity rows.
- Major: final SSSOM `other` includes `(2S)-2-aminobutanedioic acid` and
  `ASPARTIC ACID` on the parent row. Those are synonyms of anhydrous
  L-aspartic acid, not of the potassium salt, and erase the salt boundary on a
  parent mapping.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  role claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM rows, docs projections, and row-review dispositions; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The CAS primary identifier, parent ChEBI mapping, exact CAS and local registry
  rows, aggregate copy, occurrence count, and final identity rows are present
  and consistent.
- The record is incomplete until parent-compound synonyms are removed from this
  salt record and the amino-acid-source role is either supported by inspected
  claim-level evidence or removed.

## Recommended Edits

- Major: remove or demote `(2S)-2-aminobutanedioic acid` and `ASPARTIC ACID` in
  `data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml`, then
  regenerate the aggregate and final SSSOM.
- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-aspartic acid
  potassium salt as an amino acid source.
- Rerun strict, term, round-trip, component, and SSSOM validation after those
  changes.
