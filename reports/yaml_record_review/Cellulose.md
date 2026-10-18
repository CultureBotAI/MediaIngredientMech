# `data/ingredients/mapped/Cellulose.yaml`

## Verdict

Needs curation; major issue. The exact ChEBI cellulose grounding, CAS, formula,
InChI, SMILES, 45 CultureMech memberships, SSSOM row, and aggregate copy agree,
but several non-label `Optional ingredient...` strings still publish as
resolving synonyms, and the `CARBON_SOURCE` role is only a provisional ChEBI
ancestry prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Cellulose.yaml`.
- Identifier and grounding: `identifier: CHEBI:18246`,
  `ontology_mapping.ontology_id: CHEBI:18246`,
  `ontology_label: (1->4)-beta-D-glucan`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:18246` returns one active ChEBI term labelled
  `(1->4)-beta-D-glucan` with formula `(C6H10O5)n.H2O`, molecular mass
  `180.156`, and the same InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cellulose.yaml data/ingredients/mapped/Cellulose_powder.yaml data/ingredients/mapped/Cephalexin.yaml data/ingredients/mapped/Cephalosporin.yaml data/ingredients/mapped/Cephalothin.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cellulose.yaml data/ingredients/mapped/Cellulose_powder.yaml data/ingredients/mapped/Cephalexin.yaml data/ingredients/mapped/Cephalosporin.yaml data/ingredients/mapped/Cephalothin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact `MIM:Cellulose` SSSOM row, the
  `SYNONYM_ENRICH` row-review disposition, the synonym-enrichment
  `ALREADY_REPRESENTED` row, the later CultureMech alias-backfill row, and
  matching aggregate/docs rows for `CHEBI:18246`.
- `mappings/culturemech_recipe_membership.tsv` contains 45 `CHEBI:18246`
  memberships with 45 total occurrences, matching `occurrence_statistics`.
- The final SSSOM `other` field still contains `Optional ingredient`,
  `Optional ingredient (Avicel SIGMA)`,
  `Optional ingredient (Lens tissue or MN 301)`, and
  `Optional ingredient (MN 301)`. These are recipe annotations, not cellulose
  names; `docs/data/label_index.csv` also flags the bare `Optional ingredient`
  string as a cross-record conflict.
- `CARBON_SOURCE` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_chebi_ancestry` and is explicitly marked "Provisional role
  inferred from CHEBI is_a/has_role closure; review recommended."

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, kg-microbe exact
  synonyms, SSSOM row, aggregate copy, docs row, and CultureMech occurrence
  count are populated and agree.
- The only consequential gaps are the optional-ingredient strings exported as
  synonyms and the provisional carbon-source role.

## Recommended Edits

- Major: remove or reject the four `Optional ingredient...` `RAW_TEXT` synonym
  entries so they no longer publish as cellulose labels.
- Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected
  evidence for cellulose as a carbon source in media, or remove the role, then
  rerun strict validation, SSSOM QC, aggregate roundtrip, synonym export checks,
  and `git diff --check`.
