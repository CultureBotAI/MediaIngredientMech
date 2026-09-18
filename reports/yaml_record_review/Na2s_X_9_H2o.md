# `data/ingredients/mapped/Na2s_X_9_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:76209` sodium sulfide nonahydrate
identity, hydrate-specific CAS repair, formula, structure, occurrence count,
and CultureMech-backed `REDUCING_AGENT` role pass, but final SSSOM still
publishes concentration-qualified hydrate labels as synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2s_X_9_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:76209` with
  `ontology_mapping.ontology_id: CHEBI:76209`, label
  `sodium sulfide nonahydrate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2751 CultureMech recipe occurrences across 2750 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2s2o3_X_5_H2o` through `Na2seo3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:76209` as active
  `sodium sulfide nonahydrate`, with formula `9H2O.2Na.S`, CAS `1313-84-4`,
  and an InChI matching the record.
- A fresh PubChem CAS lookup for `1313-84-4` resolves to the nonahydrate formula
  and stored InChI, confirming that the #320/#334 CAS repair moved this record
  off the anhydrous sodium sulfide CAS.
- The `REDUCING_AGENT` role is supported by CultureMech `DATABASE_ENTRY`
  evidence whose curator note preserves the original role text.
- Major: final SSSOM `other` publishes `Na2S x 9 H2O (3% w/v)` and
  `Na2S x 9 H2O(24% w/v)`. These name recipe concentrations, not just the
  nonahydrate substance identity, so they should not be exact synonyms in the
  published SSSOM.
- The old raw note `(used for reduction of the medium)` remains as
  `RAW_TEXT` in YAML but is correctly filtered from the final SSSOM.

## Completeness

- The active ChEBI term, hydrate-specific CAS RN, formula, structure, 2750/2751
  occurrence statistics, duplicate merge, role evidence, and final exact SSSOM
  row agree.
- The remaining consequential gap is the pair of concentration-qualified labels
  in the final synonym surface.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2s_X_9_H2o.yaml`, demote or reject
  `Na2S x 9 H2O (3% w/v)` and `Na2S x 9 H2O(24% w/v)` so they no longer
  publish as exact `CHEBI:76209` synonyms. Rebuild final SSSOM and rerun final
  SSSOM validation plus product label validation.
