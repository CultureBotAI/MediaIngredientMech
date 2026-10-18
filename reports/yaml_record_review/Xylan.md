# `data/ingredients/mapped/Xylan.yaml`

## Verdict

Needs curation. The exact `CHEBI:37166` xylan identity, source-backed
carbon-source role, aggregate row, and final exact SSSOM predicate pass, but
final SSSOM exports substrate- and vendor-qualified parenthetical strings as
exact `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Xylan.yaml`.
- Identifier and grounding: `identifier: CHEBI:37166` with matching
  `ontology_mapping.ontology_id`, label `xylan`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one raw CultureMech role string, two clean kg-microbe synonyms, and
  two parenthetical surface forms.
- Occurrences: 29 CultureMech recipe occurrences across 29 media.
- Role: `CARBON_SOURCE` imported from CultureMech original role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xanthocidin` through `Xylan_From_Beechwood`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the four
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:37166` returns active label `xylan`, CAS
  `9014-63-5`, and clean synonyms `(1,4-beta-D-Xylan)n+1` and `xylans`.
- The `CARBON_SOURCE` role is backed by `DATABASE_ENTRY` evidence carrying the
  original CultureMech role text `Carbon Source`.
- The final SSSOM row correctly has
  `MIM:Xylan skos:exactMatch CHEBI:37166`.
- The raw `Role:`/`Properties:` CultureMech string is filtered from final SSSOM
  `other`, as intended.

## Issues

- Major: the final exact `CHEBI:37166` row exports
  `Xylan (hemicellulose substrate)` as an `other` synonym. That parenthetical
  describes a substrate usage context, not a ChEBI synonym.
- Major: the same row exports `Xylan (Tokyo Kasei or Sigma)` as an `other`
  synonym. That label names vendor/catalog provenance and is not a synonym of
  xylan.

## Completeness

- The exact CHEBI mapping, occurrence count, source-backed carbon-source role,
  aggregate copy, and SSSOM predicate agree.
- The final synonym set needs to be restricted to true xylan labels.

## Recommended Edits

- Remove or suppress `Xylan (hemicellulose substrate)` and
  `Xylan (Tokyo Kasei or Sigma)` from final SSSOM `other`.
- Rebuild SSSOM and rerun strict validation, LinkML term validation, SSSOM
  invariant validation, and the cross-record `other` synonym audit.
