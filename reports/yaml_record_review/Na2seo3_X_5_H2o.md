# `data/ingredients/mapped/Na2seo3_X_5_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:131361` disodium selenite
pentahydrate identity, CAS-backed structure, duplicate merges, occurrence
count, and `TRACE_ELEMENT` role pass, but final SSSOM still publishes a
malformed selenite formula and a concentration-qualified label as synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2seo3_X_5_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:131361` with
  `ontology_mapping.ontology_id: CHEBI:131361`, label
  `disodium selenite pentahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1622 CultureMech recipe occurrences across 1617 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2seo35h2o` through `Na2so3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:131361` as active
  `disodium selenite pentahydrate`; the term carries the stored formula,
  InChI, SMILES, and CAS `26970-82-1`.
- A fresh PubChem CAS lookup for `26970-82-1` resolves to sodium selenite
  pentahydrate with the same InChI as the record, so the chemical block matches
  the hydrate-specific ChEBI identity.
- The `TRACE_ELEMENT` role is supported by CultureMech `DATABASE_ENTRY`
  evidence from repeated `Mineral source` role text on this ingredient.
- Major: final SSSOM `other` publishes `Na2Se3 x 5 H2O`, which
  `mappings/hydrate_review.tsv` classifies as a malformed selenite formula that
  needs upstream source review.
- Major: final SSSOM `other` also publishes
  `Na2SeO3 x 5 H2O (0.01% w/v)`, a concentration-qualified label that should
  not be exported as an exact synonym for the pentahydrate substance.

## Completeness

- The active ChEBI term, canonical CAS RN, formula, structure, 1617/1622
  occurrence statistics, duplicate merges, role evidence, and exact final SSSOM
  row otherwise agree.
- The remaining consequential gaps are malformed or concentration-qualified
  tokens in the final synonym surface.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2seo3_X_5_H2o.yaml`, demote the malformed
  `Na2Se3 x 5 H2O` and concentration-qualified
  `Na2SeO3 x 5 H2O (0.01% w/v)` raw labels so they no longer publish as exact
  `CHEBI:131361` synonyms. Rebuild final SSSOM and rerun final SSSOM validation
  plus product label validation.
