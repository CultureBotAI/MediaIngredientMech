# `data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym and role-evidence issues. The
CAS-primary hydrate identity, PubChem monohydrate-like structure, close
`CHEBI:6731` melezitose parent, 0/0 occurrence count, and CAS registry row pass,
but the final `other` column exports `D-melezitose (melezitose)`, which names
the anhydrous parent rather than the hydrate subject.

## Identity

- Reviewed record: `data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`.
- Current identifier and grounding: `identifier: cas:207511-10-2`,
  `ontology_mapping.ontology_id: CHEBI:6731`,
  `ontology_label: melezitose`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:6731` returns active `CHEBI:6731` labelled
  `melezitose` with formula `C18H32O16`, confirming it is the anhydrous parent,
  not an exact hydrate term.
- PubChem CID `16217716` returns formula `C18H34O17` and a canonical SMILES
  string with one dot-separated water, matching the YAML formula and SMILES.
- Live OLS searches for exact `D-(+)-Melezitose hydrate` and for CAS
  `207511-10-2` found no CHEBI term, so the CAS-primary record remains needed.
- A hidden/ignored-inclusive exact `^identifier:`/`ontology_id:` search under
  `data/ingredients` found this CAS-primary hydrate, the sibling monohydrate
  record, and the active `Melezitose.yaml` parent at `CHEBI:6731`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Sucrose.yaml data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml data/ingredients/mapped/D-_-lyxose.yaml data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two live CHEBI-primary exact records in this batch. This
  CAS-primary registry record was skipped because `cas:` is outside the
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
- The hidden/ignored-inclusive membership search found no `cas:207511-10-2`
  rows in `mappings/culturemech_recipe_membership.tsv`, matching the record's
  0/0 `occurrence_statistics`. The two membership rows for `CHEBI:6731` belong
  to the distinct anhydrous `Melezitose` record.
- The final SSSOM rows publish
  `MIM:D-_-melezitose_Hydrate skos:closeMatch CHEBI:6731` and an exact
  `cas:207511-10-2` registry row.
- Major: the `sssom_other_backfill` synonym `D-melezitose (melezitose)` drops
  the hydrate boundary and names the anhydrous parent; final SSSOM exports it
  in `other`, which violates the final synonym-surface contract.
- The `CARBON_SOURCE` facet is supported only by `COMPUTATIONAL_PREDICTION`
  from a curated name-pattern rule and its own `curator_note` calls it
  provisional.

## Completeness

- The current row honestly represents the identity as a CAS hydrate with a
  close anhydrous parent. No exact CHEBI term was found by the live
  hidden/ignored-independent OLS searches for the label and CAS.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry, including the bad raw synonym.

## Recommended Edits

- In `data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`, remove
  `D-melezitose (melezitose)` from active synonyms or retag it as
  provenance-only so it no longer reaches final SSSOM `other`; then
  synchronize `data/curated/mapped_ingredients.yaml` and regenerate final
  SSSOM.
- Either replace the computational `CARBON_SOURCE` evidence with direct
  CultureBotHT or source-backed media-role evidence for this ingredient, or
  remove the role facet; then rerun strict validation and the final SSSOM
  build.
