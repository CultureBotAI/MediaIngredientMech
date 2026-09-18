# `data/ingredients/mapped/6-methoxy-2_3h-benzoxazolone.yaml`

## Verdict

Pass with minor issues. The Coixol ChEBI identity, CAS, synonym, chemistry,
SSSOM row, and aggregate copy pass; one historic auto-backfill `changes` string
contains a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/6-methoxy-2_3h-benzoxazolone.yaml`.
- Identifier and grounding: `identifier: CHEBI:173101` with
  `ontology_mapping.ontology_id: CHEBI:173101`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:173101` to `Coixol` with formula
  `C8H7NO3`, SMILES `COc1ccc2nc(=O)oc2c1`, and InChIKey
  `MKMCJLMBVKHUMS-UHFFFAOYSA-N`.
- Local OAK metadata carries the same formula, structure strings, average mass,
  monoisotopic mass, CAS `532-91-2`, and exact synonym
  `6-methoxy-3H-1,3-benzoxazol-2-one`.
- PubChem maps CAS `532-91-2` to CID `10772`, whose formula and InChIKey agree
  with ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-methoxy-2_3h-benzoxazolone.yaml data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/7-hydroxyflavone.yaml data/ingredients/mapped/72-Dihydroxyflavone.yaml data/ingredients/mapped/8-azaguanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/6-methoxy-2_3h-benzoxazolone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:173101 CHEBI:2268 CHEBI:94071 CHEBI:63486`:
  returned the expected ChEBI label and exact synonym for `CHEBI:173101`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:173101 CHEBI:2268 CHEBI:94071 CHEBI:63486`:
  returned the expected formula, structure strings, CAS xref, and mass for
  `CHEBI:173101`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The active ChEBI term supports the Coixol identity, while its exact synonym
  supports the record's `6-methoxy-2(3H)-benzoxazolone` preferred term.
- CAS `532-91-2`, the ChEBI metadata, and PubChem CID `10772` agree on the
  neutral `C8H7NO3` structure.
- The SSSOM row maps `MIM:6-methoxy-2_3h-benzoxazolone` to `CHEBI:173101` with
  `skos:exactMatch` and exports `6-methoxy-3H-1,3-benzoxazol-2-one` and
  `CAS:532-91-2` as exact `other` surfaces.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI after `/h`, but the live `chemical_properties.inchi` value is complete
  and matches ChEBI.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, row-review
  synonym confirmation, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/6-methoxy-2_3h-benzoxazolone.yaml` so it no longer
  shows a truncated InChI. No identity, chemistry, synonym, or SSSOM edit is
  required.
