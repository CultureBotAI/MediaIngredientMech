# `data/ingredients/mapped/Ammonium_Sulfite_Monohydrate.yaml`

## Verdict

Pass. The hydrate-specific CAS identity, broader `mesh:C048169` MeSH parent,
PubChem chemistry, hydrate-review rows, exact CAS and local SSSOM rows,
aggregate copy, and zero CultureMech memberships agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ammonium_Sulfite_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:7783-11-1` with
  `ontology_mapping.ontology_id: mesh:C048169`, source `MESH`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` confirms that the
  prefix-specific EBI OLS lookup resolves `mesh:C048169` exactly as
  `ammonium sulfite`; the `UNKNOWN_TERM` trailer came from earlier validator
  prefix coverage rather than a mapping defect.
- PubChem CID `21701053` resolves to ammonium sulfite monohydrate, CAS
  `7783-11-1`, formula `H10N2O4S`, SMILES
  `[NH4+].[NH4+].O.[O-]S(=O)[O-]`, and the stored InChI string.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium_Sulfamate.yaml data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml data/ingredients/mapped/Ammonium_Sulfite_Monohydrate.yaml data/ingredients/mapped/Amoxicillin.yaml data/ingredients/mapped/Amphomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Sulfite_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` rows 407-409 export the expected
  `skos:narrowMatch` row to `mesh:C048169`, the exact CAS registry row, and
  the exact `kgmicrobe.compound:ammonium_sulfite_monohydrate` companion row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the MeSH
  `UNKNOWN_TERM` trailer as missing prefix coverage, and classifies the CAS and
  kg-microbe companion rows as expected registry identifiers.
- `mappings/hydrate_review.tsv` records the active CAS as a correct
  monohydrate-specific identifier, and `reports/hydrate_grounding.tsv` records
  the broader ammonium sulfite parent as an OK own-CAS identity.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, MicrobeDecoder imports, and hydrate
  review files found the active record, aggregate copy, SSSOM identity rows,
  row-review and hydrate-review rows, and no
  `culturemech_recipe_membership.tsv` rows for `cas:7783-11-1`.

## Completeness

- CAS, formula, SMILES, InChI, parent MeSH mapping, exact CAS and local SSSOM
  rows, curation history, and `ingredient_type` are populated.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

None.
