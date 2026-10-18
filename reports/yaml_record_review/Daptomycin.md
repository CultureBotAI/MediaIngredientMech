# `data/ingredients/mapped/Daptomycin.yaml`

## Verdict

Needs curation. The record is an exact active ChEBI match for daptomycin, the
CAS xref and final SSSOM synonym payload pass, but the `SELECTIVE_AGENT` role
is still only a provisional computational assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Daptomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:600103` with
  `ontology_mapping.ontology_id: CHEBI:600103`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:600103` to active `daptomycin`, formula
  `C72H101N17O26`, charge `0`, InChI, SMILES, and CAS xref `103060-53-3`.
- The record's formula, InChI, and SMILES agree with the local ChEBI term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Danomycin.yaml data/ingredients/mapped/Danubomycin.yaml data/ingredients/mapped/Daptomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Danomycin.yaml data/ingredients/mapped/Danubomycin.yaml data/ingredients/mapped/Daptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed through the two ChEBI records and then failed on
  `kgmicrobe.compound:danomycin` because local registry targets hit the known
  OAK SQL label-lookup error:
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Daptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 3-file ChEBI subset after skipping the two local placeholders.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:81430 CHEBI:28197 CHEBI:600103`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:600103`.
- `curl -L ... /compound/name/103060-53-3/property/.../JSON`: PubChem
  resolved the CAS value to CID 21585658, `Daptomycin`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `CHEBI:600103`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Daptomycin` to `CHEBI:600103` with `skos:exactMatch`, canonical object
  label `daptomycin`, CHEBI object source, the ChEBI exact synonym for the full
  chemical name, and `CAS:103060-53-3` in `other`.
- The `SELECTIVE_AGENT` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note says the
  name-pattern role is provisional and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record or
  parent-mapping record for `CHEBI:600103`.
- CAS, molecular formula, InChI, SMILES, and the ChEBI exact synonym are
  populated.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- In `data/ingredients/mapped/Daptomycin.yaml`, remove the provisional
  `SELECTIVE_AGENT` role or replace its `COMPUTATIONAL_PREDICTION` evidence
  with inspected claim-level evidence for this compound.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Daptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
