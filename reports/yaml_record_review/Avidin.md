# `data/ingredients/mapped/Avidin.yaml`

## Verdict

Pass. The record preserves CAS `1405-69-2` as the exact local registry identity,
uses MeSH `D001360` as a broader parent with `NARROW_MATCH`, and publishes the
required registry SSSOM rows alongside the parent match.

## Identity

- Reviewed record: `data/ingredients/mapped/Avidin.yaml`.
- Identifier and grounding: `identifier: cas:1405-69-2` with
  `ontology_mapping.ontology_id: mesh:D001360`,
  `ontology_label: Avidin`, `ontology_source: MESH`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search for `Avidin` in MeSH returned `mesh:D001360` `Avidin`.
- The CAS and `kgmicrobe.compound:avidin` identities are preserved as exact
  registry rows because the primary ontology mapping is intentionally a parent
  match.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Avidin.yaml data/ingredients/mapped/Avocadene.yaml data/ingredients/mapped/Avocadyne.yaml data/ingredients/mapped/Avocatin_B.yaml data/ingredients/mapped/Avoparcin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation for `Avidin.yaml` passed after rerunning with `uv`
  cache access outside the sandbox.
- OLS exact search for `Avidin` and
  `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` both
  resolve the MeSH parent.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM parent row plus the two registry rows at
  `mappings/ingredient_mappings.sssom.tsv` rows 499-501 and the aggregate copy
  in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records all three
  review surfaces for `Avidin`: the MeSH parent, the CAS registry row, and the
  kg-microbe registry row.

## Completeness

- The exact local CAS, parent MeSH identifier, SSSOM parent and registry rows,
  aggregate copy, and curation-history transition to `NARROW_MATCH` are
  populated.
- The 0/0 occurrence count is correct for a CultureBotHT-only record not
  present in CultureMech recipe memberships.
- Chemical formula and structure are absent because the exact primary identity
  is a protein CAS rather than a ChEBI small-molecule term.

## Recommended Edits

- None.
