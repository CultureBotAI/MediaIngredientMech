# `data/ingredients/mapped/8-hydroxy-nitroquinoline.yaml`

## Verdict

Pass with minor issues. The CAS-backed nitroxoline identity, exact ChEBI
synonym, chemistry, SSSOM row, and aggregate copy pass; one historic
auto-backfill `changes` string contains a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/8-hydroxy-nitroquinoline.yaml`.
- Identifier and grounding: `identifier: CHEBI:67121` with
  `ontology_mapping.ontology_id: CHEBI:67121`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:67121` to `nitroxoline` with formula
  `C9H6N2O3`, SMILES `O=[N+]([O-])c1ccc(O)c2ncccc12`, and InChIKey
  `RJIWZDNTCBHXAL-UHFFFAOYSA-N`.
- Local OAK metadata carries the same formula, structure strings, average mass,
  monoisotopic mass, CAS `4008-48-4`, and exact synonym
  `5-nitroquinolin-8-ol`.
- PubChem maps CAS `4008-48-4` to CID `19910`, whose formula and InChIKey agree
  with ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/8-hydroxy-nitroquinoline.yaml data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml data/ingredients/mapped/A-Cyclodextrin.yaml data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/AQDS.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/8-hydroxy-nitroquinoline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected ChEBI label and exact synonym for `CHEBI:67121`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected formula, structure strings, CAS xref, and mass for
  `CHEBI:67121`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- CAS `4008-48-4`, PubChem CID `19910`, local OAK metadata, and the official
  ChEBI page all support the exact nitroxoline identity.
- The stored `5-nitroquinolin-8-ol` synonym is the ChEBI exact synonym and
  correctly disambiguates the source label's nitro locant.
- The SSSOM row maps `MIM:8-hydroxy-nitroquinoline` to `CHEBI:67121` with
  `skos:exactMatch`, exports `CAS:4008-48-4`, and keeps
  `CAS_RN_LOOKUP` as the active mapping grade under Rule D.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI after `/c12-8-4-3-7(11(13)14)6-2-1-5-10-`, but the live
  `chemical_properties.inchi` value is complete and matches ChEBI.
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
  `data/ingredients/mapped/8-hydroxy-nitroquinoline.yaml` so it no longer shows
  a truncated InChI. No identity, chemistry, synonym, or SSSOM edit is
  required.
