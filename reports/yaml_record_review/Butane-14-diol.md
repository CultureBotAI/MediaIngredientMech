# `data/ingredients/mapped/Butane-14-diol.yaml`

## Verdict

Pass. This file is an intentional rejected duplicate tombstone for the
comma-split `Butane-1` and `4-diol` repair; the active `CHEBI:41189`
butane-1,4-diol mapping is published only through `MIM:14-Butanediol`.

## Identity

- Reviewed record: `data/ingredients/mapped/Butane-14-diol.yaml`.
- Tombstone state: `identifier: CHEBI:41189`, `preferred_term:
  Butane-1,4-diol`, `mapping_status: REJECTED`, and
  `ontology_mapping.ontology_id: CHEBI:41189`.
- Live OLS search for `Butane-1,4-diol` returns `CHEBI:41189` as the exact
  butane-1,4-diol term.
- PubChem resolves `Butane-1,4-diol` to CID 8064 with formula `C4H10O2`, the
  same standard InChI as `CHEBI:41189`, and the same compound held by the
  active `data/ingredients/mapped/14-Butanediol.yaml` record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Butan-1-amine.yaml data/ingredients/mapped/Butane-14-diol.yaml data/ingredients/mapped/Butanol.yaml data/ingredients/mapped/Butyl_Stearate.yaml data/ingredients/mapped/Butyl_Vinyl_Ether.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Butan-1-amine.yaml data/ingredients/mapped/Butane-14-diol.yaml data/ingredients/mapped/Butanol.yaml data/ingredients/mapped/Butyl_Stearate.yaml data/ingredients/mapped/Butyl_Vinyl_Ether.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder `4-diol` fragment provenance,
  the truncated-locants row for `4-diol`, the rejected aggregate copy in
  `data/curated/mapped_ingredients.yaml`, and the active exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 75 for `MIM:14-Butanediol`.
- Hidden/ignored-inclusive search over `mappings`, `data/curated`,
  `data/ingredients`, and `reports`, with the same ignored review directories
  excluded, found no live `MIM:Butane-14-diol` SSSOM row.
- The active `MIM:14-Butanediol` SSSOM row maps to `CHEBI:41189` with
  `skos:exactMatch` and carries `Butane-1` and `4-diol` in `other`, preserving
  the split-fragment provenance that this tombstone records.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The rejected duplicate keeps the repaired label, source fragments, merge
  history, target ChEBI ID, and duplicate-tombstone status needed to explain why
  the split `Butane-1` input is no longer a live ingredient.
- The live structure, CAS `110-63-4`, formula, InChI, SMILES, SSSOM row, and
  canonical occurrence count belong to `data/ingredients/mapped/14-Butanediol.yaml`.
- No roles, components, or environmental contexts are required on this
  rejected tombstone.

## Recommended Edits

- None.
