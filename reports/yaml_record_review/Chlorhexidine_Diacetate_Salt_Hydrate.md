# `data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml`

## Verdict

Needs curation; major issue. The record is correctly kept on a local hydrate
identifier and close-matched to active `CHEBI:81711` chlorhexidine acetate, but
it still carries anhydrous chlorhexidine acetate CAS and structure fields under
`chemical_properties` for a hydrate of unspecified stoichiometry.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:chlorhexidine_diacetate_salt_hydrate`,
  `ontology_mapping.ontology_id: CHEBI:81711`,
  `ontology_label: chlorhexidine acetate`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:81711` returns one active ChEBI term labelled
  `chlorhexidine acetate` with CAS `56-95-1`, formula
  `C22H30Cl2N10.2C2H4O2`, and the same InChI and SMILES stored in
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chenodeoxycholic_Acid.yaml data/ingredients/mapped/Chitin.yaml data/ingredients/mapped/Chitosan.yaml data/ingredients/mapped/Chloramphenicol.yaml data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chenodeoxycholic_Acid.yaml data/ingredients/mapped/Chitin.yaml data/ingredients/mapped/Chitosan.yaml data/ingredients/mapped/Chloramphenicol.yaml data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found both active `MIM:Chlorhexidine_Diacetate_Salt_Hydrate` SSSOM
  rows, the synonym-enrichment `ALREADY_REPRESENTED` row, the
  `reports/hydrate_grounding.tsv` `OK_LOCAL_REGISTRY_ID` row, and matching
  aggregate/docs rows for
  `kgmicrobe.compound:chlorhexidine_diacetate_salt_hydrate`.
- The active SSSOM surface publishes a `skos:closeMatch` to the active
  anhydrous acetate parent `CHEBI:81711` and a `skos:exactMatch` registry row
  to `kgmicrobe.compound:chlorhexidine_diacetate_salt_hydrate`, preserving the
  local hydrate identity without asserting that it is the ChEBI parent.
- `mappings/hydrate_review.tsv` still marks this record `NEEDS_SOURCE`, with
  the rationale that the label says only "hydrate" and the CAS/formula metadata
  does not securely establish a unique water stoichiometry without the original
  recipe or supplier.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:chlorhexidine_diacetate_salt_hydrate` rows, matching the
  explicit 0/0 `occurrence_statistics`.

## Completeness

- The local identifier, anhydrous-parent closeMatch, registry identity row,
  zero occurrence count, SSSOM rows, aggregate copy, and docs row are populated.
- Exact hydrate structure fields are incomplete: the retained CAS, formula,
  InChI, and SMILES describe `CHEBI:81711` and do not encode a water of
  hydration or otherwise establish the named hydrate identity.

## Recommended Edits

- Major: inspect the original CultureBotHT source or supplier record for the
  intended chlorhexidine diacetate hydrate, then either replace
  `chemical_properties` with exact hydrate evidence or remove the inherited
  anhydrous CAS, formula, InChI, and SMILES fields.
- Regenerate synchronized outputs and rerun strict validation, SSSOM QC,
  aggregate roundtrip, hydrate audits, and `git diff --check`.
