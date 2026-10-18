# `data/ingredients/mapped/Dithionite.yaml`

## Verdict

Needs curation. The MicrobeDecoder identity exact-matches active `CHEBI:42160`
dithionite(2-), its CAS RN and structure agree with ChEBI and PubChem, and the
final SSSOM row is clean; the `REDUCING_AGENT` role is still only a provisional
name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Dithionite.yaml`.
- Identifier and grounding: `identifier: CHEBI:42160` with
  `ontology_mapping.ontology_id: CHEBI:42160`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 2/2 source occurrences.
- Local OAK resolves `CHEBI:42160` to active `dithionite(2-)`, CAS xref
  `14844-07-6`, formula `O4S2`, the expected InChI and SMILES, and exact or
  related dithionite synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Disodium_Oxalate.yaml data/ingredients/mapped/Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml data/ingredients/mapped/Distilled_Water.yaml data/ingredients/mapped/Dithionite.yaml data/ingredients/mapped/Dl-2-methylbutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:132764 CHEBI:34683 CHEBI:15377 CHEBI:42160 CHEBI:37070`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:42160`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `14844-07-6` to CID 1086 with formula `O4S2-2` and the
  same InChIKey as the record.
- The hidden/ignored-inclusive exact search over `data/ingredients` for
  `CHEBI:42160` and `14844-07-6` found only
  `data/ingredients/mapped/Dithionite.yaml`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Dithionite`
  to `CHEBI:42160` with `skos:exactMatch`, canonical object label
  `dithionite(2-)`, CHEBI object source, true dithionite synonyms, and
  `CAS:14844-07-6`.
- Major: `physicochemical_roles.REDUCING_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists` and a
  provisional curator note. It is not source-backed.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe synonymy, ChEBI synonymy, and
  MicrobeDecoder occurrence provenance are populated.
- Supplied forms, mixture components, nutritional roles, biological roles, and
  environmental contexts are correctly empty.

## Recommended Edits

- Major: replace the `REDUCING_AGENT` computational role in
  `data/ingredients/mapped/Dithionite.yaml` with source-backed role evidence
  scoped to dithionite, or remove the role if no support is available; then
  synchronize `data/curated/mapped_ingredients.yaml`.
