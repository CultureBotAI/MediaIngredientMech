# `data/ingredients/mapped/Palatinose.yaml`

## Verdict

Needs curation; major. The `CHEBI:18394` synonym mapping for Palatinose passes,
but final SSSOM `other` exports a sibling hydrate label and a truncated
parenthetical surface.

## Identity

- Reviewed record: `data/ingredients/mapped/Palatinose.yaml`.
- Identifier and grounding: `identifier: CHEBI:18394` with
  `ontology_mapping.ontology_id: CHEBI:18394`, label
  `6-O-alpha-D-glucopyranosyl-D-fructofuranose`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1 MicrobeDecoder `BacDive_Metabolite_utilization` occurrence and
  no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Palatinose` resolves `CHEBI:18394`
  `6-O-alpha-D-glucopyranosyl-D-fructofuranose`, matching the curated
  `SYNONYM_MATCH`.
- The final SSSOM row was inspected directly and maps `MIM:Palatinose` exactly
  to `CHEBI:18394`.

## Evidence

- The curated mapping note correctly records Palatinose, also known as
  isomaltulose, as a registered synonym of `CHEBI:18394`.
- The structured formula, SMILES, and InChI are for anhydrous isomaltulose and
  agree with the CHEBI mapping.
- Major: final SSSOM `other` includes `palatinose hydrate`, but hydrate status
  is material; `data/ingredients/mapped/Palatinose_Hydrate.yaml` separately
  models the hydrate as `cas:343336-76-5` with a `skos:closeMatch` parent edge
  to this anhydrous CHEBI term.
- Major: final SSSOM `other` also includes
  `Palatinose (6-O-alpha-D-glucopyranosyl-D-fruc`, which is a truncated
  parenthetical token backfilled from a generated SSSOM surface rather than a
  real resolving synonym.

## Completeness

- The CHEBI synonym mapping is complete enough for the anhydrous Palatinose
  record.
- The exported synonym set is not complete enough because one token crosses the
  hydrate boundary and one token is malformed.

## Recommended Edits

- Major: in `data/ingredients/mapped/Palatinose.yaml`, remove or retype the
  `Palatinose (6-O-alpha-D-glucopyranosyl-D-fruc` backfilled synonym so it no
  longer appears in final SSSOM `other`, and keep `palatinose hydrate` only on
  the separate hydrate record. Rebuild `mappings/ingredient_mappings.sssom.tsv`
  and rerun `scripts/validate_sssom_invariants.py` to prove
  `MIM:Palatinose` exports only true same-form synonyms.
