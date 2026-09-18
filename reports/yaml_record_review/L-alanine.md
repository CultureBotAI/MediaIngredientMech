# `data/ingredients/mapped/L-alanine.yaml`

## Verdict

Pass. The CultureMech exact ChEBI identity, CAS value, PubChem structure,
claim-level nitrogen-source role, refreshed occurrence count, and final SSSOM
row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-alanine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16977` with
  `ontology_mapping.ontology_id: CHEBI:16977`, label `L-alanine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `56-41-7`, molecular formula `C3H7NO2`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-_-erythrulose.yaml data/ingredients/mapped/L-_-sorbose.yaml data/ingredients/mapped/L-alaninamide.yaml data/ingredients/mapped/L-alanine.yaml data/ingredients/mapped/L-alanine_4-nitroanilide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 ChEBI records; Engine A was
  intentionally skipped for the `kgmicrobe.compound` fallback.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:16977` as active `L-alanine` and lists the
  published ChEBI and KG-Microbe synonyms that appear in final SSSOM `other`.
- PubChem resolves CAS RN `56-41-7` to CID `5950` with formula `C3H7NO2` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16977` with the
  curated exact synonyms and `CAS:56-41-7` in `other`; raw `Cross-references:`
  and `Role:` provenance strings from CultureMech are correctly filtered out.
- `nutritional_roles.NITROGEN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech pipeline with original role text `Nitrogen Source`, matching the
  migrated role enum.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, aggregate component references, and OAK/OLS row-review
  confirmation.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, aggregate copy, 109/109
  occurrence count, nitrogen-source role, and final SSSOM row are present and
  consistent.

## Recommended Edits

- None.
