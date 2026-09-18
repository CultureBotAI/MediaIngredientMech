# `data/ingredients/mapped/5-methyluridine.yaml`

## Verdict

Pass, none. The CAS-backed exact `CHEBI:45996` ribothymidine identity,
CAS, synonyms, chemistry, occurrence count, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/5-methyluridine.yaml`.
- Identifier and grounding: `identifier: CHEBI:45996` with
  `ontology_mapping.ontology_id: CHEBI:45996`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:45996` to `ribothymidine` with
  formula `C10H14N2O6`, the stored SMILES, and the stored InChI.
- Local OAK metadata carries `cas:1463-10-1`, exact synonym `5-methyluridine`,
  and the related synonyms `1-(beta-D-ribofuranosyl)thymine`, `Thymine
  riboside`, and `ribosylthymidine`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-deoxy-5-_Methylthioadenosine.yaml data/ingredients/mapped/5-didehydro-D-gluconic_Acid.yaml data/ingredients/mapped/5-fluorouracil.yaml data/ingredients/mapped/5-methyluridine.yaml data/ingredients/mapped/5-oxoproline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-methyluridine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the official exact and related synonym set for `CHEBI:45996`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the expected ChEBI formula, structure strings, CAS xref, and mass
  for `CHEBI:45996`.

## Evidence

- The active ChEBI term, OAK `cas:1463-10-1` xref, formula, SMILES, InChI, and
  official synonyms support the 5-methyluridine/ribothymidine identity.
- The refreshed occurrence count of 10 is traceable to
  `mappings/culturemech_recipe_membership.tsv`, which contains ten distinct
  CultureMech recipe rows for `CHEBI:45996`.
- The SSSOM row maps `MIM:5-methyluridine` to `CHEBI:45996` with
  `skos:exactMatch`, preserves the PubChem CAS-cross-reference provenance, and
  exports three exact source synonyms plus `CAS:1463-10-1` in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, source review confirmation, CultureMech membership rows, an unrelated
  thymidine record whose synonyms deliberately include deoxy-5-methyluridine
  labels, a component reference in `NLDM_metabolites`, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, official synonyms, occurrence counts,
  `ingredient_type`, and the creation note are populated.
- No roles, environmental context, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
