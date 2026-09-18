# `data/ingredients/mapped/Cefsulodin_Sodium_Salt_Hydrate.yaml`

## Verdict

Needs curation; major issue. The record is correctly kept on a local hydrate
identifier and close-matched to active `CHEBI:31380`, but it still carries the
anhydrous cefsulodin sodium CAS and structure fields under
`chemical_properties`, and its `SELECTIVE_AGENT` role is only a provisional
name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Cefsulodin_Sodium_Salt_Hydrate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:cefsulodin_sodium_salt_hydrate`,
  `ontology_mapping.ontology_id: CHEBI:31380`,
  `ontology_label: Cefsulodin sodium`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:31380` returns one active ChEBI term labelled
  `Cefsulodin sodium` with formula `C22H19N4O8S2.Na` and the same InChI and
  SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cefsulodin_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/Ceftazidime.yaml data/ingredients/mapped/Ceftazidime_Hydrate.yaml data/ingredients/mapped/Ceftriaxone.yaml data/ingredients/mapped/Ceftriaxone_Disodium_Salt_Hemi_Heptahydrate.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cefsulodin_Sodium_Salt_Hydrate.yaml data/ingredients/mapped/Ceftazidime.yaml data/ingredients/mapped/Ceftazidime_Hydrate.yaml data/ingredients/mapped/Ceftriaxone.yaml data/ingredients/mapped/Ceftriaxone_Disodium_Salt_Hemi_Heptahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found both active `MIM:Cefsulodin_Sodium_Salt_Hydrate` SSSOM rows,
  the `SYNONYM_ENRICH` row-review disposition, the synonym-enrichment
  `ALREADY_REPRESENTED` row, `mappings/hydrate_review.tsv`, and matching
  aggregate/docs rows for
  `kgmicrobe.compound:cefsulodin_sodium_salt_hydrate`.
- The active SSSOM surface publishes a `skos:closeMatch` to the active
  anhydrous sodium parent `CHEBI:31380` and a `skos:exactMatch` registry row to
  `kgmicrobe.compound:cefsulodin_sodium_salt_hydrate`, preserving the local
  hydrate identity without asserting that it is the ChEBI parent.
- `mappings/hydrate_review.tsv` marks this record `NEEDS_SOURCE`, with the
  rationale that the label says only "hydrate" and the CAS/formula metadata
  does not securely establish a unique water stoichiometry without the original
  recipe or supplier.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:cefsulodin_sodium_salt_hydrate` rows, which matches the
  explicit 0/0 `occurrence_statistics`.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The local identifier, anhydrous-parent closeMatch, registry identity row,
  zero occurrence count, SSSOM rows, aggregate copy, and docs row are populated.
- Exact hydrate structure fields are incomplete: the retained CAS, formula,
  InChI, and SMILES describe `CHEBI:31380` and do not encode a water of
  hydration or otherwise establish the named hydrate identity.

## Recommended Edits

- Major: inspect the original CultureBotHT source or supplier record for the
  intended cefsulodin sodium hydrate, then either replace
  `chemical_properties` with exact hydrate evidence or remove the inherited
  anhydrous CAS, formula, InChI, and SMILES fields.
- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` with inspected
  evidence for cefsulodin sodium salt hydrate as a selective agent in this
  media scope, or remove the role, then rerun strict validation, SSSOM QC,
  aggregate roundtrip, hydrate audits, and `git diff --check`.
