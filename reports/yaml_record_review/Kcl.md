# `data/ingredients/mapped/Kcl.yaml`

## Verdict

Needs curation. The exact potassium chloride identity, CAS value, ChEBI-derived
structure, occurrence count, and mineral-source role are consistent, but final
SSSOM still exports procurement and CAS-decorated raw labels as synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Kcl.yaml`.
- Identifier and grounding: `identifier: CHEBI:32588` with
  `ontology_mapping.ontology_id: CHEBI:32588`, label `potassium chloride`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7447-40-7`, molecular formula `Cl.K`, InChI, and
  SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Kcl.yaml data/ingredients/mapped/Keratin.yaml data/ingredients/mapped/Ketomycin.yaml data/ingredients/mapped/Kf.yaml data/ingredients/mapped/Kh2po4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:32588` as active ChEBI term `potassium chloride` and
  lists `KCl`, `Kaliumchlorid`, `Kaon-Cl 10`, `Klor-con`, `Klotrix`,
  `Monopotassium chloride`, `[KCl]`, `muriate of potash`, and `sylvite` as
  same-substance aliases.
- PubChem resolves CAS RN `7447-40-7` with the same InChI and the equivalent
  formula `ClK`, supporting the stored CAS and structure fields.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kcl` to
  `CHEBI:32588`.
- Major: the final SSSOM row also exports `KCl (Fisher P 217)`,
  `KCl(CAS: 7447-40-7)`, `KCl(CAS:7447-40-7)`, and `KCl(Fisher P 217)` in
  `other`. These are CultureMech supplier/CAS payloads rather than resolving
  synonyms; final SSSOM already has the normalized `CAS:7447-40-7` token.
- The raw CultureMech role/property pseudo-synonyms are filtered out of the
  final SSSOM and do not themselves create a published synonym defect.
- `nutritional_roles.MINERAL_SOURCE` is supported by the original CultureMech
  `Mineral source` role text and the current 3958 occurrence count.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, row-review dispositions, and the
  synonym-enrichment review row; it found no hits in
  `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, formula, structure fields, aggregate
  copy, occurrence count, and mineral-source role are present and consistent.
- The record is incomplete until raw procurement and CAS-decorated labels stop
  publishing as SSSOM `other` tokens.

## Recommended Edits

- Major: remove or demote `KCl (Fisher P 217)`, `KCl(CAS: 7447-40-7)`,
  `KCl(CAS:7447-40-7)`, and `KCl(Fisher P 217)` in
  `data/ingredients/mapped/Kcl.yaml`, then regenerate the aggregate and final
  SSSOM so only real potassium chloride synonyms plus `CAS:7447-40-7` publish;
  rerun strict, term, round-trip, component, and SSSOM validation.
