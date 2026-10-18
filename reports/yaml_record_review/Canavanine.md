# `data/ingredients/mapped/Canavanine.yaml`

## Verdict

Needs curation, major. The CAS-derived `CHEBI:609827` L-canavanine identity,
CAS, structure fields, synonym, SSSOM row, and aggregate copy pass, but the
active `AMINO_ACID_SOURCE` role is only a provisional ChEBI-ancestry
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Canavanine.yaml`.
- Identifier and grounding: `identifier: CHEBI:609827`,
  `ontology_mapping.ontology_id: CHEBI:609827`,
  `ontology_label: L-canavanine`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:609827` returns active label `L-canavanine`,
  CAS `543-38-4`, and formula `C5H12N4O3`.
- PubChem resolves CAS `543-38-4` to CID `439202` with the same formula,
  stereochemistry, and InChI as the local structure fields.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Camphomycin.yaml data/ingredients/mapped/Camptothecin.yaml data/ingredients/mapped/Canarius.yaml data/ingredients/mapped/Canavanine.yaml data/ingredients/mapped/Candimycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Camptothecin.yaml data/ingredients/mapped/Canavanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed both ChEBI records. Placeholder rows in the batch were skipped by the
  OBO-safe term wrapper.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The source CAS `543-38-4` resolves to ChEBI and PubChem records for
  L-canavanine, matching the local formula, InChI, SMILES, and
  `O-carbamimidamido-L-homoserine` synonym.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Canavanine` SSSOM row,
  matching aggregate/docs rows, and the `CONFIRMED_NO_ACTION` row-review
  manifest entry.
- The `AMINO_ACID_SOURCE` role has only `reference_type:
  COMPUTATIONAL_PREDICTION` from ChEBI ancestry and explicitly says review is
  recommended. Class ancestry alone does not show that this CultureBotHT-only
  compound was used as an amino acid source in a medium.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, synonym,
  single-ingredient classification, SSSOM row, aggregate copy, and docs row are
  populated.
- No media occurrences are asserted, which is coherent for this CultureBotHT
  source record.

## Recommended Edits

- In `data/ingredients/mapped/Canavanine.yaml`, remove
  `nutritional_roles.AMINO_ACID_SOURCE` unless a future curator can attach
  compound-specific evidence for L-canavanine as an amino acid source in
  microbial media.
- Regenerate `data/curated/mapped_ingredients.yaml`, docs data, and any role
  exports that consume the aggregate; prove the cleanup with strict validation
  and `scripts/validate_sssom_invariants.py`.
