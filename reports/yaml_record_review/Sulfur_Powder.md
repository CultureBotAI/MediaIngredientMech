# `data/ingredients/mapped/Sulfur_Powder.yaml`

## Verdict

Pass. This is a rejected tombstone correctly merged into the surviving
`CHEBI:33403` `Sulfur` record; its stale-looking sulfur-source history and
powder labels no longer publish as their own final SSSOM rows.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfur_Powder.yaml`.
- Identifier and grounding: `identifier: CHEBI:33403` with
  `ontology_mapping.ontology_id: CHEBI:33403`, label `elemental sulfur`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: REJECTED`, and representative `CHEBI:33403`.
- Chemical properties: empty after the sulfur-family merge.
- Occurrences: zero CultureMech recipe occurrences on this tombstone.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfur_Compounds` through `Sunflower_Oil`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:33403` with label
  `elemental sulfur`, matching the post-merge representative.
- The `fix_sulfur_family` history marks this record `REJECTED`, transfers its
  occurrences to the surviving `Sulfur` record, and records that
  `Sulfur (powder)` was only a supplied powder form of the same weighable
  elemental sulfur.
- The final SSSOM has no `MIM:Sulfur_Powder` subject row. The powder labels are
  now synonyms on the surviving `MIM:Sulfur` row, where they remain true
  surface labels for the same ingredient.

## Completeness

- The rejected status, representative pointer, zero occurrence count, and
  absence from final SSSOM agree.
- Raw role-text synonyms and the stale `SULFUR_SOURCE` facet are harmless on
  this rejected tombstone because they no longer reach the final SSSOM.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected sulfur-family merge,
  row-review, aggregate, generated docs, rejected tombstone, and surviving
  `Sulfur` SSSOM rows; no independent final SSSOM row remains for this
  subject.

## Recommended Edits

- None.
