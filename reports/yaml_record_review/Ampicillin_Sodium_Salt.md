# `data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml`

## Verdict

Needs curation. The `CHEBI:34535` ampicillin-sodium identity is real and no
`MIM:Ampicillin_Sodium_Salt` SSSOM row is exported, but the rejected duplicate
is still present in the mapped aggregate, still carries active chemistry and a
provisional role, and is still listed as `UNREVIEWED` against the live
`Na-ampicillin` record in `mappings/other_cross_record_baseline.tsv`.

## Identity

- Reviewed record: `data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:34535` with
  `ontology_mapping.ontology_id: CHEBI:34535`, source `CHEBI`,
  `mapping_quality: LEXICAL_MATCH`, and `mapping_status: REJECTED`.
- Local OAK and the official ChEBI page resolve `CHEBI:34535` to
  `ampicillin sodium` with formula `C16H18N3O4S.Na`, the stored SMILES and
  InChI, and InChIKey `KLOHDWPABZXLGI-YWUHCJSESA-M`.
- The `MERGED_INTO` history records that this duplicate was merged into the
  live `CHEBI:34535` `Na-ampicillin` record and had SSSOM rows dropped.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amphotericin_A.yaml data/ingredients/mapped/Amphotericin_B.yaml data/ingredients/mapped/Ampicillin.yaml data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml data/ingredients/mapped/Amygdalin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:2682 CHEBI:28971 CHEBI:34535 CHEBI:27613`:
  returned canonical `ampicillin sodium` and the exact structural synonym
  stored on this record for `CHEBI:34535`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:2682 CHEBI:28971 CHEBI:34535 CHEBI:27613`:
  returned the CAS, formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:34535`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/ingredients/mapped/Na-ampicillin.yaml` is the live mapped record for
  `CHEBI:34535`; it has 12 CultureMech memberships and exports the
  `MIM:Na-ampicillin` SSSOM row.
- `mappings/ingredient_mappings.sssom.tsv` row 2029 maps `MIM:Na-ampicillin`
  to `CHEBI:34535`; a hidden/ignored-inclusive search of the SSSOM and
  row-review surfaces found no active `MIM:Ampicillin_Sodium_Salt` SSSOM row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the
  historical synonym-enrichment row as `ALREADY_REPRESENTED`.
- `mappings/other_cross_record_baseline.tsv` still carries
  `MIM:Na-ampicillin` to `MIM:Ampicillin_Sodium_Salt` as `UNREVIEWED`.
- The rejected tombstone still appears in `data/curated/mapped_ingredients.yaml`
  and still carries `chemical_properties` plus a provisional
  `SELECTIVE_AGENT` role.

## Completeness

- The exact ChEBI chemistry, synonym-enrichment review row, merge history, and
  rejected status are populated.
- No occurrence, component, environmental context, discussion, or dataset entry
  is needed on the tombstone.
- The stale aggregate copy, lingering provisional role, and unreviewed
  cross-record baseline row remain active gaps.

## Recommended Edits

- Finish the `Ampicillin_Sodium_Salt` to `Na-ampicillin` retirement by removing
  the rejected tombstone from mapped aggregate exports, dropping active
  chemistry and role facets from the tombstone if they are no longer maintained,
  and marking the `mappings/other_cross_record_baseline.tsv` row reviewed or
  otherwise replacing it with the intended duplicate baseline entry.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
