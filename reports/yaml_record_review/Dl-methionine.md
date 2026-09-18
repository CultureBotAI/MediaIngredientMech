# `data/ingredients/mapped/Dl-methionine.yaml`

## Verdict

Pass. The CultureMech identity exact-matches active `CHEBI:16811` methionine by
synonym, its CAS RN and structure match ChEBI and PubChem, the CultureMech
nitrogen-source role is source-backed, and the final SSSOM row publishes only
true methionine aliases.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-methionine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16811` with
  `ontology_mapping.ontology_id: CHEBI:16811`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 28 CultureMech source occurrences.
- Local OAK resolves `CHEBI:16811` to active `methionine`, formula
  `C5H11NO2S`, the expected InChI and SMILES, CAS xref `59-51-8`, and related
  `DL-Methionine` and `Racemethionine` synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-histidine.yaml data/ingredients/mapped/Dl-malic_Acid.yaml data/ingredients/mapped/Dl-methionine.yaml data/ingredients/mapped/Dl-mevalonic_Acid.yaml data/ingredients/mapped/Dl-tryptophan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27570 CHEBI:6650 CHEBI:16811 CHEBI:25351 CHEBI:57912`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:16811`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `59-51-8` to CID 876 with formula `C5H11NO2S` and the
  same InChIKey as the record.
- A hidden/ignored-inclusive exact search over `data/ingredients` and
  `mappings` for `CHEBI:16811` and `59-51-8` found the active DL-methionine
  record, generated membership rows, the row-review confirmation, and final
  SSSOM row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `CHEBI:16811` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dl-methionine` to `CHEBI:16811` with `skos:exactMatch`, canonical
  object label `methionine`, CHEBI object source, true methionine synonyms, and
  `CAS:59-51-8`.
- `nutritional_roles.NITROGEN_SOURCE` carries `DATABASE_ENTRY` evidence
  imported from the CultureMech `Nitrogen Source` role text rather than a
  provisional name-list or ChEBI ancestry inference.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe synonymy, ChEBI synonymy,
  nitrogen-source role evidence, and CultureMech occurrence provenance are
  populated.
- The raw `Role: Nitrogen source` string is correctly excluded from final SSSOM
  synonym publication.
- Supplied forms, mixture components, physicochemical roles, biological roles,
  and environmental contexts are correctly empty.

## Recommended Edits

- None.
