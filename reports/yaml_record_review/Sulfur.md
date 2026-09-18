# `data/ingredients/mapped/Sulfur.yaml`

## Verdict

Pass. The corrected `CHEBI:33403` elemental-sulfur identity, occurrence rollup,
filtered synonym payload, aggregate row, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfur.yaml`.
- Identifier and grounding: `identifier: CHEBI:33403` with
  `ontology_mapping.ontology_id: CHEBI:33403`, label `elemental sulfur`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: intentionally empty after the sulfur-family repair moved
  this ingredient away from the sulfur-atom record.
- Occurrences: 477 occurrences across 477 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfite` through `Sulfur`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:33403` with label
  `elemental sulfur`, matching the current YAML grounding.
- `fix_sulfur_family` moved this ingredient from sulfur atom to weighable
  elemental sulfur, absorbed the `Sulphur` and `Sulfur powder` duplicates, and
  retained atom-only and polysulfur-only labels as `REJECTED_LABEL` provenance.
- The final SSSOM row exact-matches `CHEBI:33403` and its `other` tokens are
  real elemental-sulfur or sulfur-powder labels for the MIM subject; the raw
  parenthetical CultureMech labels and rejected atom/polysulfur labels stay out
  of the final published synonym payload.

## Completeness

- The elemental-sulfur identity, aggregate row, occurrence count, sulfur-source
  role, environmental context entries, and final SSSOM row agree.
- The record has no components or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureMech, merge,
  repair, aggregate, generated index, rejected tombstone, and final SSSOM rows;
  the rejected `Sulphur` and `Sulfur_Powder` tombstones no longer publish
  extra final SSSOM rows.

## Recommended Edits

- None.
