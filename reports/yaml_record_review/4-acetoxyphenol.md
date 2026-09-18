# `data/ingredients/mapped/4-acetoxyphenol.yaml`

## Verdict

Pass, none. The CAS-backed `CHEBI:31128` identity, chemistry, SSSOM row, and
aggregate row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-acetoxyphenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:31128` with
  `ontology_mapping.ontology_id: CHEBI:31128`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:31128` is active, resolves to
  `4-hydroxyphenyl acetate`, has formula `C8H8O3`, CAS `3233-32-7`, SMILES
  `CC(=O)Oc1ccc(O)cc1`, and the stored InChI.
- PubChem CAS lookup for `3233-32-7` resolves to CID `96009` with formula
  `C8H8O3` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-acetoxyphenol` to `CHEBI:31128` row.

## Evidence

- The CultureBotHT CAS lookup, current ChEBI CAS xref, PubChem CAS lookup,
  formula, InChI, and SMILES all support the same ester identity.
- The August `CAS_RN_LOOKUP` grade correctly records that the CAS xref, not a
  primary-label match, established the mapping to the canonical
  `4-hydroxyphenyl acetate` label.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- The SSSOM `other` field carries only `CAS:3233-32-7`; no rejected or broader
  synonym is exported for this record.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, stale advisory rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, and `ingredient_type` are populated.
- This CultureBotHT CAS import has no recipe-count occurrence; no role,
  component, environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
