# `data/ingredients/mapped/Soya_Peptone.yaml`

## Verdict

Needs curation - major. This soya-peptone spelling is independently mapped to
the same FOODON parent and occurrence counts as `Soy_Peptone`, and its
`PROTEIN_SOURCE` role is still the older provisional name-pattern assertion
rather than the source-backed role evidence now present on the canonical record.

## Identity

- Reviewed record: `data/ingredients/mapped/Soya_Peptone.yaml`.
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
- The curation note says the record mirrors sibling `Soy_Peptone` after
  replacing a CAS fallback whose PubChem structure was wrong.
- Final SSSOM publishes a duplicate exact FOODON row with `CAS:91079-46-8` as
  `other`.
- Major: this spelling should be an alias or source label on the canonical
  `Soy_Peptone` record, not a separate active subject with the same aggregate
  occurrence counts.
- Major: `nutritional_roles.PROTEIN_SOURCE` is backed only by a provisional
  name-pattern `COMPUTATIONAL_PREDICTION`, while the canonical `Soy_Peptone`
  record already has source-backed protein-role evidence.

## Completeness

- The close FOODON parent, CAS provenance, and undefined-mixture classification
  are appropriate for soya peptone, but the duplicate active row and stale role
  evidence need cleanup.

## Recommended Edits

- Major: merge `data/ingredients/mapped/Soya_Peptone.yaml` into
  `data/ingredients/mapped/Soy_Peptone.yaml`, preserving `Soya peptone` and
  `CAS:91079-46-8` as source provenance if checked.
- Major: retire this record's provisional `PROTEIN_SOURCE` role rather than
  leaving duplicate role evidence on a residual alias row.
