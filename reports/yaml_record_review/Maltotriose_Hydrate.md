# `data/ingredients/mapped/Maltotriose_Hydrate.yaml`

## Verdict

Needs curation. The CAS-primary hydrate identity and close parent mapping to
anhydrous `CHEBI:61993` are appropriate, but the final SSSOM is missing the
local exact `kgmicrobe.compound` anchor row expected for this CAS-primary
hydrate pattern.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Maltotriose_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:312693-63-3` with
  `ontology_mapping.ontology_id: CHEBI:61993`, label `maltotriose`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local subject: maltotriose hydrate, with anhydrous `CHEBI:61993` retained
  only as a close parent.
- CAS: `312693-63-3`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Maltose_2` through `Maltotriose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- LinkML term validation was skipped for this CAS-primary record because the
  subject identifier is outside the CHEBI/OBO term adapter scope.

## Evidence

- EBI OLS4 resolves `CHEBI:61993` as active anhydrous `maltotriose` with
  formula `C18H32O16`.
- A current exact EBI OLS4 search for `Maltotriose hydrate` returned no ChEBI
  hits, so the CAS-primary hydrate pattern remains appropriate.
- PubChem resolves CAS `312693-63-3` to CID 16218586 with formula
  `C18H34O17` and a one-water hydrate InChI.
- The final SSSOM has the expected close row to `CHEBI:61993` and exact row to
  `cas:312693-63-3`.
- `reports/hydrate_grounding.tsv` classifies this record as
  `CAS_MISSING_ANCHOR_ROWS`.

## Completeness

- The record has the right CAS subject and does not overclaim an exact match to
  the anhydrous ChEBI parent.
- The final SSSOM lacks the exact `kgmicrobe.compound` local registry row that
  should sit alongside the parent ChEBI row and exact CAS row for
  CAS-primary hydrate identities.
- `CARBON_SOURCE` is backed only by `COMPUTATIONAL_PREDICTION` evidence from a
  curated media-role name-pattern rule with a provisional curator note.

## Recommended Edits

- Add or regenerate the missing exact local `kgmicrobe.compound` registry
  anchor for `Maltotriose hydrate` while keeping the ChEBI relation at
  `CLOSE_MATCH`.
- Remove `CARBON_SOURCE` unless source-backed evidence can be attached.
