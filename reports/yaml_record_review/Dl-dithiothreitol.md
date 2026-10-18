# `data/ingredients/mapped/Dl-dithiothreitol.yaml`

## Verdict

Needs curation. The record now points at active `CHEBI:18320`
1,4-dithiothreitol, whose CAS RN and generic structure match the record, but
the final SSSOM row still publishes L-dithiothreitol labels from sibling
`CHEBI:42106` and a concentration-bearing CultureMech surface as synonyms, and
the `REDUCING_AGENT` role is still only a provisional name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-dithiothreitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:18320` with
  `ontology_mapping.ontology_id: CHEBI:18320`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 121 CultureMech source
  occurrences.
- Local OAK resolves `CHEBI:18320` to active `1,4-dithiothreitol`, formula
  `C4H10O2S2`, CAS xref `3483-12-3`, the expected non-isomeric InChI and
  SMILES, and DL/threo/racemic DTT synonyms including `rac-Dithiothreitol`.
- Local OAK resolves `CHEBI:42106` to the stereospecific sibling
  `L-1,4-dithiothreitol`, with the same formula but a stereospecific InChIKey
  and exact synonym for the 2R,3R isomer.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16494 CHEBI:22660 CHEBI:17126 CHEBI:18320 CHEBI:42106 CHEBI:30314 CHEBI:43796`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:18320` and
  `CHEBI:42106`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- CAS `3483-12-3` resolves in PubChem to the L-DTT stereospecific CID, which
  shares the `C4H10O2S2` formula but has the stereospecific `CHEBI:42106`
  InChIKey rather than the non-isomeric `CHEBI:18320` key.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:42106`, L-DTT labels, `Dithiothreitol (0.25 M)`, and
  the bare 100 mM solution label found the stale `CHEBI:42106` row review, the
  stale residual triage row for the 0.25 M CultureMech surface, the active DTT
  YAML, and the final SSSOM row.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row maps to
  `CHEBI:18320`, but its `other` column also includes the 2R,3R isomer labels
  and L-DTT labels curated from the older `CHEBI:42106` SSSOM payload. Those
  labels are not synonyms for the broader `CHEBI:18320` subject.
- Major: the final SSSOM `other` column includes
  `Dithiothreitol (0.25 M)`, which is a concentration-bearing CultureMech
  surface and not a same-substance synonym.
- Major: `physicochemical_roles.REDUCING_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists` and a
  provisional curator note. It is not source-backed.

## Completeness

- Formula, InChI, SMILES, the resolved CAS RN, generic/racemic kg-microbe
  synonymy, and occurrence provenance are populated.
- The bare `(100 mM solution)` raw synonym is correctly filtered from final
  SSSOM publication; the non-bare `Dithiothreitol (0.25 M)` surface is not.
- Supplied forms, mixture components, nutritional roles, biological roles, and
  environmental contexts are correctly empty.

## Recommended Edits

- Major: demote the L-DTT and 2R,3R-only labels in
  `data/ingredients/mapped/Dl-dithiothreitol.yaml` to `REJECTED_LABEL` or move
  them into provenance so a rebuild of `mappings/ingredient_mappings.sssom.tsv`
  stops publishing them as synonyms for `CHEBI:18320`; then synchronize
  `data/curated/mapped_ingredients.yaml`.
- Major: demote `Dithiothreitol (0.25 M)` to provenance rather than a resolving
  synonym; then regenerate `mappings/ingredient_mappings.sssom.tsv`.
- Major: replace the `REDUCING_AGENT` computational role with source-backed
  evidence scoped to dithiothreitol, or remove the role if no support is
  available; then synchronize `data/curated/mapped_ingredients.yaml`.
