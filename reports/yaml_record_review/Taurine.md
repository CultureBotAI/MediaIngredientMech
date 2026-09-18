# `data/ingredients/mapped/Taurine.yaml`

## Verdict

Pass. The CultureMech taurine record maps exactly to active `CHEBI:15891`, its
CAS and synonym fields agree with ChEBI and PubChem, its occurrence count is
refreshed, and the final SSSOM exact row publishes only valid taurine synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Taurine.yaml`.
- Identifier and grounding: `identifier: CHEBI:15891` with
  `ontology_mapping.ontology_id: CHEBI:15891`, label `taurine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `107-35-7`, formula `C2H7NO3S`, and PubChem-backed
  InChI and SMILES for taurine.
- Occurrences: 12 CultureMech recipe occurrences across 12 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Taurine` through `Tea`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:15891` as `taurine`, lists
  `cas:107-35-7` as a database cross-reference, and includes all four curated
  synonyms.
- Fresh PubChem lookup by CAS `107-35-7` resolves CID 1123, confirms the same
  `C2H7NO3S` formula and InChI, and lists CAS `107-35-7`.
- `mappings/culturemech_recipe_membership.tsv` has 12 `CHEBI:15891` rows,
  agreeing with `total_occurrences: 12` and `media_count: 12`.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Taurine`, points at
  `CHEBI:15891`, names `obo:chebi.owl`, and publishes only the curated
  same-substance names plus `CAS:107-35-7` in `other`.

## Completeness

- The CHEBI identity, CAS, structure fields, occurrence count, aggregate row,
  and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureMech import,
  synonym enrichment, occurrence refresh, aggregate, final SSSOM, generated,
  and recipe-membership rows.

## Recommended Edits

- None.
