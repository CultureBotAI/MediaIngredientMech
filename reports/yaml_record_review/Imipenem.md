# `data/ingredients/mapped/Imipenem.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, restored high-number ChEBI target,
structure fields, source-occurrence count, empty synonym export, and final
SSSOM row all describe imipenem.

## Identity

- Reviewed record: `data/ingredients/mapped/Imipenem.yaml`.
- Identifier and grounding: `identifier: CHEBI:471744` with
  `ontology_mapping.ontology_id: CHEBI:471744`, label `imipenem`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C12H17N3O4S`, InChI
  `InChI=1S/C12H17N3O4S/c1-6(16)9-7-4-8(20-3-2-14-5-13)10(12(18)19)15(7)11(9)17/h5-7,9,16H,2-4H2,1H3,(H2,13,14)(H,18,19)/t6-,7-,9-/m1/s1`,
  SMILES
  `[H]C(=N)NCCSC1=C(C(=O)O)N2C(=O)[C@]([H])([C@@H](C)O)[C@@]2([H])C1`,
  and molecular weight `299.352`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hypoxanthine.yaml data/ingredients/mapped/IPTG.yaml data/ingredients/mapped/Icosane.yaml data/ingredients/mapped/Imidazole.yaml data/ingredients/mapped/Imipenem.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 5-file CHEBI batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1530`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1530`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:471744` as the active ChEBI class `imipenem`, with
  formula `C12H17N3O4S`, the same InChI and SMILES stored on the record, and a
  CAS xref for imipenem.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Imipenem` to
  `CHEBI:471744` with empty `other`.
- The append-only history records both the false-positive high-accession
  demotion and the later restoration; the current active fields point at the
  real, resolving ChEBI term.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, molecular weight,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
