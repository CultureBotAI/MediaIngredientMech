# `data/ingredients/mapped/Thiamine-hcl_X_2_H2o.yaml`

## Verdict

Needs curation. The exact CHEBI hydrate identity, hydrate synonyms,
occurrence counts, aggregate row, and final SSSOM structure pass, but CAS
`13465-05-9` resolves to hydrochloric acid dihydrate rather than thiamine
hydrochloride dihydrate and must not be exported as this record's CAS.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiamine-hcl_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:132751` with the same
  `ontology_mapping.ontology_id`, label `thiamine hydrochloride dihydrate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: hydrate-specific HCl and systematic ChEBI labels, plus two
  CultureMech middle-dot hydrate aliases.
- Chemical properties: formula `C12H18N4OS.2Cl.2H2O`, InChI, and SMILES match
  the ChEBI hydrate, but `cas_rn: 13465-05-9` is unsupported.
- Occurrences: 441 CultureMech recipe occurrences in 441 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine-hcl_X_2_H2o` through `Thiamine_monophosphate`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset
  from this batch: `Thiamine-hcl_X_2_H2o`, `Thiamine`, `Thiamine_Hcl`, and
  `Thiamine_monophosphate` all passed. The local `Thiamine_Vitamin_Solution`
  row was skipped because its exact `kgmicrobe.ingredient` ID and close `MICRO`
  parent are outside the CHEBI-focused term-validator subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:132751` with canonical label
  `thiamine hydrochloride dihydrate` and exact systematic synonyms that retain
  the dihydrate identity.
- The CultureMech `VITAMIN_SOURCE` role is source-backed by the original
  `DATABASE_ENTRY` role text `Vitamin`.
- Fresh PubChem lookup by CAS `13465-05-9` resolves CID 21899424, formula
  `ClH5O2`, and InChI `InChI=1S/ClH.2H2O/...`, which denotes hydrochloric acid
  dihydrate rather than thiamine hydrochloride dihydrate.
- The final SSSOM has exactly one exact row for `MIM:Thiamine-hcl_X_2_H2o`,
  points at `CHEBI:132751`, keeps the reviewed
  `OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07` validation token, and publishes
  hydrate-specific synonyms; however, it also publishes the wrong
  `CAS:13465-05-9` token in `other`.

## Completeness

- The exact CHEBI hydrate identity, occurrence count, hydrate synonyms,
  aggregate copy, and final SSSOM row shape agree.
- No components or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import, alias
  backfill, OAK/OLS row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- Major: in `data/ingredients/mapped/Thiamine-hcl_X_2_H2o.yaml`, remove
  `chemical_properties.cas_rn: 13465-05-9` or replace it with an inspected
  source-verified CAS for thiamine hydrochloride dihydrate. Then rerun strict
  validation, SSSOM publication, row review for the corrected CAS payload, and
  `scripts/validate_sssom_invariants.py`.
