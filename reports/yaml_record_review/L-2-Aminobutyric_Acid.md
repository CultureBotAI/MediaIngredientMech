# `data/ingredients/mapped/L-2-Aminobutyric_Acid.yaml`

## Verdict

Needs curation. The CAS-to-ChEBI lookup identity, ChEBI synonym, CAS value,
structure fields, and final SSSOM row are consistent, but
`AMINO_ACID_SOURCE` is only provisional ChEBI-ancestry evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/L-2-Aminobutyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:35619` with
  `ontology_mapping.ontology_id: CHEBI:35619`, label
  `L-alpha-aminobutyric acid`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `1492-24-6`, molecular formula `C4H9NO2`, InChI,
  and SMILES.

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

- EBI OLS4 resolves `CHEBI:35619` as active ChEBI term
  `L-alpha-aminobutyric acid` and lists `(2S)-2-aminobutanoic acid` as an exact
  synonym.
- PubChem resolves CAS RN `1492-24-6` with formula `C4H9NO2` and the same InChI
  as the YAML record, supporting the stored CAS and structure fields.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:L-2-Aminobutyric_Acid` to `CHEBI:35619` with
  `(2S)-2-aminobutanoic acid` and `CAS:1492-24-6` in `other`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the role claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and row-review dispositions; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, structure fields, aggregate copy, empty
  occurrence count, and final SSSOM row are present and consistent.
- The record is incomplete until the amino-acid-source role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-2-aminobutyric
  acid as an amino acid source, then rerun strict, term, round-trip, component,
  and SSSOM validation.
