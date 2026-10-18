# `data/ingredients/mapped/Isovaleric_Acid.yaml`

## Verdict

Pass. The CultureMech exact isovaleric-acid identity, resolved CAS RN, structure
fields, CultureMech-backed carbon-source role, reviewed synonyms, and final
SSSOM row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Isovaleric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:28484` with
  `ontology_mapping.ontology_id: CHEBI:28484`, label `isovaleric acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `503-74-2`, formula `C5H10O2`, InChI
  `InChI=1S/C5H10O2/c1-4(2)3-5(6)7/h4H,3H2,1-2H3,(H,6,7)`, and SMILES
  `CC(C)CC(=O)O`.

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

- OLS4 resolves `CHEBI:28484` as the active ChEBI class `isovaleric acid`,
  with CAS xref `503-74-2`, formula `C5H10O2`, the same InChI and SMILES
  stored on the record, and all exported kg-microbe and merge-survivor labels
  as exact ChEBI synonyms.
- PubChem resolves CAS RN `503-74-2` to formula `C5H10O2` and the same InChI
  stored on the record.
- `nutritional_roles.CARBON_SOURCE` is supported by CultureMech
  `DATABASE_ENTRY` evidence with original role text `Carbon Source`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Isovaleric_Acid` to `CHEBI:28484` and exports only reviewed chemical
  synonyms plus `CAS:503-74-2`; raw CultureMech `Role:` and `Properties:` text
  is correctly filtered.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, CultureMech memberships for
  the 104 current recipes, the risky CAS RN resolution, and the already
  represented synonym-enrichment review row.

## Completeness

- The active ChEBI identifier, resolved CAS RN, formula, InChI, SMILES,
  carbon-source evidence, synonyms, aggregate copy, and final SSSOM row are
  present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
