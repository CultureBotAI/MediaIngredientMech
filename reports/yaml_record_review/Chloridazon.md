# `data/ingredients/mapped/Chloridazon.yaml`

## Verdict

Pass. The MicrobeDecoder chloridazon import is exactly grounded to active
`CHEBI:81838`, and its formula, InChI, SMILES, MicrobeDecoder source
occurrence, SSSOM row, zero CultureMech occurrence count, and aggregate copy
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Chloridazon.yaml`.
- Identifier and grounding: `identifier: CHEBI:81838`,
  `ontology_mapping.ontology_id: CHEBI:81838`,
  `ontology_label: chloridazon`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct ChEBI and exact OLS lookups for `CHEBI:81838` return one active term
  labelled `chloridazon`. ChEBI publishes formula `C10H8ClN3O`, mass
  `221.647`, SMILES `Nc1cnn(-c2ccccc2)c(=O)c1Cl`, and the same standard InChI
  stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlororaphin.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 4 CHEBI-grounded records in this batch. `Chlororaphin` was
  intentionally skipped because its `kgmicrobe.compound` placeholder CURIE is a
  local registry ID outside Engine A's OBO prefix scope.
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
  `reports` found the active exact `MIM:Chloridazon` SSSOM row, the
  MicrobeDecoder import-review approval, and matching aggregate and docs rows
  for `CHEBI:81838`.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:chloridazon` in `BacDive_Metabolite_utilization` with count
  1, matching the explicit `source_occurrences` entry.
- Hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  plus `data` found no CultureMech membership rows for `CHEBI:81838`, matching
  the explicit 0/0 media-recipe `occurrence_statistics`.
- PubChem lookup by name returned the same formula and InChI as ChEBI/MIM; the
  molecular weight differs only by routine rounding.
- The record carries no synonym, role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, MicrobeDecoder source
  occurrence, SSSOM row, aggregate copy, and docs row are populated and agree.
- `synonyms` is empty, but no local alternate label, rejected label, or
  additional lookup key is required for this exact ChEBI identity.

## Recommended Edits

- None for this record.
