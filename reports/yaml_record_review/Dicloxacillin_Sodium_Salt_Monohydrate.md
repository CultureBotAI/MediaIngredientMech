# `data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml`

## Verdict

Needs curation. The CultureBotHT CAS lookup resolves to the correct hydrated
dicloxacillin sodium ChEBI term, and the structure plus final SSSOM synonym
payload pass. The `SELECTIVE_AGENT` role is still only a provisional
name-pattern inference.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:52019` with
  `ontology_mapping.ontology_id: CHEBI:52019`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:52019` to active
  `dicloxacillin sodium monohydrate`, CAS xref `13412-64-1`, formula
  `C19H16Cl2N3O5S.H2O.Na`, InChI, SMILES, exact synonym
  `sodium 6beta-{[3-(2,6-dichlorophenyl)-5-methyl-1,2-oxazol-4-yl]carboxamido}-2,2-dimethylpenam-3alpha-carboxylate--water (1/1)`,
  and related sodium hydrate synonyms for the same form.

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
  SMILES, charge, and mass for `CHEBI:52019`.
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
  `CHEBI:52019` found only
  `data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv`,
  `mappings/ingredient_mappings_synonym_enrich_review.tsv`, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` agree that the
  `CHEBI:52019` mapping needs no row-review action; the proposed
  `Dicloxacillin sodium salt monohydrate` synonym is already represented by
  `preferred_term`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dicloxacillin_Sodium_Salt_Monohydrate` to `CHEBI:52019` with
  `skos:exactMatch`, canonical object label
  `dicloxacillin sodium monohydrate`, CHEBI object source, the exact ChEBI
  synonym, and `CAS:13412-64-1`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from the curated name-pattern rule. The
  record needs source-backed evidence that this supplied form was used as a
  selective agent in the represented panel or recipe context.

## Completeness

- CAS RN, formula, InChI, SMILES, CultureBotHT provenance, CAS lookup regrade
  history, and row-review provenance are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT panel record with
  no tracked CultureMech recipe memberships; supplied forms, mixture
  components, and environmental contexts are correctly empty.

## Recommended Edits

- Major: replace the `SELECTIVE_AGENT` computational role in
  `data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml` with
  source-backed role evidence scoped to dicloxacillin sodium monohydrate, or
  remove the role if no support is available; then synchronize
  `data/curated/mapped_ingredients.yaml`.
