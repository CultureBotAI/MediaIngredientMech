# `data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The CAS-primary monohydrate
identity, PubChem structure, close `CHEBI:6731` melezitose parent, 0/0
occurrence count, CAS registry row, and final SSSOM synonym payload pass, but
`CARBON_SOURCE` is asserted only from provisional name-pattern evidence and
needs direct media-use support or removal.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml`.
- Current identifier and grounding: `identifier: cas:10030-67-8`,
  `ontology_mapping.ontology_id: CHEBI:6731`,
  `ontology_label: melezitose`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:6731` returns active `CHEBI:6731` labelled
  `melezitose` with formula `C18H32O16`, confirming it is the anhydrous parent,
  not an exact monohydrate term.
- PubChem CID `16217716` returns formula `C18H34O17` and a canonical SMILES
  string with one dot-separated water, matching the YAML formula and SMILES.
- Live OLS searches for exact `D-(+)-melezitose monohydrate` and for CAS
  `10030-67-8` found no CHEBI term, so the CAS-primary record remains needed.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml data/ingredients/mapped/D-_-pantolactone.yaml data/ingredients/mapped/D-_-tagatose.yaml data/ingredients/mapped/D-_-turanose.yaml data/ingredients/mapped/D-apiose.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-_-pantolactone.yaml data/ingredients/mapped/D-_-tagatose.yaml data/ingredients/mapped/D-_-turanose.yaml data/ingredients/mapped/D-apiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 with no failures for the four CHEBI-primary records in this batch.
  This CAS-primary registry record was skipped because `cas:` is outside the
  CHEBI/OBO term-validator scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The current `CLOSE_MATCH` parent relation is supported by the 2026-08-13
  `MIM curation (#342)` evidence, which records that a hydrate is similar to
  but not subsumed by its anhydrous form.
- The hidden/ignored-inclusive membership search found no `cas:10030-67-8`
  rows in `mappings/culturemech_recipe_membership.tsv`, matching the record's
  0/0 `occurrence_statistics`.
- The final SSSOM rows publish
  `MIM:D-_-melezitose_Monohydrate skos:closeMatch CHEBI:6731` and an exact
  `cas:10030-67-8` registry row. The only final `other` token is
  `CAS:10030-67-8`, which is safe for the monohydrate subject.
- The `CARBON_SOURCE` facet is supported only by `COMPUTATIONAL_PREDICTION`
  from a curated name-pattern rule and its own `curator_note` calls it
  provisional.

## Completeness

- The current row honestly represents the identity as a CAS monohydrate with a
  close anhydrous parent. No exact CHEBI term was found by the live OLS
  searches for the exact label or CAS.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- In `data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml`, either replace
  the computational `CARBON_SOURCE` evidence with direct CultureBotHT or
  source-backed media-role evidence for this ingredient, or remove the role
  facet; then rerun strict validation and the final SSSOM build.
