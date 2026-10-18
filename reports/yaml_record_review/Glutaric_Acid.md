# `data/ingredients/mapped/Glutaric_Acid.yaml`

## Verdict

Needs curation. The CultureBotHT exact match to active `CHEBI:17859`
glutaric acid, the CAS RN, and the final SSSOM synonyms pass, but the
`CARBON_SOURCE` role is still only a provisional computational name-pattern
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Glutaric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17859` with matching
  `ontology_mapping.ontology_id`, canonical label `glutaric acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `110-94-1`, formula `C5H8O4`, InChI
  `InChI=1S/C5H8O4/c6-4(7)2-1-3-5(8)9/h1-3H2,(H,6,7)(H,8,9)`, and SMILES
  `O=C(O)CCCC(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glutaric_Acid.yaml data/ingredients/mapped/Glutathione.yaml data/ingredients/mapped/Glutathione_Oxidized.yaml data/ingredients/mapped/Gly-DL-Asp.yaml data/ingredients/mapped/Gly-Gln_Monohydrate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glutaric_Acid.yaml data/ingredients/mapped/Glutathione.yaml data/ingredients/mapped/Glutathione_Oxidized.yaml data/ingredients/mapped/Gly-DL-Asp.yaml data/ingredients/mapped/Gly-Gln_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, CAS RN, formula, InChI, SMILES, exact
  pentanedioic-acid synonym, computational carbon-source role, and singleton
  type as the per-record YAML.
- OLS4 resolves `CHEBI:17859` as `glutaric acid`, matching the YAML
  `ontology_mapping`.
- PubChem resolves CAS `110-94-1` to formula `C5H8O4`, IUPAC name
  `pentanedioic acid`, and the same InChI as the record.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glutaric_Acid` to `CHEBI:17859` by `skos:exactMatch` and keeps
  `Pentanedioic acid` and `CAS:110-94-1` in `other`, both true synonyms for
  this subject.
- Major: `nutritional_roles.CARBON_SOURCE` is still backed only by
  `COMPUTATIONAL_PREDICTION` with the provisional name-pattern note and no
  CultureMech or literature evidence for glutaric acid as a carbon source.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, OAK/OLS row-review confirmations, generated indexes, old batch
  validation reports, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, InChI, SMILES, curated exact
  synonym, ingredient type, and final SSSOM row are populated.
- The carbon-source role needs claim-level support or removal.

## Recommended Edits

- Major: remove `nutritional_roles.CARBON_SOURCE` from
  `data/ingredients/mapped/Glutaric_Acid.yaml`, or replace the provisional
  name-pattern evidence with inspected source evidence that specifically
  supports glutaric acid as a carbon source.
