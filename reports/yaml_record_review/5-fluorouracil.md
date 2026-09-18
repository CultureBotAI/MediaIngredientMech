# `data/ingredients/mapped/5-fluorouracil.yaml`

## Verdict

Pass, none. The exact `CHEBI:46345` identity, CAS, exact synonym, chemistry,
occurrence count, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/5-fluorouracil.yaml`.
- Identifier and grounding: `identifier: CHEBI:46345` with
  `ontology_mapping.ontology_id: CHEBI:46345`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:46345` to `5-fluorouracil` with
  formula `C4H3FN2O2`, CAS `51-21-8`, the stored SMILES, and the stored
  InChI.
- Local OAK metadata carries the same formula, structure strings, CAS xref,
  and exact synonym `5-fluoropyrimidine-2,4(1H,3H)-dione`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-deoxy-5-_Methylthioadenosine.yaml data/ingredients/mapped/5-didehydro-D-gluconic_Acid.yaml data/ingredients/mapped/5-fluorouracil.yaml data/ingredients/mapped/5-methyluridine.yaml data/ingredients/mapped/5-oxoproline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-fluorouracil.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the official exact and related synonym set for `CHEBI:46345`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the expected ChEBI formula, structure strings, CAS xref, and mass
  for `CHEBI:46345`.

## Evidence

- The active ChEBI term, CAS, formula, SMILES, InChI, and exact ChEBI synonym
  all support the 5-fluorouracil identity.
- The refreshed occurrence count of 1 is traceable to
  `mappings/culturemech_recipe_membership.tsv`, which contains one
  CultureMech recipe row for `CHEBI:46345`.
- The SSSOM row maps `MIM:5-fluorouracil` to `CHEBI:46345` with
  `skos:exactMatch` and exports the exact systematic synonym plus `CAS:51-21-8`
  in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, source review confirmation, one distinct dihydrofluorouracil record, the
  microbedecoder source label, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, exact ChEBI synonym, occurrence counts, and
  `ingredient_type` are populated.
- No roles, components, environmental context, or discussion entries need
  review.

## Recommended Edits

No YAML edit is required for this record.
