# `data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml`

## Verdict

Needs curation, with major grounding and role-evidence issues. The record keeps
the correct pentahydrate formula, InChI, PubChem CID, CAS identity, and final
SSSOM `other` synonym, but `CHEBI:189430` is now an active exact
`Raffinose Pentahydrate` term and should not remain a `skos:narrowMatch`
parent row with companion registry identity rows.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml`.
- Current identifier and grounding: `identifier: cas:17629-30-0`,
  `ontology_mapping.ontology_id: CHEBI:189430`,
  `ontology_label: Raffinose Pentahydrate`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:189430` returns active `CHEBI:189430` labelled
  `Raffinose Pentahydrate` with formula `C18H32O16.5H2O`, the same InChI as
  this record, and the same exact IUPAC synonym exported in final SSSOM
  `other`.
- PubChem CID `2724100` returns formula `C18H42O21` and a canonical SMILES
  string matching the YAML pentahydrate structure.
- A hidden/ignored-inclusive exact `^identifier:`/`ontology_id:` search under
  `data/ingredients` found only this record using `cas:17629-30-0` or pointing
  at `CHEBI:189430`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Proline.yaml data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml data/ingredients/mapped/D-Ribose.yaml data/ingredients/mapped/D-Saccharic_Acid_Potassium_Salt.yaml data/ingredients/mapped/D-Serine.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Proline.yaml data/ingredients/mapped/D-Ribose.yaml data/ingredients/mapped/D-Serine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch. This record
  was skipped because its primary `cas:` identifier is outside the CHEBI/OBO
  term-validator scope.
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

- `reports/hydrate_grounding.tsv` classifies `cas:17629-30-0` as
  `OK_OWN_CAS_ID`, confirming the CAS identity is hydrate-specific and should
  not collapse to an anhydrous raffinose parent.
- `mappings/ingredient_mappings_row_review_manifest.tsv` keeps the current CAS
  and kg-microbe registry rows because they match the CAS-primary YAML, but the
  current live OLS response shows the YAML should now be promoted to the exact
  CHEBI pentahydrate instead.
- The final SSSOM rows currently publish
  `MIM:D-Raffinose_Pentahydrate skos:narrowMatch CHEBI:189430`,
  an exact CAS row, and an exact
  `kgmicrobe.compound:d-raffinose_pentahydrate` row. The CHEBI row should
  become the single ontology identity row after promotion.
- The final SSSOM `other` token is a live exact synonym of `CHEBI:189430` and
  is safe for the pentahydrate subject.
- The `CARBON_SOURCE` facet is supported only by `COMPUTATIONAL_PREDICTION`
  from a curated name-pattern rule and its own `curator_note` calls it
  provisional.

## Completeness

- The hidden/ignored-inclusive membership search found no `cas:17629-30-0`
  rows in `mappings/culturemech_recipe_membership.tsv`, matching the record's
  0/0 `occurrence_statistics`.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- In `data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml`, promote the
  record from `identifier: cas:17629-30-0` plus
  `mapping_quality: NARROW_MATCH` to CHEBI-primary exact identity at
  `CHEBI:189430`; rerun synchronization and regenerate final SSSOM so the
  narrow parent and registry rows are replaced by an exact
  `MIM:D-Raffinose_Pentahydrate skos:exactMatch CHEBI:189430` row.
- Either replace the computational `CARBON_SOURCE` evidence with direct
  CultureBotHT or source-backed media-role evidence for this ingredient, or
  remove the role facet; then rerun strict validation and the final SSSOM
  build.
