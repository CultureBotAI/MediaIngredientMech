# `data/ingredients/mapped/Diethyl_Ether.yaml`

## Verdict

Pass. The CultureBotHT record exact-matches active `CHEBI:35702` diethyl ether,
its CAS RN, formula, InChI, and SMILES agree with ChEBI, and the final SSSOM
row exports only true ChEBI synonyms plus `CAS:60-29-7`.

## Identity

- Reviewed record: `data/ingredients/mapped/Diethyl_Ether.yaml`.
- Identifier and grounding: `identifier: CHEBI:35702` with
  `ontology_mapping.ontology_id: CHEBI:35702`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:35702` to active `diethyl ether`, CAS xref
  `60-29-7`, formula `C4H10O`, InChI, SMILES, exact synonyms
  `1,1'-oxydiethane` and `Ether`, and related synonyms for the same compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Diethyl_Ether.yaml data/ingredients/mapped/Diethyl_phosphonate.yaml data/ingredients/mapped/Difucosyllactose.yaml data/ingredients/mapped/Digested_Serum.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Diethyl_Ether.yaml data/ingredients/mapped/Diethyl_phosphonate.yaml data/ingredients/mapped/Difucosyllactose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-record CHEBI subset.
- `uv run --frozen linkml-term-validator validate-data ... Digested_Serum.yaml ... --labels`:
  failed after the four CHEBI records when the local `sqlite:obo:micro`
  adapter hit an incomplete cache with no `rdfs_label_statement` table.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:52019 CHEBI:35702 CHEBI:41962 CHEBI:89917`:
  returned the canonical ChEBI label, synonyms, CAS xref, formula, InChI,
  SMILES, charge, and mass for `CHEBI:35702`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus
  plausibility warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record, generated/indexed copies, and row-review
  rows.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:35702` found only `data/ingredients/mapped/Diethyl_Ether.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:35702` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Diethyl_Ether` to `CHEBI:35702` with `skos:exactMatch`, canonical
  object label `diethyl ether`, CHEBI object source, `1,1'-oxydiethane`,
  `Ether`, and `CAS:60-29-7`.

## Completeness

- CAS RN, formula, InChI, SMILES, curated exact synonyms, CultureBotHT
  provenance, and no-action row-review provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT record with no
  tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
