# `data/ingredients/mapped/7-hydroxyflavone.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:2268` identity, CAS, synonym,
chemistry, SSSOM row, and aggregate copy pass; one historic auto-backfill
`changes` string contains a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/7-hydroxyflavone.yaml`.
- Identifier and grounding: `identifier: CHEBI:2268` with
  `ontology_mapping.ontology_id: CHEBI:2268`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:2268` to `7-hydroxyflavone` with
  formula `C15H10O3`, CAS `6665-86-7`, SMILES
  `O=c1cc(-c2ccccc2)oc2cc(O)ccc12`, and InChIKey
  `MQGPSCMMNJKMHQ-UHFFFAOYSA-N`.
- Local OAK metadata carries the same formula, structure strings, average mass,
  monoisotopic mass, CAS xref, and exact synonym
  `7-hydroxy-2-phenyl-4H-chromen-4-one`.
- PubChem maps CAS `6665-86-7` to CID `5281894`, whose formula and InChIKey
  agree with ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-methoxy-2_3h-benzoxazolone.yaml data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/7-hydroxyflavone.yaml data/ingredients/mapped/72-Dihydroxyflavone.yaml data/ingredients/mapped/8-azaguanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/7-hydroxyflavone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:173101 CHEBI:2268 CHEBI:94071 CHEBI:63486`:
  returned the expected ChEBI label and exact synonym for `CHEBI:2268`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:173101 CHEBI:2268 CHEBI:94071 CHEBI:63486`:
  returned the expected formula, structure strings, CAS xref, and mass for
  `CHEBI:2268`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The active ChEBI term, CAS, formula, SMILES, and InChI all support the exact
  7-hydroxyflavone identity.
- The stored exact synonym is ChEBI's IUPAC name and is exported as an exact
  SSSOM `other` surface along with `CAS:6665-86-7`.
- The SSSOM row maps `MIM:7-hydroxyflavone` to `CHEBI:2268` with
  `skos:exactMatch`; row review already confirmed the OAK/OLS identity and
  required no action.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI after `/c16-11-6-7-12-13(17)9-14(18-15(1`, but the live
  `chemical_properties.inchi` value is complete and matches ChEBI.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, source review
  confirmation, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/7-hydroxyflavone.yaml` so it no longer shows a
  truncated InChI. No identity, chemistry, synonym, or SSSOM edit is required.
