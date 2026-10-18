# `data/ingredients/mapped/Azadirachtin.yaml`

## Verdict

Needs curation; severity major. The bare-label exact mapping to generic
`CHEBI:38473` `azadirachtin` is defensible, but the record and SSSOM row still
carry CAS `11141-17-6`, which resolves to a single PubChem compound while
`CHEBI:38473` is a family of terpenoids with no fixed formula, structure, or CAS
annotation.

## Identity

- Reviewed record: `data/ingredients/mapped/Azadirachtin.yaml`.
- Identifier and grounding: `identifier: CHEBI:38473` with
  `ontology_mapping.ontology_id: CHEBI:38473`,
  `ontology_label: azadirachtin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:38473` to non-obsolete `azadirachtin` with the definition
  "A family of terpenoids isolated from the neem tree" and no formula, charge,
  InChI, SMILES, or CAS xref annotation.
- PubChem lookup for the local `chemical_properties.cas_rn: 11141-17-6`
  resolves to CID 5281303, title `Azadirachtin`, formula `C35H44O16`, and a
  full structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azacolutin.yaml data/ingredients/mapped/Azadirachtin.yaml data/ingredients/mapped/Azaserine.yaml data/ingredients/mapped/Azelaate.yaml data/ingredients/mapped/Azelaic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Azadirachtin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed; this confirms the canonical `CHEBI:38473` label but cannot detect the
  over-specific local CAS field.
- OLS4 lookup for `CHEBI:38473` and PubChem lookup for CAS `11141-17-6`
  confirmed the family/form mismatch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 507 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The CultureBotHT import is the only source recorded for the mapping and CAS:
  the YAML curation event says the row was created from
  `compounds_to_cas.csv (CAS=11141-17-6)`, and the SSSOM `other` field repeats
  `CAS:11141-17-6`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirmed only the
  `CHEBI:38473` OAK/OLS mapping. They do not prove that a form-specific CAS RN
  belongs on the generic ChEBI family record.

## Completeness

- The exact generic ChEBI identifier, label, SSSOM row, and aggregate copy are
  synchronized.
- The only consequential gap is the form boundary around `11141-17-6`: a future
  curation pass needs to decide whether CultureBotHT intended a specific
  azadirachtin form or only the generic family.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  present in CultureMech recipe memberships.

## Recommended Edits

- Re-curate `data/ingredients/mapped/Azadirachtin.yaml` from the original
  CultureBotHT `Azadirachtin` + `11141-17-6` source row. If the CAS identifies
  a form-specific external term, re-ground the record to that exact term and
  synchronize `data/curated/mapped_ingredients.yaml` plus
  `mappings/ingredient_mappings.sssom.tsv`; if not, keep `CHEBI:38473` as the
  family record but remove `chemical_properties.cas_rn` and the SSSOM
  `CAS:11141-17-6` assertion from this generic identity.
- Rerun focused strict and term validation, SSSOM invariants, product
  id/label correspondence, and flat-export coverage after the maintained
  curation surfaces are synchronized.
