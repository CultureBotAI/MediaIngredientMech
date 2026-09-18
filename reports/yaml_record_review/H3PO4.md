# `data/ingredients/mapped/H3PO4.yaml`

## Verdict

Pass with minor issues. The `H3PO4` residual grounding is an exact synonym match
to active `CHEBI:26078` phosphoric acid and the final SSSOM row passes, but the
newer thin record still lacks the CAS, structure, synonym, and ingredient-type
backfills used by older ChEBI records.

## Identity

- Reviewed record: `data/ingredients/mapped/H3PO4.yaml`.
- Identifier and grounding: `identifier: CHEBI:26078` with
  `ontology_mapping.ontology_id: CHEBI:26078`, label `phosphoric acid`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `match_level: NORMALIZED`, and `mapping_status: MAPPED`.
- Occurrence statistics: `total_occurrences: 2` and `media_count: 2`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H2tetramethylammonium.yaml data/ingredients/mapped/H2trimethylamine.yaml data/ingredients/mapped/H2wo4.yaml data/ingredients/mapped/H3PO4.yaml data/ingredients/mapped/H3bo2.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:26078`.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:26078` as active `phosphoric acid` and lists `H3PO4` as
  a synonym.
- OLS4 also exposes CAS `7664-38-2`, formula `H3O4P`, InChI
  `InChI=1S/H3O4P/c1-5(2,3)4/h(H3,1,2,3,4)`, and SMILES
  `[H]OP(=O)(O[H])O[H]` for the target.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:H3PO4` to
  `CHEBI:26078` and carries the restored CultureMech occurrence-table
  provenance.
- Minor: the record has not been backfilled with `ingredient_type:
  SINGLE_INGREDIENT`, `chemical_properties.cas_rn`, formula, InChI, SMILES, or
  ChEBI synonyms even though those values are available from `CHEBI:26078`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found this active YAML, matching
  aggregate copies, generated products, final SSSOM, and the CultureMech
  residual-grounding row.

## Completeness

- The active ChEBI target and final SSSOM row are present and consistent.
- The record is incomplete only in local enrichment fields that the older
  ChEBI-primary records usually carry.

## Recommended Edits

- Minor: run or reproduce the standard ChEBI enrichment so `H3PO4` gains
  `ingredient_type`, CAS RN, formula, InChI, SMILES, and appropriate exact
  synonyms for `CHEBI:26078`.
