# `data/ingredients/mapped/Adenosine.yaml`

## Verdict

Pass with minor issues. The CAS-backed `CHEBI:16335` identity, kg-microbe
synonyms, ChEBI/PubChem chemistry, occurrence count, SSSOM row, and aggregate
copy pass; one historical auto-backfill change string has a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/Adenosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16335` with
  `ontology_mapping.ontology_id: CHEBI:16335`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:16335` to `adenosine`
  with formula `C10H13N5O4`, CAS `58-61-7`, SMILES, InChI, and InChIKey
  `OIRDTQYFTABQOQ-KQYNXXCUSA-N`.
- Local OAK lists the stored kg-microbe synonym strings as aliases on
  `CHEBI:16335`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml data/ingredients/mapped/Adenomycin.yaml data/ingredients/mapped/Adenosine.yaml data/ingredients/mapped/Adenosine_35-Cyclic_Monophosphate.yaml data/ingredients/mapped/Adenosine_5-monophosphate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Adenosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:16335 CHEBI:17489 CHEBI:16027 CHEBI:16708`:
  returned the expected labels and aliases for the ChEBI targets in this batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16335 CHEBI:17489 CHEBI:16027 CHEBI:16708`:
  returned formula and structure metadata for all four ChEBI terms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The PubChem CAS xref and official ChEBI record support the exact
  `CHEBI:16335` identity.
- The official ChEBI page and local OAK metadata support the stored formula,
  SMILES, and InChI.
- `mappings/culturemech_recipe_membership.tsv` contains 14 rows for
  `CHEBI:16335`, matching `occurrence_statistics`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirms `CHEBI:16335`;
  `mappings/ingredient_mappings.sssom.tsv` row 347 maps `MIM:Adenosine` to
  `CHEBI:16335` with the confirmed trailer.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, OAK/OLS confirmation row, occurrence rows, component
  references in `NLDM_metabolites`, generated indexes, and ignored aggregate
  backups.

## Completeness

- CAS, formula, SMILES, InChI, aliases, occurrence statistics, curation history,
  and `ingredient_type` are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Optionally annotate the stale 2026-05-01 history `changes` prose in
  `data/ingredients/mapped/Adenosine.yaml`; the active `chemical_properties`
  fields are already correct.
