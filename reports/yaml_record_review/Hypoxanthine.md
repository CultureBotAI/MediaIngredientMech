# `data/ingredients/mapped/Hypoxanthine.yaml`

## Verdict

Pass. The CultureMech exact ChEBI mapping, structure fields, kg-microbe
synonyms, CAS alias, raw-cross-reference filtering, and final SSSOM row all
describe hypoxanthine.

## Identity

- Reviewed record: `data/ingredients/mapped/Hypoxanthine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17368` with
  `ontology_mapping.ontology_id: CHEBI:17368`, label `hypoxanthine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `68-94-0`, formula `C5H4N4O`, InChI
  `InChI=1S/C5H4N4O/c10-5-3-4(7-1-6-3)8-2-9-5/h1-2H,(H2,6,7,8,9,10)`,
  and SMILES `O=c1ncnc2ncnc12`.

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

- OLS4 resolves `CHEBI:17368` as the active ChEBI class `hypoxanthine`,
  with formula `C5H4N4O`, the same InChI and SMILES stored on the record, CAS
  xref `68-94-0`, and the six kg-microbe synonyms listed as ChEBI synonyms.
- PubChem resolves CAS RN `68-94-0` to formula `C5H4N4O` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hypoxanthine` to `CHEBI:17368` and exports only the six inspected
  kg-microbe synonyms plus `CAS:68-94-0` in `other`.
- The raw `Cross-references: KEGG:hxan` synonym is correctly filtered from
  the final SSSOM `other` field.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
