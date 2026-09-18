# `data/ingredients/mapped/Tetracycline.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:27902` identity, structure fields,
Achromycin trade-name synonym, occurrence count, aggregate row, and final SSSOM
row pass, but `SELECTIVE_AGENT` is still only a provisional name-pattern role.

## Identity

- Reviewed record: `data/ingredients/mapped/Tetracycline.yaml`.
- Identifier and grounding: `identifier: CHEBI:27902` with
  `ontology_mapping.ontology_id: CHEBI:27902`, label `tetracycline`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C22H24N2O8` with a ChEBI-backed InChI and
  SMILES.
- Occurrences: 3 CultureMech recipe occurrences across 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetracycline` through `Tetramethyl_Ammonium_Chloride`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:27902` as `tetracycline` and
  includes both the curated IUPAC name and the `Achromycin` trade name on that
  term.
- `mappings/culturemech_recipe_membership.tsv` has three `CHEBI:27902` rows,
  agreeing with `total_occurrences: 3` and `media_count: 3`.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Tetracycline`,
  points at `CHEBI:27902`, names `obo:chebi.owl`, and publishes only the IUPAC
  synonym plus `Achromycin` in `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` cites only
  `reference_type: COMPUTATIONAL_PREDICTION` from a curated name pattern and
  explicitly notes that review is recommended.

## Completeness

- The CHEBI identity, structure fields, occurrence count, aggregate row, and
  final SSSOM row agree.
- The selective-agent role is incomplete until it is replaced with
  source-backed evidence for tetracycline as a selective agent or removed.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT import,
  Achromycin merge, occurrence refresh, aggregate, final SSSOM, row-review, and
  recipe-membership rows.

## Recommended Edits

- Major: replace the provisional name-pattern `SELECTIVE_AGENT` role in
  `data/ingredients/mapped/Tetracycline.yaml` with source-backed evidence for
  tetracycline as a selective agent, or remove the role if no maintained source
  supports it.
- Major: after any role edit, synchronize `data/curated/mapped_ingredients.yaml`
  and regenerate generated products so the role facets match the per-record
  YAML.
