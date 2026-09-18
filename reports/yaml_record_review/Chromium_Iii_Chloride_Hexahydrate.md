# `data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml`

## Verdict

Needs curation, major. The record is correctly promoted to the active
hydrate-specific identity `CHEBI:53442` and now has the hydrated formula
`3Cl.Cr.6H2O`, but its retained CAS, InChI, and SMILES still describe
anhydrous chromium trichloride.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:53442`,
  `ontology_mapping.ontology_id: CHEBI:53442`,
  `ontology_label: chromium(3+) trichloride hexahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `chromium(3+) trichloride hexahydrate` returns one
  active `CHEBI:53442` term with the same label.
- PubChem lookup of the retained CAS `10025-73-7` resolves to CID `24808` with
  formula `Cl3Cr`, IUPAC name `trichlorochromium`, and the same anhydrous
  standard InChI stored in this hexahydrate record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Choline_Chloride.yaml data/ingredients/mapped/Cholinium_Dihydrogen_Phosphate.yaml data/ingredients/mapped/Cholinium_Lysinate.yaml data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Choline_Chloride.yaml data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three CHEBI-scoped records in this narrowed run.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chromium_Iii_Chloride_Hexahydrate`
  SSSOM row, matching aggregate/docs rows, and `reports/hydrate_grounding.tsv`
  marking the hydrate identity itself as `OK_HYDRATE_TERM`.
- That same hidden/ignored-inclusive search also found the stale anhydrous CAS
  `10025-73-7` on the active record and in the SSSOM `other` column.
- `reports/hydrate_review.tsv` marks this record `OK`, but that older check
  accepted the hydrate-specific ChEBI identity and formula; it did not catch
  that the CAS, InChI, and SMILES still came from the anhydrous import.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:53442` rows,
  matching the explicit 0/0 media-recipe occurrence statistics.
- The record carries no role, component, or environment claims.

## Completeness

- The ChEBI hexahydrate identifier, hydrated molecular formula, zero occurrence
  count, SSSOM row, aggregate copy, and docs rows are synchronized.
- The CAS and structure-derived fields still cross an anhydrous/hydrate
  boundary and need repair or removal before the chemical properties describe
  the same supplied form as `CHEBI:53442`.

## Recommended Edits

- In `data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml`, remove
  or replace the anhydrous `chemical_properties.cas_rn`, `inchi`, and `smiles`
  fields so every retained chemical property is for chromium(3+) trichloride
  hexahydrate rather than anhydrous chromium(3+) trichloride.
- Rerun strict validation, term validation, aggregate/roundtrip verification,
  `scripts/validate_sssom_invariants.py`, and the hydrate QC scripts that own
  `reports/hydrate_grounding.tsv` and `mappings/hydrate_review.tsv`.
