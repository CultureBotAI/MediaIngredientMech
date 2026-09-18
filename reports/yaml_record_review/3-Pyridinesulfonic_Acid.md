# `data/ingredients/mapped/3-Pyridinesulfonic_Acid.yaml`

## Verdict

Pass, none. The `cas:636-73-7` registry fallback is internally consistent,
PubChem resolves the same acid and structure, SSSOM carries the expected CAS
registry row, and the aggregate row is synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/3-Pyridinesulfonic_Acid.yaml`.
- Identifier and grounding: `identifier: cas:636-73-7` with matching
  `ontology_mapping.ontology_id`, source `CAS`, `mapping_quality:
  FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- Registry check: resolving CAS `636-73-7` through PubChem returned CID `69468`,
  formula `C5H5NO3S`, SMILES `C1=CC(=CN=C1)S(=O)(=O)O`, the same standard
  InChI recorded in the YAML, and the IUPAC name `pyridine-3-sulfonic acid`.
- The PubChem PUG-View record for CID `69468` lists the CAS RN and matching
  synonyms but no direct ChEBI cross-reference; the row-review triage likewise
  treats this CAS CURIE as an expected registry identifier rather than a missed
  ontology term.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Pyridinesulfonic_Acid.yaml data/ingredients/mapped/3-_N-morpholinopropanesulfonic_Acid.yaml data/ingredients/mapped/3-acetylpyridine.yaml data/ingredients/mapped/3-aminobenzoate.yaml data/ingredients/mapped/3-aminobutyrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Pyridinesulfonic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  unavailable; the local `cas:` adapter opened a SQLite DB without
  `rdfs_label_statement`, so the check crashed before judging this record.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Pyridinesulfonic_Acid` to `cas:636-73-7` registry row with
  `CAS:636-73-7` in `other`.

## Evidence

- The PubChem response corroborates the CAS fallback's formula, SMILES, and
  InChI.
- The OAK/OLS row-review triage already marks `cas:636-73-7` as
  `expected_registry_identifier`; CAS registry CURIEs are not expected to
  resolve as ontology terms.
- The batch-review ontology and CURIE warnings for `cas:636-73-7` are advisory
  false positives for an intentional fallback registry identifier.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, unknown-term triage, generated docs, and advisory batch
  rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS, PubChem CID, formula, InChI, and SMILES are populated.
- No record-local curation defect remains.

## Recommended Edits

No YAML edit is required for this record.
