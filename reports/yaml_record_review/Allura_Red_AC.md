# `data/ingredients/mapped/Allura_Red_AC.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:172687` identity, CAS xref,
CultureBotHT source, ChEBI/PubChem chemistry, exact synonym, SSSOM row, and
aggregate copy pass; only one historical auto-backfill event has truncated
structure prose.

## Identity

- Reviewed record: `data/ingredients/mapped/Allura_Red_AC.yaml`.
- Identifier and grounding: `identifier: CHEBI:172687` with
  `ontology_mapping.ontology_id: CHEBI:172687`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:172687` to
  `Allura red AC` with formula `C18H14N2O8S2.2Na`, SMILES
  `COc1cc(S(=O)(=O)[O-])c(C)cc1/N=N/c1c(O)ccc2cc(S(=O)(=O)[O-])ccc12.[Na+].[Na+]`,
  and InChIKey `CEZCCHQBSQPRMU-LLIZZRELSA-L`.
- PubChem resolves CAS `25956-17-6` to Allura Red AC and related FD&C Red 40
  names, supporting the CultureBotHT CAS assignment.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Allura_Red_AC.yaml data/ingredients/mapped/Aloin.yaml data/ingredients/mapped/Alpha-D-glucose_6-phosphate.yaml data/ingredients/mapped/Alpha-L-rhamnose.yaml data/ingredients/mapped/Alpha-Lactose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Allura_Red_AC.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned canonical `Allura red AC` and the stored exact synonym for
  `CHEBI:172687`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:172687`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` row 243 confirmed the
  `MIM:Allura_Red_AC` to `CHEBI:172687` mapping.
- `mappings/ingredient_mappings.sssom.tsv` row 371 maps `MIM:Allura_Red_AC` to
  `CHEBI:172687` with `skos:exactMatch`, exports CAS `25956-17-6`, and includes
  the only curated exact synonym.
- The ChEBI page and local ChEBI metadata support the stored formula, SMILES,
  and InChI.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated indexes,
  and ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, the exact ChEBI synonym, curation history, and
  `ingredient_type` are populated.
- `occurrence_statistics` is correctly `0/0` because the record comes from
  CultureBotHT rather than from CultureMech recipe membership.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` history event has truncated formula,
  InChI, and SMILES prose, but the current `chemical_properties` values are
  complete.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Optionally replace the truncated auto-backfill `changes` prose in
  `data/ingredients/mapped/Allura_Red_AC.yaml` with a complete structure
  summary or a concise non-structural note. No identity, mapping, or exported
  SSSOM change is needed.
