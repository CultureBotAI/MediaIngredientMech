# `data/ingredients/mapped/Na2seo4.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:77775` sodium selenate identity,
CAS-backed structure, occurrence count, `TRACE_ELEMENT` role, and hidden-hydrate
rejection pass, but stale triisocyanate aliases from the old unrelated ChEBI
mapping still publish in final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2seo4.yaml`.
- Identifier and grounding: `identifier: CHEBI:77775` with
  `ontology_mapping.ontology_id: CHEBI:77775`, label `sodium selenate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 297 CultureMech recipe occurrences across 297 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2seo35h2o` through `Na2so3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:77775` as active `sodium selenate`
  with formula `2Na.O4Se`, CAS `13410-01-0`, and an InChI matching the record.
- A fresh PubChem CAS lookup for `13410-01-0` resolves to sodium selenate with
  the same formula and InChI, confirming the CAS-backed structure.
- The 2026-04-18 `cbclaw_kg_microbe_sweep` history correctly states that the
  old `CHEBI:59160` triisocyanate target was unrelated and remapped this record
  to sodium selenate.
- The `TRACE_ELEMENT` role is supported by imported CultureMech `Mineral` role
  text; selenium is the mineral element named by this salt.
- Major: the old triisocyanate labels remained active after the remap and still
  publish in final SSSOM `other`, even though they name the unrelated old
  `CHEBI:59160` target.
- The #251 repair correctly marked the hidden decahydrate label as
  `REJECTED_LABEL`, and that rejected label is filtered from final SSSOM.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 297/297 occurrence count,
  trace-element role, rejected decahydrate label, and exact final SSSOM row
  otherwise agree.
- The remaining consequential gap is stale unrelated triisocyanate content in
  the final synonym surface.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2seo4.yaml`, reject or delete the
  `triisocyanate` and `triisocyanates` synonyms inherited from the old
  `CHEBI:59160` mapping. Rebuild final SSSOM and rerun final SSSOM validation
  plus product label validation.
