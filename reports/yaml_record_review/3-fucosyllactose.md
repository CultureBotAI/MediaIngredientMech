# `data/ingredients/mapped/3-fucosyllactose.yaml`

## Verdict

Needs curation, major. The same-formula repair to exact `CHEBI:90065`
`3-fucosyllactose`, the CAS companion row, formula, InChI, SMILES, exact
synonyms, SSSOM rows, and aggregate row pass, but `CARBON_SOURCE` is still only
backed by a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/3-fucosyllactose.yaml`.
- Identifier and grounding: local `identifier: cas:41312-47-4` with
  `ontology_mapping.ontology_id: CHEBI:90065`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:90065`
  resolves to `3-fucosyllactose`, lists formula `C18H32O15`, and matches the
  record InChI. Its stereospecific SMILES denotes the same structure represented
  by the record's PubChem-derived SMILES.
- The `#326` curation event correctly records the former parent as identical by
  formula and InChIKey via the record's own CAS.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-aminobutyric_Acid.yaml data/ingredients/mapped/3-beta-d-glucan.yaml data/ingredients/mapped/3-dehydro-D-gluconate.yaml data/ingredients/mapped/3-fucosyllactose.yaml data/ingredients/mapped/3-hydroxybenzoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-fucosyllactose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-fucosyllactose` to `CHEBI:90065` row and the companion exact
  `cas:41312-47-4` registry row.

## Evidence

- The active ChEBI page confirms the exact fucosyllactose identity, formula, and
  structure.
- The `3'-fucosyllactose` OAK/OLS synonym-enrichment candidate and the
  `cas:41312-47-4` unknown-term row have both already been triaged as
  represented/expected.
- Unsupported: `nutritional_roles.CARBON_SOURCE` has only `reference_type:
  COMPUTATIONAL_PREDICTION` from a curated media-role name pattern. That is a
  provisional inference, not direct evidence that this oligosaccharide is used
  as a microbial culture carbon source.
- Stale: `mappings/record_research_validation.tsv` still contains rows that
  describe the pre-`#326` `NARROW_MATCH`; the active record is already
  `EXACT_MATCH` and its SSSOM rows use `skos:exactMatch`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM rows, synonym/unknown-term triage, generated docs, and stale
  advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS, PubChem CID, formula, InChI, and SMILES are populated.
- The active nutritional role still needs direct exact-form evidence or removal.

## Recommended Edits

1. In `data/ingredients/mapped/3-fucosyllactose.yaml`, remove
   `nutritional_roles.CARBON_SOURCE` or replace it with direct medium-use
   evidence for this exact fucosyllactose form.
2. Run the per-record strict validator, compare the record against
   `data/curated/mapped_ingredients.yaml`, rebuild the SSSOM/docs with the
   maintained generators, and then rerun the whole-corpus SSSOM and flat-export
   checks.
