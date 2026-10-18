# `data/ingredients/mapped/Abscisic_Acid.yaml`

## Verdict

Pass with minor issues. The CAS-backed exact `(+)-abscisic acid` identity,
exact synonym, chemistry, SSSOM row, and aggregate copy pass; one historic
auto-backfill `changes` string contains a truncated InChI and SMILES.

## Identity

- Reviewed record: `data/ingredients/mapped/Abscisic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:2365` with
  `ontology_mapping.ontology_id: CHEBI:2365`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- CAS `21293-29-8` resolves through the ChEBI xref to `CHEBI:2365`,
  `(+)-abscisic acid`; the grade correctly records the CAS-RN lookup path
  instead of discarding it as a lexical match.
- The official ChEBI page resolves `CHEBI:2365` to `(+)-abscisic acid` with
  formula `C15H20O4`, CAS `21293-29-8`, and InChIKey
  `JLIDBLDQVAYHNE-YKALOCIXSA-N`.
- PubChem maps CAS `21293-29-8` to CID `5280896`; its formula and InChIKey
  agree with the official ChEBI identity.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Abikoviromycin.yaml data/ingredients/mapped/Abscisic_Acid.yaml data/ingredients/mapped/Aburamycin_A.yaml data/ingredients/mapped/Abyssomicin_B.yaml data/ingredients/mapped/Abyssomicin_D.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Abscisic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:210557 CHEBI:2365`:
  returned `Abikoviromycin`, `(+)-abscisic acid`, and exact synonyms.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:210557 CHEBI:2365`:
  returned formula and structure metadata for `CHEBI:210557` and `CHEBI:2365`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT CAS-RN lookup, official ChEBI record, local OAK metadata,
  and PubChem CID all support the exact `(+)-abscisic acid` identity.
- The stored IUPAC surface is an exact ChEBI synonym for the same compound.
- The SSSOM row maps `MIM:Abscisic_Acid` to `CHEBI:2365` with
  `skos:exactMatch` and exports the exact synonym plus `CAS:21293-29-8`.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI and SMILES, but the live `chemical_properties` values are complete and
  agree with ChEBI and PubChem.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, OAK/OLS
  confirmation row, exact synonym regrading code, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No role, component, source occurrence, environmental context, or discussion
  entry needs review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/Abscisic_Acid.yaml` so it no longer shows truncated
  structure strings. No identity, chemistry, synonym, or SSSOM edit is
  required.
