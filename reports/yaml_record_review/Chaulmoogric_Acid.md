# `data/ingredients/mapped/Chaulmoogric_Acid.yaml`

## Verdict

Pass. The CultureBotHT chaulmoogric-acid record is exactly grounded to active
`CHEBI:27939`, and its formula, non-isomeric InChI, SMILES, exact synonym, zero
occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Chaulmoogric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:27939`,
  `ontology_mapping.ontology_id: CHEBI:27939`,
  `ontology_label: chaulmoogric acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:27939` returns one active ChEBI term labelled
  `chaulmoogric acid` with formula `C18H32O2`, molecular mass `280.452`, exact
  synonym `13-cyclopent-2-en-1-yltridecanoic acid`, and the same non-isomeric
  InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chaninin.yaml data/ingredients/mapped/Charcoal.yaml data/ingredients/mapped/Chartreusin.yaml data/ingredients/mapped/Chaulmoogric_Acid.yaml data/ingredients/mapped/Chelated_Iron_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chaulmoogric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed. The same focused validator also passed for `Charcoal` and
  `Chartreusin`; `Chaninin` and `Chelated_Iron_Solution` were skipped because
  their kg-microbe CURIEs are local registry IDs outside Engine A's OBO prefix
  scope.
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
  `reports` found the active exact `MIM:Chaulmoogric_Acid` SSSOM row, the
  `CONFIRMED` row-review disposition, and matching aggregate and docs rows for
  `CHEBI:27939`.
- PubChem lookup of the stored CAS `502-30-7` returns formula `C18H32O2`,
  title `13-(Cyclopent-2-Enyl)Tridecanoic Acid`, and the same non-isomeric
  InChI as the ChEBI-backed record.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:27939` rows,
  matching the explicit 0/0 `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, exact synonym,
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.
- No component, environment, or dataset entry is required for this concrete
  fatty acid record.

## Recommended Edits

- None for this record.
