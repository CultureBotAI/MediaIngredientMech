# `data/ingredients/mapped/3-O-Methyl-D-glucopyranose.yaml`

## Verdict

Needs curation, major. The CAS-primary fallback identity for
`3-O-Methyl-D-glucopyranose` agrees with PubChem CID `83246` and is already
parked as an expected registry identifier, but the active `CARBON_SOURCE` role
is only backed by a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/3-O-Methyl-D-glucopyranose.yaml`.
- Identifier and grounding: `identifier: cas:13224-94-7` with matching
  `ontology_mapping.ontology_id`, source `CAS`, `mapping_quality:
  FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- Registry check: resolving CAS `13224-94-7` through PubChem returned CID
  `83246`, formula `C7H14O6`, the same standard InChI recorded in the YAML,
  and a stereospecific pyranose SMILES for
  `3-O-Methyl-D-glucopyranose`.
- The separate `3-O-methyl-glucose` record is grounded to `CHEBI:73918`; the
  CAS fallback here remains the pyranose registry form, not an accidental
  duplicate of the ChEBI-backed open-chain glucose analog.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Methylglutaric_Acid.yaml data/ingredients/mapped/3-O-Methyl-D-glucopyranose.yaml data/ingredients/mapped/3-O-methyl-glucose.yaml data/ingredients/mapped/3-O-methyl_Alpha-D-glucopyranoside.yaml data/ingredients/mapped/3-O-methylgallate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-O-Methyl-D-glucopyranose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  unavailable; the local `cas:` adapter opened a SQLite DB without
  `rdfs_label_statement`, so the check crashed before judging this record.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-O-Methyl-D-glucopyranose` to `cas:13224-94-7` registry row with
  `CAS:13224-94-7` in `other`.

## Evidence

- The PubChem response corroborates the CAS fallback's formula and InChI, so the
  registry identity itself is sound.
- The OAK/OLS row-review triage already marks `cas:13224-94-7` as
  `expected_registry_identifier`; CAS registry CURIEs are not expected to
  resolve as ontology terms.
- Unsupported: `nutritional_roles.CARBON_SOURCE` has only `reference_type:
  COMPUTATIONAL_PREDICTION` from a curated media-role name pattern. That is a
  provisional inference, not direct evidence that this pyranose form is used as
  a microbial culture carbon source.
- Stale/advisory: `mappings/record_research_validation.tsv` still contains
  rows proposing `UNMAPPED` or a `3-O-methyl-D-glucose` primary label; the
  expected-registry row review supersedes the UNMAPPED recommendation, while
  the PubChem CID keeps `cas:13224-94-7` tied to the pyranose record.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, unknown-term triage, generated docs, and stale advisory
  rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS, PubChem CID, formula, InChI, and SMILES are populated.
- The role evidence is not complete enough for the generic `CARBON_SOURCE`
  assertion.

## Recommended Edits

1. In `data/ingredients/mapped/3-O-Methyl-D-glucopyranose.yaml`, remove
   `nutritional_roles.CARBON_SOURCE` or replace it with direct medium-use
   evidence for this exact CAS form.
2. Run the per-record strict validator, compare the record against
   `data/curated/mapped_ingredients.yaml`, rebuild the SSSOM/docs with the
   maintained generators, and then rerun the whole-corpus SSSOM and flat-export
   checks.
