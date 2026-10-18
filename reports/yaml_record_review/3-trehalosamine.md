# `data/ingredients/mapped/3-trehalosamine.yaml`

## Verdict

Pass with minor issues, minor. The exact `CHEBI:223561` identity, ChEBI/PubChem
chemistry, microbedecoder source occurrence, SSSOM row, and aggregate row pass;
only stale import-review caveats and timestamp ordering remain.

## Identity

- Reviewed record: `data/ingredients/mapped/3-trehalosamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:223561` with
  `ontology_mapping.ontology_id: CHEBI:223561`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:223561` resolves to `3-trehalosamine`, formula
  `C12H23NO10`, net charge `0`, SMILES
  `N[C@@H]1[C@H](O)[C@@H](O[C@H]2O[C@H](CO)[C@H](O)[C@H](O)[C@H]2O)O[C@H](CO)[C@H]1O`,
  and the stored InChI.
- The direct microbedecoder `BacDive_Metabolite_production` count of 1 is
  preserved under `source_occurrences`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:3-trehalosamine` to `CHEBI:223561` row.

## Evidence

- The ChEBI identity denotes exactly the same named neutral molecule and the
  record's formula, SMILES, InChI, molecular weight, and CHEBI identifier agree.
- The older `microbedecoder_auto_mapped_review.tsv` row explicitly warned that
  its approval did not check for homonyms or wrong-sense matches. The direct
  ChEBI structure review performed here closes that gap for this record.
- Minor: the `review-ingredients` history entry has timestamp
  `2026-08-04T00:00:00+00:00`, earlier than the same-day PENDING_REVIEW event
  it resolves. This is historical ordering noise only.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, microbedecoder review row, generated
  docs, source import rows, and ignored aggregate backups.

## Completeness

- Formula, molecular weight, InChI, and SMILES are populated from ChEBI/PubChem.
- The direct microbedecoder occurrence is traceable.
- Empty `synonyms: []` is acceptable because the canonical label already names
  the exact grounded molecule and no raw dropped-locant text is needed.

## Recommended Edits

No YAML edit is required for this record. The historical timestamp ordering nit
can be left alone unless a future audit rewrites old curation-history metadata.
