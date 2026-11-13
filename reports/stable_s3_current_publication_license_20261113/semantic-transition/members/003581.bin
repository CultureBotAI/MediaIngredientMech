# `data/ingredients/mapped/Na2seo3.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:48843` disodium selenite identity,
CAS-backed structure, occurrence count, `TRACE_ELEMENT` role, and hidden-hydrate
rejections pass, but final SSSOM still publishes the garbled `Na2Se2O3` formula
as a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2seo3.yaml`.
- Identifier and grounding: `identifier: CHEBI:48843` with
  `ontology_mapping.ontology_id: CHEBI:48843`, label `disodium selenite`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 185 CultureMech recipe occurrences across 185 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2s2o3_X_5_H2o` through `Na2seo3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:48843` as active
  `disodium selenite`; its ChEBI synonyms include `Na2SeO3` and the stored
  sodium-selenite names, and its CAS xref is `10102-18-8`.
- A fresh PubChem CAS lookup for `10102-18-8` resolves to sodium selenite with
  the same formula and InChI as the record, so the #320/#334 repair correctly
  moved this anhydrous record off the pentahydrate CAS.
- The `TRACE_ELEMENT` role is supported by imported CultureMech role text
  `Mineral`; selenium is the mineral element named by this salt.
- The #251 repair correctly marked the malformed hidden-pentahydrate labels as
  `REJECTED_LABEL`, and those rejected labels do not appear in final SSSOM
  `other`.
- Major: final SSSOM still publishes `Na2Se2O3`, a garbled formula absorbed
  from `UNMAPPED_0473`, as a synonym for `CHEBI:48843`. The merge history
  describes it as a garbled spelling of `Na2SeO3`; provenance for a typo is not
  an exact synonym.

## Completeness

- The active ChEBI term, canonical CAS RN, formula, structure, 185/185
  occurrence count, trace-element role, rejected hidden-hydrate labels, and
  exact final SSSOM row otherwise agree.
- The remaining consequential gap is the malformed `Na2Se2O3` token in the
  final synonym surface.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2seo3.yaml`, demote `Na2Se2O3` from an
  active `RAW_TEXT` synonym to typo/merge provenance that does not export to
  final SSSOM. Rebuild final SSSOM and rerun final SSSOM validation plus
  product label validation.
