# `data/ingredients/mapped/D-glucose.yaml`

## Verdict

Needs curation. The `CHEBI:17634` D-glucose identity, CultureMech occurrence
count, carbon-source role, Dextrose merge, and final SSSOM synonym payload are
sound, but the record still attaches an auto-proposed PubMed snippet about
FDG/PET to the ontology mapping and still carries a provisional computational
`ENERGY_SOURCE` role.

## Identity

- Reviewed record: `data/ingredients/mapped/D-glucose.yaml`.
- Identifier and grounding: `identifier: CHEBI:17634` with
  `ontology_mapping.ontology_id: CHEBI:17634`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolved `CHEBI:17634` as active `D-glucose` with formula `C6H12O6`,
  charge `0`, CAS `50-99-7`, and exact synonyms including `D-(+)-glucose`,
  `D-gluco-hexose`, `dextrose`, and `Traubenzucker`.
- `data/ingredients/mapped/Dextrose.yaml` now has `mapping_status: REJECTED`;
  its history records the merge into this D-glucose record and the later
  tombstone ontology refresh to `CHEBI:17634`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-glucarate.yaml data/ingredients/mapped/D-gluconate.yaml data/ingredients/mapped/D-glucosamine.yaml data/ingredients/mapped/D-glucosaminic_Acid.yaml data/ingredients/mapped/D-glucose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/run_shared_evidence_validator.py`: unavailable
  because the sibling `culturebotai-claw` checkout was absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 1211 rows for
  `CHEBI:17634`, matching `occurrence_statistics.media_count`; the larger
  `total_occurrences: 1250` is consistent with duplicate ingredient
  occurrences across those recipes.
- The `CARBON_SOURCE` role has CultureMech `DATABASE_ENTRY` evidence with the
  original role text and is supported as a media-formulation role for this
  ingredient.
- The `ENERGY_SOURCE` role is supported only by a `COMPUTATIONAL_PREDICTION`
  evidence object whose curator note calls it provisional and recommends
  review.
- The `LITERATURE` evidence entry under `ontology_mapping.evidence` is sourced
  from `PubMed search ('D-Glucose')`, uses PMID `33762358`, and quotes a
  sentence about uptake of `2-deoxy-2-[18F]-fluoro-D-glucose` in FDG/PET. That
  article is about a radiolabeled deoxyglucose tracer, not an independent
  identity source for the MIM D-glucose to ChEBI D-glucose mapping.
- `mappings/ingredient_mappings.sssom.tsv` maps `MIM:D-glucose` to
  `CHEBI:17634` with `skos:exactMatch`, CHEBI object source, and
  same-subject `other` tokens
  `D-(+)-glucose|Traubenzucker|D(+)-Glucose|D-gluco-hexose|Dextrose|aldehydo-D-glucose|CAS:50-99-7`.
  The raw CultureMech `Role:` / `Properties:` strings are filtered and do not
  leak into the final row.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found only this active primary record for `CHEBI:17634`; the other
  primary record is the rejected `Dextrose` tombstone, and remaining hits are
  mixture components or provenance-only discussions in other records.
- The CAS-RN, molecular formula, CultureMech occurrence statistics,
  glucose-family merge history, and final SSSOM row are populated.
- No mixture decomposition is required for the free D-glucose record.

## Recommended Edits

- In `data/ingredients/mapped/D-glucose.yaml`, remove PMID `33762358` from
  `ontology_mapping.evidence` or replace it with evidence that actually
  supports the identity mapping to `CHEBI:17634`.
- Remove the provisional `ENERGY_SOURCE` role or replace its
  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level evidence for
  D-glucose as an energy source in media.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-glucose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
