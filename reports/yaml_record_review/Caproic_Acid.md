# `data/ingredients/mapped/Caproic_Acid.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:30776` hexanoic acid identity, CAS,
structure fields, synonyms, occurrence count, SSSOM row, and aggregate copy
pass, but the active `CARBON_SOURCE` role is supported only by a provisional
name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Caproic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30776`,
  `ontology_mapping.ontology_id: CHEBI:30776`,
  `ontology_label: hexanoic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:30776` returns active label `hexanoic acid`, CAS
  `142-62-1`, and formula `C6H12O2`.
- PubChem resolves CAS `142-62-1` to CID `8892` with the same formula, InChI,
  and SMILES as the local `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Candiplanecin.yaml data/ingredients/mapped/Cantharidin.yaml data/ingredients/mapped/Capecitabine.yaml data/ingredients/mapped/Capreomycin.yaml data/ingredients/mapped/Caproic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Candiplanecin.yaml data/ingredients/mapped/Cantharidin.yaml data/ingredients/mapped/Capecitabine.yaml data/ingredients/mapped/Capreomycin.yaml data/ingredients/mapped/Caproic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The current `mappings/culturemech_recipe_membership.tsv` rows contain 16
  distinct recipes and 16 occurrences, matching `occurrence_statistics`.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Caproic_Acid` SSSOM row with
  the ChEBI/curated synonyms plus `CAS:142-62-1`.
- The `CARBON_SOURCE` role has only `reference_type:
  COMPUTATIONAL_PREDICTION` from a curated name-pattern rule and explicitly
  says review is recommended.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, ChEBI synonyms,
  single-ingredient classification, 16/16 occurrence count, SSSOM row,
  aggregate copy, and docs row are populated.
- No raw role text is exported as an SSSOM synonym for this record.

## Recommended Edits

- In `data/ingredients/mapped/Caproic_Acid.yaml`, remove the unsupported
  `CARBON_SOURCE` role unless a future curator can attach record-specific
  evidence showing caproic acid served that role in the cited media.
- Regenerate `data/curated/mapped_ingredients.yaml`, docs data, and any role
  exports that consume the aggregate; prove the cleanup with strict validation
  and round-trip verification.
