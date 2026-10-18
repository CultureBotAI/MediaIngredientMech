# `data/ingredients/mapped/L-Carnitine.yaml`

## Verdict

Needs curation. The stereospecific regrounding to active ChEBI `(R)-carnitine`
and final SSSOM row are correct, but the InChI and SMILES still describe the
old achiral parent, `VITAMIN_SOURCE` is only provisional ChEBI-ancestry
evidence, and the notes still claim no ChEBI mapping existed.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Carnitine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16347` with
  `ontology_mapping.ontology_id: CHEBI:16347`, label `(R)-carnitine`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C7H15NO3` with stale achiral InChI
  and SMILES.

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

- EBI OLS4 resolves `CHEBI:16347` as active ChEBI term `(R)-carnitine` and lists
  `L-Carnitine` and `(3R)-3-hydroxy-4-(trimethylammonio)butanoate` as synonyms,
  supporting the `fix_stereoisomer_remaps` identity repair.
- Major: the ChEBI term's InChI and SMILES include stereochemical layers
  `/t6-/m1/s1` and `C[C@H](O)`, while the YAML still stores the achiral
  pre-repair structure backfilled from `CHEBI:17126`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:L-Carnitine` to
  `CHEBI:16347` with only the ChEBI exact IUPAC synonym in `other`.
- Major: `nutritional_roles.VITAMIN_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the role claim.
- Minor: `notes` still carries the original text saying no CHEBI mapping was
  available and curator review was needed.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and row-review dispositions; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The active ChEBI identity, aggregate copy, occurrence count, and final SSSOM
  row are present and consistent.
- The chemical structure block is incomplete until InChI and SMILES are
  regenerated for `CHEBI:16347`.
- The record is incomplete until the vitamin-source role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: update `chemical_properties.inchi` and `chemical_properties.smiles` in
  `data/ingredients/mapped/L-Carnitine.yaml` from `CHEBI:16347`, not the old
  achiral parent.
- Major: remove `nutritional_roles.VITAMIN_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-carnitine as a
  vitamin source.
- Minor: refresh the stale `notes`.
- Rerun strict, term, round-trip, component, and SSSOM validation after those
  changes.
