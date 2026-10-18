# `data/ingredients/mapped/Abietic_Acid.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:28987` identity, CAS, synonym,
chemistry, SSSOM row, and aggregate copy pass; one historic auto-backfill
`changes` string contains truncated structure strings.

## Identity

- Reviewed record: `data/ingredients/mapped/Abietic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:28987` with
  `ontology_mapping.ontology_id: CHEBI:28987`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:28987` to `abietic acid` with formula
  `C20H30O2`, CAS `514-10-3`, the stored SMILES, and InChIKey
  `RSWGJHLUYNHPMX-ONCXSQPRSA-N`.
- Local OAK metadata carries the same formula, structure strings, CAS xref, and
  exact synonym `abieta-7,13-dien-18-oic acid`.
- PubChem maps CAS `514-10-3` to CID `10569`, whose formula and InChIKey agree
  with ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix.yaml data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix_Minus_Iron.yaml data/ingredients/mapped/ATCC_Wolfes_Vitamin_Mix.yaml data/ingredients/mapped/A_Trace_Components.yaml data/ingredients/mapped/Abietic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Abietic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:28987 CHEBI:4735 CHEBI:31795 CHEBI:86364 CHEBI:26710 CHEBI:75836 CHEBI:53503 CHEBI:3312 CHEBI:32312 CHEBI:31440 CHEBI:86465 CHEBI:33118 CHEBI:75213 CHEBI:15377 CHEBI:15956 CHEBI:27470 CHEBI:30961 CHEBI:49105 CHEBI:17015 CHEBI:15940 CHEBI:31345 CHEBI:176843 CHEBI:30753 CHEBI:16494`:
  returned the expected ChEBI label and exact synonym for `CHEBI:28987`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- CAS `514-10-3`, PubChem CID `10569`, local OAK metadata, and the official
  ChEBI page all support the exact abietic acid identity.
- The stored `abieta-7,13-dien-18-oic acid` synonym is the ChEBI exact synonym.
- The SSSOM row maps `MIM:Abietic_Acid` to `CHEBI:28987` with
  `skos:exactMatch` and exports the exact synonym and `CAS:514-10-3`.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI and SMILES, but the live `chemical_properties` values are complete and
  match ChEBI.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, OAK/OLS
  confirmation row, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/Abietic_Acid.yaml` so it no longer shows truncated
  structure strings. No identity, chemistry, synonym, or SSSOM edit is
  required.
