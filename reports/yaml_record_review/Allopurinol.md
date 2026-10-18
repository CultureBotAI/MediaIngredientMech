# `data/ingredients/mapped/Allopurinol.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:40279` identity, CAS xref, CultureBotHT
source, chemistry, exact synonym, SSSOM row, and aggregate copy pass; only one
historical auto-backfill event has truncated structure prose.

## Identity

- Reviewed record: `data/ingredients/mapped/Allopurinol.yaml`.
- Identifier and grounding: `identifier: CHEBI:40279` with
  `ontology_mapping.ontology_id: CHEBI:40279`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:40279` to
  `allopurinol` with formula `C5H4N4O`, CAS `315-30-0`, SMILES
  `Oc1ncnc2nncc12`, and InChIKey `OFCNXPDARWKPPY-UHFFFAOYSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alginate.yaml data/ingredients/mapped/Alk_So42.yaml data/ingredients/mapped/Alk_So42_X_12_H2o.yaml data/ingredients/mapped/Allantoin.yaml data/ingredients/mapped/Allopurinol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Allopurinol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned canonical `allopurinol` and confirmed
  `1H-pyrazolo[3,4-d]pyrimidin-4-ol` as an exact synonym of `CHEBI:40279`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:58187 CHEBI:86463 CHEBI:86465 CHEBI:15676 CHEBI:40279`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:40279`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` row 242 confirmed the
  `MIM:Allopurinol` to `CHEBI:40279` mapping.
- `mappings/ingredient_mappings.sssom.tsv` row 370 maps `MIM:Allopurinol` to
  `CHEBI:40279` with `skos:exactMatch`, exports CAS `315-30-0`, and includes
  the only curated exact synonym.
- The ChEBI page and local ChEBI metadata support the stored CAS, formula,
  SMILES, and InChI.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated indexes,
  and ignored aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, the exact ChEBI synonym, curation history, and
  `ingredient_type` are populated.
- `occurrence_statistics` is correctly `0/0` because the record comes from a
  CultureBotHT anti-metabolite panel rather than from CultureMech recipe
  membership.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` history event has a truncated InChI in
  its descriptive `changes` text, but the current `chemical_properties.inchi`
  value is complete.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Optionally replace the truncated auto-backfill `changes` prose in
  `data/ingredients/mapped/Allopurinol.yaml` with a complete structure summary
  or a concise non-structural note. No identity, mapping, or exported SSSOM
  change is needed.
