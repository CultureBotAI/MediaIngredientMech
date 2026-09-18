# `data/ingredients/mapped/Indole_3-acetic_Acid_Sodium_Salt.yaml`

## Verdict

Pass. The CAS-specific sodium-salt record, narrow active ChEBI parent row,
CAS and local registry rows, PubChem structure fields, ChEBI synonym, and final
SSSOM rows are consistent.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Indole_3-acetic_Acid_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:6505-45-9` with
  `ontology_mapping.ontology_id: CHEBI:230840`, label
  `Indole-3-acetic acid sodium salt`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `6505-45-9`, PubChem CID `23677501`, formula
  `C10H8NNaO2`, InChI
  `InChI=1S/C10H9NO2.Na/c12-10(13)5-7-6-11-9-4-2-1-3-8(7)9;/h1-4,6,11H,5H2,(H,12,13);/q;+1/p-1`,
  and SMILES `C1=CC=C2C(=C1)C(=CN2)CC(=O)[O-].[Na+]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Indole-3-propionic_Acid.yaml data/ingredients/mapped/Indole-3-pyruvic_Acid.yaml data/ingredients/mapped/Indole.yaml data/ingredients/mapped/Indole_3-acetic_Acid_Sodium_Salt.yaml data/ingredients/mapped/Indolicidin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI/OBO-compatible
  records; `Indole-3-pyruvic_Acid` was outside adapter scope because its
  primary identifier is a CAS registry CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1555`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1555`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:230840` as active
  `Indole-3-acetic acid sodium salt`, with formula `C10H8NO2.Na`,
  the same InChI and equivalent SMILES stored on the record, and
  `sodium;2-(1H-indol-3-yl)acetate` as an exact synonym.
- PubChem resolves CAS RN `6505-45-9` to CID `23677501`, formula
  `C10H8NNaO2`, and the same InChI stored on the record.
- The final SSSOM publishes the reviewed `skos:narrowMatch` from
  `MIM:Indole_3-acetic_Acid_Sodium_Salt` to `CHEBI:230840`, preserves exact
  CAS and `kgmicrobe.compound` registry rows, and exports only the inspected
  ChEBI synonym plus `CAS:6505-45-9`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, all final SSSOM rows, docs projections, already-represented
  synonym-enrichment review, and expected registry-identifier triage rows.

## Completeness

- The CAS primary identifier, active ChEBI parent, CAS RN, PubChem CID,
  formula, InChI, SMILES, aggregate copy, and final SSSOM rows are present and
  consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
