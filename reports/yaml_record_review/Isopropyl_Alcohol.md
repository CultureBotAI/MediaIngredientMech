# `data/ingredients/mapped/Isopropyl_Alcohol.yaml`

## Verdict

Needs curation. The CultureMech exact propan-2-ol identity, CAS RN, structure
fields, kg-microbe synonyms, raw-role filtering, and final SSSOM row pass, but
`CARBON_SOURCE` is still only a provisional in-session LLM assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Isopropyl_Alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17824` with
  `ontology_mapping.ontology_id: CHEBI:17824`, label `propan-2-ol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `67-63-0`, formula `C3H8O`, InChI
  `InChI=1S/C3H8O/c1-3(2)4/h3-4H,1-2H3`, and SMILES `CC(C)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isopropyl_Alcohol.yaml data/ingredients/mapped/Isosafrole.yaml data/ingredients/mapped/Isovalerate.yaml data/ingredients/mapped/Isovaleric_Acid.yaml data/ingredients/mapped/Isovanillin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2110`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2110`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:17824` as the active ChEBI class `propan-2-ol`, with
  CAS xref `67-63-0`, formula `C3H8O`, the same InChI and SMILES stored on the
  record, and all exported kg-microbe labels as exact ChEBI synonyms.
- PubChem resolves CAS RN `67-63-0` to formula `C3H8O` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Isopropyl_Alcohol` to `CHEBI:17824` and exports only reviewed
  kg-microbe synonyms plus `CAS:67-63-0`.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from in-session LLM reasoning, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  claim.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, CultureMech memberships for
  the 6 current recipes, and the existing OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms,
  aggregate copy, and final SSSOM row are present and consistent.
- The record is incomplete until the carbon-source role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support isopropyl alcohol
  as a carbon source, then rerun strict, term, round-trip, id-label, component,
  and SSSOM validation.
