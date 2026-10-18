# `data/ingredients/mapped/Methyl-cis-p-coumarate.yaml`

## Verdict

Pass. The local cis stereochemical identity, broader ChEBI parent, rejected
target-derived synonym, and final SSSOM rows pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl-cis-p-coumarate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:methyl-cis-p-coumarate` with
  `ontology_mapping.ontology_id: CHEBI:86904`, label
  `4-coumaric acid methyl ester`, source `CHEBI`, `mapping_quality:
  NARROW_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: formula `C10H10O3`; no exact CAS or complete structure has
  been verified for the cis form.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl-alpha-D-xylopyranoside` through `Methyl-trans-p-coumarate`: exited 0
  and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local
  `kgmicrobe.compound` record because it is intentionally outside the OBO
  adapter scope.

## Evidence

- EBI OLS4 resolves `CHEBI:86904` as active `4-coumaric acid methyl ester`, a
  stereo-unspecified term for the `C10H10O3` parent.
- The #456 repair correctly moved the cis-specific subject to a local
  `kgmicrobe.compound` identifier, kept only a `skos:narrowMatch` row to the
  stereo-unspecified ChEBI parent, and marked the inherited ChEBI synonym as
  `REJECTED_LABEL`.
- A fresh exact all-ontology OLS4 search for `methyl-cis-p-coumarate` returned
  zero results.
- The final SSSOM publishes the expected `skos:narrowMatch` parent row to
  `CHEBI:86904` plus a registry `skos:exactMatch` row to
  `kgmicrobe.compound:methyl-cis-p-coumarate`; both rows have empty `other`.

## Completeness

- The record does not publish the rejected parent synonym in final SSSOM and
  does not reuse the trans-specific CAS `3943-97-3`.

## Recommended Edits

- None.
