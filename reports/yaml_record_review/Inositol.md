# `data/ingredients/mapped/Inositol.yaml`

## Verdict

Needs curation. The CultureMech exact ChEBI mapping, generic inositol
structure fields, synonym, raw-role filtering, and final SSSOM row pass, but
`VITAMIN_SOURCE` is still only a provisional name-pattern assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Inositol.yaml`.
- Identifier and grounding: `identifier: CHEBI:24848` with
  `ontology_mapping.ontology_id: CHEBI:24848`, label `inositol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, `kg_microbe_node_id: CHEBI:24848`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `87-89-8`, formula `C6H12O6`, InChI
  `InChI=1S/C6H12O6/c7-1-2(8)4(10)6(12)5(11)3(1)9/h1-12H`, and SMILES
  `OC1C(O)C(O)C(O)C(O)C1O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Indolmycin.yaml data/ingredients/mapped/Indoxyl_Acetate.yaml data/ingredients/mapped/Inosine.yaml data/ingredients/mapped/Inositol.yaml data/ingredients/mapped/Inulin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1610`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1610`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:24848` as the active ChEBI class `inositol`, defined as
  any cyclohexane-1,2,3,4,5,6-hexol, with formula `C6H12O6`, the same generic
  InChI and SMILES stored on the record, and `inositols` as an exact synonym.
- PubChem resolves CAS RN `87-89-8` to formula `C6H12O6` and the same generic
  InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Inositol` to
  `CHEBI:24848` and exports only `inositols` plus `CAS:87-89-8` in `other`;
  the raw `Role: Growth factor; Properties: ...` strings are correctly
  filtered.
- Major: `nutritional_roles.VITAMIN_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  claim.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, OAK/OLS review row marking
  this mapping `CONFIRMED`, the active `myo-Inositol` record, and the rejected
  `m-Inositol` tombstone.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, synonym, aggregate copy,
  and final SSSOM row are present and consistent.
- The record is incomplete until the vitamin-source role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.VITAMIN_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support inositol as a
  vitamin source, then rerun strict, term, round-trip, id-label, component,
  and SSSOM validation.
