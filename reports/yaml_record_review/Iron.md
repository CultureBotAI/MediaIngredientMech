# `data/ingredients/mapped/Iron.yaml`

## Verdict

Pass. The `#631` repair moved the record from the ChEBI iron atom to weighable
iron(0), merged the `Iron powder` occurrences, retained atom-only kg-microbe
aliases as rejected labels, and left the CultureMech mineral role and final
SSSOM row consistent with the repaired identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Iron.yaml`.
- Identifier and grounding: `identifier: CHEBI:82664` with
  `ontology_mapping.ontology_id: CHEBI:82664`, label `iron(0)`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7439-89-6`, formula `Fe`, InChI
  `InChI=1S/Fe`, and SMILES `[Fe]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Iodide.yaml data/ingredients/mapped/Iodonitrotetrazolium_Chloride.yaml data/ingredients/mapped/Irgasan.yaml data/ingredients/mapped/Irigenin.yaml data/ingredients/mapped/Iron.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1620`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1620`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:82664` as the active ChEBI class `iron(0)`, with CAS
  xref `7439-89-6`, formula `Fe`, and the same InChI and SMILES stored on the
  record.
- PubChem resolves CAS RN `7439-89-6` to formula `Fe` and the same InChI
  stored on the record.
- The atom-only kg-microbe aliases `26Fe`, `Eisen`, `fer`, `ferrum`, `hierro`,
  and `iron atom` are retained only as `REJECTED_LABEL` synonyms and are not
  exported.
- The `IRON_SOURCE` role is backed by CultureMech `DATABASE_ENTRY` evidence
  with original role text `Mineral`, matching the imported CultureMech claim.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Iron` to
  `CHEBI:82664` and exports only reviewed iron(0) aliases plus `CAS:7439-89-6`;
  the comment records the correction from iron atom to weighable iron(0).
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, the rejected merged `Iron powder` tombstone, the final SSSOM
  row, docs projections, and stale pre-`#631` OLS review rows that no longer
  match the current YAML/SSSOM identity.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, CultureMech role
  evidence, merged source occurrences, aggregate copy, and final SSSOM row are
  present and consistent.
- No atom-only rejected label leaks into the final SSSOM `other` field.

## Recommended Edits

- None.
