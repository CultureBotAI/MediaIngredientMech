# `data/ingredients/mapped/Soy_Peptone.yaml`

## Verdict

Pass. The soy-peptone record has a close FOODON parent, curated same-product and
catalog aliases, a PMID/DOI-backed protein-source role, refreshed occurrence
counts, and a clean final SSSOM row.

## Identity

- Reviewed record: `data/ingredients/mapped/Soy_Peptone.yaml`.
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
  `vegetable protein, hydrolyzed`, matching the stored parent target.
- The curated synonyms name soy-peptone products or supplier/catalog variants
  of the same product family, and the final SSSOM `other` column keeps the
  expected same-subject aliases.
- `nutritional_roles.PROTEIN_SOURCE` was upgraded from name-pattern evidence to
  the Kwon et al. soybean-hydrolysate citation with DOI and PMID.

## Completeness

- The FOODON parent, synonym inventory, catalog variants, occurrence count,
  protein-source role, and final SSSOM row agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found on this canonical soy-peptone record.

## Recommended Edits

- None.
