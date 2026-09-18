# `data/ingredients/mapped/5-deoxy-5-_Methylthioadenosine.yaml`

## Verdict

Pass with minor issues. The CAS-backed exact `CHEBI:17509` identity, exact
synonym, chemistry, SSSOM row, and aggregate copy pass; one historic auto-
backfill `changes` string contains a truncated InChI.

## Identity

- Reviewed record:
  `data/ingredients/mapped/5-deoxy-5-_Methylthioadenosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17509` with
  `ontology_mapping.ontology_id: CHEBI:17509`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:17509` to
  `5'-S-methyl-5'-thioadenosine` with formula `C11H15N5O3S`, CAS
  `2457-80-9`, the stored SMILES, and the stored InChI.
- Local OAK metadata carries the same CAS xref and exact synonym
  `5'-deoxy-5'-(methylsulfanyl)adenosine`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-deoxy-5-_Methylthioadenosine.yaml data/ingredients/mapped/5-didehydro-D-gluconic_Acid.yaml data/ingredients/mapped/5-fluorouracil.yaml data/ingredients/mapped/5-methyluridine.yaml data/ingredients/mapped/5-oxoproline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-deoxy-5-_Methylthioadenosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the official exact and related synonym set for `CHEBI:17509`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the expected ChEBI formula, structure strings, CAS xref, and mass
  for `CHEBI:17509`.

## Evidence

- The active ChEBI term, OAK `cas:2457-80-9` xref, stored formula, stored
  SMILES, stored InChI, and exact ChEBI synonym support the
  5'-S-methyl-5'-thioadenosine identity.
- The SSSOM row maps `MIM:5-deoxy-5-_Methylthioadenosine` to `CHEBI:17509`
  with `skos:exactMatch`, `5'-deoxy-5'-(methylsulfanyl)adenosine|CAS:2457-80-9`
  in `other`, and the expected `CAS_RN_LOOKUP` manual provenance.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI after `.../c1-20-2-5-7(17)8(18)11(19-5)1`, but the live
  `chemical_properties.inchi` value is complete and matches ChEBI.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, stale encoded MIM alias, row-review confirmation, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/5-deoxy-5-_Methylthioadenosine.yaml` so it no
  longer shows a truncated InChI. No identity, chemistry, or SSSOM edit is
  required.
