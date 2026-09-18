# `data/ingredients/mapped/Cacl2_X_7_H2o.yaml`

## Verdict

Pass. The malformed calcium chloride heptahydrate label is retained as a local
kg-microbe identity, mapped only as a close match to anhydrous `CHEBI:3312`,
and accompanied by a registry exact-match SSSOM row.

## Identity

- Reviewed record: `data/ingredients/mapped/Cacl2_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:cacl2_x_7_h2o`,
  `ontology_mapping.ontology_id: CHEBI:3312`,
  `ontology_label: calcium dichloride`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3312` returns the active label
  `calcium dichloride`; the record correctly avoids claiming exact identity
  with this anhydrous ChEBI term.
- The 2026-08-29 and 2026-09-12 curation events removed the inherited
  anhydrous CAS and unverified structure fields, leaving
  `chemical_properties: {}` while keeping the 11/11 source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cacl2_X_7_H2o.yaml data/ingredients/mapped/Caco3.yaml data/ingredients/mapped/Cadaverine.yaml data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml data/ingredients/mapped/Cadmium_Chloride_Hemipentahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cacl2_X_7_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`, `docs/data`,
  and `reports`, excluding bulky backups and generated review-report
  directories, found the exact aggregate copy in
  `data/curated/mapped_ingredients.yaml`, the two SSSOM rows at
  `mappings/ingredient_mappings.sssom.tsv`, and the `OK_LOCAL_REGISTRY_ID`
  hydrate-grounding row.
- The SSSOM parent row uses `skos:closeMatch` to `CHEBI:3312` with an explicit
  comment that `CaCl2 x 7 H2O` is an unresolved malformed MediaDive hydrate
  label and `CHEBI:3312` is only the anhydrous parent.
- The required identity row maps `MIM:Cacl2_X_7_H2o` to
  `kgmicrobe.compound:cacl2_x_7_h2o` with `skos:exactMatch`, preserving the
  local node that must not collapse into the parent ChEBI term.
- The only resolving SSSOM aliases are the 7-hydrate source forms; the
  anhydrous and wrong-hydrate labels that previously hid on this record are now
  `REJECTED_LABEL`.

## Completeness

- The local identifier, close parent, registry row, 11/11 occurrence count, raw
  role surface, and intentionally empty `chemical_properties` are populated.
- No exact ChEBI term, authoritative CAS, or structure remains unexamined in
  this record: the checked history documents why they were removed or not
  asserted.

## Recommended Edits

- None for this record.
