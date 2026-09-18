# `data/ingredients/mapped/Aloin.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:73222` identity, CAS xref,
CultureBotHT source, ChEBI/PubChem chemistry, exact synonym, SSSOM row, and
aggregate copy pass; only one historical auto-backfill event has truncated
structure prose.

## Identity

- Reviewed record: `data/ingredients/mapped/Aloin.yaml`.
- Identifier and grounding: `identifier: CHEBI:73222` with
  `ontology_mapping.ontology_id: CHEBI:73222`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:73222` to `aloin` with
  formula `C21H22O9`, SMILES
  `[H][C@@]1(C2c3cccc(O)c3C(=O)c3c(O)cc(CO)cc32)O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O`,
  and InChIKey `AFHJQYHRLPMKHU-CGISPIQUSA-N`.
- ChEBI models `CHEBI:73222` as the diastereoisomeric mixture of aloin A and
  aloin B; the generic label `Aloin` therefore agrees with the ontology scope.
- PubChem resolves CAS `5133-19-7` to aloin/barbaloin names, supporting the
  CultureBotHT CAS assignment.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Allura_Red_AC.yaml data/ingredients/mapped/Aloin.yaml data/ingredients/mapped/Alpha-D-glucose_6-phosphate.yaml data/ingredients/mapped/Alpha-L-rhamnose.yaml data/ingredients/mapped/Alpha-Lactose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Aloin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned canonical `aloin` and the stored exact synonym for `CHEBI:73222`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:73222`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` row 244 confirmed the
  `MIM:Aloin` to `CHEBI:73222` mapping.
- `mappings/ingredient_mappings.sssom.tsv` row 372 maps `MIM:Aloin` to
  `CHEBI:73222` with `skos:exactMatch`, exports CAS `5133-19-7`, and includes
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
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` history event has truncated InChI and
  SMILES prose, but the current `chemical_properties` values are complete.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Optionally replace the truncated auto-backfill `changes` prose in
  `data/ingredients/mapped/Aloin.yaml` with a complete structure summary or a
  concise non-structural note. No identity, mapping, or exported SSSOM change
  is needed.
