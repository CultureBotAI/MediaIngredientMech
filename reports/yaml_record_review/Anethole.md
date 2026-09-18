# `data/ingredients/mapped/Anethole.yaml`

## Verdict

Needs curation. The broad `CHEBI:2716` anethole mapping, formula, exact
structural synonym, row-review confirmation, and aggregate copy are internally
consistent, but the stored CAS `4180-23-8` denotes `CHEBI:35616`
`trans-anethole`; the record currently drops that stereochemical boundary and
exports a CAS for the narrower trans isomer on the broader parent.

## Identity

- Reviewed record: `data/ingredients/mapped/Anethole.yaml`.
- Identifier and grounding: `identifier: CHEBI:2716` with
  `ontology_mapping.ontology_id: CHEBI:2716`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:2716` to
  nonstereospecific `anethole` with formula `C10H12O`, the stored SMILES and
  InChI, and InChIKey `RUVINXPYWBROJD-UHFFFAOYSA-N`.
- PubChem resolves the YAML CAS `4180-23-8`, and local OAK plus the official
  ChEBI page place that CAS on `CHEBI:35616` `trans-anethole`, whose SMILES,
  InChI, and InChIKey are stereospecific.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Andrographolide.yaml data/ingredients/mapped/Anethole.yaml data/ingredients/mapped/Angolamycin.yaml data/ingredients/mapped/Angustmycin.yaml data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anethole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:65408 CHEBI:2716 CHEBI:8612 CHEBI:201752`:
  returned canonical `anethole` and the stored exact structural synonym for
  `CHEBI:2716`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:65408 CHEBI:2716 CHEBI:8612 CHEBI:201752`:
  returned formula, SMILES, InChI, InChIKey, average mass, and monoisotopic
  mass for `CHEBI:2716`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:35616 CHEBI:58981 CHEBI:58982`:
  returned the trans-anethole identity, stereospecific structure, and CAS
  `4180-23-8` for `CHEBI:35616`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Anethole` to `CHEBI:2716` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no action was
  required in that row-review pass.
- `mappings/ingredient_mappings.sssom.tsv` row 426 maps `MIM:Anethole` to
  `CHEBI:2716` with `skos:exactMatch`, the exact structural synonym, CAS
  `4180-23-8`, and the `CONFIRMED` trailer.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, CultureMech memberships, and batch
  review reports found the active YAML, aggregate copy, exact SSSOM row, and no
  other active `4180-23-8` record.

## Completeness

- Formula, SMILES, InChI, exact structural synonym, curation history, and
  `ingredient_type` are populated for generic anethole.
- No component, role, environmental context, discussion, or dataset entry is
  needed.
- The CAS/stereochemistry mismatch is the active gap: the source CAS points at
  trans-anethole, but the active identifier and structure are not
  stereospecific.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the over-broad CAS export.

## Recommended Edits

- In `data/ingredients/mapped/Anethole.yaml`, either promote the record to
  `CHEBI:35616` `trans-anethole` and update its stereospecific structure, or
  replace the CAS with source-backed evidence for unqualified `CHEBI:2716`
  anethole.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anethole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
