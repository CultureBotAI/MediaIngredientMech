# `data/ingredients/mapped/Glutaraldehyde.yaml`

## Verdict

Pass. The CultureBotHT exact match to active `CHEBI:64276` glutaraldehyde is
structurally consistent, the CAS RN resolves to the same PubChem compound, and
the final SSSOM row exports only true same-record synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Glutaraldehyde.yaml`.
- Identifier and grounding: `identifier: CHEBI:64276` with matching
  `ontology_mapping.ontology_id`, canonical label `glutaraldehyde`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `111-30-8`, formula `C5H8O2`, InChI
  `InChI=1S/C5H8O2/c6-4-2-1-3-5-7/h4-5H,1-3H2`, and SMILES `O=CCCCC=O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glutamate.yaml data/ingredients/mapped/Glutamic_Acid.yaml data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml data/ingredients/mapped/Glutaraldehyde.yaml data/ingredients/mapped/Glutarate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glutamate.yaml data/ingredients/mapped/Glutamic_Acid.yaml data/ingredients/mapped/Glutamyl-glutamic_Acid.yaml data/ingredients/mapped/Glutaraldehyde.yaml data/ingredients/mapped/Glutarate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, CAS RN, formula, InChI, SMILES, exact
  `PENTANEDIAL` synonym, singleton type, and empty occurrence set as the
  per-record YAML.
- OLS4 resolves `CHEBI:64276` as `glutaraldehyde`, matching the YAML
  `ontology_mapping`.
- PubChem resolves CAS `111-30-8` to formula `C5H8O2`, IUPAC name
  `pentanedial`, and InChI
  `InChI=1S/C5H8O2/c6-4-2-1-3-5-7/h4-5H,1-3H2`, matching the record.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glutaraldehyde` to `CHEBI:64276` by `skos:exactMatch` and keeps
  `PENTANEDIAL` and `CAS:111-30-8` in `other`, both true synonyms for this
  subject.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, synonym review rows, generated indexes, old batch validation reports,
  and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, InChI, SMILES, curated exact
  synonym, ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
