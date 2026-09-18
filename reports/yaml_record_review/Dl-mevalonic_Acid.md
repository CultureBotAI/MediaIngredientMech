# `data/ingredients/mapped/Dl-mevalonic_Acid.yaml`

## Verdict

Needs curation. The record was correctly remapped from unrelated
`CHEBI:150970` to active racemic `CHEBI:25351` mevalonic acid and the CAS RN
matches PubChem, but an old complex-polysaccharide systematic label is still
curated and still published as an SSSOM synonym, and the carbon-source role is
provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-mevalonic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:25351` with
  `ontology_mapping.ontology_id: CHEBI:25351`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 6 CultureMech source occurrences.
- Local OAK resolves `CHEBI:25351` to active `mevalonic acid`, a racemate of
  the R and S forms with formula `C6H12O4`, CAS xref `150-97-0`, and exact
  synonym `rac-3,5-dihydroxy-3-methylpentanoic acid`.
- The current ChEBI term does not carry InChI or SMILES, so the record's
  formula-only `chemical_properties` payload is expected.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27570 CHEBI:6650 CHEBI:16811 CHEBI:25351 CHEBI:57912`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref, formula,
  charge, and mass for `CHEBI:25351`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `150-97-0` to CID 449 with formula `C6H12O4` and the
  non-isomeric mevalonic acid InChIKey.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:25351` and `150-97-0` found the active DL-mevalonic
  acid record, generated membership rows, the row-review rows, and the final
  SSSOM row.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:150970` and the retained complex-polysaccharide
  systematic label found it only in this record and generated row-review/final
  SSSOM rows.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row maps to
  `CHEBI:25351`, but its `other` column still includes the long
  complex-polysaccharide systematic label from the unrelated old
  `CHEBI:150970` enrichment.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists` and a
  provisional curator note.

## Completeness

- CAS RN, formula, ChEBI synonymy, and CultureMech occurrence provenance are
  populated.
- Supplied forms, mixture components, physicochemical roles, biological roles,
  and environmental contexts are correctly empty.

## Recommended Edits

- Major: demote the complex-polysaccharide label in
  `data/ingredients/mapped/Dl-mevalonic_Acid.yaml` to `REJECTED_LABEL`
  provenance or remove it from active synonymy; then regenerate
  `mappings/ingredient_mappings.sssom.tsv` and synchronize
  `data/curated/mapped_ingredients.yaml`.
- Major: replace the `CARBON_SOURCE` computational role with source-backed role
  evidence scoped to DL-mevalonic acid, or remove the role if no support is
  available; then synchronize `data/curated/mapped_ingredients.yaml`.
