# `data/ingredients/mapped/Dl-aspartic_Acid.yaml`

## Verdict

Needs curation. The CultureMech identity exact-matches active `CHEBI:22660`
aspartic acid, its CAS RN and structure match ChEBI and PubChem, and the final
SSSOM row is clean; the `AMINO_ACID_SOURCE` role is still only a provisional
ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-aspartic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:22660` with
  `ontology_mapping.ontology_id: CHEBI:22660`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 2 CultureMech source occurrences.
- Local OAK resolves `CHEBI:22660` to active `aspartic acid`, formula
  `C4H7NO4`, the expected InChI and SMILES, CAS xref `617-45-8`, and exact or
  related DL-aspartic acid synonyms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16494 CHEBI:22660 CHEBI:17126 CHEBI:18320 CHEBI:42106 CHEBI:30314 CHEBI:43796`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:22660`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `617-45-8` to CID 424 with formula `C4H7NO4` and the
  same InChIKey as the record.
- The hidden/ignored-inclusive exact search over `data/ingredients` for
  `CHEBI:22660` and `617-45-8` found only
  `data/ingredients/mapped/Dl-aspartic_Acid.yaml`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the
  `CHEBI:22660` synonym enrichment row as already represented.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dl-aspartic_Acid` to `CHEBI:22660` with `skos:exactMatch`, canonical
  object label `aspartic acid`, CHEBI object source, true DL-aspartic acid
  synonyms, and `CAS:617-45-8`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from the ChEBI `CHEBI:33709` amino acid
  ancestry closure. It is not source-backed.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe synonymy, ChEBI synonymy, and
  CultureMech occurrence provenance are populated.
- Supplied forms, mixture components, physicochemical roles, biological roles,
  and environmental contexts are correctly empty.

## Recommended Edits

- Major: replace the `AMINO_ACID_SOURCE` computational role in
  `data/ingredients/mapped/Dl-aspartic_Acid.yaml` with source-backed role
  evidence scoped to DL-aspartic acid, or remove the role if no support is
  available; then synchronize `data/curated/mapped_ingredients.yaml`.
