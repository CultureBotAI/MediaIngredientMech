# `data/ingredients/mapped/Dl-malic_Acid.yaml`

## Verdict

Needs curation. The DL-malic acid identity now exact-matches active
`CHEBI:6650` malic acid and the CAS RN and structure match ChEBI and PubChem,
but two garciniaxanthone F labels from an older wrong `CHEBI:65947` enrichment
are still curated and still published as SSSOM synonyms, and the
`ENERGY_SOURCE` role is provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-malic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:6650` with
  `ontology_mapping.ontology_id: CHEBI:6650`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 42 CultureMech source occurrences.
- Local OAK resolves `CHEBI:6650` to active `malic acid`, formula `C4H6O5`, the
  expected non-isomeric InChI and SMILES, CAS xref `6915-15-7`, and DL-malic
  acid synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27570 CHEBI:6650 CHEBI:16811 CHEBI:25351 CHEBI:57912`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:6650`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `6915-15-7` to CID 525 with formula `C4H6O5` and the
  same InChIKey as the record.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:6650` and `6915-15-7` found the active DL-malic acid
  record, the distinct malate record, expected component and membership uses,
  and the final SSSOM row.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for the garciniaxanthone labels and `CHEBI:65947` found those
  labels only in this record and generated row-review/final SSSOM rows.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row maps to
  `CHEBI:6650`, but its `other` column still includes `garciniaxanthone F` and
  the long garciniaxanthone F systematic label. They came from an unrelated
  pre-repair ChEBI target and are not malic acid synonyms.
- `nutritional_roles.CARBON_SOURCE` is source-backed by the imported
  CultureMech `Carbon Source` role text.
- Major: `nutritional_roles.ENERGY_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from `infer_energy_source` and a
  provisional curator note.

## Completeness

- CAS RN, formula, InChI, SMILES, real kg-microbe synonymy, the source-backed
  carbon-source role, and CultureMech occurrence provenance are populated.
- The raw `Role: Carbon source` strings are correctly filtered from final SSSOM
  synonym publication.
- Supplied forms, mixture components, physicochemical roles, biological roles,
  and environmental contexts are correctly empty.

## Recommended Edits

- Major: demote the garciniaxanthone F labels in
  `data/ingredients/mapped/Dl-malic_Acid.yaml` to `REJECTED_LABEL` provenance or
  remove them from active synonymy; then regenerate
  `mappings/ingredient_mappings.sssom.tsv` and synchronize
  `data/curated/mapped_ingredients.yaml`.
- Major: replace `nutritional_roles.ENERGY_SOURCE` with source-backed evidence
  scoped to DL-malic acid, or remove the role if no support is available; then
  synchronize `data/curated/mapped_ingredients.yaml`.
