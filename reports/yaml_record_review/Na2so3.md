# `data/ingredients/mapped/Na2so3.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:86477` sodium sulfite identity,
CAS-backed structure, duplicate merge, occurrence count, `REDUCING_AGENT` role,
and final exact row pass, but the final SSSOM row still publishes a
pentahydrate label as an anhydrous-sulfite synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2so3.yaml`.
- Identifier and grounding: `identifier: CHEBI:86477` with
  `ontology_mapping.ontology_id: CHEBI:86477`, label `sodium sulfite`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 26 CultureMech recipe occurrences across 26 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2seo35h2o` through `Na2so3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:86477` as active `sodium sulfite`
  with formula `2Na.O3S`, CAS `7757-83-7`, and an InChI matching the record.
- A fresh PubChem CAS lookup for `7757-83-7` resolves to sodium sulfite with the
  same formula and InChI, so the chemical block matches the anhydrous ChEBI
  identity.
- The `REDUCING_AGENT` role is supported by CultureMech `DATABASE_ENTRY`
  evidence whose curator note preserves the original `Reducing Agent` role
  text.
- Major: final SSSOM `other` publishes `Na2SO3 x 5 H2O` on the anhydrous
  sodium sulfite row. That token names a pentahydrate surface and crosses the
  hydrate boundary.

## Completeness

- The active ChEBI term, canonical CAS RN, formula, structure, 26/26 occurrence
  count, duplicate merge, role evidence, and final exact row otherwise agree.
- The remaining consequential gap is the hydrate label in the final synonym
  surface.

## Recommended Edits

- Major: remove `Na2SO3 x 5 H2O` from the active synonym surface for
  `data/ingredients/mapped/Na2so3.yaml`; if that surface belongs to the sibling
  pentahydrate record, the fix should keep it there without exporting it back to
  the anhydrous row. Rebuild final SSSOM and rerun final SSSOM validation plus
  product label validation.
