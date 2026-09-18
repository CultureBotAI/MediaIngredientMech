# `data/ingredients/mapped/4-Deoxypyridoxine.yaml`

## Verdict

Needs curation, major. The exact neutral `CHEBI:65083` mapping, neutral formula,
SMILES, and InChI agree with 4-deoxypyridoxine, but stored CAS `148-51-6`
resolves to 4-deoxypyridoxine hydrochloride and still publishes through SSSOM
`other` on the exact neutral row.

## Identity

- Reviewed record: `data/ingredients/mapped/4-Deoxypyridoxine.yaml`.
- Identifier and grounding: `identifier: CHEBI:65083` with
  `ontology_mapping.ontology_id: CHEBI:65083`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:65083` resolves to `4-deoxypyridoxine`, formula
  `C8H11NO2`, SMILES `Cc1ncc(CO)c(C)c1O`, and the stored neutral InChI.
- PubChem lookup of CAS `148-51-6` resolves to CID `67417`, titled
  `4-Desoxypyridoxine hydrochloride`, whose InChI contains an added `.ClH`
  component.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Amino-5-hydroxymethyl-2-methylpyrimidine.yaml data/ingredients/mapped/4-Anisaldehyde.yaml data/ingredients/mapped/4-Cresol.yaml data/ingredients/mapped/4-Deoxypyridoxine.yaml data/ingredients/mapped/4-Hydroxyacetophenone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Amino-5-hydroxymethyl-2-methylpyrimidine.yaml data/ingredients/mapped/4-Anisaldehyde.yaml data/ingredients/mapped/4-Cresol.yaml data/ingredients/mapped/4-Deoxypyridoxine.yaml data/ingredients/mapped/4-Hydroxyacetophenone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Deoxypyridoxine` to `CHEBI:65083` row, including the stale
  CAS `148-51-6` in `other`.

## Evidence

- The ChEBI identity and structure fields are self-consistent for the neutral
  molecule.
- Major: the CAS RN in `chemical_properties.cas_rn` denotes the hydrochloride
  salt rather than neutral `CHEBI:65083`; exporting it as `CAS:148-51-6` in
  SSSOM `other` makes the exact neutral row carry a salt registry number.
- The OAK/OLS row-review manifest confirms the ChEBI mapping, but it did not
  validate the stored CAS form.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, advisory rows, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, exact synonym, and `ingredient_type` are populated for
  the neutral molecule.
- The CAS is not complete or correct for the neutral modeled form.
- This was a CultureBotHT CAS import with no recipe-count occurrence, so
  `total_occurrences: 0` and `media_count: 0` are expected.

## Recommended Edits

1. Remove or reject `148-51-6` from the neutral `CHEBI:65083` record, or remodel
   the record as a hydrochloride salt if CultureBotHT intended the supplied salt.
2. Rebuild SSSOM so `CAS:148-51-6` no longer publishes as `other` on an exact
   row for neutral 4-deoxypyridoxine.
3. Run `just sync-curated`, rebuild SSSOM and docs, then verify with
   `just validate-all`, `just qc-sssom`, `just qc-roundtrip`, and
   `just validate-terms data/ingredients/mapped/4-Deoxypyridoxine.yaml`.
