# `data/ingredients/mapped/3-trichloropropane.yaml`

## Verdict

Needs curation, major. The exact repaired mapping to `CHEBI:34036`, ChEBI/PubChem
chemistry, microbedecoder source occurrence, SSSOM row, and aggregate row pass,
but the impossible dropped-locant text `3-trichloropropane` remains as a
`RAW_TEXT` synonym and therefore still publishes in the SSSOM `other` field.

## Identity

- Reviewed record: `data/ingredients/mapped/3-trichloropropane.yaml`.
- Identifier and grounding: `identifier: CHEBI:34036` with
  `ontology_mapping.ontology_id: CHEBI:34036`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:34036` resolves to `1,2,3-Trichloropropane`,
  formula `C3H5Cl3`, net charge `0`, SMILES `ClCC(Cl)CCl`, and InChI
  `InChI=1S/C3H5Cl3/c4-1-3(6)2-5/h3H,1-2H2`; the record matches.
- The direct microbedecoder `BacDive_Metabolite_utilization` count of 1 is
  preserved under `source_occurrences`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:3-trichloropropane` to `CHEBI:34036` row, including the stale
  `other` value `3-trichloropropane`.

## Evidence

- The target mapping was correctly repaired to the full 1,2,3-trichloropropane
  ChEBI term after `scripts/apply_locant_corrections.py` identified the original
  raw label as a comma-splitting dropped-locant artifact.
- Major: the rejected artifact is still stored as a `RAW_TEXT` synonym. Because
  SSSOM generation exports `IngredientRecord.synonyms` into `other`, the active
  SSSOM row still advertises `3-trichloropropane` as a label for `CHEBI:34036`.
- Minor: the top-level `notes` field still says there was no CAS-RN or
  CHEBI/NCIT match and curator review was needed, even though the record is now
  mapped and structurally enriched.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, generated docs, dropped-locant repair
  script, source import rows, advisory TSVs, and ignored aggregate backups.

## Completeness

- Formula, molecular weight, InChI, and SMILES are populated from ChEBI/PubChem.
- The direct microbedecoder occurrence is traceable as the source of the
  malformed input label.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

1. Remove or reject the `3-trichloropropane` `RAW_TEXT` synonym so this
   impossible dropped-locant artifact no longer ships in SSSOM `other`.
2. Replace the stale top-level `notes` text with the durable explanation already
   present on the mapping evidence: the original source label was a
   dropped-locant artifact of `1,2,3-trichloropropane`.
3. Run `just sync-curated`, rebuild SSSOM and docs, then verify with
   `just validate-all`, `just qc-sssom`, `just qc-roundtrip`, and
   `just validate-terms data/ingredients/mapped/3-trichloropropane.yaml`.
