# `data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml`

## Verdict

Needs curation; severity major. The CAS fallback identity and SSSOM registry
row are internally consistent, and a current exact OLS search still found no
external term for the full label, but the stored `pubchem_cid: 870` and
structure describe PubChem's amylotetraose record rather than CAS `9036-88-8`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml`.
- Identifier and grounding: `identifier: cas:9036-88-8` with
  `ontology_mapping.ontology_id: cas:9036-88-8`,
  `ontology_label: b-Mannan borohydrate reduced carob seed`,
  `ontology_source: CAS`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- OLS4 exact search across `CHEBI`, `MESH`, and `NCIT` returned zero exact
  matches for `b-Mannan borohydrate reduced carob seed`.
- PubChem lookup for CAS `9036-88-8` currently resolves to CID 25147451,
  `alpha-D-Mannan`, formula `C24H42O21`.
- PubChem lookup for the local `pubchem_cid: 870` resolves to
  `Amylotetraose; Fujioligo 450; alpha-1,4-Tetraglucose`, which is not a
  mannan identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azureomycin.yaml data/ingredients/mapped/B-Glucan_From_Oat.yaml data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml data/ingredients/mapped/BHI.yaml data/ingredients/mapped/Bacillomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `cas` is a non-OBO prefix.
- OLS4 exact lookup for `b-Mannan borohydrate reduced carob seed` in `CHEBI`,
  `MESH`, and `NCIT` returned no exact candidate.
- PubChem lookups for CAS `9036-88-8` and CID 870 showed that the local CID and
  structure are not the current CAS-resolved PubChem compound.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 518 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` correctly classify
  the SSSOM `cas:9036-88-8` object as an expected registry identifier rather
  than an OBO lookup failure.
- `mappings/hydrate_review.tsv` correctly treats `borohydrate reduced` as not
  being a hydrate string and leaves the CAS fallback intact.
- The current `chemical_properties` combine the CAS fallback with a PubChem CID
  and structure for a different carbohydrate.

## Completeness

- The CAS primary identifier, SSSOM row, aggregate copy, and provisional
  `CARBON_SOURCE` role are populated.
- The PubChem structure block is consequentially wrong and should not be
  trusted until rederived from CAS `9036-88-8`.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  present in CultureMech recipe memberships.

## Recommended Edits

- Re-curate `data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml`
  from CAS `9036-88-8`: at minimum remove `pubchem_cid: 870` and its derived
  InChI/SMILES fields, then add replacement PubChem fields only if the
  CAS-resolved compound is verified to represent the exact
  borohydrate-reduced carob seed mannan identity.
- Synchronize `data/curated/mapped_ingredients.yaml` and rerun focused strict
  validation, SSSOM invariants, product id/label correspondence, duplicate-ID
  baseline audit, and flat-export coverage.
