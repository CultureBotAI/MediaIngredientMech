# `data/ingredients/mapped/Natural_Sea_Water.yaml`

## Verdict

Pass. The local natural-seawater registry identity, curated close match to
`ENVO:00002149`, natural-source environment annotation, occurrence count, and
final SSSOM companion rows agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Natural_Sea_Water.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:natural_sea_water` with
  `ontology_mapping.ontology_id: ENVO:00002149`, label `sea water`, source
  `ENVO`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 54 source occurrences across 54 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Natural_Sea_Water` through `Neomycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this
  registry-primary record.

## Evidence

- A fresh EBI OLS4 lookup resolves `ENVO:00002149` as active `sea water` with
  `ocean water` and `seawater` synonyms, so the curated ENVO close match is
  still live.
- The final SSSOM emits both the curated `skos:closeMatch` to `ENVO:00002149`
  and an exact `kgmicrobe.ingredient:natural_sea_water` registry row, matching
  the May 2026 correction that kept natural sea water narrower than generic sea
  water.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the local
  `kgmicrobe.ingredient:natural_sea_water` exact row as an expected registry
  identifier rather than an OAK/OLS repair target.
- The `environmental_context` entry points to the same ENVO sea-water term with
  `NATURAL_SOURCE`, matching an untreated natural-seawater ingredient.

## Completeness

- The local identity, ENVO parent, local registry exact row, occurrence count,
  and empty final `other` fields are synchronized.
- No chemical, role, or component assertions are present; those optional slots
  are appropriately empty for a complex environmental source ingredient.

## Recommended Edits

- None.
