# `data/ingredients/mapped/Isobutyric_Acid.yaml`

## Verdict

Pass. The CultureMech exact ChEBI identity, CAS RN, structure fields,
CultureMech-backed carbon-source role, kg-microbe and ChEBI synonyms, and final
SSSOM row all describe isobutyric acid.

## Identity

- Reviewed record: `data/ingredients/mapped/Isobutyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16135` with
  `ontology_mapping.ontology_id: CHEBI:16135`, label `isobutyric acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `79-31-2`, formula `C4H8O2`, InChI
  `InChI=1S/C4H8O2/c1-3(2)4(5)6/h3H,1-2H3,(H,5,6)`, and SMILES
  `CC(C)C(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isobutyrate.yaml data/ingredients/mapped/Isobutyric_Acid.yaml data/ingredients/mapped/Isocaproate.yaml data/ingredients/mapped/Isocitrate.yaml data/ingredients/mapped/Isoliquiritigenin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2050`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2050`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:16135` as the active ChEBI class `isobutyric acid`, with
  CAS xref `79-31-2`, formula `C4H8O2`, the same InChI and SMILES stored on
  the record, and all exported kg-microbe and ChEBI synonyms as exact ChEBI
  synonyms.
- PubChem resolves CAS RN `79-31-2` to formula `C4H8O2` and the same InChI
  stored on the record.
- `nutritional_roles.CARBON_SOURCE` is supported by CultureMech
  `DATABASE_ENTRY` evidence with original role text `Carbon Source`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Isobutyric_Acid` to `CHEBI:16135` and exports only reviewed chemical
  synonyms plus `CAS:79-31-2`; raw CultureMech `Role:` and `Properties:` text
  is correctly filtered.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, occurrence memberships for
  the 116 current recipes, and existing OAK/OLS-confirmed review row.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, carbon-source
  evidence, synonyms, aggregate copy, and final SSSOM row are present and
  consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
