# `data/ingredients/mapped/Grisamine.yaml`

## Verdict

Pass. The `kgmicrobe.compound:grisamine` placeholder remains a reasonable local
identity after fresh OLS/PubChem no-hit checks, no unsupported roles are
asserted, and the final registry SSSOM row is clean.

## Identity

- Reviewed record: `data/ingredients/mapped/Grisamine.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:grisamine` with
  matching `ontology_mapping.ontology_id`, local label `Grisamine`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Granaticin.yaml data/ingredients/mapped/Grasseriomycin.yaml data/ingredients/mapped/Green_House_Soil.yaml data/ingredients/mapped/Grisamine.yaml data/ingredients/mapped/Griseolutein_A.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was skipped for this local `kgmicrobe.compound`
  placeholder because the term validator does not resolve local registry CURIEs.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- The 2026-05-10 placeholder review retained `kgmicrobe.compound:grisamine`
  after the UNKNOWN_TERM no-hit artifact found no exact OLS candidate and no
  normalized local duplicate.
- Fresh OLS exact search for `Grisamine` returned `numFound: 0`, and PubChem
  name lookup for `Grisamine` returned no CID, so the old no-hit decision is
  still current within those checked endpoints.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Grisamine` to `kgmicrobe.compound:grisamine` by `skos:exactMatch` with
  an empty `other` payload.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, the
  placeholder no-hit TSVs, matching aggregate copies, generated products, the
  final SSSOM row, row-review TSVs, and ignored aggregate backups.

## Completeness

- The placeholder local identity, review note, singleton type, and final SSSOM
  exact local row are populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
