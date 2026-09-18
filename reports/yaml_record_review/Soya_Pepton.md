# `data/ingredients/mapped/Soya_Pepton.yaml`

## Verdict

Needs curation - major. This misspelled soy-peptone surface is independently
mapped to the same `FOODON:03315720` parent and carries the same 833/1089
occurrence counts as `Soy_Peptone`; it should be represented as provenance on
the canonical soy-peptone record, not as a separate active subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Soya_Pepton.yaml`.
- Identifier and grounding: `identifier: FOODON:03315720` with
  `ontology_mapping.ontology_id: FOODON:03315720`, label
  `vegetable protein, hydrolyzed`, source `FOODON`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 1089 source occurrences across 833 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sorgoleone` through `Soya_Peptone`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this FOODON-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `FOODON:03315720` with label
  `vegetable protein, hydrolyzed`.
- The curation note explicitly says `Soya pepton` is a misspelling of soy
  peptone and mirrors sibling `Soy_Peptone`.
- Major: the record duplicates the canonical soy-peptone subject instead of
  keeping the misspelled source label as an alias on `Soy_Peptone`.

## Completeness

- The close FOODON parent and undefined-mixture classification are appropriate
  for soy peptone, but this residual duplicate has no role evidence, carries no
  curated soy-peptone synonym inventory, and should not duplicate the canonical
  row's occurrence count.

## Recommended Edits

- Major: merge `data/ingredients/mapped/Soya_Pepton.yaml` into
  `data/ingredients/mapped/Soy_Peptone.yaml`, retaining `Soya pepton` as a raw
  misspelling/provenance label and dropping the extra final SSSOM subject.
