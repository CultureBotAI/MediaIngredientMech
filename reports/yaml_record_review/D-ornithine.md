# `data/ingredients/mapped/D-ornithine.yaml`

## Verdict

Needs curation. The `CHEBI:16176` D-ornithine identity and BacDive source count
pass, but the final SSSOM row exports `(+)-l-ornithine`, which resolves toward
L-ornithine rather than D-ornithine.

## Identity

- Reviewed record: `data/ingredients/mapped/D-ornithine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16176` with
  `ontology_mapping.ontology_id: CHEBI:16176`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:16176` to active `D-ornithine` with formula
  `C5H12N2O2`, charge `0`, InChI, SMILES, CAS `348-66-3`, and exact
  D-ornithine synonyms.
- The MicrobeDecoder source label is exactly `D-ornithine`, so the core
  lexical match preserves D stereochemistry.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-ornithine.yaml data/ingredients/mapped/D-psicose.yaml data/ingredients/mapped/D-rhamnose.yaml data/ingredients/mapped/D-sorbitol.yaml data/ingredients/mapped/D-sorbose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-ornithine.yaml data/ingredients/mapped/D-psicose.yaml data/ingredients/mapped/D-rhamnose.yaml data/ingredients/mapped/D-sorbitol.yaml data/ingredients/mapped/D-sorbose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16176 CHEBI:27605 CHEBI:63150 CHEBI:17924 CHEBI:17317`:
  returned formula, charge, CAS, InChI, SMILES, mass, synonyms, and xrefs for
  `CHEBI:16176`.
- `curl -L ... q=%28%2B%29-l-ornithine&ontology=chebi&exact=true`: found
  `L-ornithine` among the live OLS hits and did not return `CHEBI:16176`.
- `curl -L ... /compound/name/%28%2B%29-l-ornithine/property/.../JSON`:
  PubChem reported `No CID found`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `D-ornithine` label with 1 BacDive utilization mention, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:16176`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-ornithine` to `CHEBI:16176` with `skos:exactMatch` and canonical
  object label `D-ornithine`, but its `other` column contains
  `(+)-l-ornithine`.
- `(+)-l-ornithine` is not a same-subject D-ornithine synonym. Local OAK has no
  such synonym on `CHEBI:16176`, live OLS exact search points at L-ornithine,
  and PubChem does not resolve the backfilled raw token.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:16176`.
- The chemical-property block is complete for the active ChEBI small molecule.
- The record does not assert nutritional roles, environmental contexts, or
  mixture components, so there are no unsupported claim-specific evidence
  objects besides the synonym backfill.

## Recommended Edits

- In `data/ingredients/mapped/D-ornithine.yaml`, remove
  `(+)-l-ornithine` from the active synonym list or convert it into rejected
  provenance so the SSSOM builder drops it from `other`.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-ornithine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
