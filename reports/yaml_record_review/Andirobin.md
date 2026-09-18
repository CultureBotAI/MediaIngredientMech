# `data/ingredients/mapped/Andirobin.yaml`

## Verdict

Pass with minor issues. The direct CAS fallback identity, exact CAS SSSOM row,
row-review disposition, aggregate copy, and zero CultureMech memberships agree,
but the CAS now resolves to PubChem CID `12306782` and the record still lacks
formula, SMILES, InChI, and PubChem CID fields.

## Identity

- Reviewed record: `data/ingredients/mapped/Andirobin.yaml`.
- Identifier and grounding: `identifier: cas:6488-63-7` with
  `ontology_mapping.ontology_id: cas:6488-63-7`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the CAS
  `UNKNOWN_TERM` trailer as an expected registry identifier rather than an
  ontology lookup defect.
- PubChem resolves CAS `6488-63-7` to CID `12306782` with formula `C27H32O7`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amylopectin_From_Maize.yaml data/ingredients/mapped/Amylose_From_Potato.yaml data/ingredients/mapped/Anabasine_Hydrochloride.yaml data/ingredients/mapped/Anaerobic_water.yaml data/ingredients/mapped/Andirobin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Andirobin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  unavailable for this direct-CAS fallback; `linkml-term-validator` attempted
  to look up `cas:6488-63-7` in an ontology SQL adapter and failed on a missing
  `rdfs_label_statement` table.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` row 424 maps `MIM:Andirobin` to
  `cas:6488-63-7` with `skos:exactMatch` and the expected CAS
  `UNKNOWN_TERM` trailer.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the CAS row
  as an expected registry identifier with no mapping repair needed.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, CultureMech memberships, SSSOM and row-review TSVs, and batch
  review reports found the active YAML, aggregate copy, exact CAS SSSOM row,
  row-review row, and no `culturemech_recipe_membership.tsv` rows for
  `cas:6488-63-7`.

## Completeness

- CAS, curation history, `ingredient_type`, and the direct registry SSSOM row
  are populated.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.
- The missing PubChem-derived chemistry is non-blocking because the exact CAS
  registry identity is still preserved.

## Recommended Edits

- In `data/ingredients/mapped/Andirobin.yaml`, add source-backed PubChem
  chemistry for CAS `6488-63-7` if the curation workflow wants CAS fallbacks to
  be structure-complete where PubChem has a CID.
